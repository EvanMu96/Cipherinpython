# Hacking Caesar Cipher
import sys

def brute_force(cipher_text):
    __letters__ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length = len(__letters__)
    for key in range(length):
        # Traverse all possible key
        translated = ''
        for word in cipher_text:
            if word in __letters__:
                num = __letters__.find(word)
                num = num - key
                # handle the wrap-around if num is 26 or larger or less than 0
                if num < 0:
                    num += length
                translated = translated + __letters__[num]
            else:
                # just add the word without en/decrypt
                translated = translated + word
        print('KEY #%s: %s' % (key, translated))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: $python BruteForce.py [filename]')
        exit(1)
    try:
        f = open(sys.argv[1])
    except FileNotFoundError as e:
        print(e)
        exit(1)

    cipher_text = f.read().upper()
    brute_force(cipher_text)
