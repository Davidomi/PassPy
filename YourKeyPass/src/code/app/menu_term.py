#bbdd sqlite


import random
import string

def comparar_numero(valor, valor_correcto):
    
    while valor_correcto == False:
        if valor.isnumeric() == True:
            while valor <= 0:
                print("Error, el valor debe ser positivo")
                valor = int(input("Ingrese el valor: "))
                valor_correcto = True
        elif valor.isnumeric() == False:
            print("Error, el valor debe ser un numero")
            valor = int(input("Ingrese el valor: "))
            valor_correcto = False
            

def Hola_Mundo() :
    print("Hola, bienvenid@ a la aplicación que te va ha solucionar el mayor poroblema que tienes; las CONTRASEÑAS.")
    print("Para empezar, te voy ha explicar como funciona la aplicación en si, a contunuacion tienes un pequeño menu en el que aparece diferentes opciones.")
    print("La primera opcion que tienes es basicamente el crear una contraseña, te va ha pedir que cantidad de caracteres quieres que tenga tu contraseña, y que dificultad quieres")
    print("y te va a devolver una contraseña con esa cantidad de caracteres.")
    print("Piensa que contra mas dificil sea la contraseña, mas dificil va ha ser de romper/hackear aunque tambien va ha ser mas dificil de recordar.")
    Menus()


def Menus():
    print ("MENU:")
    print ("1. Crear contraseña")
    
    opcion = int(input("Ingrese la opcion: "))
    #comparar_numero(opcion, True)
    
    if opcion == 1:
        Create_Password()
    else:
        print("Error, el valor debe ser positivo")
        opcion = int(input("Ingrese la opcion: "))
        Menus()
        
        
        
def Create_Password():
    print("Crear contraseña")
    print("Para crear una contraseña,necesito la  cantidad de caracteres quieres que tenga tu contraseña")
    valor =  int(input("Ingrese el valor: "))
    
    #comparar_numero(valor, False)
            
        
    print("Para crear una contraseña,necesito la dificultad de la contraseña")
    print("1. Muy Facil")
    print("2. Facil")
    print("3. Medio")
    print("4. Dificil")
    print("5. Muy Dificil")
    dificultad = int(input("Ingrese el valor: "))
    
    
   # comparar_numero(dificultad, False)
    while dificultad <= 0 or dificultad > 5:
        print("Error, el valor debe ser positivo")
        dificultad = int(input("Ingrese el valor: "))
        print("La contraseña es:")
    if dificultad == 1:
       
        print("".join(random.choice(string.ascii_lowercase) for _ in range(valor)))
    elif dificultad == 2:
        print("".join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(valor)))
    elif dificultad == 3:
        print("".join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(valor)))
    elif dificultad == 4:
        print("".join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation) for _ in range(valor)))
    elif dificultad == 5:
        print("".join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation + string.whitespace) for _ in range(valor)))
    else:
        print("Error, el valor debe ser positivo")
        valor = int(input("Ingrese el valor: "))
    print("Gracias por utilizar la aplicación")
    print("Que tenga un buen dia, gracias")
    
    
Hola_Mundo()

