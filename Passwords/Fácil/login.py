###### Esta função não te vai ajudar a resolver o desafio #####################
def str_xor(segredo, chave):
    nova_chave = chave
    i = 0
    while len(nova_chave) < len(segredo):
        nova_chave = nova_chave + chave[i]
        i = (i + 1) % len(chave)        
    return "".join([chr(ord(segredo_c) ^ ord(nova_chave_c)) for (segredo_c,nova_chave_c) in zip(segredo,nova_chave)])
###############################################################################

segredo_enc = open('segredo.txt.enc', 'rb').read()

def login():
    password = input("Por favor coloca a password correta: ")
    if( password == chr(100) + chr(111) + chr(106) + chr(111) + chr(115) + chr(101) + chr(99) + chr(114) + chr(101) + chr(116) + chr(111)):
        print("Bem vindo ninja... Aqui está o segredo:", end=" ")
        segredo = str_xor(segredo_enc.decode(), password)
        print(segredo)
        return
    print("A password está incorreta. Tenta novamente.")

login()