"""" Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado."""

# Inputs.
valor_casa = float(input('Qual o valor da casa desejada?: '))
valor_salario = float(input('Qual o valor do seu salário?: '))
tempo_pagamento_anos = int(input('Em quantos anos pretende pagar o financiamento?: '))

# Processing.
# Calculations.
tempo_em_meses = 12 * tempo_pagamento_anos
valor_parcela_mensal = valor_casa / tempo_em_meses
valor_teto_maximo_parcela = valor_salario * 0.3  # 30% do salário.

# Output.
print('-' * 50)
print(f'Valor da casa: R$ {valor_casa:.2f}')
print(f'Valor do salário: R$ {valor_salario:.2f}')
print(f'Tempo para pagamentos em anos: {tempo_pagamento_anos} anos')
print('-' * 50)
print(f'Tempo em meses: {tempo_em_meses} meses')
print(f'Valor mensal das parcelas: R$ {valor_parcela_mensal:.2f}')
print(f'Teto máximo da parcela (30% do salário): R$ {valor_teto_maximo_parcela:.2f}')
print('-' * 50)

# Verificação do empréstimo.
if valor_parcela_mensal <= valor_teto_maximo_parcela:
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO. A parcela excede 30% do salário.')
