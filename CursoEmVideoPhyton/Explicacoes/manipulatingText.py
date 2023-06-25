# Curso em video Python

frase = 'Curso em Video Python'
frase2 = '   Aprenda Python  '

# Fatiamento

# frase[9] = V
print(frase[9])

# frase[9:13] = Vide
print(frase[9:13])

# frase[9:21] = Video Python
print(frase[9:21])

# frase[9:21:2] = VdoPto
print(frase[9:21:2])

# frase[:5] = Curso
print(frase[:5])

# frase[15:] = Python
print(frase[15:])

# frase[9::3] = VePh
print(frase[9::3])


# Analise

# len(frase) = 21
print(len(frase))

# frase.count('o') = 3
print(frase.count('o'))

# frase.count('o', 0, 13) = 1
print(frase.count('o', 0, 13))

# frase.find('deo') = 11
# ele vai procurar a string 'deo' e vai retornar a posição que ela começa
print(frase.find('deo'))

# frase.find('Android') = -1
# se ele não encontrar a string ele retorna -1
print(frase.find('Android'))


# Operacoes

# 'Curso' in frase = True
# se ele encontrar a string ele retorna True
print('Curso' in frase)


# Transformacao

# frase.replace('Python', 'Android') = Curso em Video Android
# ele vai substituir a string 'Python' por 'Android'
print(frase.replace('Python', 'Android'))

# frase.upper() = CURSO EM VIDEO PYTHON
# ele vai deixar todas as letras maiusculas
print(frase.upper())

# frase.lower() = curso em video python
# ele vai deixar todas as letras minusculas
print(frase.lower())

# frase.capitalize() = Curso em video python
# ele vai deixar a primeira letra maiuscula e o resto minuscula
print(frase.capitalize())

# frase.title() = Curso Em Video Python
# ele vai deixar a primeira letra de cada palavra maiuscula e o resto minuscula
print(frase.title())

# frase2.strip() = Aprenda Python
# ele vai remover os espaços inuteis no inicio e no fim da string
print(frase2.strip())

# frase2.rstrip() =    Aprenda Python
# ele vai remover os espaços inuteis a partir da direita
print(frase2.rstrip())

# frase2.lstrip() = Aprenda Python
# ele vai remover os espaços inuteis a partir da esquerda
print(frase2.lstrip())


# Divisao

# frase.split() = ['Curso', 'em', 'Video', 'Python']
# ele vai dividir a string em uma lista
print(frase.split())


# Juncao

# '-'.join(frase) = C-u-r-s-o- -e-m- -V-i-d-e-o- -P-y-t-h-o-n
# ele vai juntar a string com o caractere que você escolher
print('-'.join(frase))


print("""Caros amigos, o desenvolvimento contínuo de distintas formas de atuação cumpre um papel essencial na formulação
dos procedimentos normalmente adotados. Por outro lado, o aumento do diálogo entre os diferentes setores produtivos talvez
venha a ressaltar a relatividade do sistema de participação geral. Desta maneira, a contínua expansão de nossa atividade
estimula a padronização do levantamento das variáveis envolvidas. Assim mesmo, a estrutura atual da organização auxilia
a preparação e a composição dos paradigmas corporativos.
""")
