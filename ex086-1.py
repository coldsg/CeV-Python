matriz = [[], [], []]
valor = c = i = 0
for p in range(0, 9):
    if p in [0, 1, 2]:
        c = 0
        valor = int(input(f'Digite um valor para [{c}, {i}]'))
        matriz[0].append(valor)
        i = i + 1
        if p == 2:
            i = 0
    elif p in [3, 4, 5]:
        c = 1
        valor = int(input(f'Digite um valor para [{c}, {i}]'))
        matriz[1].append(valor)
        i = i + 1
        if p == 5:
            i = 0
    elif p in [6, 7, 8]:
        c = 2
        valor = int(input(f'Digite um valor para [{c}, {i}]'))
        matriz[2].append(valor)
        i = i + 1
        if p == 8:
            i = 0
print(matriz[0])
print(matriz[1])
print(matriz[2])
