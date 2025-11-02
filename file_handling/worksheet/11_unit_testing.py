
import re
from collections import defaultdict

def group_by_severity(log_text):
    grouped_logs = defaultdict(list)
    pattern = re.compile(r'^(?P<timestamp>\S+\s+\S+),\d+\s+(?P<severity>INFO|DEBUG|WARNING|ERROR):')

    for line in log_text.strip().splitlines():
        match = pattern.match(line)
        if match:
            severity = match.group('severity')
            grouped_logs[severity].append(line.strip())

    return grouped_logs

#Read the actual log file content
log_file_path = r'file_handling\files\server_logs.log'
try:
    with open(log_file_path, 'r') as f:
        log_text = f.read()
except FileNotFoundError:
    print(f"File not found: {log_file_path}")
    exit()

#parse actual content
grouped = group_by_severity(log_text)


#Print grouped logs
for level in ["INFO", "DEBUG", "WARNING", "ERROR"]:
    print(f"\n{level}: {len(grouped.get(level, []))} line(s)")
    for line in grouped[level]:
        print(line)
