""" Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%. """

salario = float(input('Entre o valor do salário em reais: '))
valor_base = float(1250.00)
reajuste1 = float(0.10)
reajuste2 = float(0.15)

if salario > valor_base:
    salario_reajustado = salario + (salario * reajuste1)
    print(f'Seu salário de R$ {salario} foi reajustado em 10%, ficando em R$ {salario_reajustado}.')
else:
    salario_reajustado = salario + (salario * reajuste2)
    print(f'Seu salário de R$ {salario} foi reajustado em 15%, ficando em R$ {salario_reajustado}.')
