def encrypt_message(msg, key):
    cipher = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(msg):
            cipher[col] += msg[pointer]
            pointer += key
    return ''.join(cipher)

def decrypt_message(cipher, key):
    num_rows = len(cipher) // key
    if len(cipher) % key != 0:
        num_rows += 1

    plain = [''] * len(cipher)
    index = 0
    for col in range(key):
        pointer = col
        while pointer < len(cipher):
            plain[pointer] = cipher[index]
            index += 1
            pointer += key
    return ''.join(plain)

message = input("Enter message: ")
key = int(input("Enter key: "))

encrypted = encrypt_message(message, key)
print("Encrypted:", encrypted)

decrypted = decrypt_message(encrypted, key)
print("Decrypted:", decrypted)
