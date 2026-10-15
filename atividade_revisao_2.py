idade = 31
texto = "minha idade "
print(texto + str(idade))

altura = "1.75"
idade += float(altura)

print("E minha altura " + altura + " somada a minha idade resulta em " + str(idade))

altura_correta = altura == "1.75"
idade_correta = idade == 31


"""
Atividade de Revisão:

Podem consultar o codecademy para tirar dúvidas. 

CodeCademy Python:
7) annual_rainfall += july_rainfall
8) #Comentario
9)  total_cost = cucumbers * price_per_cucumber (contas com variáveis)
10) quotient1 = float(7)/2 ou quotient1 = 7./2
11) """
	Strings e Comentarios
	De Multiplas Linhas
      """
12) Boolean = True ou False
13) str(idade) e int(floarNumber)

Escreveremos o código da Atividade no workspacde do codecademy e no fim salvaremos a resposta no google docs.
Vamos dividir cada atividade em partes para facilitar a programação delas. Iremos escrever um programa só com todos passos para resolver as questões a seguir:
Parte 1 =
Declare uma variável int que contém a sua idade. 
Declare uma variável string que contem o texto  "minha idade ".
Faça um print que contém as duas variáveis, usando o que aprendemos para não dar erro.
Parte 2 = 
Continuando o código anterior, declare uma variável string com sua altura (contendo 2 casas decimais depois do ponto flutuante).
Incremente a variável que continha sua idade usando essa nova variável da altura (Aplique o que aprendemos para incrementar escrevendo o nome de cada variável só uma vez).
Faça um print com "e minha altura 1.84 somada a minha idade resulta em 30.84" trocando os meus números pelos seus números usando as suas variáveis ( e usando o que aprendemos para não dar erro).
Parte 3 = 
Crie uma variável booleana informando se a variável que contém a sua ALTURA ainda está contendo a sua verdadeira altura depois de executar o programa.
Crie uma variável booleana informando se a variável que contém a sua IDADE ainda está contendo a sua verdadeira idade depois de executar o programa.
Faça um print informando se a sua altura e idade estão certas. Use concatenação, espaço entre as palavras e o que for preciso para não dar erro.
Comente o seu código para aparecer só uma mensagem na tela.

"""



print("Minha altura está correta? " + str(altura_correta) + " Minha idade está correta? " + str(idade_correta))
