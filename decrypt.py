import sys

class InputError(Exception):
    def __init__(self,
                 message="Input incorect\n format decriptare: decrypt output key input_recuperat.txt"):
        super().__init__(message)


def xorBin(poz, binar):
    binKey = format(ord(sys.argv[2][poz%len(sys.argv[2])]),"08b")
    pow = 1
    nr = 0
    for i in range(7,-1,-1):
        if ord(binKey[i])^ord(binar[i]) != 0:
            nr += pow
        pow <<= 1
    return chr(nr)


def decrypt():
    try:
        with open(sys.argv[1]) as f:
            text = f.read()
    except:
        print("Fisierul nu exista")
    txtDecriptat = []
    for i in range(0,len(text),8):
        txtDecriptat.append(xorBin(i//8, text[i:i+8]))

    with open(sys.argv[3],"w") as f:
        f.write("".join(txtDecriptat))


if __name__ == '__main__':

    n = len(sys.argv)

    if n != 4:
        raise InputError
        sys.exit()

    decrypt()


