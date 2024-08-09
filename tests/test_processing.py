from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


# function filter_by_state
@pytest.mark.parametrize(
    "state, expected_result",
    [
        ("EXECUTED", [{"id": 1, "state": "EXECUTED", "amount": 100}, {"id": 3, "state": "EXECUTED", "amount": 300}]),
        ("PENDING", [{"id": 2, "state": "PENDING", "amount": 200}]),
        ("FAILED", [{"id": 4, "state": "FAILED", "amount": 400}]),
        ("CANCELED", []),
    ],
)
def test_filter_by_state(
    list_of_dicts: List[Dict[str, Any]], state: str, expected_result: List[Dict[str, Any]]
) -> None:
    assert filter_by_state(list_of_dicts, state) == expected_result


# function sort_by_state


def test_sort_by_date_ascending(dicts_list_fixture: List[Dict[str, Any]]) -> None:
    assert sort_by_date(dicts_list_fixture, ascending=True) == [
        {"date": "2022-01-01", "name": "John"},
        {"date": "2022-01-02", "name": "Bob"},
        {"date": "2022-01-03", "name": "Alice"},
    ]


def test_sort_by_date_descending(dicts_list_fixture: List[Dict[str, Any]]) -> None:
    assert sort_by_date(dicts_list_fixture, ascending=False) == [
        {"date": "2022-01-03", "name": "Alice"},
        {"date": "2022-01-02", "name": "Bob"},
        {"date": "2022-01-01", "name": "John"},
    ]


def test_sort_by_date_equal_dates(dicts_list_fixture_equal_dates: List[Dict[str, Any]]) -> None:
    sorted_list = sort_by_date(dicts_list_fixture_equal_dates)
    assert sorted_list == dicts_list_fixture_equal_dates


def test_sort_by_date_invalid_date_format(dicts_list_fixture_invalid_date_format: List[Dict[str, Any]]) -> None:
    sorted_list = sort_by_date(dicts_list_fixture_invalid_date_format)
    assert sorted_list == [{"date": "01-01-2022", "name": "John"}, {"date": "2022-01-01", "name": "Eve"}]
