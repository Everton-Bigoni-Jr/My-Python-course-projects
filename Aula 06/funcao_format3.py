print("------------------------------------------")
print("Hello World | 👑-JESUS is KING-👑") # CODE BY @evertin_bg
print("------------------------------------------")

# Arrays
produtos = []
valores = []
# ------------------------------------------


for i in range(3):
    produto = input("Digite o nome do produto {}: " .format(i + 1))
    print("------------------------------------------")
    valor = float(input("Digite o valor do produto {}: " .format(i + 1)))
    print("------------------------------------------")

    produtos.append(produto)
    valores.append(valor)


for produto, valor in zip(produtos , valores):
    print("O valor de {} é R$ {}" .format(produto , valor))


