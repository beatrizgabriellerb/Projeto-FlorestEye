import string

# C(x) == (5x + 8) % 26
# D(x) == 21 * (x - 8) % 26

alfabeto = string.ascii_uppercase

def criptografar(texto):
    return "".join(alfabeto[(5 * alfabeto.index(c) + 8) % 26] if c in alfabeto else c for c in texto.upper())

def descriptografar(texto):
    return "".join(alfabeto[(21 * (alfabeto.index(c) - 8)) % 26] if c in alfabeto else c for c in texto.upper())

if __name__ == '__main__':
    mensagem = "OLA MUNDO1"
    cifra = criptografar(mensagem)

    print("Criptografada:", cifra)
    print("Original:", descriptografar(cifra))

