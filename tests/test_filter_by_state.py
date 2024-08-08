from src.processing import filter_by_state

data = [
    {"id": 1, "state": "EXECUTED"},
    {"id": 2, "state": "PENDING"},
    {"id": 3, "state": "EXECUTED"},
    {"id": 4, "state": "CANCELED"},
    {"id": 5, "state": "EXECUTED"}
]

filtered_data = filter_by_state(data)
print(filtered_data)
