import re

log_path = r'file_handling\files\mixed_logs.log'
try:
    with open(log_path, 'r') as file:
        log_entries = file.readlines()
except FileNotFoundError:
    print(f"File not found: {log_path}")
    exit()

#Extract only ERROR entries using list comprehension
error_entries = [
    {
        "timestamp": line.split(" ")[0] + " " + line.split(" ")[1].rstrip(","), 
        "module": re.search(r"\[(.*?)\]", line).group(1),
        "message": line.split(" - ", 1)[1].strip()
    }
    for line in log_entries
    if "ERROR" in line
]

# Validation
expected_count = 1 
if len(error_entries) == expected_count:
    print("Validation Passed: Correct number of error entries found.")
else:
    print(f"Validation Failed: Expected {expected_count}, found {len(error_entries)}.")

# Print results
print("\nExtracted ERROR Entries:")
for entry in error_entries:
    print(f"[{entry['timestamp']}] ({entry['module']}) - {entry['message']}")