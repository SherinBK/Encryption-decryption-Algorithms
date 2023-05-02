import hashlib
result1 = hashlib.md5(b'GeeksforGeeks')
print("The byte equivalent of hash is : ", end ="")
print(result1.digest())
str2hash = "GeeksforGeeks"
result2 = hashlib.md5(str2hash.encode())
print("The hexadecimal equivalent of hash is : ", end ="")
print(result2.hexdigest())
