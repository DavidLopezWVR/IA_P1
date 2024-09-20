'''
Los datos en si mismo.
Un literal se refiere a datos cuyos valores están determinados por el literal mismo.
+===================================+
|      10, 3.14, "Hola", True       |
+===================================+
'''
# Se puede elegir el valor correcto sin algo de conocimiento adicional.
#Ejemplo:       #Encontramos dos tipos diferentes de literales
print("2")      #UNA CADENA
print(2)        #UN NUMERO ENTERO

#La función print() los muestra exactamente de la misma manera - Sin embargo, internamente, la memoria de la computadora los almacena de dos maneras completamente diferentes 
# - La cadena existe como eso solo una cadena - una serie de letras.
# - El número es convertido a una representación máquina (una serie de bits).

#Si se codifica un literal y se coloca dentro del código de Python, la forma del literal determina la representación (tipo) que Python utilizará para almacenarlo en la memoria.

'''Enteros'''
#Enteros, es decir, aquellos que no tienen una parte fraccionaria. Ejemplo: 100   256  900  5  1
#Forma incorrecta de escribir numeros enteros de gran tamaño
# 11 111 111                             *Utilizar espacios 
'>>> Dos formas correctas de escribir numeros enteros de gran tamaño'
# 11111111      o    11_111_111          *Separarlo con guiones bajos.

'''Flotantes'''
#Los flotantes tienen una parte decimal no vacía (una parte fraccionaria después del punto decimal). Ejemplo: 0.4  1.5  3.2
#Enteros vs Flotantes
#El punto decimal es esencialmente importante para reconocer números punto-flotantes en Python.
#    4                  *Entero
#    4.0                *Flotante
#El punto decimal es lo que determina si es flotante.
#¿Cómo almacenar números que son muy pequeños? Ejemplo:  6.62607 x 10^-34     =    6.62607E-34

'''Cadenas'''
#Las cadenas se emplean cuando se requiere procesar texto (como nombres de cualquier tipo, direcciones, novelas, etc.), no números.
print("Me gusta Monty Python")    #Cadena con comillas dobles
print('Me gusta Monty Python')    #Cadena con comillas simples
print('Me gusta "Monty Python"')  #Solucion para mostrar comillas en una cadena sin utilzar el carcater de escape (\)
#Una cadena vacia sigue siedno una cadena:    " "     ' '

''' Valores Booleanos'''
# Se emplean para representar un valor muy abstracto - la veracidad.
#Provienen de la Algebra Booleana- una parte del álgebra que hace uso de dos valores:True y False, denotados como 1 y 0.
'''
las computadoras solo conocen dos tipos de respuestas:
Si, esto es verdad.  (1)
No, esto es falso.   (0)
'''
print(True > False)      # Uno es mayor a cero? = True(verdadero)
print(True < False)      # Uno es menor a cero? = False(falso)