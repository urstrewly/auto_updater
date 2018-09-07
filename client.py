import socket
from datetime import datetime

class client:
    """ A simple client class """

    HOST    = '127.0.0.1'
    PORT    = 65222
    VERSION = 'VERSION/1.0'

    update = {
        "Update":  0,
        "Version": 0,
        "Time": str(datetime.now())
        
    }

    def connect_client(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
            clientSocket.connect((self.HOST, self.PORT))
            clientSocket.sendall(str.encode(self.VERSION))
            data = clientSocket.recv(1024).decode()


            print(data)






client1 = client()


client1.connect_client()
