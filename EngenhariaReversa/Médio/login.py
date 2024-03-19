import base64
from cryptography.fernet import Fernet

# Código do programa, mas cifrado
texto_cifrado = b'gAAAAABl4dDK8puyQzWFvnvOaTyrcQhIIT76I-MMLUXLqqjKFgnE_nChNgqoXBKraXSkrYInNK-tgkN4_4JOiJRPU8t5Tq-LXasmSrpZTblsKlMOPPz88fG6W-YvszQS0kJMPBGH6oAiU_Vt_ogblFt9c07BoKjmsmrhWXg2-4skh3Fbsma9NGV6mRacW5HIzZzPHNjj7BjktHJK4AXC8KHfTduqVhTl8n__okNAbob7gKITrR0qmeMikiYmZeaRu9QSYM-bLJfFpq0btjbot6c_rLATWxZhrA=='

chave = 'coderdojobragacoderdojobragacode'
chave_base64 = base64.b64encode(chave.encode())

# Texto é decifrado
f = Fernet(chave_base64) 
codigo = f.decrypt(texto_cifrado)

# Código é executado
exec(codigo.decode())