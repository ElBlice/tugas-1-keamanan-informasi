import socket
from des_core import encrypt

SHARED_KEY = "ITS_RAFI" 

def start_client():
    host = '192.168.83.129'
    port = 65432
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    message = "Halo Rafi! Ini pesan rahasia jaringan."
    print(f"[*] Original Message: {message}")
    
    encrypted_data = encrypt(message, SHARED_KEY)
    print(f"[+] Encrypted Ciphertext (Binary): {encrypted_data}")
    
    client_socket.send(encrypted_data.encode())
    print("[*] Ciphertext successfully transmitted.")
    
    client_socket.close()

if __name__ == '__main__':
    start_client()
