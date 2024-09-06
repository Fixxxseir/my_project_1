import unittest
from typing import Dict, List
from unittest.mock import MagicMock, patch

import pandas as pd

from src.data_reader import read_transactions_from_csv, read_transactions_from_excel


class TestReadTransactionsFromExcel(unittest.TestCase):

    @patch("pandas.read_excel")
    def test_read_transactions_success(self, mock_read_excel: MagicMock) -> None:
        # Создаем фейковый DataFrame
        data = {"state": ["EXECUTED"], "from": ["Account1"], "amount": [100]}
        mock_df = pd.DataFrame(data)
        mock_read_excel.return_value = mock_df

        # Вызов функции
        result: List[Dict] = read_transactions_from_excel("dummy_path.xlsx", state_filter="EXECUTED")

        # Проверка результатов
        self.assertEqual(result, [{"state": "EXECUTED", "from": "Account1", "amount": 100}])

    @patch("pandas.read_excel")
    def test_missing_state_column(self, mock_read_excel: MagicMock) -> None:
        # Создаем фейковый DataFrame без колонки 'state'
        data = {"from": ["Account1"], "amount": [100]}
        mock_df = pd.DataFrame(data)
        mock_read_excel.return_value = mock_df

        # Вызов функции
        result: List[Dict] = read_transactions_from_excel("dummy_path.xlsx", state_filter="EXECUTED")

        # Проверка, что результат пустой
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()


class TestReadTransactionsFromCSV(unittest.TestCase):

    @patch("pandas.read_csv")
    def test_read_transactions_success(self, mock_read_csv: MagicMock) -> None:
        # Создаем фейковый DataFrame
        data = {"state": ["EXECUTED"], "from": ["Account1"], "amount": [100]}
        mock_df = pd.DataFrame(data)
        mock_read_csv.return_value = mock_df

        # Вызов функции
        result: List[Dict] = read_transactions_from_csv("dummy_path.csv", state_filter="EXECUTED")

        # Проверка результатов
        self.assertEqual(result, [{"state": "EXECUTED", "from": "Account1", "amount": 100}])

    @patch("pandas.read_csv")
    def test_missing_state_column(self, mock_read_csv: MagicMock) -> None:
        # Создаем фейковый DataFrame без колонки 'state'
        data = {"from": ["Account1"], "amount": [100]}
        mock_df = pd.DataFrame(data)
        mock_read_csv.return_value = mock_df

        # Вызов функции
        result: List[Dict] = read_transactions_from_csv("dummy_path.csv", state_filter="EXECUTED")

        # Проверка, что результат пустой
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
