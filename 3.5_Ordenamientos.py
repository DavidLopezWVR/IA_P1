'''
Ordenamiento Burbuja
Se usa muy raramente, y ciertamente no para listas extensas.
La esencia de este algoritmo es simple: comparamos los elementos adyacentes y, al intercambiar algunos de ellos, logramos nuestro objetivo.
'''

'''Ordenando una lista'''
my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

'El ordenamiento burbuja - versión interactiva'
my_list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nOrdenada:")
print(my_list)

'>>> Si quieres que Python ordene tu lista, puedes hacerlo de la siguiente manera:'
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)
