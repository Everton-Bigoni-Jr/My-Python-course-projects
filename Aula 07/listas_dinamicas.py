print("------------------------------------------")
print("   Hello World | 👑-JESUS is KING-👑") # CODE BY @evertin_bg
print("------------------------------------------")

lista_de_carros = []

print("==========================================")

# Inserindo a quantidade de carros que o usuário deseja adicionar
quantidade = int(input("Quantos carros você deseja adicionar à lista? "))
# -------------------------------------------------

print("==========================================")

# Adiciona carros à lista conforme a quantidade especificada
for i in range(1, quantidade + 1):
    carro = input(f"Digite o nome do carro {i}: ")
    lista_de_carros.append(carro)

    print("------------------------------------------")
# -------------------------------------------------

# Irforma a ordem da lista de carros
for lista, i in enumerate(lista_de_carros, start=1):
    print(lista, "Carro:" , i)
# -------------------------------------------------

# Informa a lista de carros criada
print("------------------------------------------")
print("Lista criada" , lista_de_carros)
print("------------------------------------------")
# -------------------------------------------------

# Cria um loop para exibir a posição e o carro na lista
for index, carro in enumerate(lista_de_carros, start=1):
    print(f"Na posição {index} está o carro: {carro}")
# -------------------------------------------------

# Solicita o índice para excluir
indice_exclusao = int(input(f"Digite o índice de 0 a {len(lista_de_carros) -1} para excluir um carro: "))
# -------------------------------------------------

# Verifica se o índice está dentro do intervalo válido

if indice_exclusao <= len(lista_de_carros):
    carro_removido = lista_de_carros.pop(indice_exclusao)
    print(f"Carro {carro_removido} foi removido da lista" )

else:
    print("Índice inválido :/")

# -------------------------------------------------
