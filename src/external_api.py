import os
# from src.utils import get_transactions
from typing import Dict, Generator, Optional

import requests
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Получение API ключа
API_KEY = os.getenv("API_KEY")

# Пути к файлам
json_file = r"../data/operations.json"


def convert_to_rub(transactions: Generator[Dict, None, None]) -> Generator[Optional[float], None, None]:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    for transaction in transactions:
        amount: float = float(transaction["operationAmount"]["amount"])
        currency_code: str = transaction["operationAmount"]["currency"]["code"]
        if currency_code == "RUB":
            yield amount
        elif currency_code in ["USD", "EUR"]:
            headers = {"apikey": API_KEY}
            payload = {
                "amount": transaction["operationAmount"]["amount"],
                "from": transaction["operationAmount"]["currency"]["code"],
                "to": "RUB",
            }
            url: str = (
                f"https://api.apilayer.com/exchangerates_data/convert?to={payload['to']}&from={payload['from']}&amount={payload['amount']}"
            )
            try:
                response = requests.request("GET", url, headers=headers, params=payload)
                response.raise_for_status()
                result: float = response.json()["result"]
                yield float(result)
            except (requests.exceptions.HTTPError, requests.exceptions.RequestException) as err:
                print(f"Ошибка при конвертации: {err}")
                yield None
        else:
            print(f"Неподдерживаемая валюта: {currency_code}")
            yield None


# if __name__ == "__main__":
#     transactions_1 = get_transactions(json_file)
#
#     # Создаём генератор
#     result_generator = convert_to_rub(transactions_1)
#
#     # Получаем первую транзакцию
#     print(next(result_generator))
