import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Inicializando o MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Configurações da tela
screen_w, screen_h = pyautogui.size()

# Inicializando o detector de mãos
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        # Converter a imagem para RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_rgb)

        # Desenhar as landmarks na mão, se houver
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Obter os pontos da mão
                thumb_tip = hand_landmarks.landmark[4]  # Ponta do polegar
                index_tip = hand_landmarks.landmark[8]  # Ponta do indicador

                # Coordenadas do indicador
                x = int(index_tip.x * screen_w)
                y = int(index_tip.y * screen_h)

                # Calcular a diferença entre a posição do polegar e do indicador
                thumb_x = int(thumb_tip.x * screen_w)
                thumb_y = int(thumb_tip.y * screen_h)

                # Distância entre polegar e indicador
                dist_x = abs(x - thumb_x)
                dist_y = abs(y - thumb_y)

                # Detectar o gesto de apontar para a direita (indicador à direita do polegar)
                if dist_x > 50 and x > thumb_x:  # Apontar para a direita
                    pyautogui.press('right')  # Avançar slide
                    print("Avançando slide para a direita")

                # Detectar o gesto de apontar para a esquerda (indicador à esquerda do polegar)
                elif dist_x > 50 and x < thumb_x:  # Apontar para a esquerda
                    pyautogui.press('left')  # Voltar slide
                    print("Voltando slide para a esquerda")

        # Mostrar a imagem na tela
        cv2.imshow('Hand Tracking - PowerPoint Control', frame)

        # Fechar a janela pressionando 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

