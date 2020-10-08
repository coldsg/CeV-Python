numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número [de 1 a 20 ]\nOu outro valor para sair: '))
    if numero < 0 or numero > 20:
        break
    else:
        print(f'Você digitou o número {numeros[numero]}')
print('FIM DO PROGRAMA')
