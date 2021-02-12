"""
shallow copy, copy  y deep copy
"""
import copy

a = [1,2,[3,4]]
#
b = list(a) # Tanto a "b" como a "c" le afectan los cambios que se realicen en referencias en el interior de "a"
c = copy.deepcopy(a) # LOs cambios posteriores en "a" no le afecta
d = a.copy()
#
print("a: " + str(a))
print("b: " + str(b))
print("c: " + str(c))
print("d: " + str(d))
#
print("Añadimos el número 5 a a[2] y el 6 a a")
a[2].append(5)
a.append(6)
#
print("a: " + str(a))
print("b: " + str(b))
print("c: " + str(c))
print("d: " + str(d))