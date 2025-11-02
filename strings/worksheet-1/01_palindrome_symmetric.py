def check_string(s):
    n = len(s)
    half = n // 2

    is_palindrome = s == s[::-1]
    if n % 2 == 0:
        is_symmetrical = s[:half] == s[half:]
    else:
        is_symmetrical = s[:half] == s[half+1:]

    return is_symmetrical, is_palindrome

s = input("Enter a string: ")
sym, pal = check_string(s)

print("Symmetrical:", sym)
print("Palindrome:", pal)