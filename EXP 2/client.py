import socket

def start_client():
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    
    server_address = ('localhost', 12345)

    try:
        
        message = "Hello, server!"
        client_socket.sendto(message.encode(), server_address)

        
        data, server_address = client_socket.recvfrom(1024)
        print(f"Received: {data.decode()} from {server_address}")

    finally:
        
        client_socket.close()

if __name__ == '__main__':
    start_client()