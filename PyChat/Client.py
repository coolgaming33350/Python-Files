import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog

# Global variables
client = None
nickname = None
chat_window = None
chat_display = None
message_entry = None

def create_gui():
    global chat_window, chat_display, message_entry
    chat_window = tk.Tk()
    chat_window.title("Chat Client")

    chat_display = scrolledtext.ScrolledText(chat_window)
    chat_display.pack(expand=True, fill=tk.BOTH)
    chat_display.config(state=tk.DISABLED)

    message_entry = tk.Entry(chat_window, font=("Helvetica", 14))
    message_entry.pack(side=tk.BOTTOM, fill=tk.X)
    message_entry.bind("<Return>", send_message)

    send_button = tk.Button(chat_window, text="Send", command=send_message)
    send_button.pack(side=tk.BOTTOM)

    chat_window.protocol("WM_DELETE_WINDOW", on_closing)

def receive_messages():
    global client, chat_display
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                display_message(message)
        except Exception as e:
            print(f'An error occurred while receiving messages: {str(e)}')
            break

def send_message(event=None):
    global client, message_entry
    message = message_entry.get().strip()
    if message:  # Check if message is not empty
        client.send(message.encode('utf-8'))
        display_message(f"You > {message}")  # Prefix your message before displaying
        message_entry.delete(0, tk.END)

def display_message(message):
    global chat_display
    chat_display.config(state=tk.NORMAL)
    
    # Extract sender's nickname and display the message with the prefix
    sender_end_index = message.find(" > ")
    if sender_end_index != -1:
        sender_nickname = message[:sender_end_index]
        chat_display.insert(tk.END, f"{sender_nickname}: {message[sender_end_index + 3:]}\n")
    else:
        # If sender's nickname is not found, display the message as it is
        chat_display.insert(tk.END, message + '\n')
    
    chat_display.config(state=tk.DISABLED)
    chat_display.see(tk.END)  # Scroll to the end

def on_closing():
    global client, chat_window
    try:
        client.send("exit".encode('utf-8'))  # Notify server that client is exiting
        client.close()
    except Exception as e:
        print(f'An error occurred while closing the client socket: {str(e)}')
    finally:
        chat_window.destroy()

if __name__ == "__main__":
    nickname = simpledialog.askstring("Nickname", "Choose a Nickname")
    if nickname:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('192.168.0.104', 5555))  # Connect to the server

        create_gui()

        # Send the nickname to the server
        client.send(nickname.encode('utf-8'))

        # Start a thread for receiving messages
        receive_thread = threading.Thread(target=receive_messages)
        receive_thread.daemon = True
        receive_thread.start()

        # Start the GUI main loop
        chat_window.mainloop()
