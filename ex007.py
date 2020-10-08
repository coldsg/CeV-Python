# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

nota1 = float(input('Digite a primeira nota '))
nota2 = float(input('Digite a segunda nota '))

media = (nota1 + nota2) / 2

print(f'A media entre a nota 1 -> {nota1:.1f} e a nota 2 -> {nota2:.1f} é igual a {media:.1f}')