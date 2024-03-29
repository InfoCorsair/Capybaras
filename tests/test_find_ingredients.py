import unittest
from unittest.mock import patch
from io import StringIO
from find_ingredients import find_ingred, ingredient_list  # Corrected import statement

class TestIngredientFunctions(unittest.TestCase):

    @patch('builtins.input', side_effect=["green bean", "2"])
    def test_find_ingred_existing(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            find_ingred()
            self.assertEqual(len(ingredient_list), 0)  # No ingredient should be found

    # Add more tests as needed

