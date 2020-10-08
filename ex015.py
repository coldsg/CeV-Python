#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Digite a quantidade de dias -> '))
KM = float(input('Digite a quantidade de Km percorridos -> '))

preço = (60 * dias) + (0.15 * KM)

print(f'O preço foi R$ {preço} ')
