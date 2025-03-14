import dlib
import os
import numpy as np
import cv2
from PIL import Image

detector_face = dlib.get_frontal_face_detector()
detector_pontos = dlib.shape_predictor(r"D:\mat_curso\Weights\shape_predictor_68_face_landmarks.dat")
descritor_facial_extrator = dlib.face_recognition_model_v1(r"D:\mat_curso\Weights\dlib_face_recognition_resnet_model_v1.dat")

index = {}
idx = 0
descritores_faciais = None

paths = [os.path.join(r"D:\mat_curso\Datasets\yalefaces\train", f) for f in os.listdir(r"D:\mat_curso\Datasets\yalefaces\train")]
for path in paths:
    print(path) # Percorre todas as imagens de treinamento.
    imagem = Image.open(path).convert('RGB')
    imagem_np = np.array(imagem, 'uint8')
    deteccoes = detector_face(imagem_np, 1)
    for face in deteccoes:
        l, t, r, b = face.left(), face.top(), face.right(), face.bottom()
        cv2.rectangle(imagem_np, (l, t), (r, b), (0, 0, 255), 2)

        pontos = detector_pontos(imagem_np, face)
        for ponto in pontos.parts():
            cv2.circle(imagem_np, (ponto.x, ponto.y), 2, (0, 255, 0), 1)

        descritor_facial = descritor_facial_extrator.compute_face_descriptor(imagem_np, pontos)

        # print(type(descritor_facial))
        # print(len(descritor_facial))
        # print(descritor_facial)
        descritor_facial = [f for f in descritor_facial]
        # print(descritor_facial)
        descritor_facial = np.asarray(descritor_facial, dtype=np.float64)
        print(descritor_facial)
        print(descritor_facial.shape)

    # Exibir a imagem (usando cv2 imshow, já que cv2_imshow não está disponível fora do Colab)
    # cv2.imshow("Imagem", imagem_np)
    if cv2.waitKey(0) & 0xFF == ord('q'):  # Pressionar 'q' para fechar a janela.
        break

    cv2.destroyAllWindows()




# # Carregar o detector de rosto e o preditor de pontos faciais
# detector_face = dlib.get_frontal_face_detector()
# detector_pontos = dlib.shape_predictor(r"D:\mat_curso\Weights\shape_predictor_68_face_landmarks.dat")
# descritor_facial_extrator = dlib.face_recognition_model_v1(r"D:\mat_curso\Weights\dlib_face_recognition_resnet_model_v1.dat")
#
# # Dicionário para armazenar descritores faciais
# index = {}
# idx = 0
# descritores_faciais = None
#
# # Caminho local para as imagens
# paths = [os.path.join(r"D:\mat_curso\Datasets\yalefaces\train", f) for f in os.listdir(r"D:\mat_curso\Datasets\yalefaces\train")]
#
# # Processar as imagens
# for path in paths:
#     print(path)
#     imagem = Image.open(path).convert('RGB')  # Converte para RGB
#     imagem_np = np.array(imagem, 'uint8')
#
#     # Detecta rostos na imagem
#     deteccoes = detector_face(imagem_np, 1)  # Escala 1 para o detector de rostos
#     for face in deteccoes:
#         l, t, r, b = face.left(), face.top(), face.right(), face.bottom()
#         cv2.rectangle(imagem_np, (l, t), (r, b), (0, 0, 255), 2)  # Desenha um retângulo no rosto
#
#         # Detecta pontos faciais
#         pontos_faciais = detector_pontos(imagem_np, face)
#         for ponto in pontos_faciais.parts():
#             cv2.circle(imagem_np, (ponto.x, ponto.y), 2, (0, 255, 0), 1)  # Marca os pontos
#
#         # Extrai o descritor facial
#         descritor_facial = descritor_facial_extrator.compute_face_descriptor(imagem_np, pontos_faciais)
#         print(descritor_facial)
#
#     # Exibir a imagem (usando cv2 imshow, já que cv2_imshow não está disponível fora do Colab)
#     cv2.imshow("Imagem", imagem_np)
#     if cv2.waitKey(0) & 0xFF == ord('q'):  # Espera o usuário pressionar 'q' para fechar a janela
#         break
#
# cv2.destroyAllWindows()
