'''Enter a 16-bit value and print if parity (number of 1s) is even or odd.
Input: 0xAAAA
Output: Parity: Even'''

val=int(input(),16)
cnt = bin(value).count('1')
if cnt % 2 == 0:
    print("Parity: Even")
else:
    print("Parity: Odd")