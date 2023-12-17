import socket

def start_server():
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    
    server_address = ('localhost', 12345)

    
    server_socket.bind(server_address)

    print(f"Server is listening on {server_address[0]}:{server_address[1]}...")

    while True:
        
        print("Waiting for a message...")
        data, client_address = server_socket.recvfrom(1024)

        try:
            print(f"Received: {data.decode()} from {client_address}")

            
            message = "Received your message!"
            server_socket.sendto(message.encode(), client_address)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    start_server()