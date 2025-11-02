fruits=["apple","banana","cherry","kiwi","mango"]
new=[i for i in fruits if "a" in i]
print(new)
upper=[i.upper() for i in fruits]
print(upper)
s=["orange"]
new_list=["orange" if i=="banana" else i for i in fruits]
print(new_list)