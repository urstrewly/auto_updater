import socket
from datetime import datetime

class auto_client:
    HOST    = '127.0.0.1'
    PORT    = 65222
    VERSION = 'VERSION/6.2.4'       # VERSION/6.2.4 -- newest version in text file to use as test

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

            print(self.update["Time"] + " -- This clients current build: " + self.VERSION)        
            print(self.update["Time"] + " -- Current build version: " + self.update["Version"])
            print(self.update["Time"] + " -- update bool: " + self.update["Update"])

            if (self.update["Update"] == '1'):
                # run closeme.exe and close alpha.exe -- run new update.
                return(True)
            
            else:
                return(True)
            
            
        return(False)

    def send_version(self, socket):           
            if not (socket.sendall(str.encode(self.VERSION))):
                return(True)
           

client1 = auto_client()

# regardless of new update, client always needs new software
if not (client1.connect_client()):
    print("Client cant connect")
