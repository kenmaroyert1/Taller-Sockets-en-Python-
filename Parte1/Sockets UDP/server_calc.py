import socket
import sys
import struct

# Crear un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Enlazar el socket a la dirección y puerto
server_address = ('localhost', 10009)
sock.bind(server_address)

# Bucle para recibir y procesar datos
while True:
    data, addr = sock.recvfrom(1024)  # Recibir datos del cliente
    print(data, addr)
    
    # Desempaquetar los datos recibidos (dos números y una operación)
    a, b, op = struct.unpack("III", data)
    print(a)
    print(b)
    print(op)
    
    # Realizar la operación (suma o resta)
    if op == 0:
        res = a + b
    else:
        res = a - b
    
    # Empaquetar el resultado y enviarlo de vuelta al cliente
    data = struct.pack("I", res)
    sock.sendto(data, addr)
