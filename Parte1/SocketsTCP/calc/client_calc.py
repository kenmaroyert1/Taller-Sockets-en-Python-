import socket
import sys

# Función para leer un número del socket
def readNumber(sock):
    a = ''
    while True:
        msg = sock.recv(1)
        if (msg == b'\0'):  # Leer hasta encontrar el carácter nulo
            break
        a += msg.decode()  # Convertir de bytes a string
    return int(a, 10)  # Convertir a entero

# Verificar que los argumentos son suficientes
arguments = len(sys.argv)
if arguments < 3:
    print('Uso: client_calc <host> <port>')
    exit()

# Crear el socket y conectarse al servidor
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (sys.argv[1], int(sys.argv[2]))
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # Enviar los valores al servidor
    a = 5  # Primer número
    b = 8  # Segundo número
    op = 1  # Operación (1 para resta en tu código)

    # Enviar los datos al servidor, seguidos de '\0'
    sock.sendall(str(a).encode())
    sock.sendall(b'\0')
    sock.sendall(str(b).encode())
    sock.sendall(b'\0')
    sock.sendall(str(op).encode())
    sock.sendall(b'\0')

    # Recibir y mostrar el resultado
    res = readNumber(sock)
    print(res)

finally:
    # Cerrar el socket
    print('closing socket')
    sock.close()
