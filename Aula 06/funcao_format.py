print("------------------------------------------")
print("Hello World | 👑-JESUS is KING-👑") # CODE BY @evertin_bg
print("------------------------------------------")


# Criando um array de tamanho 5

numeros = [0] * 5

# ------------------------------------------------

# Solicitando 5 inteiros ao usuário

for i in range(5):
    numeros[i] = int(input("Digite o {} número inteiro: " .format(i + 1)))

# ------------------------------------------------

print("------------------------------------------")
print("------------------------------------------")

# Imprimindo cada número com sua posição na lista

for i, numero in enumerate(numeros):
    print("O número {} está na posição {} da lista" .format(numero , i))


# ------------------------------------------------


print("------------------------------------------")
print("Sua lista está assim" , numeros)