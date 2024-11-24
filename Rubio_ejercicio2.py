from gpiozero import LED
from time import sleep
import threading

# Definir los pines GPIO para cada color del LED RGB
led_rojo = LED(17)
led_azul = LED(27)
led_verde = LED(22)

# Funci�n para hacer parpadear los LEDs seg�n el intervalo especificado
def parpadear(led, intervalo):
    while True:
        led.on()
        sleep(intervalo)
        led.off()
        sleep(intervalo)

# Crear hilos para cada LED con su intervalo espec�fico
hilo_rojo = threading.Thread(target=parpadear, args=(led_rojo, 1))
hilo_azul = threading.Thread(target=parpadear, args=(led_azul, 0.5))
hilo_verde = threading.Thread(target=parpadear, args=(led_verde, 0.25))

# Iniciar los hilos
hilo_rojo.start()
hilo_azul.start()
hilo_verde.start()

# Mantener el programa en ejecuci�n para que los hilos contin�en ejecut�ndose
hilo_rojo.join()
hilo_azul.join()
hilo_verde.join()