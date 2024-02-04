#!/usr/local/bin/python3
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