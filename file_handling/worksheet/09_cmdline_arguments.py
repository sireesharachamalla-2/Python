import sys

def search_in_file(filename, search_term):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return

    matches = [line.strip() for line in lines if search_term in line]

    if matches:
        print(f"\nLines matching '{search_term}' in '{filename}':\n")
        for line in matches:
            print(line)
    else:
        print(f"\nNo matches found for '{search_term}' in '{filename}'.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python search_logs.py <filename> <search_term>")
    else:
        filename = sys.argv[1]
        search_term = sys.argv[2]
        search_in_file(filename, search_term)