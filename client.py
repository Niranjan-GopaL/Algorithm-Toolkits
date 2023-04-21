from socket import *
serverName = gethostbyname(gethostname()) #Hint : Change accordingly.
# serverName = '119.161.98.68' #Hint : Change accordingly.
serverPort = 9999
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("Input lowercase sentence : ")


# fine
clientSocket.sendto(message.encode(),(serverName, serverPort))
print("check 1")
print(serverName)


modifiedMessage, serverAddress = clientSocket.recvfrom(4096)    
print("check 2")

print(modifiedMessage.decode())
print("check 3")

clientSocket.close()
print("check 4")
