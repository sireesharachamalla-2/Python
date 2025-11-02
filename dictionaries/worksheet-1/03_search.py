d = {}
n = int(input("size of dict"))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value
print("Dictionary:", d)
for key in d:
    if key=="fruit":
        print(True)
    else:
        print(False)