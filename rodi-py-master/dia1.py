print(2+2)
print(2+4)
print(20/2)
print(2+12)
print(12/6)#division de numeros enteros
print("hola mundo")#cocatenacion de palabras
print("mbae la porte")
print("hola "*2)#multiplicacion de palabras
r = 12
a = 2
print(a*r)
print("hola",a,r)
nombre = "pedro"
edad = 22
print("hola me llamo",nombre,"tengo",edad,"aos")
hobby = "leer"
print("hola me llamo",nombre,"y tengo",edad,"aos y mi hoby es",hobby,)
#corchete es una lista
datos = [nombre,edad,hobby]
datos.append("contador")
print(datos)
datos.append("futbol")
print(datos)
datos.pop()
print(datos)
print(len(datos))
print("la lista de datos tiene",(len(datos)),"elementos")
lista_larga = [2,2,3,4,3,2,2,5,6,7,8,9,8]
print(len(lista_larga))
indice_ultimo = lista_larga[len(lista_larga)-1]
print(indice_ultimo)
lista_temas = ["variables", "listas", "tipos de datos"]
for concept in lista_temas:   #boocle va repetir las veces que este en la lista los elementos
    print("hoy aprendi", concept)
print("fin!!!")
for concept in lista_larga:
    print("comiendo",concept)
    print("que bien")
#len append pop print for
for melon in range(3):
    print("pomelo",melon)
#ej. imprimir los numeros del 1 al 100 usando for 
#y rango
for x in range(1,101):
    print(x)

#imprimir el resultado de la suma
#del 1 al 10 usando range >> 1+2+3+4+5+6+7+8+9+10=55
chalenge=[1,2,3,4,5,6,7,8,9,10]
a=0
for x in chalenge:
    a=a+x
print(a)
