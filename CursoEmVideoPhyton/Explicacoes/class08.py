# Para efetuar uma importacao de um modulo, basta usar o comando import
# import math # importa todas as funcoes do modulo math
# from math import sqrt # importa apenas a funcao sqrt do modulo math

# import math
import random
from math import sqrt, ceil, floor
import emoji

num = int(input('Digite um número: '))
# raiz = math.sqrt(num)
raiz = sqrt(num)

print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
# print('A raiz de {} é igual a {:.2f}'.format(num, math.ceil(raiz)))
# print('A raiz de {} é igual a {:.2f}'.format(num, math.floor(raiz)))
print(emoji.emojize("Python is fun :sunglasses:", variant="emoji_type"))


num = random.randint(1, 10)
