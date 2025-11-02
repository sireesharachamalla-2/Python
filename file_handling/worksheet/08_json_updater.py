
import json
import os

def update_config(filepath, updates):
    """
    Loads a JSON file, updates specified keys, and saves the changes back to file.
    - filepath: path to JSON config file
    - updates: dictionary of updates to apply
    """

    # Step 1: Load JSON config
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        return

    try:
        with open(filepath, 'r') as file:
            config = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return

    # Step 2: Apply updates
    for key, value in updates.items():
        if '.' in key:
            keys = key.split('.')
            ref = config
            for k in keys[:-1]:
                ref = ref.setdefault(k, {})  
            ref[keys[-1]] = value
        else:
            config[key] = value

    # Step 3: Write back to file
    try:
        with open(filepath, 'w') as file:
            json.dump(config, file, indent=2)
        print("Configuration updated successfully.")
    except Exception as e:
        print(f"Error writing file: {e}")

if __name__ == "__main__":
    config_file = "file_handling/files/config.json"
    updates = {
        "version": "1.1.0",
        "debug": True,
        "features.logging": False,
        "features.dark_mode": True
    }

    update_config(config_file, updates)
