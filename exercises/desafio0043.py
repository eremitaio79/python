""" Escreva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre
seu status, de acordo com a tabela abaixo:

- Abaixo de 18,5: ABAIXO DO PESO
- Entre 18,5 e 25: PESO IDEAL
- 25 a 30: SOBREPESO
- 30 a 40: OBESIDADE
- Acima de 40: OBESIDADE MÓRBIDA"""

# Input: Recebendo peso e altura do usuário.
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))

# Processing: Calculando o IMC.
imc = peso / (altura ** 2)

# Output: Exibindo o IMC e o status.
print(f"Seu IMC é: {imc:.2f}")  # Mostra o IMC com duas casas decimais.

# Determinando o status do IMC.
if imc < 18.5:
    print("Status: ABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print("Status: PESO IDEAL")
elif 25 <= imc < 30:
    print("Status: SOBREPESO")
elif 30 <= imc < 40:
    print("Status: OBESIDADE")
else:
    print("Status: OBESIDADE MÓRBIDA")
