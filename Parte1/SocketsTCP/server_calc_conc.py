import threading
import socket

def readNumber(sock):
    a = ''
    while True:
        msg = sock.recv(1)
        if (msg == b'\0'):
            break
        a += msg.decode()
    return int(a, 10)

def worker(sock):
    try:
        # Leer números y operación del cliente
        a = readNumber(sock)
        b = readNumber(sock)
        op = readNumber(sock)
        
        # Realizar la operación correspondiente
        if (op == 0):
            res = a + b
        else:
            res = a - b
        
        # Preparar y enviar el resultado al cliente
        message = str(res) + "\0"
        message += "\0"
        sock.sendall(message.encode())
    finally:
        # Limpiar la conexión
        sock.close()

# Crear el socket del servidor
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('localhost', 10009)
sock.bind(server_address)
sock.listen(5)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    print('connection from', client_address)
    
    # Crear un hilo para manejar la conexión del cliente
    t = threading.Thread(target=worker, args=(connection,))
    t.daemon = True  # Hacer el hilo un hilo daemon
    t.start()
