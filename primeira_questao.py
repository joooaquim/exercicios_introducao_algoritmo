# Questão 1 
# A exposição excessiva à radiação ultravioleta (UV) proveniente do sol é um dos principais fatores de risco para o
# desenvolvimento de câncer de pele. Por isso, diversos aplicativos de clima e saúde pública divulgam
# diariamente o índice UV, um indicador que mede a intensidade da radiação ultravioleta em um determinado
# local e horário. Quanto maior o valor do índice UV, maior é o risco de danos à pele e aos olhos, sendo
# recomendadas medidas de proteção como uso de protetor solar, chapéus e evitar exposição direta ao sol nos
# horários mais críticos.
# Um aplicativo de clima deseja informar aos usuários o nível de risco associado ao valor do índice UV observado
# em determinado momento. Para isso, o sistema deve classificar o índice UV em quatro categorias de risco:
# baixo, moderado, alto ou muito alto, de acordo com o valor do índice informado. A partir dessa classificação, o
# aplicativo poderá exibir ao usuário uma indicação clara do nível de exposição ao qual ele está sujeito.
# Escreva um programa em python que será utilizado pelo aplicativo. Ele deverá armazenar o valor do índice em
# uma variável e classificar o risco.

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

