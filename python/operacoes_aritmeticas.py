# Operadores aritméticos.

n1 = float(input('Entre o primeiro número: '))
n2 = float(input('Entre o segundo número: '))

# Operadores.
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao_padrao = n1 / n2

potencia = n1 ** n2
funcao_potencia = pow(n1, n2)

divisao_inteira = n1 // n2
resto = n1 % n2

# Output.
print(f'Soma: {n1} + {n2} = {soma}')
print(f'Subtração: {n1} - {n2} = {subtracao}')
print(f'Multiplicação: {n1} * {n2} = {multiplicacao}')
print(f'Divisão Padrão: {n1} / {n2} = {divisao_padrao}')
print('-' * 40)
print(f'Potência: {n1} ** {n2} = {potencia}')
print(f'Função Potência: {n1} ** {n2} = {funcao_potencia}')
print('-' * 40)
print(f'Divisão Inteira: {n1} // {n2} = {divisao_inteira}')
print(f'Resto da Divisão: {n1} % {n2} = {resto}')