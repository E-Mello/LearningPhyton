# Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

result = input('Digite algo: ')

print('Os tipos primitivos de {} são:'.format(result))
print('{} é um número? {}'.format(result, result.isnumeric()))
print('{} é alfabético? {}'.format(result, result.isalpha()))
print('{} é alfanumérico? {}'.format(result, result.isalnum()))
print('{} é decimal? {}'.format(result, result.isdecimal()))
print('{} é um dígito? {}'.format(result, result.isdigit()))
print('{} é um identificador? {}'.format(result, result.isidentifier()))
print('{} é imprimível? {}'.format(result, result.isprintable()))
print('{} é um espaço? {}'.format(result, result.isspace()))
print('{} é um título? {}'.format(result, result.istitle()))
print('{} é um caractere? {}'.format(result, result.isascii()))
print('{} é uma letra maiúscula? {}'.format(result, result.isupper()))
print('{} é uma letra minúscula? {}'.format(result, result.islower()))
print('O tipo primitivo de {} é {}'.format(result, type(result)))
