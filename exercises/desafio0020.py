"""
O mesmo professor do desafio 19 quer sortear a ordem da apresentação de trabalhos dos alunos. Escreva
um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

from random import shuffle as s

# Inputs.
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
a5 = str(input('Aluno 5: '))

# Processing.
lista_alunos = [a1, a2, a3, a4, a5]

# Randomizing list items.
s(lista_alunos)

# Output.
print(f'Ordem de apresentação dos alunos. {lista_alunos}')
for i, aluno in enumerate(lista_alunos, 1):
    print(f'{i}: {aluno}')