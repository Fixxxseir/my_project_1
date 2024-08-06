def filter_by_state(list_of_dicts: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    # Будет выведен список, содержащий только словари с state = 'EXECUTED'
    new_dict = []
    for i in list_of_dicts:
        if i.get("state") == state:
            new_dict.append(i)
    return new_dict


#############################################################################


def sort_by_date(dicts_list: list, ascending: bool = True) -> list:
    """Функция возвращает новый список, отсортированный по дате"""
    # Сортировка по дате
    return sorted(dicts_list, key=lambda x: x["date"], reverse=not ascending)
