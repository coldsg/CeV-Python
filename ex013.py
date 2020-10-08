# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento.

salário = float(input('Digite o salário R$ '))

novo = salário + (salário * 0.15)

print(f'O salário de R$ {salário:.2f} com 15% de aumento é R$ {novo:.2f}')