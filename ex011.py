# Faça um programa que leia a largura e a altura de uma parede em metro, calcule a
# sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta,
# pinta uma área de 2m².

largura = float(input('Digite a largura '))
altura = float(input('Digite a altura '))

area = largura * altura
litro = area / 2

print(f'É necessario {litro:.3f} litros de tinta para uma area de {area:.3f} m²')