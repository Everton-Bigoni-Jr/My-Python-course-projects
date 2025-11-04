print("------------------------------------------")
print("Hello World | 👑-JESUS is KING-👑") # CODE BY @evertin_bg
print("------------------------------------------")

usuarios = ["Luiz" , "Felipe" , "Tiago" , "Ricardo"]

print("Escolha uma opção:")
print("1. Opção 1")
print("2. R - Leitura de usuários")
print("3. Opção 3")
print("4. Opção 4")

opcao = int(input("Digite o número da opção desejada: "))

while opcao > 0 and opcao < 5: 
    if opcao == 1:
        print("Você escolheu a opção 1.")

    elif opcao == 2:
        print("Você escolheu a opção Leitura")
        print("-----------------------------")
        for usuario in usuarios:
            print(usuario)
        print("-----------------------------")


    elif opcao == 3:
        print("Você escolheu a opção 3.")

    elif opcao == 4:
        print("Você escolheu a opção 4.")


    opcao = int(input("Digite o número da opção desejada: "))

print("Opção inválida. Tente novamente.")
print("Encerrando o sistema")