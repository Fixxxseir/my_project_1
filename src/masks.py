import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
    filename="../logs/masks.log",
    filemode="w",
    encoding="utf-8",
)

mask_number_logger = logging.getLogger("get_mask_card_number")

mask_account_logger = logging.getLogger("get_mask_account")


def get_mask_card_number(user_card_number: str) -> str:
    """Функция, проверяет что номер карты состоит из 16 цифр
    и отдает замаскированный номер карты в формате: 7000 79** **** 6361"""
    mask_number_logger.info(f"Проверка номера карты {user_card_number}")
    if not user_card_number.isdigit() or len(user_card_number) != 16:
        mask_number_logger.error(f"Неверный формат номера карты {user_card_number}")
        raise ValueError("Номер карты должен содержать ровно 16 цифр")

    # Маскируем номер карты
    mask_number_logger.info("Маскировка номера карты")
    masked_number = user_card_number[:4] + " " + user_card_number[4:6] + "** **** " + user_card_number[12:]
    mask_number_logger.info(f"Замаскированный номер карты  {masked_number}")
    mask_number_logger.info("Завершение работы приложения")
    return masked_number


# masks_card = get_mask_card_number("3242123312223241")
# print(masks_card)


#############################################################################


def get_mask_account(user_account_number: str) -> str:
    """Функция, которая проверяет что номер счета состоит из 20 цифр
    и отдает замаскированный номер счета в формате: **4305"""
    mask_account_logger.info("Проверка номера счёта")
    if not user_account_number.isdigit() or len(user_account_number) < 20:
        mask_account_logger.error(f"Не корректный номер счёта {user_account_number}")
        raise ValueError("Номер счета должен содержать ровно 20 цифр")

    # Маскируем номер счета
    mask_account_logger.info("Маскировка номера счёта")
    masked_account_number = "**" + user_account_number[-4:]
    mask_account_logger.info(f"Замаскированный номер счёта {masked_account_number}")
    mask_account_logger.info("Завершение работы приложения")

    return masked_account_number


# mask_account = get_mask_account('12312345645612312345')
# print(mask_account)
#############################################################################
