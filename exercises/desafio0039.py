""" Escreva um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade.=:

- Se ele vai se alistar no serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

A idade para o alistamento militar é 18 anos.
O programa também deverá mostrar o tempo que faltou ou que passou do prazo."""

from datetime import date

# Input.
ano_nascimento = int(input('Digite o ano de nascimento: '))

# Processing.
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
idade_alistamento = 18
diferenca = idade - idade_alistamento

# Output.
print('-' * 50)
print(f'Ano de nascimento: {ano_nascimento}')
print(f'Idade atual: {idade} anos')

if idade < idade_alistamento:
    anos_restantes = abs(diferenca)
    ano_alistamento = ano_atual + anos_restantes
    print('Você ainda vai se alistar no serviço militar.')
    print(f'Faltam {anos_restantes} anos para o alistamento.')
    print(f'Seu alistamento será no ano de {ano_alistamento}.')
elif idade == idade_alistamento:
    print('Está na hora de se alistar no serviço militar.')
    print(f'Seu alistamento é neste ano de {ano_atual}.')
else:
    anos_atrasados = diferenca
    ano_alistamento = ano_atual - anos_atrasados
    print('Você já passou do tempo de alistamento.')
    print(f'Você está {anos_atrasados} anos atrasado.')
    print(f'Seu alistamento foi no ano de {ano_alistamento}.')
