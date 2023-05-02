#Importing Socket Library
import socket
#Function to encrypt the message
def encrypt_text(plaintext,n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
       	# check if space is there then simply add space
        if ch==" ":
            ans+=" "
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
    return ans

#Function to decrypt the message
def decrypt_text(plaintext,n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        
        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            ans += chr((ord(ch) - n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        
        else:
            ans += chr((ord(ch) - n-97) % 26 + 97)
    
    return ans

#Server SocketConnection
serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(("127.0.0.1",9090))
serverSocket.listen(1)
while(True):
    (clientConnected,clientAddress)=serverSocket.accept()
    print(clientAddress[0],clientAddress[1])
    msg=input("Enter the message that needs to be sent to the client:")
    n=1
    ans=encrypt_text(msg,n)
    print("The Encrypted Message is:",ans)
    #Sending message to the client
    clientConnected.send(ans.encode())
    #Receiving message from the client
    datafromClient=clientConnected.recv(1024)
    res2=datafromClient.decode()
    ans2=decrypt_text(res2,1)
    print("The Decrypted form of the received message is:",ans2)
