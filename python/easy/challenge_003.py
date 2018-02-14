#ALPHABET CHIPERS.
#TODO raise different error if encrypt/decrypt command not found.
import sys, string

ALPHABET = string.ascii_lowercase
ALPHABET_LEN = len(ALPHABET)

def encrypt(line, n):
    encrypt_line = ''
    for letter in line:
        if letter.isalpha():
            index = ALPHABET.find(letter)
            move = (index + n) % ALPHABET_LEN
            encrypt_line += ALPHABET[move]
    
    return encrypt_line

def caesar():
    try:
        #print(sys.argv[1])
        #print(sys.argv[2])
        with open(sys.argv[1]) as f_in:
            lines = list(f)

    except IndexError as e:
        print("Input file name cannot be empty.")

if __name__ == "__main__":
    #caesar()
    print(encrypt('abcde', 2))
    print(encrypt('abcde', 28))