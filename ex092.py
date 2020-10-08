import datetime
"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""
carteira = {
    "nome": '',
    "ano": 0,
    "idade": 0,
    "ctps": -1,
    "contrato": 0,
    "salário": 0.0,
    "aposentadoria": 0
}
while True:
    now = datetime.datetime.now()
    carteira["nome"] = str(input('Nome: '))
    carteira["ano"] = int(input('Ano de nascimento: '))
    carteira["idade"] = now.year - carteira["ano"]
    carteira["ctps"] = int(input('CTPS: '))
    if carteira["ctps"] > 0:
        carteira["contrato"] = int(input('Ano de contratação: '))
        carteira["salário"] = float(input('Salário: R$ '))
        carteira["aposentadoria"] = carteira["idade"] + ((carteira["contrato"] + 35) - now.year)
    break

for k, v in carteira.items():
    if k or v != 0:
        print(f'- {k} -> {v}')
