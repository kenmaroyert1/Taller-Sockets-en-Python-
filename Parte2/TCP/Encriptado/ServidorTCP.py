import socket
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import os

def start_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(1)
    print("Servidor TCP en espera de conexión...")

    # Generar par de llaves RSA
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()

    while True:
        conn, addr = server_socket.accept()
        print(f"Conexión establecida con {addr}")

        # Enviar llave pública al cliente
        conn.sendall(public_key.export_key())

        # Recibir llave de sesión AES cifrada
        encrypted_session_key = conn.recv(256)
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(encrypted_session_key)

        while True:
            # Recibir mensaje cifrado y descifrarlo
            data = conn.recv(1024)
            if not data:
                break
            nonce = data[:16]
            tag = data[16:32]
            ciphertext = data[32:]
            cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce=nonce)
            message = cipher_aes.decrypt_and_verify(ciphertext, tag)
            print(f"Mensaje recibido: {message.decode('utf-8')}")
            conn.sendall(b"Mensaje recibido")

        conn.close()

if __name__ == "__main__":
    start_tcp_server()
