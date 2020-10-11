from time import sleep
"""
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""


def maior(* num):
    m = 0
    if num > m:
        m = num
        print('-=' * 20)
    print('Analisando os valores passados...')
    print(num, end='')


# Função principal (main)
numero = int(input('Digite os valor numérico '))
maior(2, 9, 4, 5, 7, 1)
