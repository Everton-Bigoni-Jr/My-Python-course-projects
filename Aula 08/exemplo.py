print("------------------------------------------")
print("    Hello World | 👑-JESUS is KING-👑") # CODE BY @evertin_bg
print("------------------------------------------")

print("")
print("")

# 1. Criando uma lista de frutas disponíveis
frutas_disponiveis = ["Banana" , "Maçã" , "Laranja"]
# ------------------------------------------


# 2. Criando uma tupla com informações sobre uma fruta
# (nome, preço, quantidade)
info_fruta = ("Banana" , 3.50 , 20)
# ------------------------------------------


# 3. Criando um conjunto de frutas fora de estoque
frutas_fora_de_estoque = {"Maçã" , "Kiwi"}
# ------------------------------------------


# 4. Criando um dicionário para associar frutas e preços e quantidades
estoque = {
    "Banana": {"preço": 3.50 , "quantidade": 20},
    "Laranja": {"preço": 3.75 , "quantidade": 15},
}
# ------------------------------------------


# Exibindo informações
print("Frutas disponíveis: " , frutas_disponiveis)
print("------------------------------------------")
print("Informações sobre a fruta: " , info_fruta)
print("------------------------------------------")
print("Frutas fora de estoque: " , frutas_fora_de_estoque) 
print("------------------------------------------")
print("Estoque atualizado: " , estoque)
# ------------------------------------------

print("")
print("==========================================")
print("")

# Exibindo preço e quantidade da Banana
print("Preço da Banana: " , estoque["Banana"]["preço"])
print("Quantidade de Banana: " , estoque["Banana"]["quantidade"])
# ------------------------------------------









