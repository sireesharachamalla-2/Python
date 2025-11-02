import re
from collections import defaultdict

def group_by_severity(log_text):
    severity_pattern = r"\b(INFO|DEBUG|WARNING|ERROR):"
    grouped = defaultdict(list)

    for line in log_text.strip().splitlines():
        match = re.search(severity_pattern, line)
        if match:
            severity = match.group(1)
            grouped[severity].append(line.strip())

    return grouped

def show_grouped_summary(grouped_logs):
    print("Severity Counts:")
    for severity in ['INFO', 'DEBUG', 'WARNING', 'ERROR']:
        count = len(grouped_logs.get(severity, []))
        print(f"{severity}: {count} line(s)")

if __name__ == "__main__":
    filepath = r"file_handling\files\large_log.txt"
    
    try:
        with open(filepath, 'r') as f:
            log_data = f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        exit()

    grouped_logs = group_by_severity(log_data)
    show_grouped_summary(grouped_logs)