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
  

    #ClientSocket Connection
    clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientSocket.connect(("127.0.0.1",9090))

    #Receiveing the message from server which is in encrypted form
    datafromServer=clientSocket.recv(1024)
    datafromServer1=clientSocket.recv(1024)
   

    #print(datafromServer.decode())
    key=datafromServer.decode()
    key = bytes(key,'utf-8')
    e_msg=datafromServer1
    d_msg = decryption(key,e_msg)
    
    print("The decrypted form of the message received from the server is:",d_msg)

    key=input("Enter the key value:")
    clientSocket.send(key.encode())
    key = bytes(key,'utf-8')
    message=input("Enter the message that needs to be encrypted:")
    message =  bytes(message,'utf-8')
    e_msg= encryption(key,message)
    print("The Encrypted message is:",e_msg)
    clientSocket.send(e_msg)
