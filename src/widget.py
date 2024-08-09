def mask_account_card(account_or_card: str) -> str:
    """Функция, которая возвращает строку с замаскированным номером.
    Для карт и счетов использует разные типы маскировки."""
    # Определяем, является ли входная строка номером карты или счета
    if account_or_card.lower().startswith("visa") or account_or_card.lower().startswith("mastercard"):
        # Маскировка для карт
        parts = account_or_card.split()
        card_number = parts[-1]
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return " ".join(parts[:-1]) + " " + masked_number
    elif account_or_card.lower().startswith("счет"):
        # Маскировка для счетов
        parts = account_or_card.split()
        account_number = parts[-1]
        masked_number = f"**{account_number[-4:]}"
        return " ".join(parts[:-1]) + " " + masked_number
    else:
        return "Invalid input"

####################################################################


def get_date(date_str: str) -> str:
    """Функция, которая преобразовывает строку даты
    из '2024-03-11T02:26:18.671407' в формат '11.03.2024'"""
    if not date_str:
        raise ValueError("Входная строка пуста")
    # Разделяем дату и время
    try:
        date_part = date_str.split("T")[0]
        # Разделяем дату на год, месяц, день
        year, month, day = date_part.split("-")
        # Возникает, если в строке недостаточно частей для разбиения
    except IndexError:
        raise ValueError("Неверный формат даты")
    # Форматируем дату как: "день, месяц, год"
    formatted_date = f"{day}.{month}.{year}"
    return formatted_date

#######################################################################
