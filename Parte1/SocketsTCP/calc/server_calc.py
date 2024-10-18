import socket
import sys

# Función para leer un número del socket
def readNumber(sock):
    a = ''
    while True:
        msg = sock.recv(1)
        if (msg == b'\0'):
            break
        a += msg.decode()
    # Convierte la secuencia de bytes a un string y luego a entero
    return int(a, 10)

# Crear el socket y configurar el servidor
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('localhost', 10009)
sock.bind(server_address)
sock.listen(5)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address)
        
        # Leer números del cliente
        a = readNumber(connection)
        b = readNumber(connection)
        op = readNumber(connection)
        
        # Realizar la operación de suma o resta
        if (op == 0):
            res = a + b
        else:
            res = a - b
        
        # Crear el mensaje y enviar el resultado
        message = str(res) + "\0"
        connection.sendall(message.encode())
    
    finally:
        # Convierte a una secuencia de bytes y cierra la conexión
        connection.close()
