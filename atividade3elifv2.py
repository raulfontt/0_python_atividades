idade = int(input("Digite sua idade: "))
ingresso = input("\nPossui ingresso?(sim/nao) ")
autorizacao = input("\nPossui autorizacao?(sim/nao) ")
lista_vip = input("\nPossui lista vip?(sim/nao) ")


if idade < 18 and (lista_vip == "sim" or ingresso == "sim") and autorizacao == "sim":
    print("\nEntrada de menor permitida devido a autorização dos pais e ingresso ou vip")
elif idade < 12:
    print("\nNão pode entrar de jeito nenhum.")
elif idade >= 18 and (ingresso == "sim" or lista_vip == "sim"):
    print("\nEntrada permitida!")
else:
    print("\nEntrada Negada!")

"""  Vamos criar um sistema de controle de entrada para um evento! As Regras são:
A entrada é permitida se a pessoa tem idade maior ou igual a 18 anos e tem ingresso.
Se a pessoa tem menos de 18 anos, só pode entrar com autorização dos pais e ingresso.
Pessoas com idade menor que 12 anos não podem entrar de jeito nenhum"""