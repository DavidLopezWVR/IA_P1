#Practica de Módulo 2
#Estes programa nos ayudara con un tema importante en el analisis de vibraciones mecanicas que es determinar la Rigidez Equivalente (Ke) de algunos sistemas.
#El sistema que anlizaremos es la de una Viga simplemente apoyada, enunidades de el Sisitema Internacional (metro,Kilogramo,segundo).

print("""
Viga Simplemente Apoyada
                     
                               Fuerza o carga               Ke =   3 E I(a + b)       Donde: Ke = Rigidez equivalente   [N/m].
                                                                 ----------------             E = Modulo de elasticidad  [Pa].
                                      |                               a^2 b^2                 I = Inercia de área       [m^4].
                                      ↓                                                       a = Distancia del punto A a la 
 |<---------------- a --------------->|<---- b ---->|                                             fuerza o carga aplicada [m].  
  __________________________________________________                                          b = Distancia del punto B a la
 |  ___                                      ___    |                                             fuerza o carga aplicada [m].          
 |_/ o \\ _______|___________________________/ o \\___|   
 _/_____\\_      |                         _/_____\\_ 
 /////////      |                        //////////
     A          |                             B
                +---> E
""")
#Para poner guion arriba Alt + 238
print("Ingrese el Modulo de elasticidada de la viga,", end=" recuerde que 6X10^9 = 6e9\n")
modulo = float(input())
distancia_A = float(input("Ingrese la distancia del punto \"A\" a la carga:"))
distancia_B = float(input("Ingrese la distancia del punto \"B\" a la carga:"))
mensaje1 = '\tPara calcular la Inercia de área necesitamos tener un corte transversal de la viga '
print('\n',mensaje1 + 'y obtener \n\tel largo "b" y altura "h" de la geometria.')

print('''                  
                  y        Rectangulo:          b h^3            
                  |                      Ix =  -------
                  |                               12
 _______ _________↓________   
  h   __|//////////////////| _______x
 _|_____|__________________|
                  |
        |<------- b ------>|

''')

largo = float(input("Ingrese el largo del rectangulo [m], 'b':\n"))
altura = float(input("Ingrese la altura del rectangulo [m], 'h':\n"))
Ix = (largo*altura**3)/ 12
print("La Inercia de area de la viga es de:" + str(Ix) + "m^4", end="\n" )
kequi = (3 * modulo * Ix * (distancia_A + distancia_B))/(distancia_A**2*distancia_B**2)
print("\nLa Rigidez equivalente del sistema es de: " , kequi, "N/m")

