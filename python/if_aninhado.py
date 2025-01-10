# if aninhado.

nome = input('Entre um nome qualquer: ')

if nome == 'Paulo':
    print(f'Nome foi {nome}.')
elif nome == 'Ana' or nome == 'Pedro':
    print(f'Agora o nome foi: {nome}')
elif nome in ('Ana Maria Pereira Geoconda'):
    print(f'Agora: {nome}')
else:
    print(f'Nenhum nome que eu conheça.')

    print(f'Todos os nomes foram interessantes.')