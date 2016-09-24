# Caesar Cipher

import pyperclip, sys

__author__ = 'Evan Mu'


def caesar_cipher(text, key, mode='encrypt'):
    __letters__ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length = len(__letters__)
    key = int(key)
    translated = ''
    for word in text:
        if word in __letters__:
            num = __letters__.find(word)
            if mode == 'encrypt' or 'en':
                num += key
            elif mode == 'decrypt' or 'de':
                num -= key
            # handle the wrap-around if num is larger than the length of
            # __letters__ or less than 0

            if num >= length:
                num -= length
            elif num < 0:
                num += length
            translated += __letters__[num]
        else:
            translated = translated + word
    print(translated)
    pyperclip.copy(translated)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: $python Caesar.py [filename] [key] [mode,en or de]')
        exit(1)
    try:
        f = open(sys.argv[1])
    except FileNotFoundError:
        print('File not found')
        exit(1)
    except IndexError:
        print('please input your file name,the file must in the same directory')
        exit(1)

    file_text = f.read().upper()

    caesar_cipher(file_text, sys.argv[2], sys.argv[3])

