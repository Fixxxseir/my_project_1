###############################################################################
def get_mask_card_number(user_card_number: str) -> str:
    """Функция, проверяет что номер карты состоит из 16 цифр
    и отдает замаскированный номер карты в формате: 7000 79** **** 6361"""
    if not user_card_number.isdigit() or len(user_card_number) != 16:
        raise ValueError("Номер карты должен содержать ровно 16 цифр")

    # Маскируем номер карты
    masked_number = user_card_number[:4] + " " + user_card_number[4:6] + "** **** " + user_card_number[12:]

    return masked_number

#############################################################################
def get_mask_account(user_account_number: str) -> str:
    """Функция, которая проверяет что номер счета состоит из 20 цифр
    и отдает замаскированный номер счета в формате: **4305"""
    if not user_account_number.isdigit() or len(user_account_number) < 20:
        raise ValueError("Номер счета должен содержать ровно 20 цифр")

    # Маскируем номер счета
    masked_account_number = "**" + user_account_number[-4:]

    return masked_account_number


#############################################################################
