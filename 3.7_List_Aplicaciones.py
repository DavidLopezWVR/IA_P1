''' Listas dentro de listas'''
#El fragmento de código genera una lista de diez elementos y la rellena con cuadrados de diez números enteros que comienzan desde cero.
squares = [x ** 2 for x in range(10)]
print(squares)

#El fragmento crea un arreglo de ocho elementos que contiene las primeras ocho potencias del numero dos
twos = [2 ** i for i in range(8)]
print(twos)

#El fragmento crea una lista con solo los elementos impares de la lista squares.
odds = [x for x in squares if x % 2 != 0 ]
print(odds)



'''Arreglos de dos dimensiones'''
###
EMPTY = "D"
board = []
 
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

'''
la parte interior del bucle crea una fila que consta de ocho elementos (cada uno de ellos es igual a EMPTY) y lo agrega a la lista del board;
la parte exterior se repite ocho veces;
en total, la lista board consta de 64 elementos (todos iguales a EMPTY).

La variable board ahora es un arreglo bidimensional. También se le llama, por analogía a los términos algebraicos, una matriz.
'''

#Como las listas de comprensión puede ser anidadas, podemos acortar la creación del tablero de la siguiente manera:
EMPTY = "2"
board = [[EMPTY for i in range(8)] for j in range(8)]
print(board)

'La parte interna crea una fila, y la parte externa crea una lista de filas.'

'''>>>El acceso al campo seleccionado del tablero requiere dos índices - el primero selecciona la fila; el segundo - el número del campo dentro de la fila, el cual es un número de columna.'''

"""
TABLERO:
             A        B        C        D        E        F        G       H
        +--------+--------+--------+--------+--------+--------+--------+--------+
        | [0][0] | [0][1] | [0][2] | [0][3] | [0][4] | [0][5] | [0][6] | [0][7] |
    8   |        |        |        |        |        |        |        |        |   8
        +--------+--------+--------+--------+--------+--------+--------+--------+
        | [1][0] | [1][1] | [1][2] | [1][3] | [1][4] | [1][5] | [1][6] | [1][7] |
    7   |        |        |        |        |        |        |        |        |   7
        +--------+--------+--------+--------+--------+--------+--------+--------+
        | [2][0] | [2][1] | [2][2] | [2][3] | [2][4] | [2][5] | [2][6] | [2][7] |
    6   |        |        |        |        |        |        |        |        |   6
        +--------+--------+--------+--------+--------+--------+--------+--------+
        | [3][0] | [3][1] | [3][2] | [3][3] | [3][4] | [3][5] | [3][6] | [3][7] |
    5   |        |        |        |        |        |        |        |        |   5
        +--------+--------+--------+--------+--------+--------+--------+--------+
        | [4][0] | [4][1] | [4][2] | [4][3] | [4][4] | [4][5] | [4][6] | [4][7] |
    4   |        |        |        |        |        |        |        |        |   4
        +--------+--------+--------+--------+--------+--------+--------+--------+
        | [5][0] | [5][1] | [5][2] | [5][3] | [5][4] | [5][5] | [5][6] | [5][7] |
    3   |        |        |        |        |        |        |        |        |   3
        +--------+--------+--------+--------+--------+--------+--------+--------+
        | [6][0] | [6][1] | [6][2] | [6][3] | [6][4] | [6][5] | [6][6] | [6][7] |
    2   |        |        |        |        |        |        |        |        |   2
        +--------+--------+--------+--------+--------+--------+--------+--------+
        | [7][0] | [7][1] | [7][2] | [7][3] | [7][4] | [7][5] | [7][6] | [7][7] |
    1   |        |        |        |        |        |        |        |        |   1
        +--------+--------+--------+--------+--------+--------+--------+--------+
             A        B        C        D        E        F        G       H
"""
#TORRES
board[0][0] = 'ROOK'
board[0][7] = 'ROOK'
board[7][0] = 'ROOK'
board[7][7] = 'ROOK'
#CABALLO
board[4][2] = 'KNIGHT'
#Peón a E5:
board[3][4] = 'PAWN'
print(board)


'''Naturaleza multidimensional de las listas: aplicaciones avanzadas'''
#Para crear un arreglo que alamacene valos de temperatuta cada hora del dia por 1 mes
temps = [[0.0 for h in range(24)] for d in range(31)]

'-------------------------------------------------------------------------------------------------'
###Para determinar la temperatura promedio mensual del mediodía. Suponiendo que la temperatura de medianoche se almacena primero. 
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Temperatura promedio al mediodía:", average)

'---------------------------------------------------------------------------------------------'
###Ahora encuentra la temperatura más alta durante todo el mes
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("La temperatura más alta fue:", highest)

'--------------------------------------------------------------------------------------------------'
###Ahora cuenta los días en que la temperatura al mediodía fue de al menos 20 ℃:
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#

hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "fueron los días calurosos.")

#Para crear un arreglo tridimencional que verifique que habitaciones estan ocupadas en cada uno de los tres eificios que cuentan con 15 pisos de 20 cuartos cada uno
#Resume la información disponible: tres edificios, 15 pisos, 20 habitaciones.

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

'Ahora ya puedes reservar una habitación para dos recién casados: en el segundo edificio, en el décimo piso, habitación 14:'
rooms[1][9][13] = True

'y desocupar el segundo cuarto en el quinto piso ubicado en el primer edificio:'
rooms[0][4][1] = False

'Verifica si hay disponibilidad en el piso 15 del tercer edificio:'
vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1


