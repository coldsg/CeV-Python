"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
 em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""

pessoa = dict()
pessoas = list()
mulheres = list()
superiorm = list()
op = 0
tot = 0
media = 0.0
while True:
    pessoa['nome'] = str(input('Digite o nome: '))
    pessoa['sexo'] = str(input('Digite o sexo [M/F]: '))
    pessoa['idade'] = int(input('Digite a idade: '))
    pessoas.append(pessoa)
    tot = tot + 1
    media = media + (pessoa['idade'] / tot)
    if pessoa['idade'] > media:
        superiorm.append(pessoa)
    if pessoa['sexo'] in 'Ff':
        mulheres.append(pessoa)
    input()
    op = input('Deseja adicionar outra pessoa ? \n1 - SIM \n2 - NÃO\n ')
    if op == 2:
        break
print(f'Foram cadastradas {tot} pessoas ')
print(f'A média da idade é {media}')
print(f'A lista das mulheres: ')
for c, n in mulheres:
    print(f'A {c}° mulher se chama: {n[0]} e tem {n[1]} anos')
print(f'A lista de pessoas com idade acima da média: ')
for c, i in superiorm:
    print(f' Sr(a) {i[0]} está com idade acima da média ')
