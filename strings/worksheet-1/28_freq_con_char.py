def consecutive_char_freq(s):
    prev = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == prev:
            count += 1
        else:
            print(f"{prev}: {count}")
            prev = s[i]
            count = 1

    print(f"{prev}: {count}")

text = input()
consecutive_char_freq(text)