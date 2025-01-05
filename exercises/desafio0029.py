""" Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada km acima do limite. """

velocidade_carro = float(input('Qual a velocidade do carro?: '))
velocidade_limite = int(80)
valor_multa_por_km = float(7.00)

# Verifica se foi multado.
if velocidade_carro > 80:
    multa = (velocidade_carro - velocidade_limite) * valor_multa_por_km
    print(f'Você excedeu em {velocidade_carro - velocidade_limite} km/h.'
          f'\nSerá multado em R$ {multa:.2f}')
else:
    print(f'Você estava dentro do limite permitido de {velocidade_limite} km/h.')
