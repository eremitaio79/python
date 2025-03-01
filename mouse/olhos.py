import cv2
import dlib
import pyautogui
import numpy as np
from scipy.spatial import distance as dist

# Carregando o detector de faces do dlib e o preditor de pontos faciais
detector_face = dlib.get_frontal_face_detector()
predictor_face = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


# Função para calcular a razão de aspecto dos olhos
def calcular_ear(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear


# Definindo o limiar para detectar o piscar de olhos
LIMITE_EAR = 0.25
CONSECUTIVE_FRAMES = 20

# Inicializando a captura de vídeo
cap = cv2.VideoCapture(0)

# Inicializando as variáveis do controle do mouse
piscar_contador = 0
screen_width, screen_height = pyautogui.size()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertendo a imagem para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectando faces no vídeo
    faces = detector_face(gray)

    for face in faces:
        # Detectando os pontos faciais
        shape = predictor_face(gray, face)
        pontos_olho_esquerdo = np.array([(shape.part(i).x, shape.part(i).y) for i in range(36, 42)])
        pontos_olho_direito = np.array([(shape.part(i).x, shape.part(i).y) for i in range(42, 48)])

        # Calculando o EAR para ambos os olhos
        ear_esquerdo = calcular_ear(pontos_olho_esquerdo)
        ear_direito = calcular_ear(pontos_olho_direito)

        # Média do EAR dos dois olhos
        ear = (ear_esquerdo + ear_direito) / 2.0

        # Desenhando os pontos faciais e os olhos na tela
        for (x, y) in pontos_olho_esquerdo:
            cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
        for (x, y) in pontos_olho_direito:
            cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

        # Verificando se o olho está piscando
        if ear < LIMITE_EAR:
            piscar_contador += 1
            if piscar_contador >= CONSECUTIVE_FRAMES:
                print("Piscar detectado - Clicando!")
                pyautogui.click()  # Simula o clique do mouse
        else:
            piscar_contador = 0

        # Movendo o mouse com o movimento dos olhos (baseado no centro dos olhos)
        olho_esquerdo_centro = np.mean(pontos_olho_esquerdo, axis=0).astype("int")
        olho_direito_centro = np.mean(pontos_olho_direito, axis=0).astype("int")

        # Média entre os centros dos dois olhos
        centro_olhos = np.mean([olho_esquerdo_centro, olho_direito_centro], axis=0)

        # Normalizando a posição do mouse na tela
        x_screen = np.interp(centro_olhos[0], [0, frame.shape[1]], [0, screen_width])
        y_screen = np.interp(centro_olhos[1], [0, frame.shape[0]], [0, screen_height])

        # Movendo o mouse
        pyautogui.moveTo(x_screen, y_screen)

    # Exibindo o vídeo
    cv2.imshow("Eye Tracking - Mover Mouse e Clicar", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
