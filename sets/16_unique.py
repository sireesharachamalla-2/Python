def is_pangram(s):
    return set("abcdefghijklmnopqrstuvwxyz").issubset(s.lower())

s="The quick brown fox jumps over the lazy dog"
print(is_pangram(s)) 