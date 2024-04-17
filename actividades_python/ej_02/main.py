from gpiozero import LED     #Importe desde la gpiozero la función led y del tiempo la función sleep. 
from time import sleep

ledR = LED(13)
ledB = LED(19)
ledG = LED(26)

rojo = 0
azul = 0
verde = 0

while True:

   if rojo < 4:
      ledR.on()
   if rojo >=4:
      ledR.off()

   if azul <2:
      ledB.on()
   if azul >=2:
      ledB.off()

   if verde == 0:
      ledG.on()
   if verde == 1:
      ledG.off()

rojo = rojo + 1
azul = azul + 1
verde = verde + 1

if rojo == 8:
   rojo = 0
if azul == 4:
   azul = 0
if verde == 2:
   verde = 0

sleep(0.25)
