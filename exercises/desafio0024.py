""" Escreva um programa que leia o nome de uma cidade e diga se esse nome começa
ou não com "Santo". """

# Input.
city_name = input('Entre o nome de uma cidade brasileira: ')

# Processing.
search_word = 'Santo'
find_word = (search_word in city_name)

# Output.
print(f'{find_word}')