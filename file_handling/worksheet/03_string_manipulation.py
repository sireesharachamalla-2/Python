import re

def parse_log_line(line):
    """
    Extracts timestamp, severity, and message from a log line.
    Format:
    2025-03-01 14:05:00,001 INFO ModuleA - User login successful for user 'alice'.
    """
    pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})\s+(\w+)\s+\w+\s+-\s+(.*)"
    match = re.match(pattern, line)
    if match:
        timestamp, severity, message = match.groups()
        return {
            "timestamp": timestamp,
            "severity": severity,
            "message": message.strip()
        }
    return None

def process_log_file(filename):
    parsed_logs = []
    with open(filename, 'r') as f:
        for line in f:
            parsed = parse_log_line(line.strip())
            if parsed:
                parsed_logs.append(parsed)
    return parsed_logs

def validate(parsed_logs):
    for log in parsed_logs:
        if not all(key in log for key in ("timestamp", "severity", "message")):
            print("Validation failed: Missing fields.")
            return
    print("Validation passed: All entries have timestamp, severity, and message.")


input_filename = r'file_handling\files\applicaiton_logs.txt'

    # Step 1: Parse log file
parsed_logs = process_log_file(input_filename)

    # Step 2: Validate parsed data
validate(parsed_logs)

    # Step 3: Print parsed log entries
print("\n Parsed Log Entries:")
for entry in parsed_logs:
    print(entry)