#------------------------------------
print("Hello World") #CODE BY @evertin_bg
#------------------------------------

# Solicita os anos de experiência do profissinal
anos_experiencia = int(input("Digite quantos anos de experiência o profissoinal possui: "))
#------------------------------------

# Verificar a classificação do profssional com base nos anos de experiência
if anos_experiencia < 5:
    print("Profissional em início de carreira - Júnior")
elif anos_experiencia >= 5 and anos_experiencia < 10:
    print("Profisional Pleno")
elif anos_experiencia >= 10 and anos_experiencia < 15:
    print("Profissional Sênior")
else:
    print("Profisional Master")
#------------------------------------
