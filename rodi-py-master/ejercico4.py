import rodi
import time



robot = rodi.RoDI()        #instanciamos un objeto RoDI

"""
robot.move_forward()       #movemos el robot hacia adelante
time.sleep(1.0)  
robot.move_backward()      #movemos el robot hacia atras
time.sleep(1.0)
robot.move_left()          #movemos el robot hacia la izquierda
time.sleep(1.0)
robot.move_right()        #movemos el robot hacia la derecha
time.sleep(1.0)
robot.move_stop()         #hacemos que el robot pare
"""

"""
robot.move_forward()
time.sleep(1)
robot.move_right()
time.sleep(0.5)
robot.move_forward()
time.sleep(1)
robot.move_right()
time.sleep(0.5)
robot.move_forward()
time.sleep(1)
robot.move_right()
robot.move_forward()
time.move_right()
robot.move_stop()
"""
"""
import rodi
import time

robot = rodi.RoDI()        #instanciamos un objeto roDI

while True:
    print(robot.see())     #leemos el sensor de distancia
    time.sleep(0.1)

#desafio      

import rodi
import time

robot = rodi.RoDI()
distancia=5
while True:                      #mientras que sea verdad
    distancia=robot.see() #se guarda los elementos    
    if distancia > 16:
        robot.move_forward()
             #si distancia el mayor a 5 el robot avanza hacia adelante
    else:
        robot.move_stop()        #sino el robot para


#desafio
import rodi
import time
contador=0
inicio=0
final=4
while contador<4:
    print(contador)

    robot.move_forward()
    time.sleep(1)
    robot.move_right()
    time.sleep(0.5)
    contador=contador+1
robot.move_stop    
"""

import rodi
import time
robot = rodi.RoDI()            #instanciamos un objeto RoDI

while true:
      luz = robot.light()      #leemos e imprimimos la lectura del sensor de luz
      time.steep(0.5)

    