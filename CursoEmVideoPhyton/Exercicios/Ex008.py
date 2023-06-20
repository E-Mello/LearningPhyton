# Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

num = float(input('Digite um valor em metros: '))

print('O valor digitado foi {}m, que equivale a {}km, {}hm, {}dam, {}dm {}cm, {}mm'.format(
    num, (num / 1000), (num / 100), (num / 10), (num * 10), (num * 100), (num * 1000)))
