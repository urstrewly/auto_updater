import socket
import os
import json
import sys
from datetime import datetime

class auto_updater:
    """ A simple server class """

    FILE    = 'update/readme.txt'
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
                while True:
                    self.VERSION = connectionSocket.recv(1024)            
                    if not self.VERSION:
                        return(False);
                     
                    
                    else:
                        if not(self.verify_client()):
                            self.no_update(connectionSocket)
                        
                       
                        else:
                            self.update_client(connectionSocket)
                            
    def no_update(self, socket):
        if not(self.update["Update"] == "0"):
            self.update["Update"] = "0"
                                                    
            for item in self.update:
                socket.sendall(str.encode(self.update[item]))
            return(False)

    def update_client(self, socket):
        if not(self.update["Update"] == "1"):
            self.update["Update"] = "1"
            
            for item in self.update:
                socket.sendall(str.encode(self.update[item]))


            # call patch

            # close old executable
                            
            # execute update and run file               
            return(True);         

    def verify_client(self):
        file = open(self.FILE).read().split('\n')

        #update
        if not(file[0] == self.VERSION.decode()):
            return(True)


        # dont update    
        else:
            return(False)
            
cl_updater = auto_updater()
cl_updater.update_manager()
        
        

