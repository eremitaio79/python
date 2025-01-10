"""" Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão.

- 1 para binário
- 2 para octal
- 3 para hexadecimal"""

# Input.
num = int(input('Entre um número inteiro: '))
print('Escolha a base de conversão:')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')

opcao = int(input('Sua escolha: '))

# Processing.
if opcao == 1:
    resultado = bin(num)[2:]  # Converte para binário, removendo o prefixo '0b'.
    base = "Binário"
elif opcao == 2:
    resultado = oct(num)[2:]  # Converte para octal, removendo o prefixo '0o'.
    base = "Octal"
elif opcao == 3:
    resultado = hex(num)[2:]  # Converte para hexadecimal, removendo o prefixo '0x'.
    base = "Hexadecimal"
else:
    resultado = None
    base = None

# Output.
if resultado:
    print(f'O número {num} convertido para {base} é: {resultado}')
else:
    print('Opção inválida! Tente novamente.')
