t = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
c="White"
for i in t:
    if c in i:
        print(True)
        break

    else:
        print(False)