
import csv
import json

def csv_to_json(csv_file, json_file):
    """
    Converts a CSV file to a JSON file containing a list of JSON objects.
    """
    with open(csv_file, mode='r', newline='') as f_csv:
        reader = csv.DictReader(f_csv)
        data = [row for row in reader] 
    with open(json_file, mode='w') as f_json:
        json.dump(data, f_json, indent=2)

    print(f"Converted '{csv_file}' to '{json_file}' successfully.")

csv_to_json("file_handling/files/sample.csv", "file_handling/files/output.json")
