matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = colunas = linhas = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        colunas += matriz[l][2]
        if matriz[1][c] > linhas:
            linhas = matriz[1][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma de todos os valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {colunas}')
print(f'O maior valor da segunda linha é {linhas}')
