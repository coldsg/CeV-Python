# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

numero = int(input('Digite um numero '))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print(f'O dobro de {numero} é igual a {dobro}, seu triplo é igual {triplo} e sua raiz é igual a {raiz:.2f}')
