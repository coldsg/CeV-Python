"""
Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
função(parametro)
calculo e resultado
princial
menu
entrada(?)
"""
def área(largura, comprimento):
    area = largura * comprimento
    print(f'A area de um terreno {largura:.1f} x {comprimento:.1f} é de {area:.1f}m²')


print(' Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
