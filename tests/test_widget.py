from typing import Any

import pytest

from src.widget import get_date, mask_account_card


# function mask_account_card
@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),
        ("MasterCard 8765432187654321", "MasterCard 8765 43** **** 4321"),
        ("Счет 1234567890123456", "Счет **3456"),
        ("CreditCard 1234", "Invalid input"),
        ("Account 12", "Invalid input"),
        ("Unknown 12345678", "Invalid input"),
    ],
)
def test_mask_account_card(account_card_data: Any, input_data: Any, expected_output: Any) -> None:
    assert mask_account_card(input_data) == expected_output


# function get_date
class TestGetDate:
    @pytest.mark.parametrize(
        "date_str, expected",
        [
            ("2024-03-11T02:26:18.671407", "11.03.2024"),
            ("2024-12-31T23:59:59", "31.12.2024"),
            ("2024-01-01T00:00:00", "01.01.2024"),
        ],
    )
    def test_get_date(self, date_str: str, expected: str) -> None:
        assert get_date(date_str) == expected

    def test_get_date_empty_string(self) -> None:
        date_str = ""
        with pytest.raises(ValueError):
            get_date(date_str)

    def test_get_date_invalid_format(self) -> None:
        date_str = "01.01.2024"
        with pytest.raises(ValueError):
            get_date(date_str)

    @pytest.mark.parametrize(
        "date_str",
        [
            "2024-03-11T02:26:18.671407Z",
            "2024-03-11T02:26:18.671407+03:00",
            "2024-03-11T02:26:18.671407-03:00",
        ],
    )
    def test_get_date_with_timezone(self, date_str: str) -> None:
        expected = "11.03.2024"
        assert get_date(date_str) == expected
