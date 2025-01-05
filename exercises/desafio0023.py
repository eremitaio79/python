""" Escreva um programa que leia um número de 0 a 9999 e mostre na tela cada
um dos dígitos separados.
Exemplo: 1234
Unidade: 4
Dezena: 3
Centena: 2
Milhar: 1 """

# # Input.
# num = input('Entre um número inteiro entre 0 e 9999: ')
#
# # Processing.
# u = num[3]
# d = num[2]
# c = num[1]
# m = num[0]
#
# # Output.
# print(f'Número entrado: {num}')
# print(f'Unidade: {u}')
# print(f'Dezena: {d}')
# print(f'Centena: {c}')
# print(f'Milhar: {m}')

# Input
num = input('Entre um número inteiro entre 0 e 9999: ').strip()

# Verificação da entrada
if not num.isdigit() or int(num) < 0 or int(num) > 9999:
    print("Erro: Por favor, insira um número inteiro entre 0 e 9999.")
else:
    # Ajustando o número para ter 4 dígitos (preenchendo com zeros à esquerda)
    num = num.zfill(4)

    # Processamento
    m = num[0]  # Milhar
    c = num[1]  # Centena
    d = num[2]  # Dezena
    u = num[3]  # Unidade

    # Output
    print(f'Número entrado: {int(num)}')
    print(f'Milhar: {m}')
    print(f'Centena: {c}')
    print(f'Dezena: {d}')
    print(f'Unidade: {u}')
