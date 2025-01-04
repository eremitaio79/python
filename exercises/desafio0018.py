"""
Escreva um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

import math as m

# Input.
angle_deg = float(input('Enter the angle value in degrees: '))

# Converting to radians.
angle_rad = m.radians(angle_deg)

# Calculating sine, cosine, and tangent of the angle.
sine = m.sin(angle_rad)
cosine = m.cos(angle_rad)

""" Avoiding error for undefined tangent.
I included a try/except block to catch tangent errors at angles like 90° and 270°, where the
function may produce undefined values. """

try:
    tangent = m.tan(angle_rad)
except OverflowError:
    tangent = 'Undefined'

# Output.
print('-' * 50)
print(f'Angle entered: {angle_deg}°')
print('-' * 50)
print(f'Sine: {sine:.3f}')
print(f'Cosine: {cosine:.3f}')
print(f'Tangent: {tangent:.3f}')
