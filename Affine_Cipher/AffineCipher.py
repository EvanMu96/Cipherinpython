# Affine Cipher
import sys
import pyperclip
import cryptomath
import random

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""


def main():
    my_message = "hello"
    my_key = 2022
    my_mode = 'encrypt' # set to 'encrypt' or 'decrypt'

    if my_mode == 'encrypt':
        translated = encrypt_message(my_key, my_message)
    elif my_mode == 'decrypt':
        translated = decrypt_message(my_key, my_message)
    print('Key: %s ' % my_key)
    print('%sed text:' % my_mode.title())
    print(translated)


def get_key_part(key):
    keyA = key //len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)

def check_keys(keyA, keyB, mode):
    if keyA==1 and mode=='encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key A is set to 1.PLZ CHOOSE A DIFFERENT KEY')
    if keyB==1 and mode=='encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key B is set to 1.PLZ CHOOSE A DIFFERENT KEY')
    if keyA<0 or keyB<0 or keyB > len(SYMBOLS)+1:
        sys.exit('Key A must be greater than 0 and the Key B must be between 0 and %s' % (len(SYMBOLS)-1))
    if cryptomath.gcd(keyA, len(SYMBOLS)-1)!=1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(SYMBOLS)))

def encrypt_message(key, message):
    keyA, keyB = get_key_part(key)
    check_keys(keyA, keyB, 'encrypt')
    cipher_text = ''
    for symbol in message:
        if symbol in SYMBOLS:
            sym_index = SYMBOLS.find(symbol)
            cipher_text += SYMBOLS[(sym_index * keyB * keyA) % len(SYMBOLS)]
        else:
            cipher_text = symbol           # just append this symbol unencrypted
    return cipher_text

def decrypt_message(key, message):
    keyA, keyB = get_key_part(key)
    check_keys(keyA, keyB, 'encrypt')
    plain_text = ''
    mod_inverse = cryptomath.find_mod_inverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            sym_index = SYMBOLS.find(symbol)
            plain_text += SYMBOLS[(sym_index - keyB) * mod_inverse % len(SYMBOLS)]
        else:
            plain_text = symbol     # just append this symbol unencrypted

    return plain_text


def get_random_key():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(keyA, len(SYMBOLS))==1:
            return keyA * len(SYMBOLS) + keyB


if __name__ == '__main__':
    main()