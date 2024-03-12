
# Intentionat sa fie rulat pe windows, nu am gasit metode simple de a captura input in realtime in Unix

import socket, win32gui, win32process, os
from pynput import keyboard

# Creare client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conectare la IP
###IP = input("IP: ")
IP = "localhost"
s.connect((IP, 8008))

# O functie care trimite input-ul de la tastatura serverului
def on_press(key):
    focus_window_pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[1]
    current_process_pid = os.getppid()
    if focus_window_pid == current_process_pid:
        s.sendall(str(key).encode('utf-8'))

# Asculta pentru input-uri
listener = keyboard.Listener(
        on_press=on_press,
        on_release=None)
listener.start()


print("Successfully connected to " + IP)


# Loop pentru desenare imediata a informatiilor primite de la server
while True:
    data = s.recv(1024)

    if data:
        os.system('cls')
        print(data.decode('utf-8'))