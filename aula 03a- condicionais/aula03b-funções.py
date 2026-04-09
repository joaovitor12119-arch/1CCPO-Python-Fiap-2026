def print_lyrics():
    print("i ain't gonna live forever")
    print("i just want to live while i'm alive")

print_lyrics()

def boas_vindas(nome):
    print(f"Ola, {nome}! Seja bem-vindo!!")

nome_digitado = input("Digite o seu nome :")
boas_vindas(nome_digitado)

#funcao de retorno e com parametro
def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

resultado_soma = soma(2,10)


