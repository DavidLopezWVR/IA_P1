'''
Un operador es un símbolo del lenguaje de programación, el cual es capaz de realizar operaciones con los valores.
+=====+
|     |
|  +  |
|  -  |
|  *  |
|  /  |
| //  |
|  %  |
|  ** |
|     |
+=====+
'''
# Cuando los datos y operadores se unen, forman juntos expresiones. La expresión más sencilla es el literal.
'''Exponenciación'''
print(2 ** 3)                             #Cuando ambos ** argumentos son enteros, el resultado es entero, también.
print(2 ** 3.)                            #Cuando al menos un ** argumento es flotante, el resultado también es flotante.
print(2. ** 3)
print(2. ** 3.)

'''Multiplicación'''
# Un símbolo de * (asterisco) es un operador de multiplicación.
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

'''División'''
# Un símbolo de / (diagonal) es un operador de división.
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
#El resultado producido por el operador de división siempre es flotante, sin importar si a primera vista el resultado es flotante: 1 / 2, o si parece ser completamente entero: 2 / 1

'''División entera'''
# Un símbolo de // (doble diagonal) es un operador de división entera. los resultados siempre son redondeados
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
#El resultado de la división entera siempre se redondea al valor entero inferior mas cercano del resultado de la división no redondeada.
'>>>Esto es muy importante: el redondeo siempre va hacia abajo.' #Ejemplo:
print(-6 // 4)       #Salida: -2
print(6. // -4)      #Salida: -2.0
#La division entera también se le suele llamar en inglés floor division.

'''Residuo (módulo)'''
#Su representación gráfica en Python es el símbolo de % (porcentaje).
#El resultado de la operación es el residuo que queda de la división entera. En otras palabras, es el valor que sobra después de dividir un valor entre otro para producir un resultado entero.
print(14 % 4)       #14 // 4 da como resultado un 3 → esta es la parte entera, es decir el cociente;
                    #3 * 4 da como resultado 12 → como resultado de la multiplicación entre el cociente y el divisor;
                    #14 - 12 da como resultado 2 → este es el residuo.

'''Suma'''
#El símbolo del operador de suma es el + (signo de más), el cual esta completamente alineado a los estándares matemáticos.
print(-4 + 4)
print(-4. + 8)

'''El operador de resta, operadores unarios y binarios'''
#El símbolo del operador de resta es obviamente - (el signo de menos), sin embargo debes notar que este operador tiene otra función - puede cambiar el signo de un número.
print(-4 - 4)
print(4. - 8)
print(-1.1)

'''
LISTA DE PRIORIDADES (de la más alta (1) a la más baja (4) prioridad.)
+=====+========================================================+
|  1  |  **                                                    |
|_____|________________________________________________________|
|  2  |  +,- (Los operadores unarios a la derecha del operador |
|     |       expenecial enlazan con mayor fuerza.)            |
|_____|________________________________________________________|
|  3  |  *,/,//,%                                              |
|_____|________________________________________________________|
|  4  |  +,-                                                   |
+=====+========================================================+
'''

'''Operadores y paréntesis'''
#Por supuesto, se permite hacer uso de paréntesis, lo cual cambiará el orden natural del cálculo de la operación.
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)