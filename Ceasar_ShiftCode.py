LOWER_OFFSET = 97
UPPER_OFFSET = 65


def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if (ord(char) >= ord('A')) and (ord(char) <= ord('Z')):
            char = ord(char) - UPPER_OFFSET
            char = (char + key) % 26
            char = char + UPPER_OFFSET
            ciphertext += chr(char)
        elif (ord(char) >= ord('a')) and (ord(char) <= ord('z')):
            char = ord(char) - LOWER_OFFSET
            char = (char + key) % 26
            char = char + LOWER_OFFSET
            ciphertext += chr(char)
        else:
            ciphertext += char

    return ciphertext

ciphertext = encrypt("intro to Cryptography", 6)
print(ciphertext)
# otzxu zu Ixevzumxgvne

def decrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if (ord(char) >= ord('A')) and (ord(char) <= ord('Z')):
            char = ord(char) - UPPER_OFFSET
            char = (char - key) % 26
            char = char + UPPER_OFFSET
            ciphertext += chr(char)
        elif (ord(char) >= ord('a')) and (ord(char) <= ord('z')):
            char = ord(char) - LOWER_OFFSET
            char = (char - key) % 26
            char = char + LOWER_OFFSET
            ciphertext += chr(char)
        else:
            ciphertext += char

    return ciphertext
ciphertext = decrypt("otzxu zu Ixevzumxgvne", 6)
print(ciphertext)
# otzxu zu Ixevzumxgvne