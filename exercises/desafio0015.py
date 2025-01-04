""" Escreva um programa  que pergunte a quantidade de kilômetros percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o
carro custa R$ 60,00 por dia e R$ 0,15 por km rodado. """

# Input.
qtd_km = float(input('Informe a quantidade de Km percorridos: '))
qtd_dias_alugado = int(input('O carro foi alugado por quantos dias?: '))

# Cálculos.
valor_por_dia = 60.00
valor_por_km_rodado = 0.15

preco_por_dia = qtd_dias_alugado * valor_por_dia
preco_por_km = qtd_km * valor_por_km_rodado
preco_a_pagar = (preco_por_km) + (preco_por_dia)

# Output.
print('-'*60)
print(f'Quantidade de km rodados: {qtd_km} km')
print(f'Quantidade de dias alugados: {qtd_dias_alugado} dias.')
print('-'*60)
print(f'Valor a pagar por dia: R$ {valor_por_dia}')
print(f'Valor a pagar por km rodado: R$ {valor_por_km_rodado}')
print('-'*60)
print(f'Preço total pelos dias rodados: R$ {preco_por_dia}')
print(f'Preço total por km rodado: R$ {preco_por_km}')
print('-'*60)
print(f'Preço final a pagar: R$ {preco_a_pagar:.2f}')