import socket   

def encrypt(text,s):

    result = ""
    s=int(s)   
    for i in range(len(text)):
        char = text[i]     
 
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)        
        elif(char.islower()):
            result += chr((ord(char) + s - 97) % 26 + 97)            
        else:
            result += char 
    return result   

def decrypt(text,s):
    result = ""
    s=int(s)    
    for i in range(len(text)):
        char = text[i] 
        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)       
        elif(char.islower()):
            result += chr((ord(char) - s - 97) % 26 + 97)           
        else:
            result += char 
    return result            
 
# next create a socket object
s = socket.socket()        
print ("Socket successfully created")
 

port = 65432              
 

s.bind(('', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)    
print ("socket is listening")           
 

while True:
 

  c, addr = s.accept()    
  print ('Got connection from:', addr )
 
  
  c.send('Thank you for connecting'.encode())
  
  key=c.recv(65432).decode()
  en_rec_text=c.recv(1024).decode()
  print("Received Encrypted Text:", en_rec_text)
  de_text=decrypt(en_rec_text,key)
  print("Received Decrypted Text:", de_text)
  
  reply_text = input("Enter the reply text:")
  en_se_text = encrypt(reply_text,key)
  
  c.sendall(key.encode('utf-8'))
  c.sendall(en_se_text.encode('utf-8'))
  
  c.close()
