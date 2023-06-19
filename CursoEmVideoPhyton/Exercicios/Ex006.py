# Crie um algortimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt


n1 = int(input('Digite um número: '))

print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(
    n1, n1 * 2, n1 * 3, sqrt(n1)))
