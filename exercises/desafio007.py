"""
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""

# Entrada de dados.
nota1 = float(input('Entre a primeira nota: '))
nota2 = float(input('Entre a segunda nota: '))

# Calcula a média.
media = (nota1 + nota2) / 2

# Output.
print(f'Nota1: {nota1}')
print(f'Nota2: {nota2}')
print(f'A média entre as notas {nota1} e {nota2} é {media}')

# Verifica se foi aprovado.
if media >= 7.0:
    print(f'Aprovado')
else:
    print(f'Reprovado')