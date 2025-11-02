
import re
from datetime import datetime

def filter_logs_by_criteria(filepath, start_time, end_time, keyword=None):
    """
    Filters log lines based on time range and optional keyword using regex.
    - start_time, end_time: Strings in HH:MM format
    - keyword: Optional regex pattern to match in message
    """
    result = []

    # Convert input strings to datetime.time objects
    fmt = "%H:%M"
    start = datetime.strptime(start_time, fmt).time()
    end = datetime.strptime(end_time, fmt).time()

    # Regex pattern to extract timestamp and message
    log_pattern = re.compile(r"^(?P<ts>\d{4}-\d{2}-\d{2} (?P<hm>\d{2}:\d{2}):\d{2},\d+).* - (?P<msg>.+)")

    with open(filepath, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                time_part = match.group("hm")
                msg = match.group("msg")

                log_time = datetime.strptime(time_part, fmt).time()
                if start <= log_time <= end:
                    if keyword is None or re.search(keyword, msg, re.IGNORECASE):
                        result.append(line.strip())

    return result

if __name__ == "__main__":
    log_file = "file_handling/files/mixed_logs.log"
    filtered = filter_logs_by_criteria(
        filepath=log_file,
        start_time="16:30",
        end_time="16:50",
        keyword="Authenticating"   
    )

    print("Filtered Log Entries:")
    for line in filtered:
        print(line)
