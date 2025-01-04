"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Escreva um programa que ajude ele,
lendo o nome dos alunos e escrevendo o nome do escolhido.
"""
from random import choice

# Inputs.
aluno1 = str(input('Entre o nome do primeiro aluno: '))
aluno2 = str(input('Entre o nome do segundo aluno: '))
aluno3 = str(input('Entre o nome do terceiro aluno: '))
aluno4 = str(input('Entre o nome do quarto aluno: '))

# Processing.
lista_de_alunos = [aluno1, aluno2, aluno3, aluno4]
aluno_sorteado = choice(lista_de_alunos)

print(f'Aluno sorteado: {aluno_sorteado}')