# Crie um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan

angulo = float(input('Digite o valor do ângulo: '))

print('O seno do ângulo {} é {:.2f}'.format(angulo, sin(angulo)))
print('O cosseno do ângulo {} é {:.2f}'.format(angulo, cos(angulo)))
print('A tangente do ângulo {} é {:.2f}'.format(angulo, tan(angulo)))
