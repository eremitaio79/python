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

            # Move o mouse com base no dedo indicador
            pyautogui.moveTo(index_tip.x * screen_w, index_tip.y * screen_h)

            # Pega a ponta do polegar
            thumb_tip = hand_landmarks.landmark[4]

            # Verifica a distância entre polegar e indicador para clique
            distance = abs(thumb_tip.x - index_tip.x) + abs(thumb_tip.y - index_tip.y)

            # Se a distância entre polegar e indicador for pequena, faz clique ou duplo clique
            if distance < 0.03:
                current_time = time.time()
                if current_time - last_click_time < 0.3:  # Se o segundo clique for rápido, faz duplo clique
                    pyautogui.doubleClick()
                else:
                    pyautogui.click()
                last_click_time = current_time  # Atualiza o tempo do clique

            # Verifica se todos os dedos estão levantados para ativar Drag and Drop
            fingers_up = [hand_landmarks.landmark[i].y < hand_landmarks.landmark[i - 2].y for i in [8, 12, 16, 20]]

            if all(fingers_up):  # Todos os dedos estão levantados
                if not dragging:
                    pyautogui.mouseDown()  # Pressiona o botão do mouse
                    dragging = True
            else:
                if dragging:
                    pyautogui.mouseUp()  # Solta o botão do mouse
                    dragging = False

            # Exibe as coordenadas dos dedos e o estado dos dedos na tela
            for i, finger_tip in enumerate([hand_landmarks.landmark[4], hand_landmarks.landmark[8],
                                             hand_landmarks.landmark[12], hand_landmarks.landmark[16],
                                             hand_landmarks.landmark[20]]):
                finger_x = int(finger_tip.x * w)
                finger_y = int(finger_tip.y * h)
                cv2.putText(frame, f"Finger {i+1}: ({finger_x}, {finger_y})",
                            (finger_x, finger_y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Adiciona o estado de cada dedo (levantado ou abaixado)
            for i, is_raised in enumerate(fingers_up):
                finger_status = "Up" if is_raised else "Down"
                cv2.putText(frame, f"Finger {i+1}: {finger_status}",
                            (50, 50 + i*30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # Exibe o vídeo com as detecções
    cv2.imshow("Hand Tracking Mouse", frame)

    # Fecha ao pressionar "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
