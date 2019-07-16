#######condicionales
#=igual
#>mayor
#<menor
#>=mayor o igual
#<=menor o igual
#!distinto 








#ej crear una funcion que reciba como parametro una nota 
#nota del 1 al 100 e imprima si pasaste o te aplazaste
# a=90
# if a > 3 and a < 10:
#     print("a es mayor que 5 y menor que 10")
# else:
#     print("a no es mayor que 5 y menor que 10")
# edad = 35                                        #si la edad es mayor a 18 y menor que 25
# if edad > 18 and edad <  25:                     #imprime que deberia estar en la universidad 
#     print("deberia estar en la universidad")         #sino en la secundaria 
# elif edad < 13:                                  #caso de no cumplir las 2 opciones pasa a cumplir la siguiente 
#     print("deberia estar en la secundaria")     #que seria mayor a 30 y menor qu 60 cumple la funcion de trabajando
# elif edad > 30:                            #caso contrario ejecuta com ultimo recurso la de estar jubilado
#     if edad < 60:
#         print("deberia estar trabajando")
#     else:
#         print("deberia estar jubilado")
# horario1 = 00
# def horario(rutina):
#     if rutina > 5 and rutina < 10:
#         print("desayunar")
#     elif rutina > 10:
#         print("merienda")
#     elif rutina > 12:
#         print("almuerzo")
#     return rutina 
# print(horario(11))
# #ej crear una funcion puntaje que reciba como parametro una nota del 1 al 100 e imprima que nota sacaste
# #nota 60 -----> 
# #<60----------1
# #60y60----------------2
# #71 y 75-----------3
# #76 y 85-------------4
# #mayor a 85----------5
# nombre = input("ingresa tu nombre")#el input recibe cada mensaje comoo un string 
# #int = convierte un string en numeros
# #str = convierte los numeros en textos
# #ej pedir al usuario que ingrese 3 numeros y multiplicarlos entre si imprimir el resultado
# usuario = input("ingresa el primer numero")
# usuario1 = input("ingresa el 2 numero")
# usuario2 = input("ingresa el 3 numero")
# resul=int(usuario) * int(usuario1) *int(usuario2)

# print(resul)

# #ej 2 pedir al usuario un numero del 1 al 100 y llamar al funcion que retornaba la nota que creamos hace un rato
# #utilizando el valor ingresado por el usuario
# usuarrrio = input("ingresa tu numero de cuenta bancaria")

# contador=10
# while contador >= 0:
#     print("hola esto es un coteo en reversa")
#     contador = contador - 1
#     print("te quedan", contador,"oportunidades")
# print("game over")

# #usando while pedir al usuario ingredientes para hacer una pizza y agregar a una lista 
# conteo=0
# while conteo >= 5:
#     print("ingrese ingrediente")
#     conteo = conteo + 1
#     print("aaaaaaaaaaaaaaaaaaaaaaaa", conteo)
# ingredientes=input("ingrese ingrediente")
numero_secreto= 7
adivino= False
while adivino == False:
    apuesta= input("ingrese un numero de 1 a 10")
    if int(apuesta) == numero_secreto:
        print("ganaste")
        adivino= True
    else:
        print("segui participando")

what= False
real=4
while what == False:
    gatillo= input("apueste numero")
    if int(gatillo) == real:
        print("regana")
        what ==True
    elif int(gatillo) > 4:
        print(input("ingrese numero menor"))
    elif int(gatillo) < 4:
        print(input("ingrese numero mayor"))
    elif int(gatillo) >  10:
        print("error")

