# Simple Substitution Cipher
import pyperclip
import sys
import random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    my_message = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell'
    my_key = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    my_mode = 'encrypt'

    # Check my_key is valid or not
    check_valid_key(my_key)

    if my_mode=='encrypt':
        translated = encrypt_message(my_key, my_message)
    elif my_mode=='decrypt':
        translated = decrypt_message(my_key, my_message)
    print('Using key %s' % my_key)
    print('THe %sed message is :' % my_mode)
    print(translated)
    pyperclip.copy(translated)
    print()
    print('This message has copied to clipboard')


def check_valid_key(key):
    key_list = list(key)
    letters_list = list(LETTERS)
    key_list.sort()
    letters_list.sort()
    if key_list != letters_list:
        sys.exit('There is an error in the key or symbol set')


def encrypt_message(key, message):
    return translate_message(key, message, 'encrypt')


def decrypt_message(key, message):
    return translate_message(key, message, 'decrypt')


def translate_message(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode=='decrypt':
        # For decrypting, we can use the same code as encrypting.
        # We just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA
    # Loop each symbol in message
    for symbol in message:
        if symbol.upper() in charsA:
            # encrypt/decrypt the symbol
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated +=symbol

    return translated


def get_random_key():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

if __name__ == '__main__':
    main()