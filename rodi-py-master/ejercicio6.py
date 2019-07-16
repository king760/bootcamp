#clases
#estructura basica

class persona:
    def __init__(self,nombre1,edad1,altura1):           #creamos la clase persona
        self.nombre=nombre1     #inicializamos las caracteristicas de las clase persona
        self.edad=edad1             #edad
        self.altura=altura1          #en cm

    #aca debajo se realizan las acciones (metodos)
    def comer(self):             #definimos los metodos de la clase persona
        print("quiero anburgueza")

    def dormir(self):              #otro metodo de la clase persona
        print("estoy durmiendo")

laura=persona("laura",17,163)                #instanciamos la clase persona y creamos el objeto profesor

#vamos a describir al pinguino
class animal1:
    """
    recibimos los parametro nombre,altura,sexo,colores
    """
    #definimos los atributos
    def__init__(self,vvcito,altura,sexo,colores):
        self.nombre=vvcito    #nombre
        self.altura=altura
        self.sexo=sexo
        self.colores=colores
    #ahora agregamos las acciones que puede realizar(metodos)
    # con self indicamos que el metodo es de la clase
    def nadar(self):
        print("estoy nadando")
    def comer(self,comida):
        print("estoy comiendo,comida")
    def hablar(self):
        print("mi estatura es",self.altura)
    #creamos una lista para instanciar
    lista_colores=["blanco,amarillo,negro"!
    pinguino=animal("pinwui",40,"x",lista_colores) #instanciamos las clases
    #abajo, instanciamos y enviamos la lista directamente
    perrito=animal("ritz",35,"m",["blanco","azul"]) 
    personal=animal("ritz",35."m",["blanco","azul"]) 
    """
    ejercicio
    con respecto al ejercicio anterior crea un metodo crecer() que haga crecer 1 cm al animal
    desafio:crear un metodo agrega_colores() , que reciba como parametro un color y que agrega a la lista 
    de colores al animal
    """
               
class Animal:
    """
        recibimos los parametro nombre,altura,sexo,colores
    """
    #definimos los atributos
    def __init__(self,vvcito,altura,sexo,colores):
        self.nombre=vvcito    #nombre
        self.altura=altura
        self.sexo=sexo
        self.colores=colores
    #ahora agregamos las acciones que puede realizar(metodos)
    # con self indicamos que el metodo es de la clase
    def nadar(self):
        print("estoy nadando")
    def comer(self,comida):
        print("estoy comiendo,comida")
    def hablar(self):
        print("mi estatura es",self.altura)
    def crecer(self):
        self.altura=self.altura+1
        print(self.altura)   
    def agrega_colores(self,colorido):
        self.colores.append(colorido)
    def delcolor(self):     #elimina el ultimo color de la lista
        self.colores.pop()

   
 
#creamos una lista para instanciar
lista_colores=["blanco","amarillo","negro"]
pinguino=Animal("pinwui",40,"x",lista_colores) #instanciamos las clases
#abajo, instanciamos y enviamos la lista directamente
perrito=Animal("ritz",35,"m",["blanco","azul"]) 
personal=Animal("ritz",35,"m",["blanco","azul"]) 

#ejercicio
#crear una clase llamada vehiculo
#con las siguientes caracteristicas: numero_ruedas, marca,kilometraje
#con las siguientes acciones:
#          pinchar_rueda(), y debe de restar una rueda
#          sumar_kilometraje(), y que reciba la cantidad de kilometraje que se debe de sumar
#DESAFIO: agregar a lo anterior un metodo llamada tipo()que retorne el tipo de vehiculo dependiendo
#         de la calidad de ruedas que posea, por ejemplo
#          si tiene 4 ruedas es un auto
#          si tiene 3 ruedas es un triciclo/motocarga
#          si tiene 2 ruedas, moto/bicicleta
#          si  tiene 1 rueda, monociclo

class vehiculo:
    def __init__(self,numero_ruedas,marca,kilometraje):
        self.numero_ruedas=numero_ruedas
        self.marca=marca
        self.kilometraje=kilometraje
    def pinchar_ruedas(self):
        self.numero_ruedas=self.numero_ruedas-1      
        print("menos una rueda",self.numero_ruedas)
    def sumar_kilometraje(self,cantidad):
        self.kilometraje=self.kilometraje+cantidad
        print("el nuevo kilometraje",self.kilometraje)     

carro=vehiculo(4,"ferrari",500)
carro.kilometraje(3,"motocarga",200)