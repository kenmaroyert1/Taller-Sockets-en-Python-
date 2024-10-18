import socket
import struct
import sys

# Verificar que se hayan pasado suficientes argumentos
arguments = len(sys.argv)
if arguments < 3:
    print('Uso: client_calc <host> <port>')
    exit()

# Crear un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Definir la dirección del servidor
    serverAddress = (sys.argv[1], int(sys.argv[2]))
    
    # Definir los valores a enviar
    a = 10
    b = 500
    op = 0  # 0 para suma, otro valor para resta
    
    # Empaquetar los datos en formato binario
    data = struct.pack('III', a, b, op)
    
    # Enviar los datos al servidor
    sock.sendto(data, serverAddress)
    
    # Recibir la respuesta del servidor
    message, addr = sock.recvfrom(1024)
    
    # Desempaquetar el resultado
    res = struct.unpack("I", message)
    print('Resultado:', res[0])

finally:
    # Cerrar el socket
    print('closing socket')
    sock.close()
