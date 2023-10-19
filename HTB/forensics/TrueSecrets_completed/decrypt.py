from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import base64

def decrypt(encrypted_text, key, iv):
    key_bytes = key.encode('utf-8')
    iv_bytes = iv.encode('utf-8')
    encrypted_bytes = base64.b64decode(encrypted_text)
    
    cipher = DES.new(key_bytes, DES.MODE_CBC, iv_bytes)
    decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes), DES.block_size)
    
    return decrypted_bytes.decode('utf-8')

# Example usage:

encrypted_text_lines = open("/media/veracrypt1/malware_agent/sessions/de008160-66e4-4d51-8264-21cbc27661fc.log.enc","r").readlines()  # Replace with your encrypted text
key = "AKaPdSgV"  # Replace with your key
iv = "QeThWmYq"   # Replace with your IV
for i in range(len(encrypted_text_lines)):
	decrypted_text = decrypt(encrypted_text_lines[i], key, iv)
	print(decrypted_text)
