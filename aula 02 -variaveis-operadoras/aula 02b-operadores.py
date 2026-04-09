from operator import truediv

num1 = 5
num2 = 5

print(type(num1), type(num2))

operacao = num1 + num2
print(operacao, type(operacao))

# operador de atribuiçao
num = 15
print() # pular uma linha
print(num)

num = num + 2
print(num)


num += 2
print(num)

# relacionais
print()
print(6 != 6)

idade = 20
print(idade == 20)

logado = True
print(logado, type(logado))


maior_idade = idade >= 18
print(maior_idade)

# strings
nome1 = "Marcos"
nome2 = "marcos"

print(nome1.upper() == nome2.upper())
