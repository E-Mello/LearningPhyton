# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte Inteira 6.

from math import trunc

num = float(input('Digite um número real: '))

print('O número {} tem a parte inteira {}'.format(num, trunc(num)))
