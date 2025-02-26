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

# Extraindo as avaliações dos filmes Star Trek e Exterminador do Futuro para os eixos X e Y
indice_star_trek = filmes.index('Star Trek')
indice_exterminador = filmes.index('Exterminador do Futuro')

x_values = matriz_avaliacoes[:, indice_star_trek]
y_values = matriz_avaliacoes[:, indice_exterminador]

# Calculando a semelhança de Pearson entre os usuários
similaridade = 1 - cdist(matriz_avaliacoes, matriz_avaliacoes, metric='correlation')

# Gerando o gráfico de dispersão
plt.figure(figsize=(8, 6))

# Plotando os pontos de dispersão (usando as avaliações de Star Trek e Exterminador do Futuro)
for i in range(len(usuarios)):
    for j in range(i + 1, len(usuarios)):
        # Definindo a cor ou o tamanho do ponto com base na similaridade
        plt.scatter(x_values[i], y_values[i], c='blue', s=similaridade[i, j] * 100, alpha=0.5)

# Configurando os rótulos dos usuários no gráfico
for i, usuario in enumerate(usuarios):
    plt.text(x_values[i] + 0.05, y_values[i] + 0.05, usuario, fontsize=9)

# Adicionando título e rótulos
plt.title('Avaliações dos usuários para Star Trek (X) e Exterminador do Futuro (Y)')
plt.xlabel('Avaliação de Star Trek')
plt.ylabel('Avaliação de Exterminador do Futuro')

# Exibindo o gráfico
plt.grid(True)
plt.show()
