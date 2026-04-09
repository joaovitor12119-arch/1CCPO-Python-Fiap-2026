# 0 --> sair do program
# 1 --> entrar no pragrama
# ----> erro!!
escolha_usuario = 0

match escolha_usuario:
    case 0:
        print("sair do programa")
    case 1:
        print("Entrar no programa")
    case _:
        print("Erro!!")