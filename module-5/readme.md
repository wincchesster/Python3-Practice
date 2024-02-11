# Module 5

## Task 1 (Caching Fibonacci) 
This program calculates the Fibonacci sequence using a recursive function and a cache to store the results of the function calls.
> The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

```python
import sys

def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 fibonacci.py <number>")
        sys.exit(1)

    fib_number = int(sys.argv[1])
    fib = caching_fibonacci()
    print(fib(fib_number))
```

Output:

<img src="https://i.imgur.com/MWvhiZe.png" alt="drawing" width="75%"/></img>

## Task 2 (Finding sum of all numbers in a input text)
This program reads a text file and finds the sum of all the numbers in the file.
> Aditionally, added a input prompt for the user to enter the text.

```python
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
```

Output:

<img src="https://i.imgur.com/lPRqpdP.png" alt="drawing" width="75%"/></img>

## Task 3 (Logs Analysis)
This program reads a log file and finds the number of each type of log message. 
> Aditionaly, added a color to the output.

```python
import re
import sys
from typing import List, Dict, Callable

# Функції для форматування тексту кольором
def color_red(text): return f"\033[91m{text}\033[0m"
def color_gray(text): return f"\033[90m{text}\033[0m"
def color_blue(text): return f"\033[94m{text}\033[0m"
def color_orange(text): return f"\033[33m{text}\033[0m"

def parse_log_line(line: str) -> dict:
    match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)', line)
    if match:
        return {
            "datetime": match.group(1),
            "level": match.group(2),
            "message": match.group(3)
        }
    return {}

def load_logs(file_path: str) -> List[dict]:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log = parse_log_line(line)
                if log:
                    logs.append(log)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return logs

def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    return [log for log in logs if log['level'].upper() == level.upper()]

def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    counts = {}
    for log in logs:
        level = log['level']
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        if level == "INFO":
            print(f"{color_blue(level):<25} | {count}")
        elif level == "DEBUG":
            print(f"{color_gray(level):<25} | {count}")
        elif level == "ERROR":
            print(f"{color_red(level):<25} | {count}")
        elif level == "WARNING":
            print(f"{color_orange(level):<25} | {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_log_file> [log_level]")
        sys.exit(1)

    log_file_path = sys.argv[1]
    logs = load_logs(log_file_path)
    log_counts = count_logs_by_level(logs)

    display_log_counts(log_counts)

    if len(sys.argv) == 3:
        log_level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, log_level)
        print(f"\nДеталі логів для рівня '{log_level}':")
        for log in filtered_logs:
            if log['level'] == "INFO":
                print(color_blue(f"{log['datetime']} - {log['message']}"))
            elif log['level'] == "DEBUG":
                print(color_gray(f"{log['datetime']} - {log['message']}"))
            elif log['level'] == "ERROR":
                print(color_red(f"{log['datetime']} - {log['message']}"))
            elif log['level'] == "WARNING":
                print(color_orange(f"{log['datetime']} - {log['message']}"))
```

Output:

<img src="https://i.imgur.com/JdUC57w.png" alt="drawing" width="70%"/></img>

## Task 4 (Enhanced Bot)
This program is an enhanced version of the bot from the previous module. Now the bot can handle wrong input from the user and provide a more user-friendly experience.
> Adittionally, added a new command "help" to show the available commands and formating names to capitalize.

```python
import sys

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "No such contact found."
        except ValueError:
            return "Give me the correct name and phone please."
        except IndexError:
            return "Enter the argument for the command."
    return inner

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Invalid command format.")
    name, phone = args
    name = name.capitalize()
    contacts[name] = phone
    return f"Contact {name} added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Invalid command format.")
    name, new_phone = args
    name = name.capitalize()
    if name not in contacts:
        raise KeyError("No such contact found.")
    contacts[name] = new_phone
    return f"Contact {name} updated."

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError("Invalid command format.")
    name = args[0].capitalize()
    if name not in contacts:
        raise KeyError("No such contact found.")
    return f"{name}'s phone number is {contacts[name]}"

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])

def parse_input(user_input):
    parts = user_input.strip().lower().split()
    command = parts[0]
    args = parts[1:]
    return command, args

def print_help():
    return """
Available commands:
- add [name] [phone]: Add a new contact.
- change [name] [new_phone]: Change the phone number of an existing contact.
- phone [name]: Show the phone number of a contact.
- all: Show all contacts.
- help: Show this help message.
- ping: to play ping-pong.
- close/exit: Close the program.
"""

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in ["hello", "hi", "hey", "hihi"]:
            print("How can I help you?")
        elif command == "ping":
            print("pong")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "help":
            print(print_help())
        else:
            print("Invalid command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()
```

Output:

<img src="https://i.imgur.com/6LQ7qMi.png" alt="drawing" width="75%"/></img>




