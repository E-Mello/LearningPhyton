# Operadores Aritméticos

n1 = int(5)
n2 = int(2)

# + Adição
result = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, result))
# - Subtração
result = n1 - n2
print('A subtração entre {} e {} vale {}'.format(n1, n2, result))
# * Multiplicação
result = n1 * n2
print('A multiplicação entre {} e {} vale {}'.format(n1, n2, result))
# / Divisão
result = n1 / n2
print('A divisão entre {} e {} vale {}'.format(n1, n2, result))
# ** Potência
result = n1 ** n2
print('A potência entre {} e {} vale {}'.format(n1, n2, result))
# // Divisão Inteira
result = n1 // n2
print('A divisão inteira entre {} e {} vale {}'.format(n1, n2, result))
# % Resto da Divisão
result = n1 % n2
print('O resto da divisão entre {} e {} vale {}'.format(n1, n2, result))


# Ordem de Precedência
# 1º ()
# 2º **
# 3º * / // %
# 4º + -

n3 = int(3)

result = n1 + n2 * n3
# 5 + 2 * 3 = 11
# (5 + 2) * 3 = 21

print('=' * 20)

nome = str(input('Qual é o seu nome? '))
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' >>> ') :.3f = 3 casas decimais, end=' >>> ' = não quebra linha
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira {} e potência {}'.format(di, e))
