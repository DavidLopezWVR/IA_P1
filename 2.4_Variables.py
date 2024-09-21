'''
Variables.
Python ofrece "cajas" (o "contenedores") especiales para almacenar valores numericos o cadenas, estas cajas son llamadas variables. 
El nombre mismo sugiere que el contenido de estos contenedores puede variar en casi cualquier forma.

Componentes o elementos de una variable
+===================================+
| - Un nombre                       |
| - Un valor (contenido)            |
+===================================+
'''

'''
Si se desea nombrar una variable, se deben seguir las siguientes reglas:
+=======================================================================================================================+
| * El nombre de la variable debe de estar compuesto por MAYÚSCULAS, minúsculas, dígitos, y el carácter _ (guion bajo)  |
| * El nombre de la variable debe comenzar con una letra                                                                |
| * El carácter guion bajo es considerado una letra                                                                     |
| * Las mayúsculas y minúsculas se tratan de forma distinta                                                             |
| * El nombre de las variables no pueden ser igual a alguna de las palabras reservadas de Python                        |
+=======================================================================================================================+
'''

#Nombres de variable que son CORRECTOS:
['MyVariable', 'i', 'l', 't34', 'contador', 'Adios_señora']

#Nombres de variable que son INCORRECTOS:
# 10t (no comineza con una letra) 
# !importante (no comineza con una letra)  
# color imagen (contiene un espacio) 

'''Palabras Clave'''
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


'''Cómo crear una variable'''
#Una variable se crea cuando se le asigna un valor. A diferencia de otros lenguajes de programación, no es necesario declararla.
'>>>La creación (o su sintaxis) es muy simple: solo utiliza el nombre de la variable deseada, después el signo de igual (=) y el valor que se desea colocar dentro de la variable.'
var = 1
print(var)

'''Cómo emplear una variable'''
#Se tiene permitido utilizar cuantas declaraciones de variables sean necesarias para lograr el objetivo del programa, por ejemplo:
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

'''Cómo asignar un nuevo valor a una variable ya existente'''
#El signo de igual es de hecho un operador de asignación.
var = 1
print(var)
var = var + 1
print(var)

'''Resolviendo problemas matemáticos simples'''
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

'''Operadores Abreviados
# Se desea utilizar la misma variable al lado derecho y al lado izquierdo del operador = operator. Por ejemplo: x = x * 2  o  sheep = sheep + 1

+=================================+==================================+
|            Expresion            |        Operador abreviado        |
+=================================+==================================+
|          i = i +2 * j           |            i += 2*j              |
|          var = var/2            |            var /= 2              |
|         rem = rem % 10          |            rem %= 10             |
|     j = j - (i + var + rem)     |      j -= (i + var + rem)        |
|           x = x ** 2            |            x **= 2               |
+=================================+==================================+
'''
