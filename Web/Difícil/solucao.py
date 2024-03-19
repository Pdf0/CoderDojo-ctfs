import requests

def verificar_subdiretorias(arquivo):
    with open(arquivo, 'r') as f:
        subdiretorias = f.readlines()
        subdiretorias = [subdiretoria.strip() for subdiretoria in subdiretorias]

        for subdiretoria in subdiretorias:
            url = f'http://di.uminho.pt/{subdiretoria}'
            resposta = requests.get(url)

            if resposta.status_code == 200:
                print(f"A subdiretoria /'{subdiretoria}' existe.")
                
if __name__ == "__main__":
    arquivo_subdiretorias = "/home/pdf/cybersecurity/wordlists/directory-list-2.3-medium.txt"
    verificar_subdiretorias(arquivo_subdiretorias)
