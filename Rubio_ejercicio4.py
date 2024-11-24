import time
from gpiozero import PWMLED
from Adafruit_ADS1x15 import ADS1115

# Configuración de los pines GPIO para los LEDs
led_rojo = PWMLED(17)
led_azul = PWMLED(27)

# Inicializar el ADC
adc = ADS1115()

# Ganancia para el ADS1115
GAIN = 1

def leer_potenciometro():
    # Leer el valor del potenciometro (Canal 0)
    valor_adc = adc.read_adc(0, gain=GAIN)
    # Escalar el valor a una temperatura entre 0 y 30 grados Celsius
    temperatura_pot = valor_adc * 30.0 / 32767.0
    return temperatura_pot

def leer_termistor():
    # Leer el valor del termistor (Canal 1)
    valor_adc = adc.read_adc(1, gain=GAIN)
    # Aquí deberías convertir el valor ADC a temperatura según las características del termistor
    # Supongamos una conversión simple para el ejemplo
    temperatura_real = valor_adc * 30.0 / 32767.0
    return temperatura_real

def control_proporcional():
    while True:
        temperatura_pot = leer_potenciometro()
        temperatura_real = leer_termistor()
        diferencia = temperatura_real - temperatura_pot

        if diferencia > 0:
            # La temperatura real está por encima de la fijada, encender el LED azul
            brillo_azul = min(diferencia / 5.0, 1.0)
            led_azul.value = brillo_azul
            led_rojo.off()
        else:
            # La temperatura real está por debajo de la fijada, encender el LED rojo
            brillo_rojo = min(abs(diferencia) / 5.0, 1.0)
            led_rojo.value = brillo_rojo
            led_azul.off()

        print(f"Temp. Potenciómetro: {temperatura_pot:.2f}°C, Temp. Real: {temperatura_real:.2f}°C")

        time.sleep(1)

if __name__ == "__main__":
    try:
        control_proporcional()
    except KeyboardInterrupt:
        print("Programa terminado.")
        led_rojo.off()
        led_azul.off()