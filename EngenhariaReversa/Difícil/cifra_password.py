def encrypt_message(mensagem):
    mesangem_cifrada = ""

    mesangem_cifrada += mensagem[16]
    mesangem_cifrada += mensagem[5]
    mesangem_cifrada += mensagem[6]
    mesangem_cifrada += mensagem[10]
    mesangem_cifrada += mensagem[3]
    mesangem_cifrada += mensagem[1]
    mesangem_cifrada += mensagem[7]
    mesangem_cifrada += mensagem[14]
    mesangem_cifrada += mensagem[8]
    mesangem_cifrada += mensagem[13]
    mesangem_cifrada += mensagem[2]
    mesangem_cifrada += mensagem[15]
    mesangem_cifrada += mensagem[4]
    mesangem_cifrada += mensagem[12]
    mesangem_cifrada += mensagem[9]
    mesangem_cifrada += mensagem[0]
    mesangem_cifrada += mensagem[11]

    mesangem_cifrada = mesangem_cifrada[::-1]

    return mesangem_cifrada