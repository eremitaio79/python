""" Escreva um programa que leia um número inteiro e mostre na tela
se ele é par ou ímpar. """

num = int(input('Entre um número inteiro qualquer: '))

# Verifica se é par ou ímpar.
if num % 2 == 0:
    print(f'O número {num} informado é PAR.')
else:
    print(f'O número {num} informado é ÍMPAR.')