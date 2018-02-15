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
    processed_lines = ''
    try:
        filename = sys.argv[1]
        n = 13 #amount of letter move.
        with open(filename) as f_in:
            lines = list(f)

        if sys.argv[2] == 'decrypt':
            for line in lines:
                processed_lines += decrypt(line, n)
                with open(filename.split('.')[0] + '_decrypt.txt', w) as f_out:
                    f_out.writelines(processed_lines)
        else:
            for line in lines:
                processed_lines += encrypt(line, n)
                with open(filename.split('.')[0] + '_encrypt.txt', w) as f_out:
                    f_out.writelines(processed_lines)

    except IndexError as e:
        print("Input file name cannot be empty.\nMake sure the filename is correct and encrypt/decrypt is specified.")

if __name__ == "__main__":
    caesar()
    