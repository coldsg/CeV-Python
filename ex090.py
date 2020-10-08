"""Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
 No final, mostre o conteúdo da estrutura na tela."""
aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['média'] = float(input(f'Média de {aluno["nome"]} '))
if aluno['média'] >= 7.0:
    aluno['situação'] = 'Aprovado'
elif 4.0 <= aluno['média'] < 7.0:
    aluno['situação'] = 'VS'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
