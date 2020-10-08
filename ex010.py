# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar

real = float(input('Digite o valor na carteira ? R$ '))
dolar = real / 3.78
iene = real / 0.035
euro = real / 4.21

print(f'Com R$ {real:.2f} você pode comprar US$ {dolar:.2f}, {iene:.2f} Iene(s) e {euro:.2f} Euro(s)'.format(real, dolar, iene, euro))