""" Escreva um programa que leia o nome de uma pessoa e diga se possui "Silva" no nome. """

# Input.
name = str(input('Entre o nome da pessoa: ')).strip().lower()

# Output.
print(f'Existe "Silva" no nome informado?: {'Silva'.lower() in name}')