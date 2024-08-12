from typing import Any, Dict, List, Tuple

import pytest

from tests.test_widget import get_date


################################################################################################
# test_masks
# function get_mask_card_number
@pytest.fixture
def card_numbers() -> dict[str, str]:
    return {
        "standard": "1234567812345678",
        "short": "1234",
        "empty": "",
        "single_digit": "1",
        "non_numeric": "abcd5678",
        "special_chars": "12$%^5678",
        "spaces": " 1234 5678  ",
        "custom_length": "1234567",
    }


# function get_mask_account
@pytest.fixture
def valid_account_numbers() -> List[Tuple[str, str]]:
    return [
        ("12345678901234567890", "**7890"),
        ("00000000000000004305", "**4305"),
    ]


@pytest.fixture
def invalid_account_numbers() -> Dict[str, str]:
    return {
        "few_numbers": "1234567890123456789",
        "lot_of_numbers": "123456789012345678901",
        "contains_letters": "1234567890abcdef1234",
        "contains_characters": "1234567890123456789a",
    }


##################################################################################
# test_widget
# function mask_account_card
@pytest.fixture
def account_card_data() -> Dict[str, str]:
    return {
        "visa_card": "Visa 1234567812345678",
        "mastercard": "MasterCard 8765432187654321",
        "account": "Счет 1234567890123456",
        "invalid_card": "CreditCard 1234",
        "invalid_account": "Account 12",
        "unknown_format": "Unknown 12345678",
    }


# function get_date


@pytest.fixture
def date_str() -> str:
    return "2024-03-11T02:26:18.671407"


def test_get_date_fixture(date_str: str) -> None:
    expected = "11.03.2024"
    assert get_date(date_str) == expected


# test_processing
# test function filter_by_state


@pytest.fixture
def list_of_dicts() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "state": "EXECUTED", "amount": 100},
        {"id": 2, "state": "PENDING", "amount": 200},
        {"id": 3, "state": "EXECUTED", "amount": 300},
        {"id": 4, "state": "FAILED", "amount": 400},
    ]


# test function sort_by_date


@pytest.fixture
def dicts_list_fixture() -> List[Dict[str, Any]]:
    return [
        {"date": "2022-01-01", "name": "John"},
        {"date": "2022-01-03", "name": "Alice"},
        {"date": "2022-01-02", "name": "Bob"},
    ]


@pytest.fixture
def dicts_list_fixture_equal_dates() -> List[Dict[str, Any]]:
    return [
        {"date": "2022-01-01", "name": "John"},
        {"date": "2022-01-01", "name": "Eve"},
        {"date": "2022-01-01", "name": "Bob"},
    ]


@pytest.fixture
def dicts_list_fixture_invalid_date_format() -> List[Dict[str, Any]]:
    return [{"date": "01-01-2022", "name": "John"}, {"date": "2022-01-01", "name": "Eve"}]
