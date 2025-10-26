'''Given a digital input value (0–255), determine and print which of 4 quadrants it falls into:
- 0–63, 64–127, 128–191, 192–255'''

n=int(input())
#n=67
if n<0 and n>255:
    print("invalid input: n is 0-255")
elif (n>=0) & (n<=63):
    print("Quadrant-1")
elif (n>=64) & (n<=127):
    print("Quadrant-2")
elif (n>=128) & (n<=191):
    print("Quadrant-3")
elif (n>=192) & (n<=255):
    print("Quadrant-4")
