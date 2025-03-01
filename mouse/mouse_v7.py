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
screen_w, screen_h = pyautogui.size()
dragging = False
last_click_time = 0
last_right_click_time = 0

# Verifica se a câmera abriu corretamente
if not cap.isOpened():
    print("Erro: Não foi possível acessar a câmera.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret or frame is None:
        print("Erro ao capturar o frame.")
        continue

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Obtém a ponta do indicador, polegar e dedo médio
            index_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]
            middle_tip = hand_landmarks.landmark[12]

            # Converte para coordenadas da tela
            x, y = int(index_tip.x * w), int(index_tip.y * h)
            pyautogui.moveTo(index_tip.x * screen_w, index_tip.y * screen_h)

            # Exibe coordenadas para depuração
            print(f"Indicador: ({x}, {y}) | Polegar: ({thumb_tip.x}, {thumb_tip.y}) | Médio: ({middle_tip.x}, {middle_tip.y})")

            # Calcula distâncias
            distance_thumb_index = abs(thumb_tip.x - index_tip.x) + abs(thumb_tip.y - index_tip.y)
            distance_index_middle = abs(index_tip.x - middle_tip.x) + abs(index_tip.y - middle_tip.y)

            # Clique esquerdo e duplo clique
            if distance_thumb_index < 0.04:
                current_time = time.time()
                if current_time - last_click_time < 0.3:
                    pyautogui.doubleClick()
                else:
                    pyautogui.click()
                last_click_time = current_time

            # Clique direito
            if distance_thumb_index < 0.05 and distance_index_middle < 0.05:
                current_time = time.time()
                if current_time - last_right_click_time > 1:
                    pyautogui.rightClick()
                    last_right_click_time = current_time

            # Drag and Drop
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

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
