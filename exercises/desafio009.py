"""
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
"""

# Entrada
num = int(input('Entre um número inteiro qualquer: '))

# Tabuada do número entrado
print(f'Tabuada do número {num}:')
for i in range(1, 11):  # De 1 até 10 (inclusive)
    print(f'{num} x {i} = {num * i}')
