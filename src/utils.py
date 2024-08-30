import json
import os


def get_transactions(file_path: str) -> list:
    """Функция, которая принимает на вход путь до JSON файла и возвращает список
    с данными о финансовых транзакциях, если файл не существует или не содержит
     список то функция возвращает пустой список"""
    # возвращает пустой список потому что файл не найден
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):  # если файл = List, то возвращаем файл
                return data
            else:
                return []  # в остальных ситуациях возвращаем пустой список
    except (json.JSONDecodeError, IOError):  # обработка ошибок: "чтение" и "доступ"
        return []


# file_path = "../data/operations.json"
# transactions = get_transactions(file_path)
# print(transactions)
