import subprocess

ficheiro = open("passwords.txt").readlines()

for password in ficheiro:
    password = password.rstrip()
    resultado = subprocess.run(["./login",password], capture_output=True, text=True)
    if resultado.stdout != "":
        print("Password: " + password + " | " + resultado.stdout)
    

