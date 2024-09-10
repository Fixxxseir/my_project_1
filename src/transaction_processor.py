import re
from collections import defaultdict


def filter_transactions_by_word(transactions_list: list[dict], search_word: str) -> list[dict]:
    """Функция, которая возвращает список словарей,
    имеющих в описании данную строку {search_word}"""
    transactions_sort = []
    pattern = re.compile(search_word, re.IGNORECASE)

    for operation in transactions_list:
        if pattern.search(operation.get("description", "")):
            transactions_sort.append(operation)

    return transactions_sort


# transactions = []
# search_string = ''
# filtered_transactions = filter_transactions_by_word(transactions, search_string)
# print(filtered_transactions)


def count_transactions_by_category(transactions: list[dict], categories: list[str]) -> dict[str, int]:
    """ """
    category_counts: defaultdict[str, int] = defaultdict(int)
    # Проходимся по каждой транзакции
    for transaction in transactions:
        description = transaction.get("description", "")

        # Проверяем каждую категорию
        for category in categories:
            # Если категория найдена в описании, увеличиваем счетчик
            if re.search(category, description, re.IGNORECASE):
                category_counts[category] += 1

    return dict(category_counts)
