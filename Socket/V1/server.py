import socket
import threading
import pickle #LEARN PICKLE TO SEND CUSTOM OBJECTS



class Server:
    def __init__(self,PORT,SERVER,HEADER=64,FORMAT='utf-8'):
        self.PORT = PORT
        self.SERVER = SERVER
        self.HEADER = HEADER
        self.FORMAT = FORMAT

    def start_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.SERVER,self.PORT))

    def handle_client(self, conn, addr):
        try:
            print(f"[NEW CONNECTION] {addr} connected.")
            connected = True
            while connected:
                msg_length = conn.recv(self.HEADER).decode(self.FORMAT)
                if msg_length:
                    msg_length = int(msg_length)
                    msg = conn.recv(msg_length).decode(self.FORMAT)
                    if msg == "!DISCONNECT":
                       connected = False
                       print(f"[DISCONNECTION] {addr} disconnected.")
                    else:
                       print(f"[{addr}]: {msg}")
                       #Validate new size
                       conn.send("Msg recieved".encode(self.FORMAT))
        except:
                raise Exception()
        conn.close()

    def run(self):
        self.start_server()
        self.server.listen()
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        while True:
            try:
                client_connection, addr = self.server.accept()
                thread = threading.Thread(target=self.handle_client,args=(client_connection,addr))
                thread.start()
                print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
            except:
                print(f"[ERROR OCURRED] connection with {addr} closed")
                client_connection.close()



Server = Server(5050,socket.gethostbyname(socket.gethostname()))

Server.run()
