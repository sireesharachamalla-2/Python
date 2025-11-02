def snake_to_pascal(n):
    parts = n.split('_')
    pascal_str = ''.join(word.title() for word in parts)
    return pascal_str

n=input()
print(snake_to_pascal(n))