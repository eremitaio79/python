import cv2
import mediapipe as mp
import pyautogui

# Inicializa o Mediapipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Captura de vídeo
cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()  # Obtém o tamanho da tela

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

            # Se a distância entre os dedos for pequena, executa um clique
            if abs(thumb_tip.x - index_tip.x) < 0.03 and abs(thumb_tip.y - index_tip.y) < 0.03:
                pyautogui.click()

    # Exibe o vídeo com as detecções
    cv2.imshow("Hand Tracking Mouse", frame)

    # Fecha ao pressionar "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
