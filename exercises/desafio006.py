"""
Faça um algorítmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

# Número entrado.
num = float(input('Digite um número qualquer: '))

# Dobro do número.
dobro = num * 2

# Triplo do número.
triplo = num * 3

# Raiz quadrada do número.
raizQuadrada = num ** (1/2)

# Output.
print(f'Número entrado: {num}')
print(f'-' * 50)
print(f'Dobro do número: {dobro}')
print(f'Triplo do número: {triplo}')
print(f'Raíz quadrada do número: {raizQuadrada:.2f}')