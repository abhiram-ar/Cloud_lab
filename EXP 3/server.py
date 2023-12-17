import socket
import threading

# List to keep track of connected clients
clients = []

# Function to broadcast messages to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                # Remove broken connections
                remove(client)

# Function to remove a client from the list
def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

# Function to handle client connections
def handle_client(client_socket):
    
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                sender_name, message_content = message.split(":", 1)
                reversed_message = message_content[::-1]  # Reverse the message content
                broadcast(f"{sender_name}: {reversed_message}".encode('utf-8'), client_socket)
            else:
                remove(client_socket)
                break
        except:
            remove(client_socket)
            break

# Start the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 56789)
    server_socket.bind(server_address)
    server_socket.listen(5)

    print(f"Server is listening on {server_address[0]}:{server_address[1]}...")

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == '__main__':
    start_server()
