# Crie um programa que converta uma temperatura digitada em ºC e converta para ºF.

temp = float(input('Informe a temperatura em ºC: '))

print('A temperatura de {}ºC corresponde a {}ºF!'.format(temp, ((temp * 9/5) + 32)))
