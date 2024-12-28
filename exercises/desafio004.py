"""
Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
"""
value = input('Entre um valor qualquer: ')

print(type(value))
print(f'Valor entrado: {value}')
print(f'É alfanumérico? {value.isalnum()}')
print(f'É texto? {value.isalpha()}')
print(f'É ascii? {value.isascii()}')
print(f'É um dígito? {value.isdigit()}')
print(f'É decimal? {value.isdecimal()}')
print(f'É maiúsculo? {value.isupper()}')
print(f'É numérico? {value.isnumeric()}')