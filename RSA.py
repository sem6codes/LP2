from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Input message
message = input("Enter message to encrypt: ").encode()

# Key generation
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Encrypt the message
encrypted = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Decrypt the message
decrypted = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Output
print("\n=== RSA Encryption and Decryption ===\n")
print(f"Enter Message       : {message.decode()}")
print("Public Key          : RSA Public Key")
print("Private Key         : RSA Private Key")
print(f"Encrypted Message   : {encrypted.hex()}")
print(f"Decrypted Message   : {decrypted.decode()}")
