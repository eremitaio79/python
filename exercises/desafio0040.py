""" Escreva um programa que leia duas notas de um aluno e calcule sua média, mostrando
uma mensagem no final, de acordo com a mádia atingida:

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO"""

# Input.
nota1 = float(input('Entre a primeira nota: '))
nota2 = float(input('Entre a segunda nota: '))

# Processing.
media = (nota1 + nota2) / 2

# Output.
print(f'Nota 1: {nota1}')
print(f'Nota 2: {nota2}')
print(f'Média: {media:.2f}')  # Exibe a média com duas casas decimais.

if media >= 7.0:
    print('APROVADO')
elif 5.0 <= media < 7.0:  # Corrigido para incluir médias menores que 7.0.
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')
