
"""Duelo entre Cavaleiros de Bronze e de Ouro."""

# Pergunta o cosmo dos dois cavaleiros
cosmo_bronze = int(input("Digite o cosmo do Cavaleiro de Bronze: "))
cosmo_ouro = int(input("Digite o cosmo do Cavaleiro de Ouro: "))

# Verifica se o herói está usando a armadura completa
armadura = input("O Cavaleiro de Bronze está com a armadura completa? (sim/nao): ")

# Aplica bônus ou penalidade no cosmo do herói
if armadura == "sim":
    cosmo_bronze += 20
    print("Armadura completa! O cosmo aumentou em 20 pontos.")
else:
    cosmo_bronze -= 10
    print("Armadura incompleta! O cosmo diminuiu em 10 pontos.")

# Compara os cosmos e define o resultado
if cosmo_bronze > cosmo_ouro:
    resultado = "VITÓRIA!"
elif cosmo_bronze == cosmo_ouro:
    resultado = "EMPATE!"
else:
    resultado = "DERROTA!"

# Mostra o resultado final
print(f"\nO cosmo final do Cavaleiro de Bronze é {cosmo_bronze}.")
print(f"Resultado do duelo: {resultado}")
