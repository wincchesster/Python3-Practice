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
