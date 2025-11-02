matrix = []
for i in range(3):
    row = []
    for j in range(3):
        x = int(input(f"Enter element [{i}][{j}]: "))
        row.append(x)
    matrix.append(row)

print("\nMatrix:")
for r in matrix:
    print(r)
