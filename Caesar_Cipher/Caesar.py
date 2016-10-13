# Caesar Cipher

import pyperclip

__author__ = 'Evan Mu'


def main():
    my_message = 'helloworld'
    #  Your Cipher key
    my_key = 3
    my_message = my_message.upper()
    # mode = 'decrypt'
    translated = caesar_cipher(my_message, my_key)
    # Save to clipboard
    pyperclip.copy(translated)
    print(translated)
    print('Cipher text has save to clipboard')


def caesar_cipher(text, key, mode='encrypt'):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length = len(LETTERS)
    translated = ''
    key = int(key)
    for word in text:
        if word in LETTERS:
            num = LETTERS.find(word)
            if mode == 'encrypt' or 'en':
                num += key
            elif mode == 'decrypt' or 'de':
                num -= key
            # handle the wrap-around if num is larger than the length of
            # LETTERS or less than 0

            if num >= length:
                num -= length
            elif num < 0:
                num += length
            translated += LETTERS[num]
        else:
            translated = translated + word

    return translated


if __name__ == '__main__':
    main()