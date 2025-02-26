import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

# Dados de avaliações dos usuários
avaliacoes = {
    'Ana': {'Freddy x Jason': 2.5, 'O Ultimato Bourne': 3.5, 'Star Trek': 3.0, 'Exterminador do Futuro': 3.5, 'Norbit': 2.5, 'Star Wars': 3.0},
    'Marcos': {'Freddy x Jason': 3.0, 'O Ultimato Bourne': 3.5, 'Star Trek': 1.5, 'Exterminador do Futuro': 5.0, 'Star Wars': 3.0, 'Norbit': 3.5},
    'Pedro': {'Freddy x Jason': 2.5, 'O Ultimato Bourne': 3.0, 'Exterminador do Futuro': 3.5, 'Star Wars': 4.0},
    'Claudia': {'O Ultimato Bourne': 3.5, 'Star Trek': 3.0, 'Star Wars': 4.5, 'Exterminador do Futuro': 4.0, 'Norbit': 2.5},
    'Adriano': {'Freddy x Jason': 3.0, 'O Ultimato Bourne': 4.0, 'Star Trek': 2.0, 'Exterminador do Futuro': 3.0, 'Star Wars': 3.0, 'Norbit': 2.0},
    'Janaina': {'Freddy x Jason': 3.0, 'O Ultimato Bourne': 4.0, 'Star Wars': 3.0, 'Exterminador do Futuro': 5.0, 'Norbit': 3.5},
    'Leonardo': {'O Ultimato Bourne': 4.5, 'Norbit': 1.0, 'Exterminador do Futuro': 4.0}
}

# Preenchendo avaliações ausentes com 0 (para facilitar o cálculo de semelhança)
todos_filmes = set()
for usuario in avaliacoes.values():
    todos_filmes.update(usuario.keys())

# Criando uma matriz de avaliações (rows = usuários, columns = filmes)
usuarios = list(avaliacoes.keys())
matriz_avaliacoes = np.zeros((len(usuarios), len(todos_filmes)))

# Preenchendo a matriz com as avaliações
filmes = list(todos_filmes)
for i, usuario in enumerate(usuarios):
    for j, filme in enumerate(filmes):
        matriz_avaliacoes[i, j] = avaliacoes[usuario].get(filme, 0)

# Calculando a semelhança de Pearson entre os usuários
similaridade = 1 - cdist(matriz_avaliacoes, matriz_avaliacoes, metric='correlation')

# Gerando o gráfico de dispersão (semelhança entre os usuários)
plt.figure(figsize=(8, 6))
for i in range(len(usuarios)):
    for j in range(i + 1, len(usuarios)):
        plt.scatter(i, j, c='blue', s=similaridade[i, j] * 1000, alpha=0.5)

plt.xticks(range(len(usuarios)), usuarios, rotation=90)
plt.yticks(range(len(usuarios)), usuarios)
plt.title('Semelhança de Pearson entre os usuários')
plt.xlabel('Usuários')
plt.ylabel('Usuários')
plt.show()
