import sys

class InputError(Exception):
    def __init__(self,
                 message="Input incorect\nformat criptare: encrypt key input.txt output"):
        super().__init__(message)


def xorLista(lista):
    criptatBin = ""
    for index in range(len(lista)):
        criptatBin += format(ord(lista[index])^ord(sys.argv[1][index % (len(sys.argv[1]))]), "08b")
    return criptatBin


def encrypt():
    text = ""
    try:
        with open(sys.argv[2]) as f:
            text = f.read()
    except:
        print("Fisierul nu exista")
    caractere = [i for i in text]
    listaCriptata = xorLista(caractere)
    with open(sys.argv[3],"w") as f:
        f.write("".join(listaCriptata))


if __name__ == '__main__':

    n = len(sys.argv)

    if n != 4:
        raise InputError
        sys.exit()

    encrypt()
