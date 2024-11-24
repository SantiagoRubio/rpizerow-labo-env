from gpiozero import LED, Buzzer
import sys

# Definir los pines GPIO para los LEDs RGB y el buzzer
led_rojo = LED(17)
led_azul = LED(27)
led_verde = LED(22)
buzzer = Buzzer(18)

def procesar_comando(comando, opcion):
    if comando == "buzz":
        if opcion == "on":
            buzzer.on()
            print("Buzzer encendido")
        elif opcion == "off":
            buzzer.off()
            print("Buzzer apagado")
        else:
            print("Opción no reconocida para buzz")
    elif comando == "rgb":
        if opcion == "red":
            led_rojo.toggle()
            print("LED rojo cambiado de estado")
        elif opcion == "blue":
            led_azul.toggle()
            print("LED azul cambiado de estado")
        elif opcion == "green":
            led_verde.toggle()
            print("LED verde cambiado de estado")
        else:
            print("Opción no reconocida para rgb")
    else:
        print("Comando no reconocido")

def main():
    while True:
        try:
            entrada = input("prompt: ")
            comando, opcion = entrada.split()
            procesar_comando(comando, opcion)
        except ValueError:
            print("Entrada inválida. Usa el formato: [COMANDO] [OPCION]")
        except KeyboardInterrupt:
            print("\nSaliendo del programa...")
            sys.exit()

if __name__ == "__main__":
    main()