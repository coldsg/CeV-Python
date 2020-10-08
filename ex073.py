times = ['Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Corinthians',
         'Internacional', 'Fortaleza', 'Goiás', 'Bahia', 'Atlético-MG', 'Vasco', 'Fluminense',
         'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí']
op = 0
print('-=' * 30)
print(f'{"Brasileirão 2019":^60}')
print('-=' * 30)
print(f'''[ 0 ] = Mostrar todos
[ 1 ] = Cinco primeiros
[ 2 ] = Quatro ultimos 
[ 3 ] = Times em ordem alfabética
[ 4 ] = Posição da Chapecoense''')
while True:
    op = int(input('[-> ] = '))
    if op > 4:
        break
    elif op == 0:
        print(f'Lista de times do Brasileirão:{times}')
    elif op == 1:
        print(f'Os 5 primeiros são {times[0:5]}')
    elif op == 2:
        print(f'Os 4 últimos são {times[-4:]}')
    elif op == 3:
        print(f'Times em ordem alfabética: {sorted(times)}')
    elif op == 4:
        print(f'O Chapecoense está na {times.index("Chapecoense") + 1} ° posição')
print('FIM')

