import cv2
import mediapipe as mp
import pyautogui
import time

# Inicializa o Mediapipe para Face e Hands
mp_face_mesh = mp.solutions.face_mesh
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Inicia os detectores do Mediapipe
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.7, min_tracking_confidence=0.7)
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Captura de vídeo
cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()  # Dimensões da tela

last_click_time = 0  # Controle de tempo para evitar cliques múltiplos
last_right_click_time = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Espelha a imagem
    h, w, _ = frame.shape  # Obtém dimensões da imagem

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Converte para RGB

    # Processa a detecção de face
    face_results = face_mesh.process(rgb_frame)
    # Processa a detecção de mãos
    hand_results = hands.process(rgb_frame)

    # Mover o mouse com a cabeça
    if face_results.multi_face_landmarks:
        for face_landmarks in face_results.multi_face_landmarks:
            # Desenha a malha facial
            mp_draw.draw_landmarks(frame, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION,
                                   mp_draw.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                                   mp_draw.DrawingSpec(color=(0, 255, 0), thickness=1))

            # Usa o landmark do nariz (0, 1 ou 4 podem ser usados)
            nose = face_landmarks.landmark[1]  # 1 é geralmente o centro do nariz
            x, y = int(nose.x * w), int(nose.y * h)

            # Exibe um ponto vermelho no nariz
            cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)

            # Move o cursor suavemente com um fator de escala
            pyautogui.moveTo(nose.x * screen_w, nose.y * screen_h, duration=0.05)
    else:
        print("⚠️ Nenhuma face detectada!")

    # Clique com a mão
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Obtém a ponta do polegar e do indicador
            thumb_tip = hand_landmarks.landmark[4]
            index_tip = hand_landmarks.landmark[8]
            middle_tip = hand_landmarks.landmark[12]

            # Calcula distâncias entre os dedos
            distance_thumb_index = abs(thumb_tip.x - index_tip.x) + abs(thumb_tip.y - index_tip.y)
            distance_index_middle = abs(index_tip.x - middle_tip.x) + abs(index_tip.y - middle_tip.y)

            # Clique Esquerdo - Polegar e Indicador Juntos
            if distance_thumb_index < 0.03:
                current_time = time.time()
                if current_time - last_click_time > 0.3:
                    pyautogui.click()
                    print("🖱️ Clique esquerdo")
                    last_click_time = current_time

            # Clique Direito - Polegar, Indicador e Médio Juntos
            if distance_thumb_index < 0.04 and distance_index_middle < 0.04:
                current_time = time.time()
                if current_time - last_right_click_time > 1:
                    pyautogui.rightClick()
                    print("🖱️ Clique direito")
                    last_right_click_time = current_time

    # Exibe a imagem com as marcações
    cv2.imshow("Controle com Cabeça e Mãos", frame)

    # Fecha com "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
