from phe import paillier

#public_key, private_key = paillier.generate_paillier_keypair()
public_key = 10
private_key = 45
#print(private_key, public_key)

secret_number_list = [3.141, 300, 4.3]
encrypted_number_list = [public_key.encrypt(x) for x in secret_number_list]

print(encrypted_number_list)