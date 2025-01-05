""" Escreva um programa que leia o comprimento de 3 retas e diga ao usuário
se elas podem ou não formar um triângulo. """

# Verificando se três retas podem formar um triângulo
def pode_formar_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Desenhando o triângulo no terminal
def desenhar_triangulo(base):
    for i in range(1, base + 1):
        espacos = " " * (base - i)
        estrelas = "*" * (2 * i - 1)
        print(espacos + estrelas)

# Entrada dos comprimentos
reta1 = float(input("Digite o comprimento da primeira reta: "))
reta2 = float(input("Digite o comprimento da segunda reta: "))
reta3 = float(input("Digite o comprimento da terceira reta: "))

# Verificando e gerando a saída
if pode_formar_triangulo(reta1, reta2, reta3):
    print("\nAs retas podem formar um triângulo!")
    # Calculando a altura aproximada para o desenho
    base = int(min(reta1, reta2, reta3))  # Considera o menor lado como a base
    print("\nDesenho do triângulo:")
    desenhar_triangulo(base)
else:
    print("\nAs retas NÃO podem formar um triângulo.")

