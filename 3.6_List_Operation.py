'''
Operaciones con listas
'''
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)   #Salida:   2  ¿Por qué sucede esto?

'''>>>La asignación: list_2 = list_1 copia el nombre del arreglo no su contenido. 
En efecto, los dos nombres (list_1 y list_2) identifican la misma ubicación en la memoria de la computadora. Modificar uno de ellos afecta al otro, y viceversa.'''

# Para copiar su contendo:
# Afortunadamente, la solución está al alcance de tu mano - su nombre es slice.
'Una rebanada es un elemento de la sintaxis de Python que permite hacer una copia nueva de una lista, o partes de una lista.'
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)             #Salida: 1

'''
+===================================+
|       my_list[inicio:fin]         |
+===================================+
'''
#Una rebanada de este tipo crea una nueva lista (de destino), tomando elementos de la lista de origen - los elementos de los índices desde el start hasta el fin fin - 1.
# Copiando la lista completa.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copiando parte de la lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

'+-----------------------------------------------------------------------------------------+'
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)
###
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)

#Copiar toda la lista
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

'''Más sobre la instrucción del'''
#La instrucción del descrita anteriormente puede eliminar más de un elemento de la lista a la vez - también puede eliminar rebanadas:
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)
 
#También es posible eliminar todos los elementos a la vez:
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

#La instrucción del eliminará la lista, no su contenido.
my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list)

'''Los operadores in y not in'''
#Python ofrece dos operadores muy poderosos, capaces de revisar la lista para verificar si un valor específico está almacenado dentro de la lista o no.´
'''
    elem in my_list
    elem not in my_list
'''
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)        #Salida Falce
print(5 not in my_list)    #salida True
print(12 in my_list)       #Salida True

''' Listas - algunos programas simples'''

#El primero de ellos intenta encontrar el valor mayor en la lista
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

#El código puede ser reescrito para hacer uso de la forma recién introducida del bucle for:
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)

#Si necesitas ahorrar energía de la computadora, puedes usar una rebanada:
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list[1:]:
    if i > largest:
        largest = i
 
print(largest)

#Ahora encontremos la ubicación de un elemento dado dentro de una lista:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")





