from socket import *
serverPort = 9999
serverName = gethostbyname(gethostname())
# serverName = '119.161.98.68' #Hint : Change accordingly.


# SOCKET OBJECT => ( IPv4 , UDP )
serverSocket = socket(AF_INET, SOCK_DGRAM)
print(serverSocket)

# BInding server name and port to A SOCKET
serverSocket.bind((serverName, serverPort))
print("The server is ready to receive")

while True:

    message, clientAddress = serverSocket.recvfrom(4096)
    print("clientAddress : ", clientAddress)

    modifiedMessage = message.decode().upper()
    print("check 2")

    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    print("check 3")
