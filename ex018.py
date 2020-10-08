from math import sin, cos, tan
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo

ângulo = float(input('Digite o ângulo '))
print(f'O valor do seno é {sin(ângulo):.2f} ')
print(f'O valor do cosseno é {cos(ângulo):.2f} ')
print(f'O valor da tangente é {tan(ângulo):.2f} ')