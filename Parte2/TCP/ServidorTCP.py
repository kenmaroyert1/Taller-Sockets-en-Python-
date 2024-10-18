import socket
import os

def start_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))  # Cambia el puerto según sea necesario
    server_socket.listen(1)
    print("Servidor TCP en espera de conexión...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Conexión establecida con {addr}")
        
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            if data.decode('utf-8') == "SEND_FILE":
                filename = conn.recv(1024).decode('utf-8')
                with open(filename, 'wb') as f:
                    while True:
                        bytes_read = conn.recv(1024)
                        if not bytes_read:
                            break
                        f.write(bytes_read)
                print(f"Archivo recibido: {filename}")
            else:
                print(f"Mensaje recibido: {data.decode('utf-8')}")
                conn.sendall(b"Mensaje recibido")

        conn.close()

if __name__ == "__main__":
    start_tcp_server()
