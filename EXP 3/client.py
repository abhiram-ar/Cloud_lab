import tkinter as tk
import threading
import socket

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                chat_box.insert(tk.END, message + '\n')
        except:
            print("An error occurred!")
            break

def send_message(event=None):
    message = my_message.get()
    if message:
        chat_box.insert(tk.END, client_name + ':' + message + '\n')
        client_socket.send(f"{client_name}:{message}".encode('utf-8'))
        my_message.set("")  # Clear the input field

root = tk.Tk()
root.title("Chat Application")

frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_box = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
chat_box.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=chat_box.yview)

name_label = tk.Label(root, text="Enter your name:")
name_label.pack(pady=(10, 5))

my_name = tk.StringVar()
name_entry = tk.Entry(root, textvariable=my_name)
name_entry.pack(pady=5)

my_message = tk.StringVar()
entry_field = tk.Entry(root, textvariable=my_message, state=tk.DISABLED)
entry_field.bind("<Return>", send_message)
entry_field.pack(pady=5)

send_button = tk.Button(root, text="Send", command=send_message, state=tk.DISABLED)
send_button.pack()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 56789))

client_name = ""

def enable_chat():
    global client_name
    client_name = my_name.get()
    entry_field.config(state=tk.NORMAL)
    send_button.config(state=tk.NORMAL)
    name_submit_button.config(state=tk.DISABLED)

name_submit_button = tk.Button(root, text="Submit Name", command=lambda: enable_chat())
name_submit_button.pack(pady=(0, 10))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

root.mainloop()

client_socket.close()
