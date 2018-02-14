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
        else:
            encrypt_line += letter
    
    return encrypt_line

def decrypt(line, n):
    if n > ALPHABET_LEN:
        n = n % 26
    
    decrypt_line = ''
    for letter in line:
        if letter.isalpha():
            index = ALPHABET.find(letter)
            move = (abs(index - n)) % ALPHABET_LEN
            decrypt_line += ALPHABET[move]
        else:
            decrypt_line += letter

    return decrypt_line

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
    print(decrypt(encrypt('abcde', 2), 2))
    print(encrypt('abcde', 28))
    print(decrypt(encrypt('abcde', 28) ,28))