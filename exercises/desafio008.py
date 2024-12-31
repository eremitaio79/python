"""
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

# Entrada.
valorEmMetros = float(input('Entre um valor em metros: '))

# Converte o valor entrado para centímetros.
valorEmCentimetros = valorEmMetros * 100

# Converte o valor entrado para milímetros.
valorEmMilimetros = valorEmMetros * 1000

# Output.
print(f'Valor entrado em metros: {valorEmMetros} m')
print(f'Valor convertido para centímetros: {valorEmCentimetros} cm')
print(f'Valor convertido para milímetros: {valorEmMilimetros} mm')