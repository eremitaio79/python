import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

from recomendacao import avaliacoes

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

# Gerando o gráfico de dispersão
plt.figure(figsize=(8, 6))

# Adicionando pontos de dispersão representando a semelhança entre usuários
for i in range(len(usuarios)):
    for j in range(i + 1, len(usuarios)):
        plt.scatter(i, j, c='blue', s=similaridade[i, j] * 1000, alpha=0.5)

# Configurando os rótulos dos usuários no eixo X e Y
plt.xticks(range(len(usuarios)), usuarios, rotation=90)
plt.yticks(range(len(usuarios)), usuarios)

# Adicionando título e rótulos
plt.title('Semelhança de Pearson entre os Usuários')
plt.xlabel('Usuários')
plt.ylabel('Usuários')

# Exibindo o gráfico
plt.show()
