import socket
from des_core import decrypt

SHARED_KEY = "ITS_1960" 

def start_server():
    host = '0.0.0.0'
    port = 65432
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    
    print(f"[*] Server listening on {host}:{port}...")
    conn, addr = server_socket.accept()
    print(f"[*] Connection established from {addr}")
    
    encrypted_data = conn.recv(4096).decode()
    print(f"\n[+] Received Ciphertext (Binary): {encrypted_data}")
    
    decrypted_text = decrypt(encrypted_data, SHARED_KEY)
    print(f"[+] Decrypted Message: {decrypted_text}\n")
    
    conn.close()

if __name__ == '__main__':
    start_server()