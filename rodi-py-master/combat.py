import rodi
import time 
# from random import 
arduin.move(20,20)
try:
    while True:
        muv=arduin.see()
    if muv >= 4:
        arduin.move_forward()
        arduin.pixel(0,100,0)
#      elif muv >= 5:
#         arduin.move_right()
#         time.sleep(0,12)
#         arduin.move_stop()
#      elif muv == 10:
#         arduin.move(50,50)
#         arduin.pixel(25,100,75)
#      elif muv <= 5:
#         arduin.pixel(100,0,0)
#  except KeyboardInterrupt:
#     print("fatallity")
#     arduin.move_stop()
# from random import randint

#     arduin.light()
#     color=randint(1,255)
#     co=randint(1,255)
#     lor=randint(1,255)
#     arduin.pixel(color,co,lor)
#     time.sleep(0.5)
