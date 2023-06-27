numeros = ["9","8","7","6","5","4","3","2","1"]

import random

print("---------Bienvenido a CODIGO SECRETO---------")
print()
print()
print("Deberá adivinar el codigo creado por la computadora a utilizando su deducción")
print()
print('Ingrese el codigo que usted cree posible (solo 4 digitos), la computadora devolverá la cantidad de digitos con posicion correcta en "x".')
print()
print('En el caso en el que el digito sea correcto, pero su posicion sea errónea, la computadora devolvera un mensaje con "o".')
print()
print('Si se diera el caso en el que el digito no sea el correcto, la computadora devolvera una "-".')
print()
print('Por ultimo, al igualar el codigo creado por la computadora, esta devolvera un mensaje de "xxxx".')
print()
a = random.choice(numeros)
numeros.remove(a)#remuevo los elementos para evitar que se repitan

b = random.choice(numeros)
numeros.remove(b)

c =  random.choice(numeros)
numeros.remove(c)

d = random.choice(numeros)
numeros.remove(d)

j = random.choice(numeros)
numeros.remove(j)
k = random.choice(numeros)
#print(a,b,c,d,j,k)
#input()




codigo = [a,b,c,d]
ayuda = 0


e,f,g,h,q,r = 0,0,0,0,0,0
codigo_us = [e,f,g,h]
intento = 0
ce = 0
sub = 0
contador_dificultad = 0

lista_deop = ["","Facil","facil","FACIL","Normal","normal","NORMAL","Dificil","dificil","DIFICIL","muy dificil", "Muy dificil", "MUY DIFICIL,","imposible","Impoible","IMPOSIBLE"]
inte = 0
print("Los grados de dificultad son: ")
print()
print("_Facil = infinitos intentos")
print("_Normal = 20 intentos")
print("_Dificil = 10 intentos")
print("_Muy dificil = 5 intentos")
print("_Imposible = 5 intentos - codigo de 6 cifras")
print()
print("Tenga en cuenta que si no ingresa una opcion, se tomará la dificultad facil como predeterminada.")
print()
dificultad = input("Por favor ingrese el grado de dificultad: ")
while sub == 0:
    if dificultad in lista_deop:
        if dificultad == "":
            dificultad = "facil"
            contador_dificultad =-1
            break
        if dificultad == "facil" or dificultad == "Facil" or dificultad == "FACIL":
            contador_dificultad =-1
            break
        if dificultad == "normal" or dificultad == "Normal" or dificultad == "NORMAL":
            contador_dificultad =21
            break
        if dificultad == "dificil" or dificultad == "Dificil" or dificultad == "DIFICIL":
            contador_dificultad =11
            break
        if dificultad == "muy dificil" or dificultad == "Muy dificil" or dificultad == "MUY DIFICIL":
            contador_dificultad =6
            break
        if dificultad == "imposible" or dificultad == "Imposible" or dificultad == "IMPOSIBLE":
            contador_dificultad =6
            break
    else:
        dificultad = input("Por favor ingrese el grado de dificultad: ")
if dificultad == "imposible" or dificultad == "Imposible" or dificultad == "IMPOSIBLE":
    codigo = [a,b,c,d,j,k]
    codigo_us = [e,f,g,h,q,r]
cont_intentos = -1

ayuda_imposible = 0
if dificultad == "imposible" or dificultad == "Imposible" or dificultad == "IMPOSIBLE":
    ayuda_imposible = 1


while codigo_us != codigo or contador_dificultad != 0:
    if contador_dificultad < 0 or contador_dificultad == 6 or contador_dificultad == 21 or contador_dificultad == 11:
        print ("Intentos: ",intento)
    else:
        if intento > 1:
            print ("Intentos: ",intento,"                                     ","Intentos restantes: ",contador_dificultad)
        else:
            print ("Intento: ",intento,"                                     ","Intento restante: ",contador_dificultad)

    print()
    print()

    cx = 0
    lr = 0
            
    while lr != 5:
        lr = 0
        activador =0
        while activador == 0:
            try:
                preg = int(input("Ingrese su codigo: "))
                if preg == "----":
                    print (codigo)
                    break
                activador = 1
            except ValueError:
                print ("Por favor ingrese un codigo de caracter numerico: ")
        if preg <  0:
            print("Por favor, el codigo debe ser positivo")
        else:
            lr+=1######
        pregunta = []
        preg = str(preg)
        pregunta.append(preg)
        pregunta = str(pregunta)
        try:
            e = pregunta[2]
            f = pregunta[3]
            g = pregunta[4]
            h = pregunta[5]
            if dificultad ==  "imposible" or dificultad == "Imposible" or dificultad == "IMPOSIBLE":
                q = pregunta[6]
                r = pregunta [7]


            if e == f or e == g or e == h:
                 print("Por favor ingrese un numero sin repetir digitos")
                     #print("1")
            elif f == e or f == g or f == h:
                 print("Por favor ingrese un numero sin repetir digitos")
                     #print("2")
            elif g == e or g == f or g == h:
                 print("Por favor ingrese un numero sin repetir digitos")
                     #print("3")
            elif h == e or h == g or h == f:
                print("Por favor ingrese un numero sin repetir digitos")
                     #print("4")
            else:
                lr+=1
            if ayuda_imposible == 1:
                if q == f or q == g or q == h or q == r:
                    print("Por favor ingrese un numero sin repetir digitos")
                if r == f or r == g or r == h or r == q:
                        print("Por favor ingrese un numero sin repetir digitos")
            else:
                lr+=1#######


            numero = len(pregunta)
            if ayuda_imposible == 1:
                if numero < 10:
                    print("Por favor, recuerde que su codigo debe tener 6 caracteres")
                else:
                    lr +=1
                    
                if numero > 10:
                    print("Por favor, recuerde que su codigo debe tener 6 caracteres")
                else:
                    lr+=1

            else:
                if numero < 8:
                    print("Por favor, recuerde que su codigo debe tener 4 caracteres")
                else:
                    lr += 1############
                if numero > 8:
                    print("Por favor, recuerde que su codigo debe tener 4 caracteres")
                else:
                    lr+=1############

            if dificultad == "imposible" or dificultad == "Imposible" or dificultad == "IMPOSIBLE":
                if lr == 4:
                    break
            else:
                if lr==5:
                    break
        except IndexError:
           print("Por favor, recuerde que su codigo debe tener 4 caracteres")
############################fin de bucle de errores#############################

    if contador_dificultad == 1:
        print()
    if contador_dificultad == 2:
        cont_intentos = 20
    if contador_dificultad == 3:
         cont_intentos = 10
    if contador_dificultad == 4:
         cont_intentos = 5
        
    contador = 0
    cerca = 0
    ce = 0
    activador = 0
    pregunta = []
    #while activador == 0:
        #try:
            #######
          #  preg = int(input("ingrese su codigo: "))
            #######
            #break


            #activador = 1
        #except ValueError:
          #  print ("Por favor ingrese un codigo de caracter numerico: ")
        #else:
          #  if preg == "----":
            #    print (codigo)
            
    #preg = str(preg)
    #pregunta.append(preg)
    #pregunta = str(pregunta)
    #numero = len(pregunta)

    





    
    if e == codigo[0]:
        contador +=1
    elif e in codigo:
        #
        ce +=1
 #   else:
   #     contador -=1

        
    if f == codigo[1]:
        contador +=1
    elif f in codigo:
        #
        ce +=1
    #else:
      #  contador -=1


    if g == codigo[2]:
       contador +=1
    elif g in codigo:
        #
        ce +=1
   # else:
     #   contador -=1


    if h == codigo[3]:
       contador +=1
    elif h in codigo:
        #
        ce +=1
    #else:
       # contador -=1
    if ayuda_imposible == 1:
        if q == codigo[4]:
            contador +=1
        elif q in codigo:
            ce += 1
        if r == codigo[5]:
            contador +=1
        elif r in codigo:
            ce +=1################################

        
    intento+=1
 


 
    if ce == 1:
        if ayuda_imposible == 1:
            print("o-----")
        else:
            print ("o---")
    if ce == 2:
        if ayuda_imposible == 1:
            print("oo----")
        else:
            print("oo--")
    if ce == 3:
        if ayuda_imposible == 1:
            print("ooo---")
        else:
            print("ooo-")
    if ce == 4:
        if ayuda_imposible == 1:
            print("oooo--")
        else:
            print("oooo")
    if ce == 5:
        print("ooooo-")
    if ce ==6:
        print("oooooo")


    

    
    
    if contador == 0:
        if ayuda_imposible == 1:
            print("------")
        else:
            print  ("----")
    if contador == 1:
        if ayuda_imposible == 1:
            print("x-----")
        else:
            print("x---")
    if contador == 2:
        if ayuda_imposible == 1:
            print("xx----")
        else:
            print("xx--")
    if contador == 3:
        if ayuda_imposible == 1:
            print("xxx---")
        else:
            print("xxx-")
    if ayuda_imposible ==1:
        if contador == 4:
            print("xxxx--")
        if contador == 5:
            print("xxxxx-")
    if dificultad == "imposible" or dificultad == "Imposible" or dificultad == "IMPOSIBLE":
        if contador ==6:
                print("xxxxxx")
                print("CODIGO CORRECTO")
                intento -=1
                print("Ha logrado resolver el codigo en ", intento," intentos", " en la dificultad: ", dificultad )
                break

    else:
        if contador == 4:
                print("xxxx")
                print("CODIGO CORRECTO")
                intento -=1
                print("Ha logrado resolver el codigo en ", intento," intentos", " en la dificultad: ", dificultad )
                break
    
    print()
    contador_dificultad -= 1
    if contador_dificultad == 0:
        print("INTENTOS ACABADOS")
        if ayuda_imposible == 1:
            print("El codigo era: ", codigo[0],"-", codigo[1],"-", codigo[2],"-", codigo[3],"-",codigo[4],"-",codigo[5])
            break
        else:   
            print("El codigo era: ", codigo[0],"-", codigo[1],"-", codigo[2],"-", codigo[3])
            break
   

    print ("________________________________________________________________________________")
