from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd

# Определение корневой директории проекта
DIR_ROOT = Path(__file__).resolve().parent.parent

# Определение пути к файлу данных
DIR_DATA = DIR_ROOT / "data"
FILE_EXCEL = DIR_DATA / "transactions_excel.xlsx"
FILE_CSV = DIR_DATA / "transactions.csv"


def read_transactions_from_excel(
    file_path: str, state_filter: Optional[str] = None, exclude_empty_from: bool = True
) -> List[Dict]:
    """Функция фильтрации транзакций файлов .xlsx через DataFrame, функция возвращает
    отфильтрованный словарь по успешным транзакциям"""
    try:
        # Чтение данных из Excel
        df = pd.read_excel(file_path)

        # Фильтрация по столбцу 'state'
        if state_filter:
            if "state" in df.columns:
                df = df[df["state"] == state_filter]
            else:
                print("Столбец 'state' отсутствует в данных.")
                return []

        # Удаление строк с пустым 'from'
        if exclude_empty_from:
            if "from" in df.columns:
                df = df[df["from"].notna()]
            else:
                print("Столбец 'from' отсутствует в данных.")
                return []

        # Преобразование в список словарей
        transactions = df.to_dict(orient="records")

        return transactions

    except Exception as e:
        print(f"Ошибка: {e}")
        raise


# Пример использования
file_path_xlsx = "path/to/your/transactions.xlsx"
excel_transactions = read_transactions_from_excel(
    str(FILE_EXCEL),
    state_filter="EXECUTED",
    exclude_empty_from=True,
)
print(excel_transactions)


def read_transactions_from_csv(
    file_path: str, state_filter: Optional[str] = None, exclude_empty_from: bool = True
) -> List[Dict]:
    """Функция фильтрации транзакций из файлов .csv через DataFrame, возвращает
    отфильтрованный список словарей по успешным транзакциям."""
    try:
        # Чтение данных из CSV с указанием разделителя
        df = pd.read_csv(file_path, delimiter=";")

        # Вывод имен столбцов для отладки
        print("Имена столбцов:", df.columns)

        # Фильтрация по столбцу 'state'
        if state_filter:
            if "state" in df.columns:
                df = df[df["state"] == state_filter]
            else:
                print("Столбец 'state' отсутствует в данных.")
                return []

        # Удаление строк с пустым 'from'
        if exclude_empty_from:
            if "from" in df.columns:
                df = df[df["from"].notna()]
            else:
                print("Столбец 'from' отсутствует в данных.")
                return []

        # Преобразование DataFrame в список словарей
        transactions = df.to_dict(orient="records")

        return transactions

    except Exception as e:
        print(f"Ошибка при чтении файла CSV: {e}")
        return []


# Пример использования
file_path_csv = "path/to/your/transactions.csv"
csv_transactions = read_transactions_from_csv(
    str(FILE_CSV),
    state_filter="EXECUTED",
    exclude_empty_from=True,
)
print(csv_transactions)
