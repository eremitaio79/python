# Importa o módulo math completo.
import math
# Importa somente os pacotes sqrt e ceil do módulo math.
# from math import sqrt, ceil
# Importa somente o pacote mean (média aritmética) do módulo statistics.
from statistics import mean

import emoji

# Input.
num = int(input('Entre um número inteiro: '))

# Calculate.
# raiz = sqrt(num)
raiz = math.sqrt(num)

# Output.
print(f'A raiz quadrada do número {num} é {raiz:.2f}')
print(emoji.emojize('Hello!! :sunglasses:'))