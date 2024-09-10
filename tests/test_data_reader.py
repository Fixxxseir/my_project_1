import unittest
from unittest.mock import MagicMock, patch

import pandas as pd

from src.data_reader import read_transactions_from_csv, read_transactions_from_excel


class TestReadTransactionsFromExcel(unittest.TestCase):

    @patch("pandas.read_excel")
    def test_read_excel_success(self, mock_read_excel: MagicMock) -> None:
        # Создаем mock DataFrame, чтобы возвращать тестовые данные
        mock_df = pd.DataFrame([{"column1": "value1", "column2": "value2"}])
        mock_read_excel.return_value = mock_df

        # Тестовый вызов функции
        result = read_transactions_from_excel("test_file.xlsx")

        # Проверяем, что mocking работает
        mock_read_excel.assert_called_once_with("test_file.xlsx")
        self.assertEqual(result, [{"column1": "value1", "column2": "value2"}])


class TestReadTransactionsFromCsv(unittest.TestCase):

    @patch("pandas.read_csv")
    def test_read_csv_success(self, mock_read_csv: MagicMock) -> None:
        # Создаем mock DataFrame для возвращаемых тестовых данных (теперь пустой)
        mock_df = pd.DataFrame()
        mock_read_csv.return_value = mock_df

        # Тестовый вызов функции без разделителя
        read_transactions_from_csv("test_file.csv")

        # Проверяем, что mocking работает с правильными аргументами
        mock_read_csv.assert_called_once_with("test_file.csv", delimiter=";")
        self.assertTrue(mock_df.empty)  # Now the DataFrame is empty


if __name__ == "__main__":
    unittest.main()
