import socket
import os
import json
import sys
from datetime import datetime
# 9/15/2018 
class auto_updater:
    
    FILE    = 'update/vs.txt'
    VERSION =  "0"
    HOST    = '127.0.0.1' 
    PORT    = 65222                     # PORT TO LISTEN ON non privileged ports are > 1023

    update = {
        "Update": "1",
        "Version": VERSION,
        "Time": str(datetime.now())
     }
  
    def update_manager(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listenSocket:
            listenSocket.bind((self.HOST, self.PORT))
            listenSocket.listen()
            connectionSocket, info = listenSocket.accept()
            
            with connectionSocket:
                print('Client connected from ', info)
                self.VERSION = connectionSocket.recv(1024).decode() 
                while True:
                    if (self.VERSION):
                        break

                if not (self.send_version(connectionSocket)):
                        
                        if not ((self.verify_client())):
                            self.no_update(connectionSocket)

                        else:
                            self.update_client(connectionSocket) # while loop for client data

                else:
                    return(False)

        return(True)
    
    def send_version(self, socket):
        file = open(self.FILE).read().split('\n')
        
        if not ((file)):
            return(False)
            
        
        if (socket.sendall(str.encode(str(file)))):
            return(True)
        

                            
    def no_update(self, socket):
        if not ((self.update["Update"] == "0")):
            self.update["Update"] = "0"
                                                    
            for item in self.update:
                if (socket.sendall(str.encode(self.update[item]))):
                    print("sent no update needed")
                    return(True)
                
                return(False)

    def update_client(self, socket):
        if not ((self.update["Update"] == "1")):
            self.update["Update"] = "1"
            
        for item in self.update:
            socket.sendall(str.encode(self.update[item]))

            while True:
                pass
                # call closeme.exe - closeme.exe run update.exe after ( but is named test.exe for testing )
            return(True);         

    def verify_client(self):
        file = open(self.FILE).read().split('\n')

        #update
        if not ((file[0] == self.VERSION)):
            print("update required")
            return(True)


        # dont update    
        else:
            print("update not required")
            return(False)
            
cl_updater = auto_updater()
cl_updater.update_manager()
        
        
