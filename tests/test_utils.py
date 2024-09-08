import unittest
import unittest.mock as mock

from src.utils import get_transactions_json


class TestGetTransactions(unittest.TestCase):

    def test_file_not_exists(self) -> None:
        with mock.patch("os.path.exists") as mock_exists:
            mock_exists.return_value = False
            self.assertEqual(get_transactions_json("nonexistent_file.json"), [])

    def test_file_not_list(self) -> None:
        with open("test_file.json", "w") as f:
            f.write('{"key": "value"}')
        self.assertEqual(get_transactions_json("test_file.json"), [])

    def test_valid_file(self) -> None:
        with open("test_file.json", "w") as f:
            f.write('[{"key": "value"}]')
        self.assertEqual(get_transactions_json("test_file.json"), [{"key": "value"}])

    def test_file_empty(self) -> None:
        with open("test_file.json", "w"):
            pass
        self.assertEqual(get_transactions_json("test_file.json"), [])

    def test_file_corrupted(self) -> None:
        with open("test_file.json", "w") as f:
            f.write('{["key": "value"]')
        result = get_transactions_json("test_file.json")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
