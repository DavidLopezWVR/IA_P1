'''
La función input().
La función input() es capaz de leer datos que fueron introducidos por el usuario y pasar esos datos al programa en ejecución.
El programa entonces puede manipular los datos, haciendo que el código sea verdaderamente interactivo.
'''
print("Dime lo que sea...")
anything = input()
print("Hmm...", anything, "... ¿en serio?")

# La función input() es invocada sin argumentos (es la manera mas sencilla de utilizar la función); 
# la función pondrá la consola en modo de entrada; aparecerá un cursor que parpadea, y podrás introducir datos con el teclado, 
# al terminar presiona la tecla Enter.

'''La función input() con un argumento'''
#La función input() puede hacer otra cosa: puede avisar al usuario sin ninguna ayuda de print().
anything = input("Dime lo que sea...")
print("Hmm...", anything, "...¿en serio?")

#Esta variante de la invocación de input() simplifica el código y lo hace más claro.

'''El resultado de la función input()'''
# El resultado de la función input() es una cadena. Una cadena que contiene todos los caracteres que el usuario introduce desde el teclado. No es un entero ni un flotante.
anything = input("Ingresa un número:")
something = anything ** 2.0
print(anything, "al cuadrado es", something)
#Esto significa que no se debe utilizar como un argumento para operaciones matemáticas

''' Conversión de tipos 1'''
#Python ofrece dos simples funciones para especificar un tipo de dato y resolver este problema, aquí están: int() y float().
#   La función int() toma un argumento (por ejemplo, una cadena: int(string)) e intenta convertirlo a un valor entero.
#   La función float() toma un argumento (por ejemplo, una cadena: float(string)) e intenta convertirlo a flotante.
anything = float(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "a la potencia de 2 es", something)

'''Operadores cadena'''
#Los operadores aritmeticos + y * tienen una funcion secundaria. Son capaces de manipular cadenas de manera muy especifica.

'El signo de + (más), al ser aplicado a dos cadenas, se convierte en un operador de concatenación:'
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")
#Simplemnete concatena(junta) dos cadenas en una. Se puede utilizar mas de una vez en una misma expresión, y se comporta connenlazado izquierdo.
'>>> El signo + (mas) funciona como concatenador siempre y cuando ambos argumnetos sean cadenas' #NO puede mezclar los tipos de datos.

'El signo * (asterisco), cuando es aplicado a una cadena y a un número se convierte en un operador de replicacion:'
#Replica la cadena el numero de ces indicado por el numero
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

'''Conversiones de tipos 2'''
# También se puede convertir un numero a una cadena, lo cual es más fácil y seguro. La funcion capaz de hacer esto se llama:
'str(*number)'
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))
#Gracias a la funcion str() podemos pasar el resultado entero a la funcion print() como una sola cadena, sin utilizar comas.
