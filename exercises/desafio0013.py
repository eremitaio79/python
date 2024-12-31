"""
Escreva um programa que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
"""

# Entrada.
salario_bruto = float(input('Entre o valor do salário em R$: '))

# Calcula o valor do reajuste salarial.
valor_reajuste = 0.15
salario_com_aumento = salario_bruto + (salario_bruto * valor_reajuste)

# Output.
print(f'Salário atual: R$ {salario_bruto:.2f}')
print(f'Valor do aumento: {valor_reajuste * 100}%')
print(f'Salário reajustado: R$ {salario_com_aumento:.2f}')