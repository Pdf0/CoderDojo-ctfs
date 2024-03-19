import subprocess

def adivinha_password():
    with open('passwords.txt', 'r') as f:
        for linha in f:
            password = linha.strip()
            resultado = subprocess.run(["./login", password], capture_output=True, text=True)
            if resultado.stdout != "":
                print(f"Senha encontrada: {password}, {resultado.stdout.strip()}")
adivinha_password()