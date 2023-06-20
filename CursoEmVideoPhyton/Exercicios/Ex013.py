# Crie um programa que leie o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário do funcionário: '))
print('O salário do funcionário com 15% de aumento é R${:.4f}'.format(
    salario * 1.15))
