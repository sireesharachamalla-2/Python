
def count_binary_digits(n):
    binary = bin(n)[2:]
    ones = binary.count('1')
    zeros = binary.count('0')
    return ones, zeros

def are_binary_anagrams(a, b):
    ones_a, zeros_a = count_binary_digits(a)
    ones_b, zeros_b = count_binary_digits(b)
    return ones_a == ones_b and zeros_a == zeros_b

print(are_binary_anagrams(5, 6))  
 
