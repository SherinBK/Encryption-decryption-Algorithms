from tinyec import registry
import secrets

def compress(publicKey):
    return hex(publicKey.x) + hex(publicKey.y % 2)[2:]

curve = registry.get_curve('brainpoolP256r1')

Ka = secrets.randbelow(curve.field.n)
X = Ka * curve.g
print("X:", compress(X))
Kb = secrets.randbelow(curve.field.n)
Y = Kb * curve.g
print("Y:", compress(Y))
print("Currently exchange the publickey (e.g. through Internet)")

A_SharedKey = Ka * Y
print("A shared key :",compress(A_SharedKey))
B_SharedKey = Kb * X
print("(B) shared key :",compress(B_SharedKey))
print("Equal shared keys:", A_SharedKey == B_SharedKey)
