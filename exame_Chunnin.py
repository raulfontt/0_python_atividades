"""Simula o Exame Chunin de um ninja de Konoha."""
# Registra os dados iniciais do candidato
nome = "Naruto"
print("")
pontos = 10
chakra = 100.5
time = True
penalidade = 5
print("Exame iniciado. Se os alunos forem pegos colando, perdem " + str(penalidade) + " pontos.")

tecnica_clone = 13.7
clones = 3
chakra -= clones*tecnica_clone
print("Naruto usou " + str(clones) + " clones para tentar colar ficando com " + str(round(chakra,2)) + " de chakra.")

if clones == 3:
  print("Conseguiu colar, sem ser pego.")
else:
  pontos -= penalidade
  print("Naruto foi pego olhando a prova do lado. Perdeu "+ str(penalidade) + " pontos ficando com " + str(pontos))

resto = pontos % 2
if resto == 0:
  time = "Sorte"
else:
  time = "Azar"

print(str(time) + " do time!")

descanso = 10.3
chakra += descanso
print("Naruto descansou e recuperou "+ str(descanso)+ " de chakra ficando com " + str(round(chakra,2)) )

if pontos > 6:
  print("Naruto tirou nota boa.")
  if time == "Sorte":
    print("Time aprovado!")
  else:
    print("Time reprovado!")
else:
  print("Naruto tirou nota baixa")
  if time == "Sorte":
    print("Time aprovado!")
  else:
    print("Time reprovado!")

