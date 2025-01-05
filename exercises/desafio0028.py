""" Escreva um programa que faça o computador 'pensar' em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu. """

from random import randint
from time import sleep

# Gera um número inteiro aleatório entre 0 e 10, inclusivo.
num = randint(0,10)

print('-=-' * 30)
print(f'Tente adivinhar qual foi o número que pensei entre 0 e 10...')
print('-=-' * 30)

my_guess = int(input('Em que número pensei?: '))

# Simula um pequeno tempo de processamento.
print(f'Analisando...')
sleep(2)

# Joga com o programa.
if my_guess == num:
    print(f'Parabéns! Você acertou!!!\nPensei exatamente em {num}.')
else:
    print(f'Não foi dessa vez. Eu tinha pensando em {num}.')