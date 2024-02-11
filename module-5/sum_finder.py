import re
from typing import Callable

def generator_numbers(text: str):
    for match in re.finditer(r'\b\d+(\.\d+)?\b', text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    return sum(func(text))

if __name__ == "__main__":
    # Запит вхідного тексту у користувача
    text = input("Введіть текст для аналізу: ")

    # Обчислення та виведення загального доходу
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
