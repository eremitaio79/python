""" Escreva um programa que leia um ano qualquer e diga se ele é bissexto. """

# Input: solicitando o ano ao usuário
ano = int(input("Digite um ano: "))

# Verificando se é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
