# Crie um programa pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.


km = float(input('Informe a quantidade de KM percorridos: '))
dias = int(input('Informe a quantidade de dias pelos quais o carro foi alugado: '))

print('O preço a pagar é de R${:.2f}!'.format((dias * 60) + (km * 0.15)))
