# Crie um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota01 = float(input('Digite a primeira nota: '))
nota02 = float(input('Digite a segunda nota: '))
media = (nota01 + nota02) / 2

print('A média entre {:.2f} e {:.2f} é {:.2f}'.format(nota01, nota02, media))
