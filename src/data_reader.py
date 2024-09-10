from pathlib import Path
from typing import Dict, List

import pandas as pd

# Определение корневой директории проекта
DIR_ROOT = Path(__file__).resolve().parent.parent

# Определение пути к файлу данных
DIR_DATA = DIR_ROOT / "data"
FILE_EXCEL = DIR_DATA / "transactions_excel.xlsx"
FILE_CSV = DIR_DATA / "transactions.csv"


def read_transactions_from_excel(file_path: str) -> List[Dict]:
    """Функция считывания транзакций из файлов .xlsx через DataFrame, возвращает список словарей."""
    try:
        # Чтение данных из Excel
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def read_transactions_from_csv(file_path: str) -> List[Dict]:
    """Функция считывания транзакций из файлов .csv через DataFrame, возвращает список словарей."""
    try:
        # Чтение данных из CSV с указанием разделителя
        df = pd.read_csv(file_path, delimiter=";")
        return df.to_dict(orient="records")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
