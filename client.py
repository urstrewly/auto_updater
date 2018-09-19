import socket
from datetime import datetime

class auto_client:
    HOST    = '127.0.0.1'
    PORT    = 65222
    VERSION = 'VERSION/0.0.1'

    update = {
        "Update":  0,
        "Version": 0,
        "Time": str(datetime.now())
        
    }

    def connect_client(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
            if (clientSocket.connect((self.HOST, self.PORT))):
                print("CANT CONNECT")

            if (self.send_version(clientSocket)):
                    self.update["Version"] = clientSocket.recv(1024).decode()
                    
                    self.update["Update"]  = clientSocket.recv(1024).decode()

            print("This clients current build: " + self.VERSION)        
            print("Current build version: " + self.update["Version"])
            print("update bool: " + self.update["Update"])        

            if (self.update["Update"] == '1'):
                # run closeme.exe and close alpha.exe -- run new update.
                print("client needs update")
                return(True)
            
            else:
                print("client doesnt need update")
                return(True)
            
            
        return(False)

    def send_version(self, socket):           
            if not (socket.sendall(str.encode(self.VERSION))):
                return(True)
           

client1 = auto_client()

# regardless of new update, client always needs new software
if not (client1.connect_client()):
    print("Client cant connect")
