"""
Faça um programa que leia um número e mostre na tela o seu sucessor e seu antecessor.
"""

# Informe o número.
num = float(input('Digite um número qualquer: '))

# Sucessor do número entrado.
sucessor = num + 1

# Antecessor do número entrado.
antecessor = num - 1

# Output.
print(f'\n{"-" * 40}'
      f'\nNúmero entrado: {num}'
      f'\n{"-" * 40}'
      f'\nSeu antecessor: {antecessor}'
      f'\nSeu sucessor: {sucessor}')
