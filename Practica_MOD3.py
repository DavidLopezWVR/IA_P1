#La idea es crear una calculadora de matrices.
#Iniciaremos con matrices de 3 X 3 , con las operaciones de suma, resta

def intro():    
    intro = "Esta es una calculadora de matrices con la que podras realizar operaciones basicas como la suma y la resta"
    print(3*"\t","MATRIX F001 \n", intro)


def crear_matriz_A():
    print("\nComo primer paso determinemos el numero de filas y columnas de la matriz 'A'")

    A_filas = int(input("Ingrese el numero de filas:\t"))
    A_columnas = int(input("Ingrese el numero de columnas:\t"))

    matriz_A = [[0.0 for C in range(A_columnas)] for F in range(A_filas)]

    for x in range(A_filas):
        for y in range(A_columnas):
            valor = float(input(f"Ingrese el valor para la posición [{x+1}, {y+1}]: "))
            matriz_A[x][y] = valor
    return matriz_A
   

def crear_matriz_B():
    print("\nComo segundo paso determinemos el numero de filas y columnas de la matriz 'B'")

    B_filas = int(input("Ingrese el numero de filas:\t"))
    B_columnas = int(input("Ingrese el numero de columnas:\t"))

    matriz_B = [[0.0 for C in range(B_columnas)] for F in range(B_filas)]

    for x in range(B_filas):
        for y in range(B_columnas):
            valor = float(input(f"Ingrese el valor para la posición [{x+1}, {y+1}]: "))
            matriz_B[x][y] = valor
    return matriz_B

def operaciom_suma(matriz_A,matriz_B):
    filas = len(matriz_A)
    columnas = len(matriz_A[0])

    matriz_suma = [[0.0 for C in range(columnas)] for F in range(filas)]
    
    for i in range(filas):
        for j in range(columnas):
            matriz_suma[i][j] = matriz_A[i][j] + matriz_B[i][j]
    
    return matriz_suma

def imprimir_matriz(matriz,nombre_matriz):
    print(f"\n{nombre_matriz}")
    for fila in matriz:
        print(fila)


intro()
matriz_A = crear_matriz_A()
matriz_B = crear_matriz_B()
matriz_suma = operaciom_suma(matriz_A,matriz_B)

imprimir_matriz(matriz_A,"Matriz A")
imprimir_matriz(matriz_B,"Matriz B")
imprimir_matriz(matriz_suma,"SUMA")


####


