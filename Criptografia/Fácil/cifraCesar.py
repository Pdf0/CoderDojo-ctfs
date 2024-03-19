import string

def decifrar(texto_cifrado, chave):
    deslocamento = ord(chave) - ord('A')
    resultado = ""
    for letra in texto_cifrado:

            if letra in string.ascii_lowercase:
                letra = string.ascii_lowercase[(string.ascii_lowercase.find(letra) - deslocamento) % 26]

            elif letra in string.ascii_uppercase:
                letra = string.ascii_uppercase[(string.ascii_uppercase.find(letra) - deslocamento) % 26]

            resultado +=letra
    return resultado

texto_cifrado = "R FrghuGrmr Eudjd"
chave = "D"
texto_decifrado = decifrar(texto_cifrado, chave)
print("Mensagem decifrada:", texto_decifrado)
