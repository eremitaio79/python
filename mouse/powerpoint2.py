import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time  # Para controlar o tempo entre os eventos

# Inicializando o MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Configurações da tela
screen_w, screen_h = pyautogui.size()

# Intervalo mínimo entre os slides (em segundos)
slide_interval = 1.0  # Tempo mínimo entre as mudanças de slide
last_slide_time = time.time()  # Última vez que o slide foi alterado

# Inicializando o detector de mãos
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    cap = cv2.VideoCapture(0)

    # Variáveis para controle do movimento anterior da mão
    prev_x = None
    prev_y = None

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

                # Obter o ponto de referência da palma da mão (centro)
                palm_x = hand_landmarks.landmark[0].x  # Ponto da palma da mão (base)
                palm_y = hand_landmarks.landmark[0].y  # Ponto da palma da mão (base)

                # Converter coordenadas para a tela
                x = int(palm_x * screen_w)
                y = int(palm_y * screen_h)

                # Detecta o movimento da mão horizontal (para a esquerda ou direita)
                if prev_x is not None:
                    diff_x = x - prev_x  # Diferença no movimento horizontal

                    # Se o movimento foi para a direita e o tempo de espera for suficiente
                    if diff_x > 50 and (time.time() - last_slide_time) > slide_interval:
                        pyautogui.press('right')  # Avançar slide
                        last_slide_time = time.time()  # Atualiza o tempo da última mudança
                        print("Avançando slide para a direita")

                    # Se o movimento foi para a esquerda e o tempo de espera for suficiente
                    elif diff_x < -50 and (time.time() - last_slide_time) > slide_interval:
                        pyautogui.press('left')  # Voltar slide
                        last_slide_time = time.time()  # Atualiza o tempo da última mudança
                        print("Voltando slide para a esquerda")

                # Atualiza a posição anterior
                prev_x = x
                prev_y = y

        # Mostrar a imagem na tela
        cv2.imshow('Hand Tracking - PowerPoint Control', frame)

        # Fechar a janela pressionando 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
