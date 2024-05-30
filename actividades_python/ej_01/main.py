from gpiozero import LED, Button
from signal import pause

#importo el LED y boton  y la señal de pausa

led = LED(19)
button = Button(3)

#indico el pin del LED y el del Boton

button.when_pressed = led.on
button.when_released = led.off

#orden: cuando presiono el boton, el LED enciende, cuando se suelta se apaga

pause()

