import json
import os
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", mode="w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_transactions(file_path: str) -> list:
    """Функция, которая принимает на вход путь до JSON файла и возвращает список
    с данными о финансовых транзакциях, если файл не существует или не содержит
     список то функция возвращает пустой список"""
    logger.info("Начало работы приложения")
    # возвращает пустой список потому что файл не найден
    if not os.path.exists(file_path):
        logger.error("Файл не найден")
        return []
    try:
        logger.info("Формирование списка")
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):  # если файл = List, то возвращаем файл
                logger.info("Успешное возвращение списка и завершение работы программы")

                return data
            else:
                logger.warning("Невалидный файл JSON")
                return []  # в остальных ситуациях возвращаем пустой список
    except (json.JSONDecodeError, IOError):  # обработка ошибок: "чтение" и "доступ"
        logger.error("Ошибка в чтении или доступе")
        return []


file_path = "../data/operations.json"
transactions = get_transactions(file_path)
print(transactions)
