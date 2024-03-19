import string

def decifrar(texto_cifrado, chave):
    shift = ord(chave) - ord('A')
    resultado = ""
    for letra in texto_cifrado:

            if letra in string.ascii_lowercase:
                letra = string.ascii_lowercase[(string.ascii_lowercase.find(letra) - shift) % 26]

            elif letra in string.ascii_uppercase:
                letra = string.ascii_uppercase[(string.ascii_uppercase.find(letra) - shift) % 26]

            resultado +=letra
    return resultado
