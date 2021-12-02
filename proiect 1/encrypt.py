import sys


class InputError(Exception):
    def __init__(self, message="Input incorect\nformat criptare: \"python encrypt.py key input.txt output\""):
        super().__init__(message)


def xor_text(text):
    encrypted_text = ""
    key = sys.argv[1]
    for index in range(len(text)):
        encrypted_text += chr(ord(text[index]) ^ ord(key[index % (len(key))]))
    return encrypted_text


def encrypt():
    text = ""
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    try:
        with open(input_file, "r") as f:
            text = f.read()
    except:
        print("Fisierul nu exista")
    else:
        encrypted_text = xor_text(text)
        with open(output_file,"w", newline='') as f:
            f.write(encrypted_text)


if __name__ == '__main__':

    n = len(sys.argv)

    if n != 4:
        raise InputError
        sys.exit()

    encrypt()
