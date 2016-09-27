# Transposition Cipher Encryption
import pyperclip, sys


def main():

    if len(sys.argv) != 3:
        print('Usage: $python transposition.py [filename] [key]')
        exit(1)
    try:
        f = open(sys.argv[1])
    except FileNotFoundError as e:
        print(e)
        exit(1)
    plain_text = f.read()
    key = int(sys.argv[2])
    cipher_text = encrypt_message(key, plain_text)
    print(cipher_text + '|')

    # Copy to clipboard
    pyperclip.copy(cipher_text)
    print('Cipher text has save to clipboard')

def encrypt_message(key, message):
    # Each string in ciphertext represents a column in the grid
    cipher_text = [''] * key

    # Loop through each column in ciphertext
    for col in range(key):
        pointer = col

        # Keep looping until pointer goes past the length of the message
        while pointer < len(message):
            cipher_text[col] += message[pointer]
            pointer += key
    return ''.join(cipher_text)

if __name__ == '__main__':
    main()
