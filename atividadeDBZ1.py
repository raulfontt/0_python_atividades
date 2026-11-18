#Descreva o programa
"""Programa para simular a busca por esferas do dragão."""

nome = input("Digite o nome do guerreiro: ")
esferas_encontradas = int(input("Quantas esferas você já encontrou? "))
ki = float(input("Quanto ki você tem? "))
radar = input("Você está com o Radar do Dragão? (sim/nao): ")  

#Simulação da busca por mais esferas
esferas_faltantes = 7 - esferas_encontradas 

#Cálculo do gasto de ki
gasto_ki = sum((i + 1) * 1000 for i in range(esferas_faltantes))    

#Redução do gasto de ki se tiver o Radar do Dragão
if radar.lower() == "sim":
    gasto_ki /= 2

#Atualização do ki restante
ki_restante = ki - gasto_ki

#Decisão do destino da busca
if esferas_encontradas + esferas_faltantes == 7:
    print("\nShenlong é invocado!") 

elif esferas_encontradas + esferas_faltantes >= 4:
    print("\nA busca continua!")    

else:
    print("\nO guerreiro perdeu as esferas no meio do caminho, precisa recomeçar.")

#Verificação do ki restante
if ki_restante > 0:
    print("\nO guerreiro ainda tem energia.")
else:
    print("\nO guerreiro ficou exausto.")

#Relatório final
print(f"\nRelatório Final:\nGuerreiro: {nome}\nTotal de esferas: {esferas_encontradas + esferas_faltantes}\nKi restante: {ki_restante:.2f}")



"""Escreva um programa Python que faça o seguinte:

- Apresente o programa. No início do arquivo, descreva em poucas linhas o que ele faz.
- Pergunte os dados do guerreiro. Peça ao usuário o nome do guerreiro, quantas esferas ele já encontrou (um número inteiro) e quanto ki ele tem (um número com casa decimal).
- Pergunte se o guerreiro está com o Radar do Dragão.
- Simule a busca por mais esferas: Faça um cálculo de que para cada esfera nova que ele precisa capturar, ele vai ter que gastar mais KI (EX: já tem 4 e precisa de mais 3: a 1a custa 1000, a 2a custa 2000 e a 3a custa 3000 ) (Se ficar dificil demais, pode só multiplicar a quantidade de esferas faltantes por um valor fixo)
- Redução do gasto de ki: use uma divisão para reduzir esse gasto pela metade se o usuário tiver o Radar do Dragão.
- Decida o destino da busca. Compare a quantidade final de esferas e mostre uma mensagem diferente para cada situação:
- todas as 7 esferas reunidas: Shenlong é invocado;
- menos de 7 esferas, mas pelo menos 4: a busca continua;
- menos de 4 esferas: o guerreiro perdeu as esferas no meio do caminho, precisa recomeçar.
- Verifique o ki restante. Se o ki restante for diferente de zero, mostre que o guerreiro ainda tem energia. Se for igual a zero, mostre que ele ficou exausto.
- Mostre o relatório final. Exiba uma frase formatada com o nome do guerreiro, o total de esferas e o ki restante."""