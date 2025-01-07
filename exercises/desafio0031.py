""" Escreva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de
até 200km e R$ 0,45 para viagens mais longas. """

# Input.
distancia_viagem = float(input('Qual a distância da viagem?: '))

# Parameters.
distancia_limite = 200
valor_multa1 = 0.50
valor_multa2 = 0.45

# Processing and output.
if distancia_viagem <= distancia_limite:
    print(f'Distância informada: {distancia_viagem} km.')
    valor_final = distancia_viagem * valor_multa1
    print(f'O valor da passagem é R$ {valor_final:.2f}.')
else:
    print(f'Distância informada: {distancia_viagem} km.')
    valor_final = distancia_viagem * valor_multa2
    print(f'O valor da passagem é R$ {valor_final:.2f}.')