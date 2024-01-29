import socket
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext, simpledialog, Listbox
import time

client = None
nickname = None
chat_window = None
chat_display = None
message_entry = None
clients_listbox = None

retry_attempts = 3
reconnect_delay = 5  # seconds
MAX_RETRY_ATTEMPTS = 3
kicked = False
server_address = "127.0.0.1"
server_port = 5555
kickmsgdisplayed = False

whoisrunning = "Carter"
if whoisrunning == "Carter":
    server_address = "192.168.0.104"
elif whoisrunning == "Samuel":
    server_address = "174.27.172.190"

def create_gui():
    global chat_window, chat_display, message_entry, clients_listbox
    chat_window = tk.Tk()
    chat_window.title("PyChat Client")

    # Set a modern style for ttk widgets
    style = ttk.Style()
    style.theme_use("clam")  # You can choose other themes as well

    clients_listbox = tk.Listbox(chat_window, width=20)
    clients_listbox.pack(side=tk.LEFT, fill=tk.Y)
    clients_listbox.configure(font=("Quicksand", 10))

    chat_display = scrolledtext.ScrolledText(chat_window)
    chat_display.pack(expand=True, fill=tk.BOTH)
    chat_display.configure(font=("Quicksand Bold", 12))

    message_entry = ttk.Entry(chat_window, font=("Quicksand", 14))
    message_entry.pack(side=tk.BOTTOM, fill=tk.X)
    message_entry.bind("<Return>", send_message)

    send_button = ttk.Button(chat_window, text="Send", command=send_message)
    send_button.pack(side=tk.BOTTOM)

    chat_window.protocol("WM_DELETE_WINDOW", on_closing)

def update_clients_listbox():
    clients_listbox.delete(0, tk.END)
    for other_client in other_clients:
        clients_listbox.insert(tk.END, other_client)

def receive_messages():
    global client, chat_display, kicked

    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            if not data:
                break
            if data.startswith("/other_clients:"):
                other_clients.clear()
                other_clients.extend(data.split(":")[1].split(","))
                update_clients_listbox()
            elif data.startswith("You have been kicked by the server owner. Reconnection has been disabled."):
                kicked = True
                display_message(data)
                break
            else:
                display_message(data)
        except ConnectionResetError as e:
            print(f'Connection reset by server: {str(e)}')
            reconnect()
            break
        except Exception as e:
            print(f'An error occurred while receiving messages: {str(e)}')
            break


def send_message(event=None):
    global client, message_entry
    try:
        message = message_entry.get().strip()
        if message:
            if not kicked:
                client.send(message.encode('utf-8'))
                display_message(f"You > {message}")
                message_entry.delete(0, tk.END)
    except (ConnectionResetError, OSError) as e:
        print(f'Connection error occurred: {str(e)}')
        reconnect()

def update_clients_list():
    try:
        if not kicked:
            client.send("/get_other_clients".encode('utf-8'))
        else:
            pass
    except (ConnectionResetError, OSError) as e:
        print(f'Connection error occurred: {str(e)}')
        reconnect()
    chat_window.after(5000, update_clients_list)

def reconnect():
    global client, retry_attempts, kicked, receive_thread, server_address, server_port, chat_display, chat_window

    # Stop the receive thread before attempting to reconnect
    if receive_thread:
        receive_thread.join()

    while retry_attempts < MAX_RETRY_ATTEMPTS and not kicked:
        print("Attempting to reconnect...")
        chat_display.insert(tk.END, "Disconnected/Kicked from server. Attempting to reconnect...\n")
        try:
            client.close()
        except:
            pass

        try:
            chat_display.insert(tk.END, "Reconnecting...\n")
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((server_address, server_port))
            client.send(f"{nickname}".encode('utf-8'))
            retry_attempts = 0  # Reset retry attempts upon successful reconnection
            print("Reconnected successfully!")

            # Restart the receive thread
            receive_thread = threading.Thread(target=receive_messages)
            receive_thread.daemon = True
            receive_thread.start()

            break
        except Exception as e:
            print(f'Reconnect failed: {str(e)}')
            print("Reconnection attempt failed.")
            time.sleep(5)
            retry_attempts += 1

    else:
        if kicked:
            print("You have been kicked from the server. Reconnection is not allowed.")
            chat_display.insert(tk.END, "You have been kicked from the server. Reconnection is not allowed.\n")
        else:
            print("Max retry attempts reached. Please try again later.")
            chat_display.insert(tk.END, "Max retry attempts reached. Please try again later.\n")



def connect_to_server():
    global client, retry_attempts, kicked, server_address, server_port
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server_address, server_port))
        client.send(f"{nickname}".encode('utf-8'))

        retry_attempts = 0
        kicked = False  # Reset the kicked flag upon successful connection
    except Exception as e:
        print(f'Error connecting to the server: {str(e)}')
        reconnect()


def display_message(message):
    global chat_display
    chat_display.config(state=tk.NORMAL)

    sender_end_index = message.find(" > ")
    if sender_end_index != -1:
        sender_nickname = message[:sender_end_index]
        chat_display.insert(tk.END, f"{sender_nickname}: {message[sender_end_index + 3:]}\n")
    else:
        chat_display.insert(tk.END, message + '\n')

    chat_display.config(state=tk.DISABLED)
    chat_display.see(tk.END)

def update_clients_list():
    global kickmsgdisplayed
    try:
        if not kicked:
            client.send("/get_other_clients".encode('utf-8'))
        elif not kickmsgdisplayed:
            print("Client has been kicked. Reconnection has been disabled.")
            clients_listbox.delete(0, tk.END)
            kickmsgdisplayed = True
    except ConnectionResetError as e:
        print(f'Connection reset by server: {str(e)}')
        reconnect()
    chat_window.after(5000, update_clients_list)

def on_closing():
    global client, chat_window
    try:
        client.close()
    except Exception as e:
        print(f'An error occurred while closing the client socket: {str(e)}')
    finally:
        chat_window.destroy()

if __name__ == "__main__":
    nickname = simpledialog.askstring("Nickname", "Choose a Nickname")
    if nickname:
        other_clients = []
        create_gui()

        connect_to_server()

        receive_thread = threading.Thread(target=receive_messages)
        receive_thread.daemon = True
        receive_thread.start()

        update_clients_list()

        chat_window.mainloop()
