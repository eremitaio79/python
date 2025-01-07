""" Escreva um programa que leia um ano qualquer e diga se ele é bissexto. """

from datetime import date

# Input: solicitando o ano ao usuário
ano = int(input("Digite um ano (para o ano atual, digite -1): "))

# Verificando se é bissexto
if ano == -1:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
