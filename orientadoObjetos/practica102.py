"""
sort y sorted
pg.82
"""
import copy


name_age = [ ['Tom', 20], ['Jerry', 15], ['Pluto', 25] ]
print(name_age)
# sort by name
name_age.sort(key=lambda name: name[0])
print("Ordenado por nombre: " + str(name_age))
# sort by age
name_age.sort(key=lambda age: age[1])
print("Ordenando por edad: " + str(name_age))
x = []
print("order no devuelve la lista ordenada sino que la ordena por lo que no tiene sentido asignarla a una variable")
x = name_age.sort(key=lambda age: age[1])
print(x) # nothing is saved in x
print("Tenemos que usar sorted para salvar la lista ordenada en una variable")
y1 = sorted(name_age, key=lambda age: age[1]) # sorted() : by age
print(y1)
y2 = sorted(name_age, key=lambda age: age[1]) # sorted() : by name
print(y2)
print(y1 == y2)
y1[0][1] = 5
print(y1)
print(y2)
# lo dejamos como estaba
y1[0][1] = 20
#
print("--------------Ahora con deep copy----------------")
y1 = copy.deepcopy(sorted(name_age, key=lambda age: age[1]))
print(y1)
y2 = copy.deepcopy(sorted(name_age, key=lambda age: age[1]))
print(y2)
print(y1 == y2)
y1[0][1] = 5
print(y1)
print(y2)