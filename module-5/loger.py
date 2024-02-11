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
