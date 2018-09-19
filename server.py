import socket
import os
# 9/15/2018 
class auto_updater:
    
    FILE    = 'update/vs.txt'
    VERSION =  "0"
    HOST    = '127.0.0.1' 
    PORT    = 65222                     # PORT TO LISTEN ON non privileged ports are > 1023

    update = {
        "Update": "1",
        "Version": VERSION
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
                            if (self.no_update(connectionSocket)):
                                print("client doesnt need to update")

                        else:
                            if(self.update_client(connectionSocket)):
                                print("client needs to update") # while loop for client data

                else:
                    return(False)

        return(True)
    
    def send_version(self, socket):
        file = open(self.FILE).read().split('\n')
        
        if not ((file)):
            return(False)
            
        
        if (socket.sendall(str.encode(str(file)))):
            return(False)
        
        return(True)
                            
    def no_update(self, socket):
        if not ((self.update["Update"] == "0")):
            self.update["Update"] = "0"
            
        if (socket.sendall(str.encode(self.update["Update"]))):
            return(False)
        
        return(True)
                
        

    def update_client(self, socket):
        if not ((self.update["Update"] == "1")):
            self.update["Update"] = "1"
            
        if (socket.sendall(str.encode(self.update["Update"]))):
            return(False)
        
        return(True)
              
                  

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
        
        
