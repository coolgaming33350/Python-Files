import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog, Listbox

client = None
nickname = None
chat_window = None
chat_display = None
message_entry = None
clients_listbox = None

def create_gui():
    global chat_window, chat_display, message_entry, clients_listbox
    chat_window = tk.Tk()
    chat_window.title("Chat Client")

    clients_listbox = Listbox(chat_window, width=20)
    clients_listbox.pack(side=tk.LEFT, fill=tk.Y)

    chat_display = scrolledtext.ScrolledText(chat_window)
    chat_display.pack(expand=True, fill=tk.BOTH)
    chat_display.config(state=tk.DISABLED)

    message_entry = tk.Entry(chat_window, font=("Helvetica", 14))
    message_entry.pack(side=tk.BOTTOM, fill=tk.X)
    message_entry.bind("<Return>", send_message)

    send_button = tk.Button(chat_window, text="Send", command=send_message)
    send_button.pack(side=tk.BOTTOM)

    chat_window.protocol("WM_DELETE_WINDOW", on_closing)

def update_clients_listbox():
    clients_listbox.delete(0, tk.END)
    for other_client in other_clients:
        clients_listbox.insert(tk.END, other_client)

def receive_messages():
    global client, chat_display
    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            if not data:
                break
            if data.startswith("/other_clients:"):
                other_clients.clear()
                other_clients.extend(data.split(":")[1].split(","))
                update_clients_listbox()
            else:
                display_message(data)
        except Exception as e:
            print(f'An error occurred while receiving messages: {str(e)}')
            break

def send_message(event=None):
    global client, message_entry
    message = message_entry.get().strip()
    if message:
        client.send(message.encode('utf-8'))
        display_message(f"You > {message}")
        message_entry.delete(0, tk.END)

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
    client.send("/get_other_clients".encode('utf-8'))
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
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('192.168.0.104', 5555))

        other_clients = []
        create_gui()

        client.send(f"{nickname}".encode('utf-8'))

        receive_thread = threading.Thread(target=receive_messages)
        receive_thread.daemon = True
        receive_thread.start()

        update_clients_list()

        chat_window.mainloop()
