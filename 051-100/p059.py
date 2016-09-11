#!/usr/bin/env python3
"""Project Euler, Problem 59."""
import itertools
import string
import sys

FILE = 'p059_cipher.txt'
DICTIONARY = '/usr/share/dict/words'


def decrypt(cipher, key):
    """Return the xor decryption of the bytes in cipher using the given key."""
    return ''.join(chr(byte ^ ord(key_value)) for byte, key_value in
                   zip(cipher, itertools.cycle(key)))


def remove_punctuation(s: str):
    """Remove punctuation and digits from the beginning and end of string."""
    return s.strip(string.punctuation + string.digits)


if __name__ == '__main__':
    with open(FILE, 'r') as f, open(DICTIONARY, 'r') as dic:
        cipher = [int(byte) for byte in f.read().split(',')]
        words = {word.strip() for word in dic}

    for key in itertools.product(string.ascii_lowercase, repeat=3):
        decrypted_words = []
        for word in map(remove_punctuation, decrypt(cipher, key).split()):
            if word:
                decrypted_words.append(word)
        if all(word.lower() in words for word in decrypted_words):
            break
    else:
        print('ERROR: no possible decryption detected.', file=sys.stderr)
        sys.exit(1)

    print(sum(ord(char) for char in decrypt(cipher, key)))
