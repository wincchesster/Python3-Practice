# Module 4

## Task 1 ( Salary calculator )
This program calculates the total salary and the average salary from a file:
> For ease testing purposes, I use a sys module to get the file path from the command line arguments

```python
import sys


def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total_sum = 0
            count = 0
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2 and parts[1].isdigit():
                    salary =+ int(parts[1])
                    total_sum += salary
                    count += 1
            
            if count == 0:
                return 0, 0
            
            avarage_salary = round(total_sum / count)
            return total_sum, avarage_salary
    
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return None
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Будь ласка, вкажіть шлях до файлу як аргумент.")
    else:
        file_path = sys.argv[1]
        total, average = total_salary(file_path)
        if total is not None:
            print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
```

Output:
<img src="https://i.imgur.com/xeJHT5S.png alt="drawing" width="95%"/></img>

## Task 2 ( Cats catalog )
This program reads the file and returns a list of dictionaries with the cat's information:

```python
import sys
import json

def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats = []
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_info = {"id": parts[0], "name": parts[1], "age": parts[2]} 
                    cats.append(cat_info)
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return None

    return cats

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Будь ласка, вкажіть шлях до файлу як аргумент.")
    else:
        path = sys.argv[1]
        cats_info = get_cats_info(path)
        print(json.dumps(cats_info, indent=4, ensure_ascii=False))
```

Output:
<img src="https://i.imgur.com/Z7Z2v5D.png" alt="drawing" width="95%"/></img>

> For better output, I use json.dumps() to print the list of dictionaries in a more readable format.

<img src="https://i.imgur.com/VmYlMj9.png" alt="drawing" width="95%"/></img>


## Task 3 ( Tree program )
This program lists the contents of a directory in a tree-like structure (like the tree command in Linux):

```python
import sys
import pathlib
from colorama import init, Fore

init()

def list_directory(path, prefix=""):
    try:
        entries = [entry for entry in path.iterdir() if not entry.name.startswith('.')]
        for i, entry in enumerate(entries):
            connector = "├── " if i < len(entries) - 1 else "└── "
            if entry.is_dir():
                print(Fore.BLUE + prefix + connector + entry.name)
                list_directory(entry, prefix + ("│   " if i < len(entries) - 1 else "    "))
            else:
                print(Fore.GREEN + prefix + connector + entry.name)
    except FileNotFoundError:
        print(Fore.RED + f"Шлях {path} не існує.")
    except PermissionError:
        print(Fore.RED + f"Немає доступу до шляху {path}.")
    except Exception as e:
        print(Fore.RED + f"Помилка: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Будь ласка, вкажіть шлях до директорії.")
    else:
        dir_path = pathlib.Path(sys.argv[1])
        list_directory(dir_path)
```

> I've added lines for similiar output to the tree command in Linux.

Output:
<img src="https://i.imgur.com/UIOj3mH.png" alt="drawing" width="95%"/></img>

## Task 4 ( Bot )
This program is a simple assistant bot that can add, change, and show contacts. The bot can understand the following commands:
- hello, hi, hey - the bot responds with "How can I help you?"
- ping - the bot responds with "pong"  
- add [name] [phone] - the bot adds a new contact with the given name and phone number
- change [name] [new_phone] - the bot changes the phone number for the given contact
- phone [name] - the bot returns the phone number for the given contact
- all - the bot returns all contacts
- close, exit - the bot says "Good bye!" and exits

```python
def parse_input(user_input):
    parts = user_input.strip().lower().split()
    command = parts[0]
    args = parts[1:]
    return command, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format. Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format. Usage: change [name] [new_phone]"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name} updated."
    else:
        return f"No contact found for {name}."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command format. Usage: phone [name]"
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}"
    else:
        return f"No contact found for {name}."

def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])

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
        elif command in ["hello", "hi", "hey"]:
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
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
```

Output:
<img src="https://i.imgur.com/6pSoyJT.png" alt="drawing" width="95%"/></img>