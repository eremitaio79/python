"""
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""

# Armazena as notas em uma lista.
notas = []

# Entrada de dados.
quantidade_notas = int(input('Quantas notas deseja entrar para calcular a média?: '))

# Lê todas as notas entradas.
for i in range(quantidade_notas):
    nota = float(input(f'Digite a nota {i + 1}: '))
    notas.append(nota)

# Calcula a média com base nas notas entradas.
media = sum(notas) / len(notas)

# Output.
print("\nNotas inseridas:")
for i, nota in enumerate(notas, start=1):
    print(f'Nota {i}: {nota}')
print(f'A média entre as notas é {media:.2f}')

if media >= 7.0:
    print('Aprovado.')
else:
    print('Reprovado.')