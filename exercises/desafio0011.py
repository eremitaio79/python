"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
de tinta necessária para pintá-la, sabendo que a cada litro de tinta, pinta uma área de 2 metros quadrados.
"""

# Entrada.
largura = float(input('Entre o valor da largura da parede em metros: '))
altura = float(input('Entre o valor da altura da parede em metros: '))

# Calcula a área da parede em metros.
area_da_parede = largura * altura

# Calcula a quantidade de tinta necessária para pintar a parede.
qtd_tinta = area_da_parede / 2

# Output.
print(f'Largura da parede em metros: {largura:.3f}m')
print(f'Altura da parede em metros: {altura:.3f}m')
print(f'Área da parede em metros quadrados: {area_da_parede:.3f}m²')
print(f'Quantidade de tinta em litros para pintar a parede: {qtd_tinta:.1f}l')