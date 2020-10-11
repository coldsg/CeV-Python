from random import randint
from time import sleep
"""
Faça um programa que tenha uma lista
chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista
e a segunda função vai mostrar a soma entre todos os valores pares sorteados
pela função anterior.
"""


números = list()


def sorteia():
    cont = 0
    while cont < 5:
        num = randint(0, 100)
        números.append(num)
        cont += 1
        sleep(1.5)
    print(f'Números sorteados {números}')


def somaPar():
    pares = 0
    for c in números:
        if c % 2 == 0:
            pares += c
        elif pares == 0:
            print(f'Não há valores pares na lista')
    print(f'Soma dos valores pares é igual a {pares}')


sorteia()
somaPar()
