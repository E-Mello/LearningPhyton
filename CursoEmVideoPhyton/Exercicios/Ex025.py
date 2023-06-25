# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
# Caso nao tenha Silva no nome, o programa deve dizer que nao tem Silva no nome e mostrar o ultimo nome da pessoa.

nome = str(input('Digite seu nome completo: '))

print('Seu nome tem Silva? {}'.format('Silva' in nome))

print('Seu ultimo nome é: {}'.format(nome.split()[-1]))
