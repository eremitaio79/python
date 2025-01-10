""" Escreva um programa que faça o computador jogar JOKENPÔ com você."""

import random

# Opções do jogo
opcoes = ["Pedra", "Papel", "Tesoura"]

# Input: O jogador escolhe sua opção.
print("Escolha uma opção:")
print("[ 1 ] Pedra")
print("[ 2 ] Papel")
print("[ 3 ] Tesoura")

jogador_escolha = int(input("Digite o número correspondente à sua escolha: "))

# Verificando a escolha do jogador
if jogador_escolha == 1:
    jogador = "Pedra"
elif jogador_escolha == 2:
    jogador = "Papel"
elif jogador_escolha == 3:
    jogador = "Tesoura"
else:
    print("Escolha inválida! O jogo será encerrado.")
    exit()

# Escolha do computador
computador_escolha = random.choice(opcoes)
print(f"Computador escolheu: {computador_escolha}")

# Determinando o vencedor
if jogador == computador_escolha:
    resultado = "Empate!"
elif (jogador == "Pedra" and computador_escolha == "Tesoura") or \
     (jogador == "Papel" and computador_escolha == "Pedra") or \
     (jogador == "Tesoura" and computador_escolha == "Papel"):
    resultado = "Você ganhou!"
else:
    resultado = "Você perdeu!"

# Output: Exibindo o resultado
print(resultado)
