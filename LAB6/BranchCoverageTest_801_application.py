"""Branch coverage tests for phone_repair_quote.py.

Run from this folder:
    coverage run --branch --source=phone_repair_quote -m pytest BranchCoverageTest_801_application.py
    coverage report -m
"""
import pytest
from phone_repair_quote import repair_quote, repair_days, trade_in_value


# repair_quote: valid/invalid part and brand, flagship/budget, screen/other,
# warranty condition, and express/non-express branches.
@pytest.mark.parametrize(
    "part,tier,warranty,express,expected",
    [
        ("screen", "budget", False, False, 4600),
        ("screen", "flagship", False, True, 9100),
        ("battery", "budget", True, False, 300),
        ("battery", "flagship", False, False, 3300),
        ("camera", "budget", False, True, 3300),
        ("charging_port", "flagship", True, True, 800),
    ],
)
def test_repair_quote_valid_branch_combinations(part, tier, warranty, express, expected):
    assert repair_quote(part, tier, warranty, express) == expected


def test_repair_quote_invalid_part_branch():
    with pytest.raises(ValueError, match="unknown part"):
        repair_quote("speaker", "budget", False, False)


def test_repair_quote_invalid_brand_branch():
    with pytest.raises(ValueError, match="unknown brand tier"):
        repair_quote("screen", "premium", False, False)


# repair_days: technicians_free == 0 / nonzero; parts in stock / unavailable;
# unavailable screen, camera, and another part exercise both sides of the OR.
@pytest.mark.parametrize(
    "part,in_stock,technicians,expected",
    [
        ("battery", True, 0, 3),
        ("battery", True, 2, 1),
        ("screen", False, 0, 8),
        ("camera", False, 1, 6),
        ("battery", False, 1, 3),
        ("charging_port", False, 0, 5),
    ],
)
def test_repair_days_branches(part, in_stock, technicians, expected):
    assert repair_days(part, in_stock, technicians) == expected


# trade_in_value: invalid input checks; >48 months; all age bands and
# cracked/not-cracked outcomes, including the age-band boundaries.
@pytest.mark.parametrize(
    "price,age,cracked,expected",
    [
        (20000, 0, False, 12000),
        (20000, 12, True, 6000),
        (20000, 13, False, 8000),
        (20000, 24, True, 4000),
        (20000, 25, False, 4000),
        (20000, 48, True, 2000),
        (20000, 49, False, 0),
    ],
)
def test_trade_in_valid_branches(price, age, cracked, expected):
    assert trade_in_value(price, age, cracked) == expected


def test_trade_in_invalid_price_branch():
    with pytest.raises(ValueError, match="invalid input"):
        trade_in_value(0, 10, False)


def test_trade_in_invalid_age_branch():
    with pytest.raises(ValueError, match="invalid input"):
        trade_in_value(10000, -1, False)
