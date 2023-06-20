# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
# nome deles e escrevendo o nome do escolhido.

import random

aluno01 = input('Digite o nome do primeiro aluno: ')
aluno02 = input('Digite o nome do segundo aluno: ')
aluno03 = input('Digite o nome do terceiro aluno: ')
aluno04 = input('Digite o nome do quarto aluno: ')

result = random.choice([aluno01, aluno02, aluno03, aluno04])

print('O aluno escolhido foi {}'.format(result))
