import socket
from _thread import *
import sys

server = "192.168.15.10"
port = 5555

#******************* Criando o servidor **************************
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

#*********** Quantas pessoas podem se conectar *******************
s.listen(2)
print("Esperando conexão, servidor conectado")

#***************** Configurando as posições **********************
def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

#******************** Posição do cliente *************************
pos = [(70,70), (430,430)]

#************************** Thread *******************************
def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0

#****************************Procurando conexão*****************
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
