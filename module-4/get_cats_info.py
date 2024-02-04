#!/usr/local/bin/python3
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