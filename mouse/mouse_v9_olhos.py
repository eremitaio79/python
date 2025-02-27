import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# Inicializa os módulos do Mediapipe
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Captura de vídeo
cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

# Configuração de detecção de piscada
EYE_AR_THRESH = 0.2  # Limiar para considerar o olho fechado
EYE_AR_CONSEC_FRAMES = 3  # Número mínimo de frames para acionar o clique
eye_closed_frames = 0  # Contador de frames com olhos fechados

# Tempo para evitar cliques consecutivos
last_click_time = 0
last_right_click_time = 0
last_double_click_time = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Espelha a imagem para facilitar a interação
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Converte para RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processa a imagem para detectar a malha facial
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Pegando os pontos dos olhos
            left_eye = [face_landmarks.landmark[i] for i in [33, 160, 158, 133, 153, 144]]
            right_eye = [face_landmarks.landmark[i] for i in [362, 385, 387, 263, 373, 380]]

            # Pegando a posição do nariz como referência
            nose = face_landmarks.landmark[1]

            # Converte para coordenadas de tela
            left_eye_pts = np.array([(int(p.x * w), int(p.y * h)) for p in left_eye])
            right_eye_pts = np.array([(int(p.x * w), int(p.y * h)) for p in right_eye])

            # Calcula a relação de aspecto do olho (EAR)
            def eye_aspect_ratio(eye):
                A = np.linalg.norm(eye[1] - eye[5])
                B = np.linalg.norm(eye[2] - eye[4])
                C = np.linalg.norm(eye[0] - eye[3])
                return (A + B) / (2.0 * C)

            ear_left = eye_aspect_ratio(left_eye_pts)
            ear_right = eye_aspect_ratio(right_eye_pts)
            ear_avg = (ear_left + ear_right) / 2.0

            # Verifica se os olhos estão fechados
            if ear_avg < EYE_AR_THRESH:
                eye_closed_frames += 1
            else:
                if eye_closed_frames >= EYE_AR_CONSEC_FRAMES:
                    current_time = time.time()
                    if current_time - last_click_time > 0.5:  # Evita múltiplos cliques
                        pyautogui.click()
                        last_click_time = current_time
                eye_closed_frames = 0  # Reseta o contador

            # Captura o movimento do nariz (referência para olhar para os lados)
            nose_x = nose.x * w

            # Se o nariz estiver muito à esquerda, faz duplo clique
            if nose_x < w * 0.4:
                current_time = time.time()
                if current_time - last_double_click_time > 1:  # Evita cliques seguidos
                    pyautogui.doubleClick()
                    last_double_click_time = current_time

            # Se o nariz estiver muito à direita, faz clique direito
            elif nose_x > w * 0.6:
                current_time = time.time()
                if current_time - last_right_click_time > 1:  # Evita cliques seguidos
                    pyautogui.rightClick()
                    last_right_click_time = current_time

    # Exibe a imagem
    cv2.imshow("Controle de Mouse com os Olhos", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
