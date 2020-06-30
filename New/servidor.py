import socket
from _thread import *
from player import Player
import pickle

server = "192.168.15.10"
port = 5555

#******************* Criando o servidor **************************
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

#*********** Quantas pessoas podem se conectar *******************
s.listen(4)
print("Esperando conexão, servidor conectado")

#******************** Posição do cliente *************************
players = [Player(50,50,15,15,(255,0,0)), Player(400,400, 15,15, (0,0,255)), Player(50,400, 15,15, (0,255,0)), Player(400,50, 15,15, (0,255,255))]

#************************** Thread *******************************
def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(4096))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                elif player == 2:
                    reply = players[1]
                elif player == 3:
                    reply = players[2]
                else:
                    reply = players[3]

               # print("Received: ", data)
               # print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0

#******************** Procurando conexão ************************
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
