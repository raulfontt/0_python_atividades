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
