from typing import Any, Dict, Iterator, List, Tuple

import pytest

from src.generators import card_number_generator
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


############################################################################


# fixture function filter_by_currency, transaction_descriptions
# fixture for list transaction
@pytest.fixture
def transactions() -> List[Dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


# fixture without transactions
@pytest.fixture
def transactions_no_currency() -> List[Dict]:
    return [
        {"otherData": "example"},
        {"operationAmount": {"amount": 300}},
    ]


# fixture function transaction_descriptions
# fixture without descriptions
@pytest.fixture
def transactions_without_descriptions() -> List[Dict]:
    return [
        {
            "date": "2018-06-30T02:08:58.425572",
            "from": "Счет 75106830613657916952",
            "id": 1,
            "state": "EXECUTED",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "to": "Счет 11776614605963066702",
        },
        {
            "date": "2018-07-01T03:20:15.123456",
            "from": "Счет 23456789012345678901",
            "id": 2,
            "state": "EXECUTED",
            "operationAmount": {"amount": "150.00", "currency": {"name": "EUR", "code": "EUR"}},
            "to": "Счет 34567890123456789012",
        },
        {
            "date": "2018-07-02T04:30:32.234567",
            "from": "Счет 34567890123456789012",
            "id": 3,
            "state": "EXECUTED",
            "operationAmount": {"amount": "3000.00", "currency": {"name": "USD", "code": "USD"}},
            "to": "Счет 45678901234567890123",
        },
    ]


# fixture empty transactions


@pytest.fixture
def empty_transactions() -> List[Dict]:
    return []


# test function card_number_generator
# fixture для различных диапазонов номеров карт
@pytest.fixture
def single_number_range() -> Iterator[str]:
    return card_number_generator(1, 1)


@pytest.fixture
def small_range() -> Iterator[str]:
    return card_number_generator(9999, 10001)


@pytest.fixture
def large_range() -> Iterator[str]:
    return card_number_generator(9999999999999990, 9999999999999999)
