"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares
ela pode comprar.
-> Considere: US$ 1.00 = R$ 3,27
"""

# Entrada.
qtd_em_real = float(input('Quanto tem em R$: '))

# Converte para dólar.
cotacao_dolar = 3.27
qtd_em_dolar = qtd_em_real / cotacao_dolar

print(f'Com o valor de R$ {qtd_em_real:.2f} é possível comprar US$ {qtd_em_dolar:.2f}')