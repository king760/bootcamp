"esto es un string"#tipo de datos
#tipo de datos
#tipo de datos integer/intera/int

#listas
#acceder a un elemento de la lista
variable_lista = ["marce", 33, "programador"]
#variables
nombre = "marce"
edad = 30+3
edad_mal = "33+3"
variable_lista = ["marce", nombre, edad]
print(variable_lista[0], edad, variable_lista[2])
#acciones/operaciones sobre listas
variable_lista.append("rugby") #agregar
variable_lista.pop()
for zi in range(1,11):
    print(zi)
#imprimir el ultimo elemento sin saber cuantos elementos tiene
otra_lista = ["hola que tal", "chau", 4]
print(otra_lista)
dimension_lista = len(otra_lista) - 1
print(otra_lista[dimension_lista])
#soluciones paso por paso
dim_lista = len(otra_lista)
print("la dimension de otra lista es", dim_lista)
indice_del_ultimo = dim_lista - 1
print("el indice del ultimo elemento es", indice_del_ultimo)
#soluciones de una llinea
print(otra_lista)
######## funciones
def nombre_de_la_funcion (argumento):
    print(nombre_de_la_funcion)
nombre_de_la_funcion("hola")
print(nombre_de_la_funcion)
#crear una funcion que reciba un parametro dos numeros y retorne la resta de esos numeros
# luego llamar a la funcion e imprimir el resultado
def multiplica(num1,num2):
    return num1*num2

resultado=multiplica(2,9)  #guardamos el valor de la multiplicacion en resultado  a travez de return
print(resultado)

print(multiplica(2,2))
print(resultado)
#crea una funcion saludo que reciba como parametro nombre y con 2 que imprima hola soy........y tengo ........aos
#llamar varias veces a la funcion con ditintos valores,  nota retornar es algo opcional
def saludo(nombre,edad):
    resul="hola soy" + nombre + "y tengo" + edad +"aos"
    return resul
print(saludo("pedro","22"))
#ej. crear una funcion sumalista que reciba como argumento una lista de numeros y retorne la suma de los numeros de la lista
lista_num=[1,2,3,4,5,6,7,8,9,10]
a=[10,11,12,13,14,15,16,17,18,19,20]
def sumatoria(listanum):
    suma=0
    for x in listanum:
        suma=suma+x   
    return suma
print(sumatoria(lista_num))
def sumatoria(a):
    suma=0
    for x in a:
        suma=suma+x
    return suma
        

#ej2 lista al cuadrado 
#crear una lista de numeros como parametro y retorne una lista con los numeros al cuadrado lista_cuadradalistita1,4,9,16,25
def lista_cuadrada(lista_jeyma):
    a=[]
    for jeyma in lista_jeyma:
        a.append(jeyma *jeyma)
    return a
otravez = [1,4,9,16,25]
resutado_cuad = lista_cuadrada(otravez)
print(resutado_cuad)
# crear una funcion suma_cuadrada que reciba una lista de numeros y retorne el valor de la suma al cuadrado [1,2,3,]>>>>[1,4,9]
pordos= [1,2,3]
def lista_cuadrada(pordos):
    lista=[]
    for cuadrado in pordos:
        lista.append(cuadrado*cuadrado)
    return lista
resu=[1,2,3]
resultado=lista_cuadrada(resu+resu)
print(resultado)
edad = 35                                        #si la edad es mayor a 18 y menor que 25
if edad > 18 and edad <  25:                     #imprime que deberia estar en la universidad 
    print("deberia estar en la universidad")         #sino en la secundaria 
elif edad < 13:                                  #caso de no cumplir las 2 opciones pasa a cumplir la siguiente 
    print("deberia estar en la secundaria")     #que seria mayor a 30 y menor qu 60 cumple la funcion de trabajando
elif edad > 30:                            #caso contrario ejecuta com ultimo recurso la de estar jubilado
    if edad < 60:
        print("deberia estar trabajando")
    else:
        print("deberia estar jubilado")
