""" Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua parte inteira. """

# import math
from math import trunc as t

# Input.
num_real = float(input('Entre um número real qualquer: '))

# Processing.
parte_inteira = t(num_real)

# Output.
print(f'Número real entrado: {num_real}')
print(f'Parte inteira do número real: {parte_inteira}')