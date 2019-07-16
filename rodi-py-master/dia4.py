import rodi
import time 

arduin = rodi.RoDI()
# arduin.move_backward()
# time.sleep(2)
# arduin.move_left()
# time.sleep(0,2)
# arduin.move_stop()
# time.sleep(1)

# arduin=rodi.RoDI()
# arduin.move_forward()
# time.sleep(1,5)

# arduin.move_right()
# time.sleep(0,35)

# arduin.move_forward()
# time.sleep(1,5)

# arduin.move_right()
# time.sleep(1,5)

# arduin.move_stop()
#pasare=1
# distancia= 1
# while ditancia in == 1:
    # for pasare range(1,3):
    #     arduin.move_forward
    #     time.sleep(0,25)
    #     arduin.move_right()
    #     time.sleep(0,35)
#     print("centimetro" , arduin.see())
##################
#sensor de distaancia
# print("centimetro", arduin.see())
# while True:
#     print(arduin.see() , ("centimetros"))

arduin.move(20,20)
try:
   while True:
    muv=arduin.see()
    if muv >= 4:
        arduin.move_forward()
        arduin.pixel(0,100,0)
    elif muv >= 5:
        arduin.move_right()
        time.sleep(0,12)
        arduin.move_stop()
    elif muv == 10:
        arduin.move(50,50)
        arduin.pixel(25,100,75)
    elif muv <= 5:
        linea34= arduin.sense()
        print(linea34[0],linea34[1])
        arduin.pixel(100,0,0)
except KeyboardInterrupt:
    print("fatallity")
    arduin.move_stop()
from random import randint
while True:
    arduin.light()
    color=randint(1,255)
    co=randint(1,255)
    lor=randint(1,255)
    arduin.pixel(color,co,lor)
    time.sleep(0.5)
    arduin.sense
    #     linea = arduin.sense()
    print(linea)
    print(linea[0])
    print(linea[1])
    time.sleep(0,5)
arduin.sing(140,1000)
#seguidor de linea
# def 
# while True:
#     linea = arduin.sense()
#     print(linea)
#     print(linea(0])
#     print(linea[1])
#     time.sleep(0,5)