import socket

def start_server():
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
    server_address = ('localhost', 12345)

    
    server_socket.bind(server_address)

    
    server_socket.listen(1)

    print(f"Server is listening on {server_address[0]}:{server_address[1]}...")

    while True:
        
        print("Waiting for a connection...")
        client_socket, client_address = server_socket.accept()

        try:
            print(f"Connection established with {client_address}")

            
            data = client_socket.recv(1024)
            if data:
                print(f"Received: {data.decode()}")
                client_socket.sendall(data)
            else:
                print("No data received from client.")

        finally:
            
            client_socket.close()

if __name__ == '__main__':
    start_server()
