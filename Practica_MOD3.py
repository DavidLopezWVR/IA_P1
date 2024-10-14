#La idea es crear una calculadora de matrices.
#Iniciaremos con matrices de 3 X 3 , con las operaciones de suma, resta

#Funcion para mostrar la introduccion al programa
def intro():    
    intro = "Esta es una calculadora de matrices con la que podras realizar operaciones basicas como la suma y la resta"
    print(3*"\t","MATRIX F001 \n", intro)

#Funcion para crear la matriz 'A'.
def crear_matriz_A(): #Nombre de la funcfion si parametros.
    print("\nComo primer paso determinemos el numero de filas y columnas de la matriz 'A'")

    A_filas = int(input("Ingrese el numero de filas:\t")) #El usuario ingresa el numero de filas y se guardan en la variable A_filas.
    A_columnas = int(input("Ingrese el numero de columnas:\t")) #El usuar ingresa el numero de columnas y se guardan en la variable A_columnas.

    matriz_A = [[0.0 for C in range(A_columnas)] for F in range(A_filas)] #Creamos la matriz A con el nombre de matriz_A de acuerdo a las especificaciones antes ingresadas.

    #Interaccion con el usuario para que ingrese los datos de la matriz.
    for x in range(A_filas):#Este ciclo for itera sobre las filas de la matriz.
        for y in range(A_columnas):#Este ciclo for itera las columnas de la matriz.
            valor = float(input(f"Ingrese el valor para la posición [{x+1}, {y+1}]: "))#declaramos la variable de nombre valor para ir guardando los valores ingresados(de tipo flotante).
            matriz_A[x][y] = valor #Guardamos cada valor ingresado de acuerdo a la posicion fila-columna de la matriz A.
    return matriz_A  #Retornamos la matriz A para usarla posteriomente.

#Funcion para crear la matriz 'B'.
def crear_matriz_B():#Nombre de la funcfion si parametros.
    print("\nComo segundo paso determinemos el numero de filas y columnas de la matriz 'B'")

    B_filas = int(input("Ingrese el numero de filas:\t")) #El usuario ingresa el numero de filas y se guardan en la variable B_filas.
    B_columnas = int(input("Ingrese el numero de columnas:\t")) ##El usuar ingresa el numero de columnas y se guardan en la variable B_columnas.

    matriz_B = [[0.0 for C in range(B_columnas)] for F in range(B_filas)] #Creamos la matriz B con el nombre de matriz_B de acuerdo a las especificaciones antes ingresadas.

    for x in range(B_filas):#Este ciclo for itera las filas de la matriz.
        for y in range(B_columnas):#Este ciclo for itera sobre las columnas de la matriz.
            valor = float(input(f"Ingrese el valor para la posición [{x+1}, {y+1}]: "))#declaramos la variable de nombre valor para ir guardando los valores ingresados(de tipo flotante).
            matriz_B[x][y] = valor#Guardamos cada valor ingresado de acuerdo a la posicion fila-columna de la matriz B.
    return matriz_B#Retornamos la matriz A para usarla posteriomente.

#Definicion de la funcion operacion_suma para sumar las matrices.
def operaciom_suma(matriz_A,matriz_B):#Nombre de la funcion con parametros.
    filas = len(matriz_A) #Utilizamos la funcion len() para obtener el numero de filas de alguna de las matrices (en este caso la matriz A).
    columnas = len(matriz_A[0]) #Nuevamente Utilizamos la funcion len() para obtener el numero de columnas de la matriz A pero en la posicio [0].

    matriz_suma = [[0.0 for C in range(columnas)] for F in range(filas)]#Creamos la matriz_suma con los datos obtenidos anteriormente.
    
    for x in range(filas):#Este ciclo nos ayuda para movernos por las filas de la matriz_suma.
        for y in range(columnas):#Este ciclo nos ayuda para movernos por las filas de la matriz_suma.
            matriz_suma[x][y] = matriz_A[x][y] + matriz_B[x][y] #Procedemos a hacer la suma. De acuerdo a la Algebra vectorial la suma  La matriz suma se obtienen sumando .
                                                                #los elementos de las dos matrices que ocupan la misma posición.                                                            
    return matriz_suma

#Desfinimos una funcion para imprimir las matrices.
def imprimir_matriz(matriz,nombre_matriz): #Funcion imrprimir_matriz con parametros.
    print(f"\n{nombre_matriz}")#De acuero a la cadena que se resive en la invocacion de la funcion se mostrara el nombre de la matriz.
    for fila in matriz: #Por cada fila de la matriz que se esta evaluando.
        print(fila)     #Que haga un salto de linea y se imprima la  fila.


intro() #se invoca la funcion intro sin argumnetos
matriz_A = crear_matriz_A() #Se crea la variable matriz_A que invoca a la funcion crear_matriz_A y que guarda los datos que se retonrnaron en la funcion crear_matriz_A().
matriz_B = crear_matriz_B() #Se crea la variable matriz_A que invoca a la funcion crear_matriz_B y que guarda los datos que se retonrnaron en la funcion crear_matriz_B().
matriz_suma = operaciom_suma(matriz_A,matriz_B) #Se crea una variable matriz_suma para invocar a la funcion operacion_suma con los parametros matriz_A, matriz_B.

imprimir_matriz(matriz_A,"Matriz A") #Invocamos la funcion imprimir_matriz con los argumentos matriz_A que es la matriz creada y la cadena "Matriz A" .
imprimir_matriz(matriz_B,"Matriz B")
imprimir_matriz(matriz_suma,"SUMA")


####


