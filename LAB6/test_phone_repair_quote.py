import pytest
from phone_repair_quote import repair_quote, repair_days, trade_in_value

#Example test cases:
def test_budget_screen():
    assert repair_quote("screen", "budget", False, False) == 4600

def test_in_stock_quick():
    assert repair_days("battery", True, 2) == 1

#Write the rest of the test cases so that the code is 90- 100% covered.
# repair_quote
def test_unknown_part():
    with pytest.raises(ValueError):
        repair_quote("speaker", "budget", False, False)

def test_unknown_brand_tier():
    with pytest.raises(ValueError):
        repair_quote("screen", "premium", False, False)

def test_flagship_screen():
    assert repair_quote("screen", "flagship", False, False) == 8600

def test_flagship_camera():
    assert repair_quote("camera", "flagship", False, False) == 5300

def test_budget_battery_no_warranty():
    assert repair_quote("battery", "budget", False, False) == 1800

def test_warranty_non_screen_is_free_parts():
    assert repair_quote("battery", "budget", True, False) == 300

def test_warranty_does_not_cover_screen():
    assert repair_quote("screen", "budget", True, False) == 4600

def test_express_surcharge():
    assert repair_quote("battery", "budget", False, True) == 2300

# repair_days
def test_no_technicians_in_stock():
    assert repair_days("battery", True, 0) == 3

def test_screen_out_of_stock():
    assert repair_days("screen", False, 1) == 6

def test_camera_out_of_stock():
    assert repair_days("camera", False, 1) == 6

def test_battery_out_of_stock():
    assert repair_days("battery", False, 1) == 3

def test_charging_port_out_of_stock_no_technicians():
    assert repair_days("charging_port", False, 0) == 5

# trade_in_value
def test_trade_in_invalid_price():
    with pytest.raises(ValueError):
        trade_in_value(0, 10, False)

def test_trade_in_negative_price():
    with pytest.raises(ValueError):
        trade_in_value(-100, 10, False)

def test_trade_in_negative_age():
    with pytest.raises(ValueError):
        trade_in_value(10000, -1, False)

def test_trade_in_under_12_months():
    assert trade_in_value(10000, 6, False) == 6000

def test_trade_in_exactly_12_months():
    assert trade_in_value(10000, 12, False) == 6000

def test_trade_in_13_to_24_months():
    assert trade_in_value(10000, 18, False) == 4000

def test_trade_in_exactly_24_months():
    assert trade_in_value(10000, 24, False) == 4000

def test_trade_in_over_24_months():
    assert trade_in_value(10000, 36, False) == 2000

def test_trade_in_exactly_48_months():
    assert trade_in_value(10000, 48, False) == 2000

def test_trade_in_over_48_months():
    assert trade_in_value(10000, 49, False) == 0

def test_trade_in_cracked_screen():
    assert trade_in_value(10000, 6, True) == 3000
