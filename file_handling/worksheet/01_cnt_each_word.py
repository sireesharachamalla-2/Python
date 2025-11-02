def count_words(filename):
    word_count = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = ''.join(char.lower() if char.isalnum() else ' ' for char in line)
                words = line.split()
                for word in words:
                    word_count[word] = word_count.get(word, 0) + 1
        return word_count
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return {}

filename = r"file_handling\files\small_log.txt"  
result = count_words(filename)

print("Word Count:")
for word, count in result.items():
    print(f"{word}: {count}")
