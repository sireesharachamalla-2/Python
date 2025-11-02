friends_colors = [
    ["red", "blue"],
    ["green", "red"],
    ["yellow", "blue"]
]

u = set()

for colors in friends_colors:
    u.update(colors)

print(u)