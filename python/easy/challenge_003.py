#ALPHABET CHIPERS.
import sys

def caesar():
    try:
        print(sys.argv[1])
    except IndexError as e:
        print("Input file name cannot be empty.")

if __name__ == "__main__":
    caesar()
