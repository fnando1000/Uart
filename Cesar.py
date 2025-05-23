import serial
import time

def descifrado_cesar(texto, desplazamiento):
    resultado = ''
    for c in texto:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            resultado += chr((ord(c) - base - desplazamiento) % 26 + base)
        else:
            resultado += c
    return resultado

# Ajusta el puerto según tu sistema, por ejemplo '/dev/ttyUSB0' o '/dev/serial0'
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(2)

print("Esperando mensaje...")

while True:
    if ser.in_waiting > 0:
        linea = ser.readline().decode('utf-8').strip()
        print("Mensaje cifrado recibido:", linea)
        print("Mensaje descifrado:", descifrado_cesar(linea, 3))
        break
