
"""Simula o Exame Chunin do Time 7 de Konoha."""

# Registra os dados iniciais dos candidatos
naruto = "Naruto"
sakura = "Sakura"
sasuke = "Sasuke"

# Cada ninja começa com 10 pontos
pontos_naruto = 10
pontos_sakura = 10
pontos_sasuke = 10

# Registra o chakra de cada ninja
chakra_naruto = 100.5
chakra_sakura = 100.5
chakra_sasuke = 100.5

penalidade = 5

print("\nEXAME CHUNIN DO TIME 7")
print("Se os alunos forem pegos colando, perdem "
      + str(penalidade) + " pontos.\n")


# NARUTO
tecnica_clone = 13.7
clones_naruto = 2

chakra_naruto -= clones_naruto * tecnica_clone

print(naruto + " usou " + str(clones_naruto)
      + " clones e ficou com "
      + str(round(chakra_naruto, 2)) + " de chakra.")

if clones_naruto == 3:
    print(naruto + " conseguiu colar sem ser pego.")
else:
    pontos_naruto -= penalidade
    print(naruto + " foi pego colando e perdeu "
          + str(penalidade) + " pontos.")

# SAKURA
tecnica_clone = 13.7
clones_sakura = 3

chakra_sakura -= clones_sakura * tecnica_clone

print("")
print(sakura + " usou " + str(clones_sakura)
      + " clones e ficou com "
      + str(round(chakra_sakura, 2)) + " de chakra.")

if clones_sakura == 3:
    print(sakura + " conseguiu colar sem ser pega.")
else:
    pontos_sakura -= penalidade
    print(sakura + " foi pega colando e perdeu "
          + str(penalidade) + " pontos.")

# SASUKE
tecnica_clone = 13.7
clones_sasuke = 4

chakra_sasuke -= clones_sasuke * tecnica_clone

print("")
print(sasuke + " usou " + str(clones_sasuke)
      + " clones e ficou com "
      + str(round(chakra_sasuke, 2)) + " de chakra.")

if clones_sasuke == 3:
    print(sasuke + " conseguiu colar sem ser pego.")
else:
    pontos_sasuke -= penalidade
    print(sasuke + " foi pego colando e perdeu "
          + str(penalidade) + " pontos.")

# Define a sorte de cada ninja usando o resto da divisão
if pontos_naruto % 2 == 0:
    time_naruto = "Sorte"
else:
    time_naruto = "Azar"

if pontos_sakura % 2 == 0:
    time_sakura = "Sorte"
else:
    time_sakura = "Azar"

if pontos_sasuke % 2 == 0:
    time_sasuke = "Sorte"
else:
    time_sasuke = "Azar"

# Cada ninja descansa e recupera chakra
descanso = 10.3

chakra_naruto += descanso
chakra_sakura += descanso
chakra_sasuke += descanso

print("")
print("O Time 7 descansou e recuperou chakra.")

print(naruto + " ficou com "
      + str(round(chakra_naruto, 2)) + " de chakra.")
print(sakura + " ficou com "
      + str(round(chakra_sakura, 2)) + " de chakra.")
print(sasuke + " ficou com "
      + str(round(chakra_sasuke, 2)) + " de chakra.")

# Avalia a nota de cada ninja
print("")
print("RESULTADO INDIVIDUAL")

if pontos_naruto > 6:
    print(naruto + " tirou nota boa: "
          + str(pontos_naruto) + " pontos.")
else:
    print(naruto + " tirou nota baixa: "
          + str(pontos_naruto) + " pontos.")

if pontos_sakura > 6:
    print(sakura + " tirou nota boa: "
          + str(pontos_sakura) + " pontos.")
else:
    print(sakura + " tirou nota baixa: "
          + str(pontos_sakura) + " pontos.")

if pontos_sasuke > 6:
    print(sasuke + " tirou nota boa: "
          + str(pontos_sasuke) + " pontos.")
else:
    print(sasuke + " tirou nota baixa: "
          + str(pontos_sasuke) + " pontos.")

# O time só passa se os três ninjas tiverem nota boa
print("")
print("RESULTADO FINAL DO TIME 7")

if (pontos_naruto > 6 and pontos_sakura > 6
        and pontos_sasuke > 6):
    print("Time aprovado!")
else:
    print("Time reprovado!")
