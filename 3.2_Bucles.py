'''>>>Bucles con while (mientras)'''
# if realiza sus sentencias sólo una vez; while repite la ejecución siempre que la condición se evalúe como True.

'''
while conditional_expression:
    instruction_one
    instruction_two
    instruction_three
    :
    :
    instruction_n
'''
'Bucle infinito'
#while True:
#    print("Estoy atrapado dentro de un bucle.")

# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande.
print("El número más grande es:", largest_number)

'DETECTAR CANTIDAD DE NUMEROS PARES E IMPARES'
odd_numbers = 0
even_numbers = 0
 
# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))
 
# 0 termina la ejecución.
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))
 
# Imprimir resultados.
print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares:", even_numbers)

'''>>>Empleando contadores para salir del bucle'''
counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)


'''>>>Bucles con for (por)'''
#En realidad, el bucle for está diseñado para realizar tareas más complicadas, puede "explorar" grandes colecciones de datos elemento por elemento.
'''
for i in range(100):
    # do_something()
    pass
    
'''
# La función range() (esta es una función muy especial) es responsable de generar todos los valores deseados de la variable de control.
# La función range() comienza su trabajo desde 0 y lo finaliza un paso (un número entero) antes del valor de su argumento.
# ****nota la palabra clave pass dentro del cuerpo del bucle - no hace nada en absoluto; es una instrucción vacía - 
#     la colocamos aquí porque la sintaxis del bucle for exige al menos una instrucción dentro del cuerpo.

for i in range(10):                           # i toma los valores de 0 - (10-1)
    print("El valor de i es", i)

for i in range(2, 8):                          # i toma los valores de 2 - (8-1)
    print("El valor de i es", i)

for i in range(2, 8, 3):                       # el tercer argumento indica el paso, que en realidad significa la diferencia entre cada número en la secuencia de números generados por la función. (i+3)
    print("El valor de i es", i)

'PRIMERAS 16 POTENCIAS DE 2'
power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2

'''>>>Las sentencias break y continue''' 
#break - sale del bucle inmediatamente, e incondicionalmente termina la operación del bucle; el programa comienza a ejecutar la instrucción más cercana después del cuerpo del bucle.
#continue - se comporta como si el programa hubiera llegado repentinamente al final del cuerpo; el siguiente turno se inicia y la expresión de condición se prueba de inmediato.

# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

'----------------------------------------------------------------------------------------------------------------------'
# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

'-----------------------------------------------------------------------------------------------------------------------'
largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")

'-----------------------------------------------------------------------------------------------------------------------'
largest_number = -99999999
counter = 0

number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

if counter:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")
