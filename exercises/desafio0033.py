""" Escreva um programa que leia 3 números e mostre qual deles é
o maior e qual é o menor. """

n1 = float(input('Entre n1: '))
n2 = float(input('Entre n2: '))
n3 = float(input('Entre n3: '))

if n1 > n2 and n1 > n3:
    print(f'{n1} é maior que {n1} e {n3}')
elif n2 > n1 and n2 > n3:
    print(f'{n2} é maior que {n1} e {n3}')
else:
    print(f'{n3} é maior que {n1} e {n2}')