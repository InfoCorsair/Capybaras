import unittest
from unittest.mock import patch
from io import StringIO

class TestIngredientFunctions(unittest.TestCase):

    @patch('builtins.input', side_effect=["flour"])
    def test_find_ingred_existing(self, mock_input):
        # Assuming the CSV file has 'flour' as one of the ingredients
        with patch('sys.stdout', new=StringIO()) as fake_out:
            find_ingred()
            self.assertIn("You have inserted Ingredient", fake_out.getvalue())
            self.assertEqual(len(ingredient_list), 1)
            self.assertEqual(ingredient_list[0][1], "flour")

    @patch('builtins.input', side_effect=["sugar", "2"])
    def test_find_ingred_not_existing(self, mock_input):
        # Assuming 'sugar' is not in the CSV file
        with patch('sys.stdout', new=StringIO()) as fake_out:
            find_ingred()
            self.assertIn("No New Ingredients Inserted.", fake_out.getvalue())
            self.assertEqual(len(ingredient_list), 0)

    @patch('builtins.input', side_effect=["2"])
    def test_find_ingred_no_input(self, mock_input):
        # No ingredients provided, expecting no ingredient in the list
        find_ingred()
        self.assertEqual(len(ingredient_list), 0)

    @patch('builtins.input', return_value="weight")
    def test_find_by_amount(self, mock_input):
        # Test find_by_amount function
        with patch('sys.stdout', new=StringIO()) as fake_out:
            find_by_amount()
            self.assertIn("By Amount, Volume, or Weight:", fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()

