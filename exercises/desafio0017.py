""" Escreva um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa. """

# Modules.
from math import sqrt as sr, pow as p

# Input.
cateto_oposto = float(input('Entre o valor do cateto oposto: '))
cateto_adjacente = float(input('Entre o valor do cateto adjacente: '))

""" Processing: Computing the hypotenuse value. """
hipotenusa = sr(p(cateto_oposto, 2) + (p(cateto_adjacente, 2)))

# Output.
print('-' * 50)
print(f'Cateto oposto: {cateto_oposto}')
print(f'Cateto adjacente: {cateto_adjacente}')
print('-' * 50)
print(f'O valor da hipotenusa é: {hipotenusa:.3f}')