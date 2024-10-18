def start_udp_server():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('localhost', 65433))  # Cambia el puerto según sea necesario
    print("Servidor UDP en espera de datagramas...")

    while True:
        data, addr = udp_socket.recvfrom(1024)
        print(f"Datagrama recibido de {addr}: {data.decode('utf-8')}")
        udp_socket.sendto(b"Datagrama recibido", addr)

if __name__ == "__main__":
    start_udp_server()
