# Crie um programa que leia o nome completo de uma pessoa e mostre:
# Ela começa com 'Santo'?
# Qual é o primeiro nome dela?

nome = str(input('Digite seu nome completo: '))

print('Seu nome tem Santo? {}'.format('Santo' in nome))

print('Seu primeiro nome é: {}'.format(nome.split()[0]))
