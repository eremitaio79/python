import cv2
import mediapipe as mp
import pyautogui
import time

# Inicializa o Mediapipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Captura de vídeo
cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()  # Obtém o tamanho da tela
dragging = False  # Flag para controle do Drag and Drop
last_click_time = 0  # Guarda o tempo do último clique
last_right_click_time = 0  # Guarda o tempo do último clique direito

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Espelha a imagem para uma interação mais natural
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Converte para RGB (necessário para o Mediapipe)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processa a imagem e detecta as mãos
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Pega a ponta do indicador
            index_tip = hand_landmarks.landmark[8]
            x, y = int(index_tip.x * w), int(index_tip.y * h)

            # Exibe as coordenadas da ponta do indicador no terminal
            print(f"Coordenadas do Indicador (x, y): ({x}, {y})")

            # Move o mouse com base no dedo indicador
            pyautogui.moveTo(index_tip.x * screen_w, index_tip.y * screen_h)

            # Pega a ponta do polegar e do dedo médio
            thumb_tip = hand_landmarks.landmark[4]
            middle_tip = hand_landmarks.landmark[12]

            # Exibe as coordenadas do polegar e dedo médio no terminal
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            middle_x, middle_y = int(middle_tip.x * w), int(middle_tip.y * h)
            print(f"Coordenadas do Polegar (x, y): ({thumb_x}, {thumb_y})")
            print(f"Coordenadas do Dedo Médio (x, y): ({middle_x}, {middle_y})")

            # Verifica a distância entre polegar, indicador e dedo médio
            distance_thumb_index = abs(thumb_tip.x - index_tip.x) + abs(thumb_tip.y - index_tip.y)
            distance_index_middle = abs(index_tip.x - middle_tip.x) + abs(index_tip.y - middle_tip.y)

            # Se a distância entre polegar, indicador e dedo médio for pequena, faz o clique direito
            if distance_thumb_index < 0.05 and distance_index_middle < 0.05:  # Ajuste a distância conforme necessário
                current_time = time.time()
                if current_time - last_right_click_time > 1:  # Evita cliques rápidos
                    pyautogui.rightClick()  # Clica com o botão direito
                    last_right_click_time = current_time  # Atualiza o tempo do último clique direito

            # Verifica a distância entre polegar e indicador para clique
            distance = abs(thumb_tip.x - index_tip.x) + abs(thumb_tip.y - index_tip.y)

            # Se a distância entre polegar e indicador for pequena, faz clique ou duplo clique
            if distance < 0.03:
                current_time = time.time()
                if current_time - last_click_time < 0.3:  # Se o segundo clique for rápido, faz duplo clique
                    pyautogui.doubleClick()
                else:
                    pyautogui.click()
                last_click_time = current_time

            fingers_up = [hand_landmarks.landmark[i].y < hand_landmarks.landmark[i - 2].y for i in [8, 12, 16, 20]]

            if all(fingers_up):
                if not dragging:
                    pyautogui.mouseDown()
                    dragging = True
            else:
                if dragging:
                    pyautogui.mouseUp()
                    dragging = False

    cv2.imshow("Tracking do mouse com as mãos", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
