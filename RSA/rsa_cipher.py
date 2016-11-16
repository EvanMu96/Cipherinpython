import sys

DEFAULT_BLOCK_SIZE = 128 #128 bytes
BYTE_SIZE = 256  #256 different value in one byte

def main():
    # Runs a test that encrypts a message to a file or decrypts a message fron a file
    filename = 'encrypted_file.txt'
    mode = 'encrypt'
    # mode = 'decrypt'
    if mode == 'encrypt':
        message = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis n
        ostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis au
        te irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat null
        a pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui offici
        deserunt mollit anim id est laborum."""
        # using someone's public key
        public_key_filename = 'evan_pk1.txt'
        print('encrypting and writing to %s...' % filename)
        cipher_text = encrypt_n_write(filename, public_key_filename, message)
        print('The text has been encrypted')
        print(cipher_text)

    elif mode == 'decrypt':
        # using private_key_filename to decrypt
        private_key_filename = 'evan_pk2.txt'
        print('reading from %s and decrypting' % private_key_filename)
        plain_text = read_n_decrypt(filename, private_key_filename)

        print('The text has been decrypted')
        print(plain_text)

def get_blk_from_text(message, blocksize=DEFAULT_BLOCK_SIZE):
    # Converts a string message to a list of block integers.
    # Each integers represents 128 (or whatever blocksize u wanna to set) string characters

    message_bytes = message.encode('ascii') # Converts message to ascii code

    block_ints = []
    for blockstart in range(0, len(message_bytes), blocksize):
        # Calculate the block integer for thie block fo text
        block_int = []
        for i in range(blockstart, min(blockstart + blocksize, len(message_bytes))):
            block_int += message_bytes[i] * (BYTE_SIZE ** (i % blocksize))
        block_ints.append(block_int)
    return block_ints

def get_text_from_blocks(block_int, message_length, blocksize=DEFAULT_BLOCK_SIZE):
    # Converts a list of block integers to the original message string
    # The original message length is needed to properly convert the last block integer
    message = []
    for i in range(blocksize - 1, -1, -1):
        block_message = []
        if len(message) + i < message_length:
            ascii_number = block_int // (BYTE_SIZE ** i)
            block_int = block_int % (BYTE_SIZE ** i)
            block_message.insert(0, chr(ascii_number))
        message.extend(block_message)
    return ''.join(block_message)
