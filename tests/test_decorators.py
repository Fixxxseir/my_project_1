from typing import Optional

import pytest
from _pytest.capture import CaptureFixture

from src.decorators import log


@log()
def add(a: int, b: int) -> int:
    return a + b


@log()
def divide(a: int, b: int) -> Optional[float]:
    if b == 0:
        raise ValueError("Division by zero")
    return a / b


# Тесты
def test_add_success(capsys: CaptureFixture) -> None:
    result = add(3, 4)

    # Проверка правильности выполнения функции
    assert result == 7

    # Перехват и проверка вывода в консоль
    captured = capsys.readouterr()
    assert "Начало выполнения функции: add" in captured.out
    assert "Функция add завершена с результатом: 7" in captured.out
    assert "Завершение выполнения функции: add" in captured.out


def test_divide_success(capsys: CaptureFixture) -> None:
    result = divide(10, 2)

    # Проверка правильности выполнения функции
    assert result == 5.0

    # Перехват и проверка вывода в консоль
    captured = capsys.readouterr()
    assert "Начало выполнения функции: divide" in captured.out
    assert "Функция divide завершена с результатом: 5.0" in captured.out
    assert "Завершение выполнения функции: divide" in captured.out


def test_divide_by_zero_error(capsys: CaptureFixture) -> None:
    with pytest.raises(ValueError, match="Division by zero"):
        divide(10, 0)

    # Перехват и проверка вывода в консоль
    captured = capsys.readouterr()
    assert "Начало выполнения функции: divide" in captured.out
    assert "Ошибка в функции divide: ValueError с аргументами: args=(10, 0), kwargs={}" in captured.out
    assert "Завершение выполнения функции: divide" in captured.out
