import cifraCesar

texto_cifrado = "B KbmeeLbso Oznpa"
chave = "NINJA"
resultado = ""
i = 0
for letra in texto_cifrado:
    if letra == " ":
        resultado += " "
    else:
        resultado += cifraCesar.decifrar(letra, chave[i % len(chave)])
        i +=1

print(resultado)