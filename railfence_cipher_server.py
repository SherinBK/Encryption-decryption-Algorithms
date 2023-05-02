import socket
HOST ='127.0.0.1'
PORT = 65432

def encryptRailFence(text, key): 
    rail = [['\n' for i in range(len(text))]
                  for j in range(key)]     
    # to find the direction
    dir_down = False
    row, col = 0, 0     
    for i in range(len(text)):         
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down         
        rail[row][col] = text[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))
     



def decryptRailFence(cipher, key): 
    rail = [['\n' for i in range(len(cipher))]
                  for j in range(key)]     
    dir_down = None
    row, col = 0, 0     
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
         
        rail[row][col] = '*'
        col += 1
         
        if dir_down:
            row += 1
        else:
            row -= 1
             
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
               (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
         
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
         
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
             
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
             
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  conn, addr = s.accept()
  with conn:
    while True:
      data = conn.recv(1024)
      message = str(data.decode())
      key = int(input("Enter the key : "))
      print("Received from client before encryption:",message)
      test = decryptRailFence(message,key)
      print("Received from client after decryption:",test)
      if not data:
        break
      sendd = input("Enter the message: ")
      dataa = encryptRailFence(sendd,key)
    #   sendd = encrypt(dataa,keyy)
      conn.sendall(dataa.encode())
      break

