# Reverse cipher
import sys,pyperclip

__author__ = "Evan Mu"


def reverse_cipher(plain_text):
    translated = ''

    i = len(plain_text) - 1
    while i >= 0:
        translated = translated + plain_text[i]
        i -= 1

    return translated

if __name__ == '__main__':
    print("Reverse Cipher")
    if len(sys.argv) is 1:
        message = input("Please input your cipher text: \n")
    else:
        try:
            cipher_file = open(sys.argv[1])
        except FileNotFoundError as e:
            print("File not Exist," + e)
            exit(1)

        message = cipher_file.read()

    translated = reverse_cipher(message)
    print(translated)
    # Copy to clipboard
    pyperclip.copy(translated)
