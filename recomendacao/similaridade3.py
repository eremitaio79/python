from recomendacao import avaliacoes
from math import sqrt

from similaridade import usuario

"""
Esta função calcula a similaridade entre dois usuários.
A Distância Euclidiana calcula a distância entre dois pontos dentro do plano cartesiano.
"""
def distancia_euclidiana(usuario1, usuario2):
    # Lista de similaridade.
    similaridade = {}

    for item in avaliacoes[usuario1]:
        if item in avaliacoes[usuario2]:
            similaridade[item] = 1

    if len(similaridade) == 0:
        return 0

    soma = sum([pow(avaliacoes[usuario1][item] - avaliacoes[usuario2][item], 2)])
        for item avaliacoes[usuario1]