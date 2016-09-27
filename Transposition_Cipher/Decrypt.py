import sys, pyperclip, math

__author__ = 'Evan Mu'

def decrypt_message(key, message):

    num_of_cols = math.ceil(len(message) / key)
    num_of_rows = key
    # box without number
    num_of_shade = num_of_rows * num_of_cols - len(message)

    plain_text = [''] * num_of_cols

    col, row = 0, 0

    for symbol in message:
        plain_text[col] += symbol
        col += 1

        if (col == num_of_cols) or (col == num_of_cols -1 and row >= num_of_rows - num_of_shade):
            col = 0
            row += 1
    return ''.join(plain_text)

def main():
    if len(sys.argv) != 3:
        print('Usage: $python decrypt.py [filename] [key]')
        exit(1)
    try:
        f = open(sys.argv[1])
    except FileNotFoundError as e:
        print(e)
        exit(1)
    plain_text = f.read()
    key = int(sys.argv[2])
    cipher_text = decrypt_message(key, plain_text)
    print(cipher_text + '|')

    # Copy to clipboard
    pyperclip.copy(cipher_text)
    print('Plain text has save to clipboard')

if __name__ == '__main__':
    main()
