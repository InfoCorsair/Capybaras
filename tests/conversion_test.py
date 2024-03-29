import pytest

from tsp_conversion import (
    convert_to_teaspoons,
    convert_from_teaspoons,
    optimize_measurements,
    format_output
    )
  # Test convert_to_teaspoons function
@pytest.mark.parametrize("quantity, unit, expected", [
    (1, "teaspoon", 1),
    (2, "tsp", 2),
    (1, "tablespoon", 3),
    (1, "tbs", 3),
    (1, "cup", 48),
    (1, "pint", 96),
    (1, "quart", 192),
    (1, "gallon", 768),
    (1, "unknown_unit", 1)  # Test with an unknown unit
])
def test_convert_to_teaspoons(quantity, unit, expected):
    assert convert_to_teaspoons(quantity, unit) == expected

# Test convert_from_teaspoons function
@pytest.mark.parametrize("quantity, expected", [
    (1, {"teaspoon": 1}),
#    (2, {"teaspoon": 2}),
    (3, {"tablespoon": 1}),
    (49, {"cup": 1, "teaspoon": 1}),
#  (96, {"pint": 1}),
    (96, {"cup": 2}),
    (192, {"quart": 1}),
    (1000, {"gallon": 1, "quart": 1, "tablespoon": 13, "teaspoon": 1}),
    (5000, {"gallon": 6, "quart": 2, "tablespoon": 2, "teaspoon": 2}), #4608...
    (0, {}),
])
def test_convert_from_teaspoons(quantity, expected):
    assert convert_from_teaspoons(quantity) == expected

# Test optimize_measurements function



#******************Here is where tests for pound conversion*******************************

import pytest
from pound_conversion import to_ounces, to_pounds

# Test to_ounces function
@pytest.mark.parametrize("pounds, expected_ounces", [
    (1, 16),
    (2, 32),
    (0.5, 8),
    (0, 0),
])
def test_to_ounces(pounds, expected_ounces):
    assert to_ounces(pounds) == expected_ounces

# Test to_pounds function
@pytest.mark.parametrize("ounces, expected_pounds", [
    (16, 1),
    (32, 2),
    (8, 0.5),
    (0, 0),
])
def test_to_pounds(ounces, expected_pounds):
    assert to_pounds(ounces) == expected_pounds

