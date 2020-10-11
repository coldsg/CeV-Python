"""
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
def contador(inicio, fim, passo):
    cont = 0
    if inicio > fim:
        print(f'Contagem de {inicio} a {fim} de {passo} em {passo}')
        print('-' * 30)
        for cont in range(inicio, fim + 1, passo):
            print(f' {cont} ', end='')
        print()
        print('-' * 30)
    else:
        print(f'Contagem de {inicio} a {fim} de {passo} em {passo}')
        print('-' * 30)
        for cont in range(fim, inicio + 1, passo):
            print(f' {cont} ', end='')
        print()
        print('-' * 30)

# main
inicio = fim = passo = 0
print('Contador personalizado ')
print('Digite a opção ')
print('A - De 1 até 10, de 1 em 1')
print('B - De 10 até 0, de 2 em 2')
print('C - Personalizado')
op = str(input('Digite a opção desejada: ')).upper()
if op == 'A':
    contador(inicio=1, fim=10, passo=1)
elif op == 'B':
    contador(inicio=10, fim=0, passo=2)
elif op == 'C':
    inicio = int(input('Digite o valor do inicio: '))
    fim = int(input('Digite o valor do fim: '))
    passo = int(input('Digite o valor do passo: '))
    contador(inicio, fim, passo)
else:
    print('opção inválida')


