"""
Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração,
multiplicação e divisão.
"""
n1 = int(input('Entre o primeiro número inteiro: '))
n2 = int(input('Entre o segundo número inteiro: '))
soma = n1 + n2
print('A soma de ', n1, ' + ', n2, ' é igual a ', soma)

"""
Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz
12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média
durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE.
Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com
a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo
gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem
"""

tempo_viagem = float(input('Informe o tempo de viagem: '))
velocidade_media =  float(input('Informe a velocidade média: '))

distancia = (tempo_viagem * velocidade_media)

litros_gastos = (distancia / 12)

print('Tempo de viagem: ', tempo_viagem, ' horas')
print('Velocidade média do carro: ', velocidade_media, ' Km/h')
print('Distância percorrida: ', distancia, ' Km')
print('Quantidade de combustível consumido na viagem: ', round(litros_gastos, 2), ' litros')