from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(message, key):
    cipher = DES.new(key, DES.MODE_CBC)
    encrypted = cipher.encrypt(pad(message.encode(), DES.block_size))
    return cipher.iv + encrypted

def des_decrypt(encrypted, key):
    iv = encrypted[:DES.block_size]
    cipher = DES.new(key, DES.MODE_CBC, iv=iv)
    decrypted = unpad(cipher.decrypt(encrypted[DES.block_size:]), DES.block_size)
    return decrypted.decode()

# User input
key_input = input("Enter 8-character key for DES encryption: ").encode('utf-8')[:8]
message = input("Enter message to encrypt: ")

# Encryption
encrypted = des_encrypt(message, key_input)
decrypted = des_decrypt(encrypted, key_input)

# Print the output
print(f"\nOriginal text: {message}")
print(f"Encrypted text (in hex): {encrypted.hex()}")
print(f"Decrypted text: {decrypted}")
