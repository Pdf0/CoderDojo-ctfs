def decifrar_cifra_substituicao(texto_cifrado, alfabeto_minusculo, alfabeto_maiusculo):
    texto_decifrado = ""
    for letra in texto_cifrado:
        if letra.islower():
            if letra in alfabeto_minusculo:
                letra_decifrada = alfabeto_minusculo[letra]
                texto_decifrado += letra_decifrada
            else:
                texto_decifrado += letra
        else:
            if letra in alfabeto_maiusculo:
                letra_decifrada = alfabeto_maiusculo[letra]
                texto_decifrado += letra_decifrada
            else:
                texto_decifrado += letra
    return texto_decifrado

alfabeto_minusculo = {'f': 'a', 'j': 'b', 'h': 'c', 'y': 'd', 'd': 'e', 'l': 'f', 'b': 'g', 'n': 'h', 'p': 'i', 'c': 'j', 'e': 'k', 'w': 'l', 'i': 'm', 's': 'n', 'm': 'o', 'u': 'p', 'g': 'q', 'v': 'r', 'k': 's', 'z': 't', 'a': 'u', 'x': 'v', 't': 'w', 'r': 'x', 'q': 'y', 'o': 'z'}
alfabeto_maiusculo = {'F': 'A', 'J': 'B', 'H': 'C', 'Y': 'D', 'D': 'E', 'L': 'F', 'B': 'G', 'N': 'H', 'P': 'I', 'C': 'J', 'E': 'K', 'W': 'L', 'I': 'M', 'S': 'N', 'M': 'O', 'U': 'P', 'G': 'Q', 'V': 'R', 'K': 'S', 'Z': 'T', 'A': 'U', 'X': 'V', 'T': 'W', 'R': 'X', 'Q': 'Y', 'O': 'Z'}
texto_cifrado = "M HmydvYmcm Jvfbf"

texto_decifrado = decifrar_cifra_substituicao(texto_cifrado, alfabeto_minusculo, alfabeto_maiusculo)
print("Mensagem decifrada:", texto_decifrado)
