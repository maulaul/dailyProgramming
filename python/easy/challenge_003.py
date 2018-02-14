#ALPHABET CHIPERS.
#TODO raise different error if encrypt/decrypt command not found.
import sys

def caesar():
    try:
        #print(sys.argv[1])
        #print(sys.argv[2])
        with open(sys.argv[1]) as f_in:
            lines = list(f)

    except IndexError as e:
        print("Input file name cannot be empty.")

if __name__ == "__main__":
    caesar()
