# Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex: Digite um numero: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

num = int(input('Digite um numero de 0 a 9999: '))

print('Digito da unidade: {}'.format(num // 1 % 10))

print('Digito da dezena: {}'.format(num // 10 % 10))

print('Digito da centena: {}'.format(num // 100 % 10))

print('Digito do milhar: {}'.format(num // 1000 % 10))
