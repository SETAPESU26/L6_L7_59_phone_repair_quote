"""Line/code coverage tests for phone_repair_quote.py.

Run from this folder:
    coverage run --source=phone_repair_quote -m pytest CodeCoverageTest_801_application.py
    coverage report -m
"""
import pytest
from phone_repair_quote import repair_quote, repair_days, trade_in_value


def test_repair_quote_budget_screen_standard():
    assert repair_quote("screen", "budget", False, False) == 4600


def test_repair_quote_flagship_battery_express():
    assert repair_quote("battery", "flagship", False, True) == 3800


def test_repair_quote_warranty_non_screen():
    assert repair_quote("camera", "budget", True, False) == 300


def test_repair_quote_unknown_part():
    with pytest.raises(ValueError, match="unknown part"):
        repair_quote("speaker", "budget", False, False)


def test_repair_quote_unknown_brand_tier():
    with pytest.raises(ValueError, match="unknown brand tier"):
        repair_quote("battery", "premium", False, False)


def test_repair_days_technician_unavailable_and_part_out_of_stock():
    assert repair_days("screen", False, 0) == 8


def test_repair_days_available():
    assert repair_days("battery", True, 1) == 1


def test_repair_days_non_screen_part_out_of_stock():
    assert repair_days("battery", False, 1) == 3


def test_trade_in_under_one_year():
    assert trade_in_value(20000, 12, False) == 12000


def test_trade_in_one_to_two_years_cracked():
    assert trade_in_value(20000, 24, True) == 4000


def test_trade_in_over_two_years():
    assert trade_in_value(20000, 36, False) == 4000


def test_trade_in_over_four_years():
    assert trade_in_value(20000, 49, False) == 0


def test_trade_in_invalid_original_price():
    with pytest.raises(ValueError, match="invalid input"):
        trade_in_value(0, 10, False)


def test_trade_in_invalid_age():
    with pytest.raises(ValueError, match="invalid input"):
        trade_in_value(20000, -1, False)
