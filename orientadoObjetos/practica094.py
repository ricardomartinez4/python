"""
Iteración
"""
x = [10,11,12,13,14,15]
# Creamos un iterator sobre la lista:
y = x.__iter__()
print(y.__next__())
print(y.__next__())
while 1:
    try:
        print(y.__next__(), end=", ")
    except StopIteration:
        break    