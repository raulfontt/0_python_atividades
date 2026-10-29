
"""Simula o Exame Chunin do Time 7 de Konoha."""

# Registra os dados iniciais dos candidatos
naruto = "Naruto"
sakura = "Sakura"
sasuke = "Sasuke"

pontos_naruto = 10
pontos_sakura = 10
pontos_sasuke = 10

chakra_naruto = 100.5
chakra_sakura = 100.5
chakra_sasuke = 100.5

penalidade = 5

print("")
print("EXAME CHUNIN DO TIME 7")
print("Se os alunos forem pegos colando, perdem "
      + str(penalidade) + " pontos.")

# NARUTO
tecnica_clone = 13.7
clones_naruto = 2

chakra_naruto -= clones_naruto * tecnica_clone

print("")
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

# Todos descansam e recuperam chakra
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

# Mostra a nota individual de cada ninja
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

# Soma os pontos dos três ninjas
pontos_time = pontos_naruto + pontos_sakura + pontos_sasuke

print("")
print("RESULTADO FINAL DO TIME 7")
print("Pontuação total do time: " + str(pontos_time))

# Se a soma for par, o time tem sorte e passa
if pontos_time % 2 == 0:
    print("Sorte do time!")
    print("TIME APROVADO!")
else:
    print("Azar do time!")
    print("TIME REPROVADO!")
