lista_frutas = ["laranja","Uva", "Melão"]

# lista_fruta[0] = "laranja"
# lista_fruta[1] = "uva"
# lista_fruta[2] = "melão"

print(lista_frutas[1])

lista_frutas.append("maça")
print(lista_frutas)
# lista_frutas[3] = "maça"

for i in range(len(lista_frutas)):
    print(lista_frutas[i])

    print()

    for fruta in lista_frutas:
        print(fruta)


