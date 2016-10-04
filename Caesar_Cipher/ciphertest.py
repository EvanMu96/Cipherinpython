import random, sys
import Caesar

def main():

    for i in range(20):
        # set random message to test
        random.seed(42)

        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        # convert message to a list and shuffle it

        message = list(message)
        random.shuffle(message)
        message = ''.join(message)

        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        # Check all possible keys for each message
        for key in range(1, len(message)):
            encrypted = Caesar.caesar_cipher(message, key)
            decrypted = Caesar.caesar_cipher(encrypted, key, 'decrypt')

            # encrypted and decrypted should match
            if message != decrypted:
                print('Mismatch with key %s and message %s. \n' % (key, message))
                print(decrypted)
                sys.exit()
    print('Transposition cipher is passed')

if __name__ == '__main__':
    main()
