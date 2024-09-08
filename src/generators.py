from typing import Dict, Iterator, List


def filter_by_currency(transactions: list, currency: str) -> Iterator[Dict]:
    """Функция, которая фильтрует список транзакций по заданной валюте"""
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
        except KeyError:
            pass
        try:
            if transaction["currency_code"] == currency:
                yield transaction
        except KeyError:
            pass


def transaction_descriptions(list_of_transactions: List[Dict]) -> Iterator[str]:
    """Генерирует описание каждой транзакции по очереди"""
    for operation in list_of_transactions:
        description = operation.get("description")
        if description:
            yield description


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне.
    """
    for number in range(start, end + 1):
        # Преобразуем число в строку
        number_str = str(number)
        # Создаем 16-значную строку, добавляя нули в начале
        full_number = "0" * (16 - len(number_str)) + number_str
        # Форматируем строку в виде XXXX XXXX XXXX XXXX
        yield f"{full_number[:4]} {full_number[4:8]} {full_number[8:12]} {full_number[12:]}"
