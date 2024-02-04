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
