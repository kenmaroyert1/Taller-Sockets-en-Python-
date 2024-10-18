def send_udp_message():
    message = entry.get()
    udp_socket.sendto(message.encode('utf-8'), ('localhost', 65433))  # Cambia el puerto según sea necesario)
    response, _ = udp_socket.recvfrom(1024)
    print(response.decode('utf-8'))

# Conexión al servidor
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Cliente UDP")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

send_button = tk.Button(root, text="Enviar Datagrama", command=send_udp_message)
send_button.pack(pady=5)

root.mainloop()

udp_socket.close()
