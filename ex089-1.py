"""Exercício Python 089:
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
 No final, mostre um boletim contendo a média de cada um e permita que
 o usuário possa mostrar as notas de cada aluno individualmente."""
lista = list()
alunos = list()
resp = ''
nome = ''
nota1 = nota2 = media = 0.0
n = 0
while True:
    nome = str(input(f'Digite o nome do aluno nº {n + 1}: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    lista.append(nome)
    lista.append(nota1)
    lista.append(nota2)
    lista.append(media)
    alunos.append(lista[:])
    lista.clear()
    n += 1
    resp = input('Deseja adicionar um outra aluno? [S/N]')
    if resp in 'Nn':
        break
print('=-' * 20)
print('BOLETIM ESCOLAR'.center(20))
print('=-' * 20)
for cont, aluno in enumerate(alunos, 0):
    print(f'[Aluno nº: {cont + 1} |Nome: {aluno[0]} |Média: {aluno[2]}]')

