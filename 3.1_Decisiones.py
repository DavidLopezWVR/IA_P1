# Una computadora ejecuta el programa y proporciona las respuestas. El programa debe ser capaz de reaccionar de acuerdo con las respuestas recibidas.
#Afortunadamente, las computadoras solo conocen dos tipos de respuestas:
#Si, es cierto.
#No, esto es falso
'Para hacer preguntas, Python utiliza un conjunto de operadores muy especiales'

'''Comparación: operador de igualdad'''
#Pregunta: ¿son dos valores iguales?
'>>>Igualdad: El operador igual a (==)'
#El operador == (igual a) compara los valores de dos operandos. Si son iguales, el resultado de la comparación es True. Si no son iguales, el resultado de la comparación es False.
var = 0  # Asignando 0 a var
print(var == 0)                 #Salida True

var = 1  # Asignando 1 a var
print(var == 0)                #Salida False

'>>>Desigualdad: el operador no es igual a (!=)'
#El operador != (no es igual a) también compara los valores de dos operandos. Aquí está la diferencia: si son iguales, el resultado de la comparación es False. 
# Si no son iguales, el resultado de la comparación es True.
var = 0  # Asignando 0 a var
print(var != 0)                #Salida False
 
var = 1  # Asignando 1 a var
print(var != 0)                #Salida True
 
'>>>Operadores de comparación: mayor que'
#También se puede hacer una pregunta de comparación usando el operador > (mayor que).
100 >  2000    #True lo confirma; False lo niega. 

'>>>Operadores de comparación: mayor o igual que'
#El operador mayor que tiene otra variante especial, una variante no estricta, pero se denota de manera diferente que la notación aritmética clásica: >= (mayor o igual que).
centigrade_outside = 0.0
centigrade_outside >= 0.0  # Mayor o igual que

'>>>Operadores de comparación: menor o igual que'
#Los operadores utilizados en este caso son: El operador < (menor que) y su hermano no estricto: <= (menor o igual que).
current_velocity_mph  = 85           
#la primera pregunta es estricta, la segunda no
current_velocity_mph < 85  # Menor que
current_velocity_mph <= 85  # Menor o igual que
 
'''TABLA DE PRIORIDADES

+=============+================+===========+
|  Prioridad  |    Operador    |           |
|_____________|________________|___________|
|      1      |      + , -     | unario    |
|_____________|________________|___________|
|      2      |       **       |           |
|_____________|________________|___________|
|      3      |  *, /, //, %   |           |
|_____________|________________|___________|
|      4      |      + , -     | binario   |
|_____________|________________|___________|
|      5      |  <, <=, >, >=  |           |
|_____________|________________|___________|
|      6      |     ==, !=     |           |
|_____________|________________|___________|

'''

'ESCENARIO'
n = int(input("Ingresa un número: "))
print(n >= 100)

'>>> Condiciones y ejecución condicional'
#Esta sentencia condicional consta de los siguientes elementos, estrictamente necesarios en este orden:
'''
-La palabra clave reservada if;
-Uno o más espacios en blanco;
-Una expresión (una pregunta o una respuesta) cuyo valor se interpretar únicamente en términos de True (cuando su valor no sea cero) y False (cuando sea igual a cero);
-Unos dos puntos seguidos de una nuevalínea;
-Una instrucción con sangría o un conjunto de instrucciones (se requiere absolutamente al menos una instrucción); 
 la sangría se puede lograr de dos maneras: insertando un número particular de espacios (la recomendación es usar 
 cuatro espacios de sangría), o usando el tabulador; nota: si hay mas de una instrucción en la parte con sangría, 
 la sangría debe ser la misma en todas las líneas; aunque puede parecer lo mismo si se mezclan tabuladores con espacios, 
 es importante que todas las sangrías sean exactamente iguales Python 3 no permite mezclar espacios y tabuladores para la sangría.
'''
#Si la expresión sheep_counter no representa la verdad (es decir, su valor es igual a cero), las sentencias con sangría se omitirán
#Si la expresión sheep_counter no representa la verdad (es decir, su valor es igual a cero), las sentencias con sangría se omitirán (ignorado), y la siguiente instrucción ejecutada será la siguiente al nivel de la sangría original.
#if sheep_counter >= 120:
#    make_a_bed()
#    take_a_shower()
#    sleep_and_dream()
#feed_the_sheepdogs()
 

'''La sentencia elif'''
#elif se usa para verificar más de una condición, y para detener cuando se encuentra la primera sentencia verdadera.
'''
if si_el_clima_esta_bien:
    salimos_a_caminar()
elif si_hay_entradas_diponibles:
    vamos_al_teatro()
elif si_hay_mesas_disponibles:
    vamos_a_almorzar()
else:
    juagaremos_ajedrez_en_casa()
'''
#La forma de ensamblar las siguientes sentencias if-elif-else a veces se denomina cascada.

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

numero_mayor = numero1 

if numero2 > numero_mayor:
    numero_mayor = numero2
    
if numero3 > numero_mayor:
    numero3 = numero_mayor
    
print("El numero mayor es: ", numero_mayor)

# Se leen tres números.
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))
 
# Verifica cuál de los números es el mayor
# y pásalo a la variable largest_number.
 
largest_number = max(number1, number2, number3)
 
# Imprime el resultado.
print("El número más grande es:", largest_number)

#De la misma manera, puedes usar la función min() para devolver el número más pequeño.

'''>>>Hay una función llamada round() que hará el redondeo por '''