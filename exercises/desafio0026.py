""" Escreva um programa que leia uma frase pelo teclado e mostre:
1. Quantas vezes a letra A aparece nela.
2. Em que posição ela aparece pela primeira vez.
3. Em que posição ela aparece pela última vez. """

# Input: Lendo a frase do teclado
frase = str(input("Digite uma frase: ")).strip().lower()

# 1. Contar quantas vezes a letra 'a' aparece
quantidade_a = frase.count('a')

# 2. Encontrar a posição da primeira ocorrência da letra 'a'
primeira_posicao = frase.find('a') + 1 if 'a' in frase else -1

# 3. Encontrar a posição da última ocorrência da letra 'a'
ultima_posicao = frase.rfind('a') + 1 if 'a' in frase else -1

# Output: Exibindo os resultados
print(f"A letra 'A' aparece {quantidade_a} vez(es) na frase.")
if primeira_posicao != -1:
    print(f"A primeira letra 'A' aparece na posição {primeira_posicao}.")
    print(f"A última letra 'A' aparece na posição {ultima_posicao}.")
else:
    print("A letra 'A' não foi encontrada na frase.")
