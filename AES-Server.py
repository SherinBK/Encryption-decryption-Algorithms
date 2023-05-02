import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)

    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

    @staticmethod
    def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        return plain_text[:-ord(last_character)]


if __name__=='__main__':
    import socket
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
        message=input("Enter the message that needs to be encrypted:")
        aes1 = AESCipher(key)
        
        encrypt=aes1.encrypt(message)
        print("The Encrypted message is:",encrypt)
        clientConnected.send(encrypt.encode())

        datafromClient=clientConnected.recv(1024)
        key=datafromClient.decode()
        datafromClient1=clientConnected.recv(1024)
        encrypt=datafromClient1.decode()
        decrypt=aes1.decrypt(encrypt)
        print("The decrypted form of the message received from the client is:",decrypt)
