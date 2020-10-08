# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele

resposta = input('Digite algo')
print(f'O tipo primitivo deste valor é: {type(resposta)}')
print(f'Só tem espaços? {resposta.isspace()}')
print(f'É um número? {resposta.isnumeric()}')
print(f'É alfabético? {resposta.isalpha()}')
print(f'É alfanumérico? {resposta.isalnum()}')
print(f'Está em maiúsculas? {resposta.isupper()}')
print(f'Está em minúsculas? {resposta.islower()}', )
print(f'Está capitalizada? {resposta.istitle()}')
