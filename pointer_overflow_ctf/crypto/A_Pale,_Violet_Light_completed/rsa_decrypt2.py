from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

# Input RSA parameters (p, q, e, N, C)
p = 5807
q = 5861
e = 5039
N = 34034827
C = 15848125

# Calculate phi(N)
phi_N = (p - 1) * (q - 1)

# Calculate the modular multiplicative inverse of e (d)
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

d = modinv(e, phi_N)

# Create an RSA key object
private_key = RSA.construct((N, e, d))

# Create a cipher object for decryption
cipher = PKCS1_OAEP.new(private_key)

# Decrypt the ciphertext
decrypted_message = cipher.decrypt(C.to_bytes((C.bit_length() + 7) // 8, byteorder='big'))

# Print the decrypted message
print("Decrypted Message:")
print(decrypted_message.decode('utf-8'))
