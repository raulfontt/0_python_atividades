"""Calcula a média de três provas de um aluno."""

# Recebe as três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Verifica a situação do aluno
if media == 10:
    print("Nota Perfeita! O aluno tirou 10 nas três provas!")
elif media < 5:
    print("Reprovado! Média: " + str(round(media, 2)))
else:
    print("Aprovado! Média: " + str(round(media, 2)))

"""A (9 a 10)
B (8 a 8.9)
C (7 a 7.9)
D (6 a 6.9)
F (Menor que 6)"""

if media == 10:
    print("Tirou nota A. Nota Perfeita")
elif media >= 9:
    print("Tirou nota A.")
elif media >= 8:
    print("Tirou nota B.")
elif media >= 7:
    print("Tirou nota C.")
elif media >= 6:
    print("Tirou nota D.")
else:
    print("Tirou nota F.")


