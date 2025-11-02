
import os
import glob
from collections import Counter
import re

def aggregate_log_levels(directory):
    """
    Aggregates counts of log levels (INFO, WARNING, ERROR) across all .log files in a directory.
    """
    log_levels = Counter()
    pattern = re.compile(r"\b(INFO|WARNING|ERROR)\b")

    log_files = glob.glob(os.path.join(directory, "*.log"))
    
    if not log_files:
        print("No .log files found.")
        return {}

    for filepath in log_files:
        with open(filepath, 'r') as file:
            for line in file:
                match = pattern.search(line)
                if match:
                    log_levels[match.group()] += 1

    return log_levels


if __name__ == "__main__":
    log_dir = "file_handling/files"  
    summary = aggregate_log_levels(log_dir)

    print("Log Level Summary:")
    for level in ['INFO', 'WARNING', 'ERROR']:
        print(f"{level}: {summary.get(level, 0)} entries")
