print("------------------------------------------")
print("    Hello World | 👑-JESUS is KING-👑") # CODE BY @evertin_bg
print("------------------------------------------")

print("")

# Criando um dicinário
precos = {"banana": 3.50 , "maçã": 4.00 , "laranja": 2.75}

# Adicionando um novo par chave-valor
precos["abacaxi"] = 5.50
print(precos)

print("------------------------------------------")

# Removendo um item do dicionário
del precos["maçã"]
print(precos)

print("------------------------------------------")

# Modificandoo valor de uma chave existente
precos["banana"] = 2.90
print(precos)

print("------------------------------------------")

# Verificando se uma chave está no dicionário
print("abacaxi" in precos) # True
print("Melancia" in precos) # False

print("------------------------------------------")

# Escrevendo o valor de uma chave especifica
print(precos["abacaxi"])

