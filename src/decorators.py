from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__name__
            log_entry = ""

            try:
                # Логируем начало выполнения функции
                log_entry = f"Начало выполнения функции: {func_name}\n"

                # Выполняем функцию
                result = func(*args, **kwargs)

                # Логируем успешное завершение функции
                log_entry += f"Функция {func_name} завершена с результатом: {result}\n"

                return result

            except Exception as e:
                # Логируем ошибку
                error_type = type(e).__name__
                log_entry += (
                    f"Ошибка в функции {func_name}: {error_type} с аргументами: " f"args={args}, kwargs={kwargs}\n"
                )
                raise

            finally:
                # Логируем завершение выполнения функции
                log_entry += f"Завершение выполнения функции: {func_name}\n"

                # Выбор записи в файл(если filename задан) либо в консоль
                if filename:
                    # Записываем лог в файл
                    with open(filename, "a") as f:
                        f.write(log_entry)
                else:
                    # Выводим лог в консоль
                    print(log_entry)

        return wrapper

    return decorator
