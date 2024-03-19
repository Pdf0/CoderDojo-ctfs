segredo = "D6DDõ6D 56 D6>AC6"

def retorna_segredo(segredo):
    x = []
    for i in range(len(segredo)):
        j = ord(segredo[i])
        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(segredo[i])
    segredo = ''.join(x)
    print(segredo)

def escolhe_maior():
    numero1 = input("Qual o primeiro número? ")
    numero2 = input("Qual o segundo número? ")
    maior = numero1

    if numero1 > numero2:
        maior = numero1
    elif numero1 < numero2:
        maior = numero2

    print( "O maior número é: " + str(maior) )

escolhe_maior()
