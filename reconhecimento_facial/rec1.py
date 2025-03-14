import cv2  # OpenCV para visão computacional
import numpy as np
import matplotlib.pyplot as plt # Para plotar os resultados de forma visual.
import zipfile
import os
import dlib


# Função para extrair um arquivo ZIP
def extrair_zip(caminho_zip, destino="./"):
    """Extrai um arquivo ZIP se ele existir."""
    if not os.path.exists(caminho_zip):
        print(f"Erro: O arquivo '{caminho_zip}' não foi encontrado. Verifique o caminho.")
        return False
    try:
        with zipfile.ZipFile(caminho_zip, 'r') as zip_object:
            zip_object.extractall(destino)
        print("Arquivo extraído com sucesso!")
        return True
    except zipfile.BadZipFile:
        print("Erro: O arquivo ZIP está corrompido.")
        return False


# Função para listar arquivos em um diretório
def listar_arquivos(diretorio):
    """Lista arquivos em um diretório se ele existir."""
    if os.path.exists(diretorio):
        arquivos = os.listdir(diretorio)
        print("Arquivos na pasta:", arquivos)
        return arquivos
    else:
        print(f"Erro: O diretório '{diretorio}' não foi encontrado. Verifique o caminho.")
        return []


# Função para exibir imagem no PyCharm (Matplotlib)
def exibir_imagem(imagem):
    """Exibe a imagem corretamente dentro do PyCharm."""
    imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)  # Converte BGR → RGB
    plt.imshow(imagem_rgb)
    plt.axis("off")  # Remove os eixos
    plt.show()


# Função para detectar e exibir rostos e pontos faciais
def detectar_face(caminho_imagem, caminho_modelo):
    """Carrega a imagem, detecta rostos e exibe os pontos faciais."""
    if not os.path.exists(caminho_imagem):
        print(f"Erro: A imagem '{caminho_imagem}' não foi encontrada.")
        return

    if not os.path.exists(caminho_modelo):
        print(f"Erro: O modelo '{caminho_modelo}' não foi encontrado.")
        return

    # Carregar a imagem
    imagem = cv2.imread(caminho_imagem)
    if imagem is None:
        print(f"Erro ao carregar a imagem '{caminho_imagem}'. Verifique o formato.")
        return

    # Inicializar detectores
    detector_face = dlib.get_frontal_face_detector()
    detector_pontos = dlib.shape_predictor(caminho_modelo)

    # Detectar rostos
    deteccoes = detector_face(imagem, 1)

    if not deteccoes:
        print("Nenhum rosto detectado.")
        return

    for face in deteccoes:
        pontos = detector_pontos(imagem, face)

        # Desenhar pontos faciais
        for ponto in pontos.parts():
            cv2.circle(imagem, (ponto.x, ponto.y), 2, (0, 255, 0), 1)

        print(f"Quantidade de pontos faciais detectados: {len(pontos.parts())}")

        # Desenhar o retângulo no rosto
        l, t, r, b = face.left(), face.top(), face.right(), face.bottom()
        cv2.rectangle(imagem, (l, t), (r, b), (255, 255, 0), 2)

    # Exibir a imagem usando Matplotlib (melhor para PyCharm)
    exibir_imagem(imagem)


# Definição de caminhos
caminho_zip = r"D:\mat_curso\Datasets\yalefaces.zip"
caminho_pasta = os.path.join(
    r"D:\mat_curso\Datasets",
    "yalefaces", "train")
caminho_imagem = r"D:\mat_curso\Images\people2b.jpg"
caminho_modelo = r"D:\mat_curso\Weights\shape_predictor_68_face_landmarks.dat"

# Executar as funções
if extrair_zip(caminho_zip):
    listar_arquivos(caminho_pasta)
    detectar_face(caminho_imagem, caminho_modelo)
