# Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

num = float(input('Digite um valor em metros: '))

print('O valor digitado foi {}m, que equivale a {}cm e {}mm'.format(
    num, num * 100, num * 1000))
