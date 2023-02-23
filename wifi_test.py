import socket
import tkinter as tk
import keyboard

# E --> arm UP
# Q --> arm DOWN
# F --> Let Go

IP_ADDRESS = "192.168.1.177"
PORT = 80

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP_ADDRESS, PORT))

def send_signal(signal):
    client_socket.send(signal)


def handle_keyboard_input(e):
    key = e.keysym
    if key == "w":
        send_signal(b'1')
        print("Signal for 'w' sent")
        w_label.config(bg="red")
    elif key == "a":
        send_signal(b'2')
        print("Signal for 'a' sent")
        a_label.config(bg="red")
    elif key == "s":
        send_signal(b'3')
        print("Signal for 's' sent")
        s_label.config(bg="red")
    elif key == "d":
        send_signal(b'4')
        print("Signal for 'd' sent")
        d_label.config(bg="red")
    elif key == "e":
        send_signal(b'5')
        print("Signal for 'e' sent")
        e_label.config(bg="red")
    elif key == "q":
        send_signal(b'6')
        print("Signal for 'q' sent")
        q_label.config(bg="red")
    elif key == "f":
        send_signal(b'7')
        print("Signal for 'f' sent")
        f_label.config(bg="red")

def handle_keyboard_release(e):
    key = e.keysym
    if key == "w":
        w_label.config(bg="white")
    elif key == "a":
        a_label.config(bg="white")
    elif key == "s":
        s_label.config(bg="white")
    elif key == "d":
        d_label.config(bg="white")
    elif key == "e":
        e_label.config(bg="white")
    elif key == "q":
        q_label.config(bg="white")
    elif key == "f":
        f_label.config(bg="white")

root = tk.Tk()
root.title("Arduino Signal Sender")
root.geometry("594x594")

# img = tk.PhotoImage(file= "mine.png")
# bg_label = tk.Label(root, image=img)
# bg_label.grid(row=0, column=0, rowspan=10, columnspan=10)



w_label = tk.Label(root, text="W", font=("Arial", 15), bg="light yellow", height=2, width=4)
w_label.place(relx=0.5, rely=0.4, anchor="center")

a_label = tk.Label(root, text="A", font=("Arial", 15), bg="light yellow", height=2, width=4)
a_label.place(relx=0.4, rely=0.5, anchor="center")

s_label = tk.Label(root, text="S", font=("Arial", 15), bg="light yellow", height=2, width=4)
s_label.place(relx=0.5, rely=0.5, anchor="center")

d_label = tk.Label(root, text="D", font=("Arial", 15), bg="light yellow", height=2, width=4)
d_label.place(relx=0.6, rely=0.5, anchor="center")

q_label = tk.Label(root, text="Q = down", font=("Arial", 15), bg="light yellow", height=4, width=8)
q_label.place(relx=0.2, rely=0.3, anchor="center")

e_label = tk.Label(root, text="E = up", font=("Arial", 15), bg="light yellow", height=4, width=8)
e_label.place(relx=0.8, rely=0.3, anchor="center")

f_label = tk.Label(root, text="F = Let Go", font=("Arial", 15), bg="light yellow", height=4, width=8)
f_label.place(relx=0.5, rely=0.3, anchor="center")


root.bind("<KeyPress>", handle_keyboard_input)
root.bind("<KeyRelease>", handle_keyboard_release)

root.mainloop()
