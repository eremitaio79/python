# String.
frase = 'O espaço, a fronteira final.'
frase2 = '    O espaço, a fronteira    final.    '
#        0123456789112345678921234567

# Fatiamento de strings.
print(f'{frase}')
print(f'{frase[3]}')
print(f'{frase[3:15]}')
print(f'{frase[0:6:2]}')
print(f'{frase[:6]}')
print(f'{frase[15:]}')
print(f'{frase[2::3]}')
print('-' * 30)

# Análise de strings.
print(f'{len(frase)} caracteres') # Retorna a quantidade de caracteres da string.
print(f'{frase.count('a')}') # Conta quantas vezes a letra 'a' aparece na string.
print(f'{frase.count('a', 0,13)}') # Conta quantas vezes a letra 'a' aparece na string entre 0 e 12.
print(f'{frase.find('front')}') # Retorne o valor a de a partir de onde inicia a 'front'.
print(f'{frase.find('Teste')}') # Se uma string não existe dentro da string, retorna -1.
print(f'{'espaço' in frase}') # Retorna True ou False.
print(f'{'espaços' in frase}') # Retorna True ou False.

# Transformações em strings.
print(f'{frase.replace('a fronteira','o limite')}') # Substitui um conjunto de caracteres por outro.
print(f'{frase.upper()}')
print(f'{frase.lower()}')
print(f'{frase.capitalize()}')
print(f'{frase.title()}')
print(f'{frase2}')
print(f'{frase2.strip()}')
print(f'{frase2.rstrip()}')
print(f'{frase2.lstrip()}')

# Divisão de strings.
print(f'{frase.split()}')
print(f'{frase.split()[3]}')

# Junção de strings.
print(f'{'-'.join(frase)}')
print(f'{'_'.join(frase)}')