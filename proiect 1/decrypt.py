import sys


class InputError(Exception):
    def __init__(self, message="Input incorect\nformat decriptare: \"python decrypt.py output cheie input_recuperat.txt\""):
        super().__init__(message)


def xor_text(text):
    decrypted_text = ""
    key = sys.argv[2]
    for index in range(len(text)):
        decrypted_text += chr(ord(text[index]) ^ ord(key[index % (len(key))]))
    return decrypted_text


def decrypt():
    text = ""
    input_file = sys.argv[1]
    output_file = sys.argv[3]
    try:
        with open(input_file, "r", newline='') as f:
            text = f.read()
    except:
        print("Fisierul nu exista")
    else:
        decrypted_text = xor_text(text)
        with open(output_file,"w") as f:
            f.write(decrypted_text)


if __name__ == '__main__':

    n = len(sys.argv)

    if n != 4:
        raise InputError
        sys.exit()

    decrypt()
