import numpy as np
import matplotlib.pyplot as plt

# Dados das avaliações
avaliacoes = {
    'Ana': {'Star Trek': 3.0, 'Exterminador do Futuro': 3.5},
    'Marcos': {'Star Trek': 1.5, 'Exterminador do Futuro': 5.0},
    'Pedro': {'Star Trek': None, 'Exterminador do Futuro': 3.5},
    'Claudia': {'Star Trek': 3.0, 'Exterminador do Futuro': 4.0},
    'Adriano': {'Star Trek': 2.0, 'Exterminador do Futuro': 3.0},
    'Janaina': {'Star Trek': None, 'Exterminador do Futuro': 5.0},
    'Leonardo': {'Star Trek': None, 'Exterminador do Futuro': 4.0}
}

# Filtra apenas usuários que avaliaram os dois filmes
usuarios_validos = {user: notas for user, notas in avaliacoes.items() if None not in notas.values()}

# Calcula distância euclidiana entre todos os pares de usuários
usuarios = list(usuarios_validos.keys())
distancias = {}

for i in range(len(usuarios)):
    for j in range(i + 1, len(usuarios)):
        u1, u2 = usuarios[i], usuarios[j]
        x1, y1 = usuarios_validos[u1]['Star Trek'], usuarios_validos[u1]['Exterminador do Futuro']
        x2, y2 = usuarios_validos[u2]['Star Trek'], usuarios_validos[u2]['Exterminador do Futuro']
        distancia = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        distancias[(u1, u2)] = distancia

# Ordena os pares por menor distância (mais parecidos)
pares_mais_parecidos = sorted(distancias.items(), key=lambda x: x[1])

# Exibe os pares mais parecidos
print("Pares de usuários mais parecidos:")
for (u1, u2), dist in pares_mais_parecidos:
    print(f"{u1} e {u2} -> Distância Euclidiana: {dist:.2f}")

# Gerando o gráfico de dispersão
plt.figure(figsize=(8, 6))
for usuario, notas in usuarios_validos.items():
    plt.scatter(notas['Star Trek'], notas['Exterminador do Futuro'], label=usuario)

plt.xlabel("Avaliação de Star Trek")
plt.ylabel("Avaliação de Exterminador do Futuro")
plt.title("Gráfico de Dispersão das Avaliações")
plt.legend()
plt.grid(True)
plt.show()
