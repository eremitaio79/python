""" Escreva um programa que converta uma temperatura de graus Celsius para graus Fahrenheit. """

# Entrada da temperatura em graus Celsius.
temp_celsius = float(input('Entre a temperatura em graus Celsius (°C): '))

""" Cálculo da conversão de Celsius para Fahrenheit.
°F=(°C×1,8)+32 """
temp_fahrenheit = (temp_celsius * 1.8) + 32

# Output.
print(f'Temperatura em graus Celsius: {temp_celsius:.2f} °C')
print(f'Temperatura em graus Fahrenheit: {temp_fahrenheit:.2f} °F')