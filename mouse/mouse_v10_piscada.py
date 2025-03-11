import cv2
import mediapipe as mp
import pyautogui
import time

# Inicializa os módulos do Mediapipe
mp_hands = mp.solutions.hands
mp_face_mesh = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils

# Configuração do Mediapipe para detecção
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Captura de vídeo
cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

# Variáveis para detecção de piscadas
blink_counter = 0
last_blink_time = 0
blink_threshold = 0.2  # Tempo máximo entre piscadas para contar como duplo clique

# Índices dos olhos no FaceMesh
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]


def eye_aspect_ratio(eye_points, landmarks):
    """Calcula a razão de aspecto do olho para detectar piscadas"""
    left = landmarks[eye_points[0]]
    right = landmarks[eye_points[3]]
    top = (landmarks[eye_points[1]], landmarks[eye_points[2]])
    bottom = (landmarks[eye_points[4]], landmarks[eye_points[5]])

    # Distâncias euclidianas
    horizontal_dist = ((left[0] - right[0]) ** 2 + (left[1] - right[1]) ** 2) ** 0.5
    vertical_dist = (((top[0][0] - bottom[0][0]) ** 2 + (top[0][1] - bottom[0][1]) ** 2) ** 0.5 +
                     ((top[1][0] - bottom[1][0]) ** 2 + (top[1][1] - bottom[1][1]) ** 2) ** 0.5) / 2

    return vertical_dist / horizontal_dist  # Quanto menor, mais fechado está o olho


while cap.isOpened():
    ret, frame = cap.read()
    if not ret or frame is None:
        continue

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processa as detecções
    hand_results = hands.process(rgb_frame)
    face_results = face_mesh.process(rgb_frame)

    # Detecta mão e controla o mouse
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Obtém a ponta do indicador
            index_tip = hand_landmarks.landmark[8]

            # Move o cursor para a posição do dedo
            cursor_x = int(index_tip.x * screen_w)
            cursor_y = int(index_tip.y * screen_h)
            pyautogui.moveTo(cursor_x, cursor_y)

    # Detecta piscadas para cliques
    if face_results.multi_face_landmarks:
        for face_landmarks in face_results.multi_face_landmarks:
            landmarks = [(int(pt.x * w), int(pt.y * h)) for pt in face_landmarks.landmark]

            left_eye_ratio = eye_aspect_ratio(LEFT_EYE, landmarks)
            right_eye_ratio = eye_aspect_ratio(RIGHT_EYE, landmarks)

            # Detecta piscada (olhos fechados)
            if left_eye_ratio < 0.2 and right_eye_ratio < 0.2:
                current_time = time.time()

                if current_time - last_blink_time > 0.5:  # Evita contagem excessiva
                    blink_counter += 1
                    last_blink_time = current_time

                # Clique esquerdo com 1 piscada
                if blink_counter == 1:
                    pyautogui.click()
                    print("Clique esquerdo")

                # Clique direito com 2 piscadas rápidas
                if blink_counter == 2 and (current_time - last_blink_time) < blink_threshold:
                    pyautogui.rightClick()
                    print("Clique direito")
                    blink_counter = 0  # Reseta contagem

            else:
                if time.time() - last_blink_time > blink_threshold:
                    blink_counter = 0  # Reseta se demorar muito entre piscadas

    cv2.imshow("Controle por Mão e Piscadas", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
