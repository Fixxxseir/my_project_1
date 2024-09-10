import os

from config import DATA_PATH
from src.data_reader import read_transactions_from_csv, read_transactions_from_excel
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.transaction_processor import filter_transactions_by_word
from src.utils import get_transactions_json
from src.widget import get_date, mask_account_card

PATH_TO_FILE_JSON = os.path.join(DATA_PATH, "operations.json")
PATH_TO_FILE_CSV = os.path.join(DATA_PATH, "transactions.csv")
PATH_TO_FILE_XLSX = os.path.join(DATA_PATH, "transactions_excel.xlsx")


def main() -> None:
    """Функция, которая отвечает за основную логику проекта"""
    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями!
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла;
    2. Получить информацию о транзакциях из CSV-файла;
    3. Получить информацию о транзакциях из XLSX-файла."""
    )
    while True:
        menu = input().strip()
        if menu == "1":
            print("Для обработки выбран JSON-файл.")
            file_selection = get_transactions_json(PATH_TO_FILE_JSON)
            break
        elif menu == "2":
            print("Для обработки выбран CSV-файл.")
            file_selection = read_transactions_from_csv(PATH_TO_FILE_CSV)
            break
        elif menu == "3":
            print("Для обработки выбран XLSX-файл.")
            file_selection = read_transactions_from_excel(PATH_TO_FILE_XLSX)
            break
        else:
            print("Не существующий номер, введите из представленных")

    # Фильтрация по статусу

    while True:
        state = input(
            """Введите статус, по которому необходимо выполнить фильтрацию.
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.
            """
        ).upper()

        if state in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        else:
            print("Не правильно")
    filtered_transaction_data = filter_by_state(file_selection, state)
    print(f"Операции отфильтрованы по статусу {state}.")

    # Фильтрация по дате
    while True:
        print("Отфильтровать операции по дате?")
        users_choice_date_sort = input("Введите да/нет: ").lower()
        if users_choice_date_sort == "да":
            print("Отфильтровать по возрастанию или убыванию?")
            users_choice_sort_direction = input("Введите по возрастанию/по убыванию: ").lower()

            if users_choice_sort_direction == "по возрастанию":
                date_sorted_transactions = sort_by_date(filtered_transaction_data, False)
                print(date_sorted_transactions)
                break

            elif users_choice_sort_direction == "по убыванию":
                date_sorted_transactions = sort_by_date(filtered_transaction_data, True)
                print(date_sorted_transactions)
                break

        elif users_choice_date_sort == "нет":
            date_sorted_transactions = filtered_transaction_data
            print(date_sorted_transactions)
            break

    while True:
        users_choice_rub = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
        if users_choice_rub in ("да", "нет"):
            if users_choice_rub == "да":
                rub_transactions = list(filter_by_currency(date_sorted_transactions, "RUB"))
                print(rub_transactions)
                break
            elif users_choice_rub == "нет":
                rub_transactions = date_sorted_transactions
                print(rub_transactions)
                break
        else:
            print("выберите да или нет")

        # Фильтрация по определённому слову в описании

    while True:
        print("Отфильтровать список по определённому слову в описании?")
        users_choice_description = input("Введите да/нет сюда: ").lower()
        if users_choice_description in ("да", "нет"):
            if users_choice_description == "да":
                users_word_to_filter = input("Введите слово для сортировки: ").lower()
                result_transactions = filter_transactions_by_word(rub_transactions, users_word_to_filter)
                break
            elif users_choice_description == "нет":
                result_transactions = rub_transactions
                break
        else:
            print("выберите да или нет")

    # Работа с итоговым списком
    count_of_transactions = len(result_transactions)
    # Вывод результатов, если список не пустой
    if count_of_transactions > 0:
        print("Распечатываю итоговый список транзакций...\n")
        print(f"Всего банковских операций в выборке {count_of_transactions}.\n")
        for item in result_transactions:
            date_str = get_date(item.get("date", "Unknown Date"))
            descr_str = item.get("description", "No Description")
            summa_str = item.get("amount", "No Amount")
            currency_str = item.get("currency_code", "Unknown Currency")

            if item.get("description") == "Открытие вклада":
                print(
                    f"""{date_str} {descr_str}
        Сумма: {summa_str} {currency_str}\n"""
                )
            else:
                from_str = mask_account_card(item.get("from", "Unknown From"))
                to_str = mask_account_card(item.get("to", "Unknown To"))
                print(
                    f"""{date_str} {descr_str}
        {from_str} -> {to_str}
        Сумма: {summa_str} {currency_str}\n"""
                )
    # Вывод результата с пустым списком
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
