import pytest
from pymongo import MongoClient
from unittest.mock import patch
from io import StringIO
import builtins

@pytest.fixture
def mongo_client():
    # Create a mock MongoClient object
    client = MongoClient()
    yield client
    # Clean up after the test
    client.close()

def test_insert_recipe(mongo_client, monkeypatch):
    # Set up the inputs to be used in the test
    inputs = ["Recipe Name", "Ingredient 1", "Ingredient 2", "STOP", "10 mins", "Tag 1", "Tag 2", "STOP", "4", "Recipe Text", "ObjectId123"]

    # Set up the expected data
    expected_data = {
        "Name": "Recipe Name",
        "Ingredients": ["Ingredient 1", "Ingredient 2"],
        "Cook_Time": "10 mins",
        "Tags": ["Tag 1", "Tag 2"],
        "Servings": "4",
        "Recipe": "Recipe Text"
    }

    # Mocking the built-in input function to provide predefined inputs
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    # Mocking print to suppress any output
    with patch('builtins.print'):
        # Importing the module here to ensure the mock for 'input' takes effect
        import insert_recipe

    # Verifying that insert_one is called with the expected data
    assert mongo_client["CapyCookin"]["Ingredients"].insert_one.called
    assert mongo_client["CapyCookin"]["Ingredients"].insert_one.call_args[0][0] == expected_data

