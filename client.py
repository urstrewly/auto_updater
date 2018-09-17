import socket
from datetime import datetime

class client:
    """ A simple client class """

    HOST    = '127.0.0.1'
    PORT    = 65222
    VERSION = 'VERSION/1.0'

    update = {import socket
from datetime import datetime

class auto_client:
    HOST    = '127.0.0.1'
    PORT    = 65222
    VERSION = 'VERSION/gay'

    update = {
        "Update":  0,
        "Version": 0,
        "Time": str(datetime.now())
        
    }

    def connect_client(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
            if (clientSocket.connect((self.HOST, self.PORT))):
                print("CANT CONNECT")

            print(self.VERSION)
            if (self.send_version(clientSocket)):
                    self.update["Update"] = clientSocket.recv(1024).decode()
                    print(self.update["Update"])

            
            
            return(True)
        return(False)

    def send_version(self, socket):           
            if not (socket.sendall(str.encode(self.VERSION))):
                return(True)
           

client1 = auto_client()

# regardless of new update, client always needs new software
if (client1.connect_client()):
    print("Client has new software")

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
