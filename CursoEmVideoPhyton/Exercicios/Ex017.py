# Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import sqrt, pow

catOposto = float(input('Digite o comprimento do cateto oposto: '))
catAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
hip = (catOposto ** 2 + catAdjacente ** 2) ** (1/2)

print('O comprimento da hipotenusa é {:.2f}'.format(
    sqrt(pow(catOposto, 2) + pow(catAdjacente, 2))))

print('O comprimento da hipotenusa é {:.2f}'.format(hip))
