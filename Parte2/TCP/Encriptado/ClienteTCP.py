import tkinter as tk
from tkinter import filedialog
import socket
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import os

def send_message():
    message = entry.get()
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(message.encode('utf-8'))
    client_socket.sendall(cipher_aes.nonce + tag + ciphertext)
    response = client_socket.recv(1024)
    print(response.decode('utf-8'))

# Conexión al servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 65432))

# Recibir llave pública del servidor
server_public_key = RSA.import_key(client_socket.recv(1024))

# Generar llave de sesión AES y enviarla cifrada al servidor
session_key = get_random_bytes(16)
cipher_rsa = PKCS1_OAEP.new(server_public_key)
encrypted_session_key = cipher_rsa.encrypt(session_key)
client_socket.sendall(encrypted_session_key)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Cliente TCP")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

send_button = tk.Button(root, text="Enviar Mensaje", command=send_message)
send_button.pack(pady=5)

root.mainloop()
client_socket.close()
