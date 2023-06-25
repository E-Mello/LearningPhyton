# Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.

# Ex: Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza

nome = str(input('Digite seu nome completo: '))

print('Seu primeiro nome é: {}'.format(nome.split()[0]))

print('Seu ultimo nome é: {}'.format(nome.split()[-1]))
