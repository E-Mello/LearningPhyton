n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
# print(type(n1))

# print('A soma entre', n1, 'e', n2, 'vale', n1 + n2)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))


teste = str(input('Digite um valor: '))
print(type(teste))
print(teste.isnumeric())
