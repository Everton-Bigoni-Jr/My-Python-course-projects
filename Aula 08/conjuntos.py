print("------------------------------------------")
print("   Hello World | 👑-JESUS is KING-👑") # CODE BY @evertin_bg
print("------------------------------------------")

print("")

# Criando um conjunto
frutas = {"banana" , "maçã" , "laranja"}

# Adicionando um item ao conjunto
frutas.add("abacaxi")
print(frutas)

print("------------------------------------------")

# Removendo um item do conjunto
frutas.remove("maçã")
print(frutas)

print("------------------------------------------")

# Tentando adicionar um item já existente (Não causa erro, mas o item não é duplicado)
frutas.add("banana")
print(frutas)

print("------------------------------------------")

# Verificando se um item está no conjunto
print("abacaxi" in frutas) # True
print("Melancia" in frutas) # False
