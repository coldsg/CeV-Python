velocidade = float(input('Qual é a velocidade autual do carro? '))
if velocidade > 80:
    print('MULTADO! Você exceu o limite permitido que é de 80KM/h')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R$ {multa:2f}')
print('Tenha um bom dia! Dirija com segurança!')
