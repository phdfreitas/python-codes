from random import randint


def encryption(string, step):
    output = ""
    for char in string:
        output += chr(ord(char) - step)

    return output


def decryption(string, step):
    output = ""
    for char in string:
        output += chr(ord(char) + step)

    return output


string = input()
step = randint(1, 26)
encrypted = encryption(string, step)
decrypted = decryption(encrypted, step)

print(f'Original: {string}')
print(f'Encrypted: {encrypted}')
print(f'Decrypted: {decrypted}')
