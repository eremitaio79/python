""" Crie um programa que leia  o nome completo de uma pessoa e mostre:
1. O nome com todas as letras em maiúsculo.
2. O nome completo em letras minúsculas.
3. Quantas letras ao todo, sem contar os espaços.
4. Quantas letras tem o primeiro nome. """

# Paulo de Tarso Eremita da Silva Filho

# Input.
full_name = str(input('Entre o nome completo: '))

# Processing.
print(f'Nome completo em maiúsculas: {full_name.upper()}')
print(f'Nome completo em minúsculas: {full_name.lower()}')
print(f'O nome tem {len(full_name.replace(' ','').strip())} letras')
print(f'O primeiro nome tem: {len(full_name.split()[0])} letras')