""" Escreva um programa que leia o nome completo de uma pessoa e mostre na saída de tela
o primeiro e o último nome separadamente. """

# Input.
full_name = str(input('Entre o nome completo: ')).strip()

# Processamento: Separando os nomes
names = full_name.split()

# Output: Exibindo o primeiro e o último nome
print(f"Primeiro nome: {names[0]}")
print(f"Último nome: {names[-1]}")
