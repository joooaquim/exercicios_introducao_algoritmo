valor_uv = int(input("Digite aqui o valor UV: "))
if valor_uv >= 20: 
    print("Muito alto!")
elif valor_uv >= 10:
    print("Alto")
elif valor_uv >= 5:
    print("Moderado")
else:
    print("Baixo")