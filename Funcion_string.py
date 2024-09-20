'''
Trabajando con la función print()
+===================================+
|  print(*objects,sep ='',end='\n') |
+===================================+
'''
#¿Qué argumnetos espera print()?
# Cualquiera. print() puede operara cn practicamnete todos los tipos de datos que pfrece Python.
#Cadenas, numeros, carcateres, valores logcos, objetos -cualquiera de estos puede pasar con exito.

#¿Qué valor devuelve?
#Ninguno. Su efcto es suficiente.

print("La Witsi Witsi Araña subió a su telaraña.")
print()                                                   #Salto de linea con print sin argumento
print("Vino la lluvia y se la llevó.")


'''Caracteres de escape y nueva línea en Python'''

#La barra invertida (\) tiene un significado muy especial cuando se usa dentro de cadenas - se llama carácter de escape.
#la barra invertida no significa nada en sí misma, sino que es solo una especie de anuncio de que el siguiente carácter después de la barra invertida también tiene un significado diferente.
#La la letra n colocada después de la barra invertida proviene de la palabra newline.
#Tanto la barra invertida como n forman un símbolo especial llamado un carácter de nuevalínea, que insta a la consola a iniciar una nuevalínea de salida.
print("\nLa Witsi Witsi Araña\nsubió a su telaraña.")
print()
print("Vino la lluvia\ny se la llevó.")

'''Usando múltiples argumentos'''

#Invocación de la función print(), pero contiene tres argumentos. Todos ellos son cadenas. 
print("La Witsi Witsi Araña" , "subió" , "a su telaraña.")
#Los argumentos están separados por comas


'''Argumentos posicionales''' 

#Este nombre proviene del hecho de que el significado del argumento está dictado por su posición (por ejemplo, el segundo argumento se mostrará después del primero, no al revés).
print("Mi nombre es", "Python.")
print("Monty Python.")


'''Argumentos de palabra clave'''

#La función print() tiene dos argumentos de palabra clave que puedes usar para tus propósitos. 
# El primero se llama end.
#El argumento de palabra clave end determina los caracteres que la función print() envía a la salida una vez que llega al final de sus argumentos posicionales.
print("Mi nombre es ", end="# ")
print("Monty Python.")

#El segundo se llama sep.
#El argumneto de la palabra clave sep separa los ragumnetos de la funcion print con el carcaterec que le asignemos
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")


'''DANDO FORMATO A LA SALIDA'''
print("""
        #%:.     
 #%=   ###%=:    
##%=   |##%::    
##%=   ###%=:    
 #%%=  |##%=:    
 ##%== ###%=:    ===
  ##%%=!##%=:    ====
   ###%%##%=   :==== 
    ######%=: .:==== 
      ####%%======= 
       ###%%%===: 
       |%#%%=:=:  
       ####%=:   
       |##%%:    
-------####%:---=
       |%#%%:    
""")