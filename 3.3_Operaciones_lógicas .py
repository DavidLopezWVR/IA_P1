'''
TABLAS DE VERDAD'
and                                         or
+-------------------------+                 +-------------------------+
|   A   |   B   | A and B |                 |   A   |   B   | A or B  |
+-------------------------+                 +-------------------------+
|   0   |   0   |    0    |                 |   0   |   0   |    0    |
+-------------------------+                 +-------------------------+
|   0   |   1   |    0    |                 |   0   |   1   |    1    |
+-------------------------+                 +-------------------------+
|   1   |   0   |    0    |                 |   1   |   0   |    1    |
+-------------------------+                 +-------------------------+
|   1   |   1   |    1    |                 |   1   |   1   |    1    |
+-------------------------+                 +-------------------------+

not
+---------------+     
|   A   |   !A  |
+---------------+
|   0   |   1   |    
+---------------+
|   1   |   0   |    
+---------------+

# Ejemplo 1:
print(var > 0)
print(not (var <= 0))
 
 
# Ejemplo 2:
print(var != 0)
print(not (var == 0))
 
'''

'''>>>Operadores bit a bit'''
# Hay cuatro operadores que le permiten manipular bits de datos individuales. Se denominan operadores bit a bit.
'''
Aquí están todos ellos:

- & (ampersand) - conjunción a nivel de bits;
- | (barra vertical) - disyunción a nivel de bits;
- ~ (tilde) - negación a nivel de bits;
- ^ (signo de intercalación) - o exclusivo a nivel de bits (xor). Si el numero de 1s es par la salida sera un 0
'''
#Agreguemos un comentario importante: los argumentos de estos operadores deben ser enteros; no debemos usar flotantes aquí.

'''>>>Desplazamiento binario a la izquierda y desplazamiento binario a la derecha'''
#desplazar un valor un bit a la izquierda corresponde a multiplicarlo por dos; 
#respectivamente, desplazar un bit a la derecha es como dividir entre dos (observa que se pierde el bit más a la derecha).

'''
valor << bits
valor >> bits
'''                                       #   64  32  16  8  4  2  1
var = 17                                  #    0   0  1   0  0  0  1
var_right = var >> 1                      #    0   0  0   1  0  0  0
var_left = var << 2                       #    1   0  0   0  1  0  0
print(var, var_left, var_right)           #Salida  17 68 8

"""
TABLA DE PRIORIDAD ACTUALIZADA
+=============+======================================================+===========+
|  Prioridad  |    Operador                                          |           |
|_____________|______________________________________________________|___________|
|      1      |      ~, + , -                                        | unario    |
|_____________|______________________________________________________|___________|
|      2      |         **                                           |           |
|_____________|______________________________________________________|___________|
|      3      |    *, /, //, %                                       |           |
|_____________|______________________________________________________|___________|
|      4      |       + , -                                          | binario   |
|_____________|______________________________________________________|___________|
|      5      |      << , >>                                         |           |
|_____________|______________________________________________________|___________|
|      6      |  <, <=, >, >=                                        |           |
|_____________|______________________________________________________|___________|
|      7      |     ==, !=                                           |           |
|_____________|______________________________________________________|___________|
|      8      |        &                                             |           |
|_____________|______________________________________________________|___________|
|      9      |        |                                             |           |
|_____________|______________________________________________________|___________|
|     10      |     =, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=      |           |
|_____________|______________________________________________________|___________|

"""
#x = 15, el cual es 0000 1111 en binario,
#y = 16, el cual es 0001 0000 en binario. 
# 
# & hace un bit a bit and (y), por ejemplo, x & y = 0, el cual es 0000 0000 en binario,
# | hace un bit a bit or (o), por ejemplo, x | y = 31, el cual es 0001 1111 en binario,
# ~ hace un bit a bit not (no), por ejemplo, ˜ x = 240*, el cual es 1111 0000 en binario,    Alt + 126 para ~
# ^ hace un bit a bit xor, por ejemplo, x ^ y = 31, el cual es 0001 1111 en binario,
# >> hace un desplazamiento bit a bit a la derecha, por ejemplo, y >> 1 = 8, el cual es 0000 1000 en binario,
# << hace un desplazamiento bit a bit a la izquierda, por ejemplo, y << 3 = 128, el cual es 1000 0000 en binario.
