from typing import Dict, Iterator, List

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# test function filter_by_currency
# Тест для проверки фильтрации по валюте
def test_filter_by_currency_found(transactions: List[Dict]) -> None:
    result = list(filter_by_currency(transactions, "USD"))
    expected = [
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
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]
    assert result == expected


# Тест для случая, когда транзакции в указанной валюте отсутствуют
def test_filter_by_currency_not_found(transactions: List[Dict]) -> None:
    result = list(filter_by_currency(transactions, "EUR"))
    assert result == []


# Тест для обработки пустого списка транзакций
def test_filter_by_currency_empty_list() -> None:
    result = list(filter_by_currency([], "USD"))
    assert result == []


# Тест для обработки транзакций без валютных операций
def test_filter_by_currency_no_currency_key(transactions_no_currency: List[Dict]) -> None:
    result = list(filter_by_currency(transactions_no_currency, "USD"))
    assert result == []


# Тест, что функция возвращает корректные описания для каждой транзакции


def test_transaction_descriptions_with_descriptions(transactions: List[Dict]) -> None:
    result = list(transaction_descriptions(transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert result == expected


# Тест без описания транзакции
def test_transaction_descriptions_without_descriptions(transactions_without_descriptions: List[Dict]) -> None:
    result = list(transaction_descriptions(transactions_without_descriptions))
    expected: List[Dict] = []
    assert result == expected


# Пустая транзакция
def test_transaction_descriptions_empty(empty_transactions: List[Dict]) -> None:
    result = list(transaction_descriptions(empty_transactions))
    expected: List[Dict] = []
    assert result == expected


# test function card_number_generator
def test_single_number_range(single_number_range: Iterator[str]) -> None:
    result = list(single_number_range)
    expected = ["0000 0000 0000 0001"]
    assert result == expected


def test_small_range(small_range: Iterator[str]) -> None:
    result = list(small_range)
    expected = [
        "0000 0000 0000 9999",
        "0000 0000 0001 0000",
        "0000 0000 0001 0001",
    ]
    assert result == expected


def test_large_range(large_range: Iterator[str]) -> None:
    result = list(large_range)
    expected = [
        "9999 9999 9999 9990",
        "9999 9999 9999 9991",
        "9999 9999 9999 9992",
        "9999 9999 9999 9993",
        "9999 9999 9999 9994",
        "9999 9999 9999 9995",
        "9999 9999 9999 9996",
        "9999 9999 9999 9997",
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
    ]
    assert result == expected


def test_empty_range() -> None:
    # Проверка на случай, если start > end
    result = list(card_number_generator(10, 9))
    expected: List[Dict] = []
    assert result == expected
