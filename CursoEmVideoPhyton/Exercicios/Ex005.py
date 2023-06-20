# Crie um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('Digite um número inteiro: '))

print('O número digitado foi {}, seu antecessor é {} e seu sucessor é {}'.format(
    n1, (n1 - 1), (n1 + 1)))
