# logica E (and)
from operator import truediv

verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha
print(login)

if not login:
    print("loga certo ai cara...")
