"""
Faça um programa que tenha uma função chamada escreva(),
 que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
"""
def escreva(mensagem):
    tamanho = len(mensagem) + 4
    print('~' * tamanho)
    print(f'  {mensagem}')
    print('~' * tamanho)

# Main
print('- Mensagem customizada - ')
msg = str(input('Digite a mensagem desejada: '))
escreva(msg)
