import tkinter as tk
from tkinter import filedialog
import socket

def send_message():
    message = entry.get()
    client_socket.sendall(message.encode('utf-8'))
    response = client_socket.recv(1024)
    print(response.decode('utf-8'))

def send_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        client_socket.sendall(b"SEND_FILE")
        client_socket.sendall(os.path.basename(file_path).encode('utf-8'))
        with open(file_path, 'rb') as f:
            bytes_read = f.read(1024)
            while bytes_read:
                client_socket.sendall(bytes_read)
                bytes_read = f.read(1024)
        print(f"Archivo enviado: {file_path}")

# Conexión al servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 65432))  # Cambia el puerto según sea necesario

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Cliente TCP")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

send_button = tk.Button(root, text="Enviar Mensaje", command=send_message)
send_button.pack(pady=5)

file_button = tk.Button(root, text="Enviar Archivo", command=send_file)
file_button.pack(pady=5)

root.mainloop()

client_socket.close()
