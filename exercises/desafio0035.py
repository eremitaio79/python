""" Escreva um programa que leia o comprimento de 3 retas e diga ao usuário
se elas podem ou não formar um triângulo. """

# Input: Recebendo o comprimento das retas.
reta1 = float(input("Digite o comprimento da primeira reta: "))
reta2 = float(input("Digite o comprimento da segunda reta: "))
reta3 = float(input("Digite o comprimento da terceira reta: "))

# Verificando as condições para formar um triângulo.
if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print("As retas podem formar um triângulo!")
else:
    print("As retas não podem formar um triângulo.")
