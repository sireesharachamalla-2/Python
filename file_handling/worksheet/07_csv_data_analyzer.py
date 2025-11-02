
import csv
from collections import Counter

def analyze_csv(filepath):
    status_counter = Counter()
    total_time = 0.0
    count = 0

    with open(filepath, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            status = row['Status'].strip()
            time = float(row['ExecutionTime'].strip())

            status_counter[status] += 1
            total_time += time
            count += 1

    avg_time = total_time / count if count else 0

    # Summary report
    print("Summary Report")

    for status, num in status_counter.items():
        print(f"{status}: {num} test(s)")

    print(f"\nAverage Execution Time: {avg_time:.2f} seconds")

if __name__ == "__main__":
    analyze_csv("file_handling/files/test_results.csv")
