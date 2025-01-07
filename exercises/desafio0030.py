""" Escreva um programa que leia um número inteiro e mostre na tela
se ele é par ou ímpar. """

# Define os códigos de cor
RESET = "\033[0m"  # Reseta a cor para o padrão
GREEN = "\033[32m"  # Verde para números pares
RED = "\033[31m"  # Vermelho para números ímpares

num = int(input('Entre um número inteiro qualquer: '))

# Verifica se é par ou ímpar.
if num % 2 == 0:
    print(f'O número {num} informado é {GREEN}PAR{RESET}.')
else:
    print(f'O número {num} informado é {RED}ÍMPAR{RESET}.')