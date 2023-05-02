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

#ClientSocket Connection

clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect(("127.0.0.1",9090))
#Receiveing the message from server which is in encrypted form
datafromServer=clientSocket.recv(1024)
res=datafromServer.decode()
#The message from server is decrypted
res1=decrypt_text(res,1)
print("The message from server which is converted to decrypted form:",res1)
#Sending the reply message from client to server
data=input("Enter the reply message which needs to be sent to the server:")
#The message that needs to sent to the server is encrypted and then sent
res2=encrypt_text(data,1)
print("The Encrypted form of the received message is:",res2)
clientSocket.send(res2.encode())
