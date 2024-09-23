'''
Listas.
Variables de múltiples valores.
+===================================+
|   [dato_1, dato_2, ..., dato_n ]  |
+===================================+
'''
'numbers = [10, 5, 7, 2, 1]'    #     [0, 1, 2, ..., n]
#numbers es una lista que consta de cinco valores, todos ellos numeros.
'>>> Los elementos dentro de una lista pueden tener diferentes tipos. Algunos de ellos pueden ser enteros, otros son flotantes y otros pueden ser listas'
'>>> Nuestra lista es una colección de elementos, pero cada elemento es un escalar.'

'''Indexación de listas'''

# ¿Cómo cambias el valor de un elemento elegido en la lista?
'Vamos a asignar un nuevo valor de 111 al primer elemento en la lista'
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista:", numbers)  # Imprimiendo contenido de la lista original.
 
numbers[0] = 111
print("Nuevo contenido de la lista: ", numbers)  # Contenido actual de la lista.

'Ahora queremos copiar el valor del quinto elemento al segundo elemento'
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo contenido de la lista original.
 
numbers[0] = 111
print("\nPrevio contenido de la lista:", numbers)  # Imprimiendo contenido de la lista anterior.
 
numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.
# El valor dentro de los corchetes que selecciona un elemento de la lista se llama un índice, mientras que la operación de seleccionar un elemento de la lista se conoce como indexación.
 
'''Acceso al contenido de las listas'''

print(numbers[0]) # Accediendo al primer elemento de la lista.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

print(numbers) # Imprimiendo la lista completa.

'''Eliminando elementos de una lista'''

#Cualquier elemento de la lista puede ser eliminado en cualquier momento - esto se hace con una instrucción llamada del (eliminar). 
# Nota: es una instrucción, no una función.
del numbers[1]
print(len(numbers))
print(numbers)

'''Los índices negativos son legales'''

#Un elemento con un índice igual a -1 es el último en la lista.
numbers = [111, 7, 2, 1]
print(numbers[-1])


'''Funciones vs métodos'''

'>>>Una función no pertenece a ningún dato - obtiene datos, puede crear nuevos datos y (generalmente) produce un resultado.'
'>>>Un método hace todas estas cosas, pero también puede cambiar el estado de una entidad seleccionada.'
#Un método es propiedad de los datos para los que trabaja, mientras que una función es propiedad de todo el código.

# En general, una invocación de función típica puede tener este aspecto:
'result = function(arg)'
# La función toma un argumento, hace algo, y devuelve un resultado.

#Una invocación de un método típico usualmente se ve así: 
'result = data.method(arg)'
# el nombre del método está precedido por el nombre de los datos que posee el método. 
# A continuación, se agrega un punto, seguido del nombre del método y un par de paréntesis que encierran los argumentos.

'>>>agregar nuevos elementos a una lista existente. Esto se puede hacer con métodos propios de las listas, no por funciones.'

'''Agregando elementos a una lista: append() y insert()'''

#Un nuevo elemento puede ser añadido al final de la lista existente:
'list.append(value)'
#Toma el valor de su argumento y lo coloca al final de la lista que posee el método.

#El método insert() es un poco más inteligente - puede agregar un nuevo elemento en cualquier lugar de la lista, no solo al final.
'list.insert(location, value)'
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

'>>>Puedes iniciar la vida de una lista creándola vacía (esto se hace con un par de corchetes vacíos) y luego agregar nuevos elementos según sea necesario.'
my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

# # # Inverso
my_list = []  # Creando una lista vacía.
 
for i in range(5):
    my_list.insert(0, i + 1)
 
print(my_list)

'''Haciendo uso de las Listas''' 

#calcular la suma de todos los valores almacenados en la lista my_list.
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

#El segundo aspecto del bucle for
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

'Listas en acción'
#Para cambiar sentido de las listas 
'''

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

'''





# 
# 
#   #