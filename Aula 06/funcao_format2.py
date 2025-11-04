print("------------------------------------------")
print("Hello World | 👑-JESUS is KING-👑") # CODE BY @evertin_bg
print("------------------------------------------")

# Criando arrays

produtos = ["Pc Gamer" , "Xbox Series" , "Playstation 5" , "Nintendo Switch" , "Notebook Gamer" , "Teste"]
valores = [8000 , 3000 , 4500 , 2500 , 6000 , 7000]

# ------------------------------------------------

# Percorrendo duas listas ao mesmo tempo
# zip()

for produto, valor in zip(produtos, valores):
    print("O valor de {} é R$ {}" .format(produto , valor))
    print("------------------------------------------")

# ------------------------------------------------

print("=========================================")
print("=========================================")

# range()

for i in range(len(produtos)):
    print("O valor de {} é R$ {}" .format(produtos[i] , valores[i]))
    print("------------------------------------------")

# ------------------------------------------------