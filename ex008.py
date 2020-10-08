# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

metros = float(input('Digite a quantidade de metros -> '))

milimetros = metros * 1000
centimetros = metros * 100
decimetros = metros * 10
decametros = metros / 10
kilometro = metros / 1000

print(f'{metros} Metros é igual a {centimetros:.0f} centimetros \ne igual a {milimetros:.0f} milimetros')