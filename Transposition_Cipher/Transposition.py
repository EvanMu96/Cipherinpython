# Transposition Cipher Encryption
import pyperclip


def main():
    # replace your key and plain text
    my_message = 'Hello world'
    my_key = 5
    cipher_text = encrypt_message(my_key, my_message)
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
