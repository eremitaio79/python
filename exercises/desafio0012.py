"""
Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
"""

# Entrada.
preco_produto = float(input('Entre o valor do produto em R$: '))
valor_desconto = float(input('Quantos % de desconto para este produto?: '))

# Calcula o desconto no preço do produto.
valor_desconto = valor_desconto / 100
preco_com_desconto = preco_produto - (preco_produto * valor_desconto)

# Output.
print(f'Preço do produto: R$ {preco_produto:.2f}')
print(f'Valor do desconto: {valor_desconto * 100}%')
print(f'Preço final com desconto: R$ {preco_com_desconto:.2f}')