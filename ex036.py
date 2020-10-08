casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print(f'Para pagar uma casa de R${casa} em {anos} anos', end='')
print(f' a prestação será de R${prestação}')
print(f'COMPARANDO tem que pagar {prestação} e o mínimo é de {mínimo}')