import math
# Faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa |_\

oposto = float(input('Digite o cateto oposto '))
adjacente = float(input('Digite o cateto adjacente '))
hipotenusa = math.hypot(oposto, adjacente)
print(f'O comprimento da hipotenusa é {hipotenusa:.1f} ')