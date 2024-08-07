from src.processing import sort_by_date

list_of_dicts = [
    {"id": "1", "date": "2024-07-08"},
    {"id": "2", "date": "2022-01-12"},
    {"id": "3", "date": "2021-09-30"},
    {"id": "4", "date": "2021-05-25"},
]

sorted_list = sort_by_date(list_of_dicts)
print(sorted_list)
