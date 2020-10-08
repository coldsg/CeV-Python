"""Crie um programa que vai ler vários números e colar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e
os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo
das três listas geradas."""
lista = []
pares = []
impares = []
valor = 0
while True:
    valor = int(input('Digite um valor númerico: '))
    lista.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)
    resp = str(input('Deseja continuar digitando [S/N]: '))
    if resp in 'Nn':
        break
print('-=' * 20)
print(f'Valores da lista total {lista}')
print(f'Valores da lista dos pares {pares}')
print(f'Valores da lista ímpares {impares}')
