from typing import Dict, List

import pytest

from src.transaction_processor import count_transactions_by_category, filter_transactions_by_word


@pytest.fixture
def transactions() -> List[Dict[str, str]]:
    """Фикстура, возвращающая список транзакций для тестирования"""
    return [
        {"description": "Открытие вклада", "amount": "1000"},  # Строка, чтобы соответствовать типу
        {"description": "Закрытие счета", "amount": "500"},
        {"description": "Платеж по кредиту", "amount": "200"},
        {"description": "Перевод средств", "amount": "300"},
    ]


def test_filter_with_existing_word(transactions: List[Dict[str, str]]) -> None:
    result = filter_transactions_by_word(transactions, "вклад")
    expected = [{"description": "Открытие вклада", "amount": "1000"}]
    assert result == expected


def test_filter_with_non_existing_word(transactions: List[Dict[str, str]]) -> None:
    result = filter_transactions_by_word(transactions, "инвестиции")
    expected: List[Dict[str, str]] = []
    assert result == expected


def test_filter_case_insensitivity(transactions: List[Dict[str, str]]) -> None:
    result = filter_transactions_by_word(transactions, "ПЛАТЕЖ")
    expected = [{"description": "Платеж по кредиту", "amount": "200"}]
    assert result == expected


def test_filter_with_empty_list() -> None:
    result = filter_transactions_by_word([], "вклад")
    expected: List[Dict[str, str]] = []
    assert result == expected


def test_filter_with_empty_search_word(transactions: List[Dict[str, str]]) -> None:
    result = filter_transactions_by_word(transactions, "")
    expected = transactions
    assert result == expected


@pytest.fixture
def sample_transactions() -> List[Dict[str, str]]:
    """Фикстура, возвращающая список транзакций для тестирования"""
    return [
        {"description": "Открытие вклада", "amount": "1000"},
        {"description": "Закрытие счета", "amount": "500"},
        {"description": "Платеж по кредиту", "amount": "200"},
        {"description": "Перевод средств", "amount": "300"},
    ]


# Фикстура для категорий
@pytest.fixture
def categories() -> List[str]:
    """Фикстура, возвращающая список категорий для тестирования"""
    return ["вклад", "счет", "кредит", "перевод"]


def test_count_transactions_by_category(transactions: List[Dict[str, str]], categories: List[str]) -> None:
    result = count_transactions_by_category(transactions, categories)
    expected: Dict[str, int] = {"вклад": 1, "счет": 1, "кредит": 1, "перевод": 1}
    assert result == expected


def test_count_transactions_with_empty_categories(transactions: List[Dict[str, str]]) -> None:
    result = count_transactions_by_category(transactions, [])
    expected: Dict[str, int] = {}
    assert result == expected


def test_count_transactions_with_partial_matches(transactions: List[Dict[str, str]]) -> None:
    categories = ["вклад", "счет", "перевод"]
    result = count_transactions_by_category(transactions, categories)
    expected: Dict[str, int] = {"вклад": 1, "счет": 1, "перевод": 1}
    assert result == expected
