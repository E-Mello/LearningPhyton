# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle, sample

aluno01 = input('Digite o nome do primeiro aluno: ')
aluno02 = input('Digite o nome do segundo aluno: ')
aluno03 = input('Digite o nome do terceiro aluno: ')
aluno04 = str(input('Digite o nome do quarto aluno: '))
result = sample([aluno01, aluno02, aluno03, aluno04], k=4)

lista = [aluno01, aluno02, aluno03, aluno04]
print('A ordem de apresentação será: {}'.format(shuffle(lista)))

print('A ordem de apresentação será: {}'.format(result))
