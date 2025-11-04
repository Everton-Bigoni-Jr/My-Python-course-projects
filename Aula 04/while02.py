print("-------------------------------------")
print("Hello World")    #CODE BY @evertin)bg
print("-------------------------------------")

# Este código solicita ao usuário uma resposta e continua executando
# ---------------------------------------
# Enquanto a resposta for "sim"


resposta =  str(input("Deseja continuar? (digite 'sim' para continuar ou 'não' para parar): ")).lower()

while resposta == "sim": 
    print("Você escolheu continuar")
    str(input("Deseja continuar? (digite 'sim' para continuar ou 'não' para parar): ")).lower()
else:
    resposta == "não"
    print("Você escolheu parar")
