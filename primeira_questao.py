# # Questão 1 
# # A exposição excessiva à radiação ultravioleta (UV) proveniente do sol é um dos principais fatores de risco para o
# # desenvolvimento de câncer de pele. Por isso, diversos aplicativos de clima e saúde pública divulgam
# # diariamente o índice UV, um indicador que mede a intensidade da radiação ultravioleta em um determinado
# # local e horário. Quanto maior o valor do índice UV, maior é o risco de danos à pele e aos olhos, sendo
# # recomendadas medidas de proteção como uso de protetor solar, chapéus e evitar exposição direta ao sol nos
# # horários mais críticos.
# # Um aplicativo de clima deseja informar aos usuários o nível de risco associado ao valor do índice UV observado
# # em determinado momento. Para isso, o sistema deve classificar o índice UV em quatro categorias de risco:
# # baixo, moderado, alto ou muito alto, de acordo com o valor do índice informado. A partir dessa classificação, o
# # aplicativo poderá exibir ao usuário uma indicação clara do nível de exposição ao qual ele está sujeito.
# # Escreva um programa em python que será utilizado pelo aplicativo. Ele deverá armazenar o valor do índice em
# # uma variável e classificar o risco.

valor_uv = int(input("Digite aqui o valor UV: "))
if valor_uv < 0:
    print("Inválido")
else:
    if valor_uv >= 20: 
        print("Muito alto!")
    elif valor_uv >= 10:
        print("Alto")
    elif valor_uv >= 5:
        print("Moderado")
    else:
        print("Baixo")

# # Questão 2
# # Faça um programa que leia um número inteiro e informe se ele é par ou ímpar.

valor = int(input("Digite aqui o valor de um número: "))
if valor % 2 == 0:
    print("É par!")
else:
    print("É impar!")

# # Questão 3 
# # Faça um programa que leia dois números inteiros e exiba o maior deles.
valor1 = int(input("Digite aqui o valor de um número: "))
valor2 = int(input("Digite aqui o segundo valor de um número: "))
if valor1 > valor2:
    print(valor1)
else:
    print(valor2)

# Questão 4 
# Faça um programa que leia três números inteiros e os exiba em ordem crescente.
valor1 = int(input("Digite aqui o valor de um número: "))
valor2 = int(input("Digite aqui o segundo valor de um número: "))
valor3 = int(input("Digite aqui o terceiro valor de um número: "))
if valor1 > valor2 and valor1 > valor3 and valor2 > valor3:
    print(valor1, valor2, valor3)
elif valor2 > valor1 and valor2 > valor3 and valor1 > valor3:
    print(valor2, valor1, valor3)
elif valor3 > valor1 and valor3 > valor2 and valor1 > valor2:
    print(valor3, valor2, valor1)
