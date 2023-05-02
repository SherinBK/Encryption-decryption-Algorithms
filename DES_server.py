from Crypto.Cipher import DES
import socket

def pad(text):
    n = len(text) % 8
    return text + (b' ' * n)

def encryption(key,text):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(text)
    encrypted_text = des.encrypt(padded_text)
    return encrypted_text
    
def decryption(key,encrypted_text):
    des = DES.new(key, DES.MODE_ECB)
    decrypted_mesg = des.decrypt(encrypted_text)
    return decrypted_mesg
    
if __name__=='__main__':
    #Server SocketConnection
    serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverSocket.bind(("127.0.0.1",9090))
    serverSocket.listen(1)
    while(True):
        (clientConnected,clientAddress)=serverSocket.accept()
        print(clientAddress[0],clientAddress[1])

        #Encryption and Decryption of a text
        key=input("Enter the key value:")
        clientConnected.send(key.encode())
        key = bytes(key,'utf-8')
        message=input("Enter the message that needs to be encrypted:")
        message =  bytes(message,'utf-8')
        e_msg = encryption(key,message)
        print("The Encrypted message is:",e_msg)
        clientConnected.send(e_msg)

        datafromClient=clientConnected.recv(1024)
        key=datafromClient.decode()
        key = bytes(key,'utf-8')
        datafromClient1=clientConnected.recv(1024)
        e_msg=datafromClient1
        d_msg = decryption(key,e_msg)
        print("The decrypted form of the message received from the client is:",d_msg)
