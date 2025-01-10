""" A confederação nacional de natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos:  INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER"""

from datetime import date

# Input.
ano_nascimento = int(input('Digite o ano de nascimento: '))

# Processing.
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

# Output.
print('-' * 50)
print(f'Ano de nascimento: {ano_nascimento}')
print(f'Idade atual: {idade} anos')
print('-' * 50)

if idade > 20.0:
    print(f'MASTER')
elif (idade > 19) and (idade <= 20):
    print(f'SÊNIOR')
elif (idade > 14) and (idade <= 19):
    print(f'JUNIOR')
elif (idade > 9) and (idade <= 14):
    print(f'INFANTIL')
else:
    print(f'MIRIM')