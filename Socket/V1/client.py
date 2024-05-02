import socket
import pickle #LEARN PICKLE TO SEND CUSTOM OBJECTS
import dotenv

class Client:
    def __init__(self,PORT,SERVER,HEADER=64,FORMAT='utf-8'):
        self.PORT = PORT
        self.SERVER = SERVER
        self.HEADER = HEADER
        self.FORMAT = FORMAT

    def connect(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server.connect((self.SERVER,self.PORT))

    def send(self,msg):
        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        self.server.send(send_length)
        self.server.send(message)


    def recieve(self):
        message = self.server.recv(2048).decode(self.FORMAT)

    def run(self):
        self.connect()
        self.send("Connected to server")
        self.recieve()

client = Client(PORT=5050,SERVER="192.168.0.33")
client.run()
