#Descreva o programa
"""Programa para simular a busca por esferas do dragão."""

nome = input("Digite o nome do guerreiro: ")
esferas_encontradas = int(input("Quantas esferas você já encontrou? "))
ki = float(input("Quanto ki você tem? "))
radar = input("Você está com o Radar do Dragão? (sim/nao): ")  

#Simulação da busca por mais esferas
esferas_faltantes = 7 - esferas_encontradas 

# Cálculo do gasto de ki
# Utilizei o conceito da Soma na matemática de números em sequência (n x (n + 1))/2 
# Multiplico por 1000 pois é uma sequência: a 1a custa 1000, a 2a custa 2000 e a 3a custa 3000
gasto_ki = (esferas_faltantes * (esferas_faltantes + 1)) / 2 * 1000
print(f"Você terá {gasto_ki} de Ki gasto para encontrar as {esferas_faltantes} esferas faltantes")

#Terá redução?
if radar == "sim":
    gasto_ki = gasto_ki/2
    ki = ki - gasto_ki
    print(f"Você tem o radar seu gasto será de {gasto_ki} e seu Ki final ficou: {ki}")
else:
    ki = ki - gasto_ki
    print(f"Você não tem o radar e seu ki final ficou: {ki}")

if gasto_ki > ki:
    print("Você não tem ki suficiente")
else:
    print("Você tem ki suficiente")

#Quantas esferas ele possui agora?
if esferas_encontradas == 7:
    print("Você pode invocar shelong.")
elif esferas_encontradas < 7:
    print("A busca deve continuar.")




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