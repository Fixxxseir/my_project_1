from typing import Dict

import pytest

from src.masks import get_mask_account, get_mask_card_number


# function get_mask_card_number
def test_mask_standard(card_numbers: Dict[str, str]) -> None:
    assert get_mask_card_number(card_numbers["standard"]) == "1234 56** **** 5678"


def test_mask_short(card_numbers: Dict[str, str]) -> None:
    with pytest.raises(ValueError):
        assert get_mask_card_number(card_numbers["short"])


def test_mask_empty(card_numbers: Dict[str, str]) -> None:
    with pytest.raises(ValueError):
        assert get_mask_card_number(card_numbers["empty"])


def test_mask_single_digit(card_numbers: Dict[str, str]) -> None:
    with pytest.raises(ValueError):
        assert get_mask_card_number(card_numbers["single_digit"])


def test_mask_non_numeric(card_numbers: Dict[str, str]) -> None:
    with pytest.raises(ValueError):
        assert get_mask_card_number(card_numbers["non_numeric"])


def test_mask_special_chars(card_numbers: Dict[str, str]) -> None:
    with pytest.raises(ValueError):
        assert get_mask_card_number(card_numbers["special_chars"])


def test_mask_spaces(card_numbers: Dict[str, str]) -> None:
    with pytest.raises(ValueError):
        assert get_mask_card_number(card_numbers["spaces"].strip())


def test_mask_custom_length(card_numbers: Dict[str, str]) -> None:
    with pytest.raises(ValueError):
        assert get_mask_card_number(card_numbers["custom_length"])


# function get_mask_card_number
def test_get_mask_account_valid(valid_account_numbers: list) -> None:
    for account, expected in valid_account_numbers:
        assert get_mask_account(account) == expected


def test_get_mask_numbers(invalid_account_numbers: Dict[str, str]) -> None:
    with pytest.raises(ValueError):
        assert get_mask_account(invalid_account_numbers["few_numbers"])


def test_get_mask_lot_of_numbers(invalid_account_numbers: Dict[str, str]) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_account_numbers["lot_of_numbers"])


def test_get_mask_letters(invalid_account_numbers: Dict[str, str]) -> None:
    with pytest.raises(ValueError):
        assert get_mask_account(invalid_account_numbers["contains_letters"])


def test_get_mask_characters(invalid_account_numbers: Dict[str, str]) -> None:
    with pytest.raises(ValueError):
        assert get_mask_account(invalid_account_numbers["contains_characters"])
