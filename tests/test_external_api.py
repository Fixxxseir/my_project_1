from unittest.mock import MagicMock, patch

from src.external_api import convert_to_rub


def test_convert_rub_to_rub() -> None:
    """Тест для конвертации транзакций в рублях."""
    transactions = [{"operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}]
    result = list(convert_to_rub((transaction for transaction in transactions)))
    assert result == [100.0], "Ожидалось, что транзакции в рублях не изменятся"


@patch("requests.request")
def test_convert_usd_to_rub(mock_request: MagicMock) -> None:
    """Тест для конвертации транзакций из долларов в рубли."""
    transactions = [{"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}]
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 7500.0}
    mock_request.return_value = mock_response

    result = list(convert_to_rub((transaction for transaction in transactions)))
    assert result == [7500.0], "Ожидалось, что транзакции в долларах будут конвертированы в рубли"


@patch("requests.request")
def test_convert_unsupported_currency(_: MagicMock) -> None:
    """Тест для обработки неподдерживаемой валюты."""
    transactions = [{"operationAmount": {"amount": "100", "currency": {"code": "BABOSISKI"}}}]
    result = list(convert_to_rub((transaction for transaction in transactions)))
    assert result == [None], "Ожидалось, что неподдерживаемая валюта вернет None"
