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
