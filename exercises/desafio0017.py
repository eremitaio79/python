""" Escreva um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa. """

# Modules.
from math import sqrt as sr, pow as p

# There is a specific package to calculate the hypotenuse.
from math import hypot as h

# Input.
cateto_oposto = float(input('Entre o valor do cateto oposto: '))
cateto_adjacente = float(input('Entre o valor do cateto adjacente: '))

""" Processing: Computing the hypotenuse value. """
# Usando as funções sqrt() e pow().
hipotenusa = sr(p(cateto_oposto, 2) + (p(cateto_adjacente, 2)))

# Usando somente as funções built-in da linguagem.
hipotenusa2 = ((cateto_oposto ** 2) + (cateto_adjacente ** 2)) ** (1/2)

# Using the hypot pack.
hipotenusa3 = h(cateto_adjacente, cateto_oposto)

# Output.
print('-' * 50)
print(f'Cateto oposto: {cateto_oposto}')
print(f'Cateto adjacente: {cateto_adjacente}')
print('-' * 50)
print(f'O valor da hipotenusa é: {hipotenusa:.3f}')
print('-' * 50)
print(f'O valor da hipotenusa2 é: {hipotenusa2:.3f}')
print('-' * 50)
print(f'O valor da hipotenusa3 é: {hipotenusa3:.3f}')