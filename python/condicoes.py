# Condicional if()
nome = str(input('Qual seu nome?: '))

if nome == 'Paulo':
    print(f'Olá {nome}')
else:
    print(f'Não conheço você.')

print(f'Linha executada fora da condição.')

print('-' * 50)

n1 = float(input('Entre a nota 1: '))
n2 = float(input('Entre a nota 2: '))
media = float((n1 + n2) / 2)

if media >= 7.0:
    print(f'Sua média foi boa')
else:
    print(f'Sua média precisa melhorar.')

print(f'Nota 1: {n1}')
print(f'Nota 2: {n2}')
print(f'Média: {media:.2f}')
