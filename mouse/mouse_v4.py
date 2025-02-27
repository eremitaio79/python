import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Inicializando o MediaPipe e o PyAutoGUI
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Configurações da tela
screen_w, screen_h = pyautogui.size()

# Variáveis para suavização do movimento
last_x, last_y = 0, 0
positions_x, positions_y = [], []


# Função para suavizar o movimento do mouse (Smoothening)
def smooth_move(x, y, alpha=0.2):
    global last_x, last_y
    smoothed_x = last_x + alpha * (x - last_x)
    smoothed_y = last_y + alpha * (y - last_y)
    last_x, last_y = smoothed_x, smoothed_y
    return smoothed_x, smoothed_y


# Função para limitar a distância do movimento
def limit_movement(x, y, max_distance=50):
    delta_x = x - last_x
    delta_y = y - last_y
    distance = (delta_x ** 2 + delta_y ** 2) ** 0.5
    if distance > max_distance:
        ratio = max_distance / distance
        x = last_x + delta_x * ratio
        y = last_y + delta_y * ratio
    return x, y


# Função para aplicar filtro de suavização com média
def apply_smoothing_filter(x, y, window_size=5):
    global positions_x, positions_y
    positions_x.append(x)
    positions_y.append(y)

    if len(positions_x) > window_size:
        positions_x.pop(0)
        positions_y.pop(0)

    smoothed_x = sum(positions_x) / len(positions_x)
    smoothed_y = sum(positions_y) / len(positions_y)

    return smoothed_x, smoothed_y


# Função para limitar a velocidade do movimento
def limit_mouse_speed(x, y, max_speed=20):
    delta_x = x - last_x
    delta_y = y - last_y
    distance = (delta_x ** 2 + delta_y ** 2) ** 0.5
    if distance > max_speed:
        ratio = max_speed / distance
        x = last_x + delta_x * ratio
        y = last_y + delta_y * ratio
    return x, y


# Função para verificar se o movimento é significativo o suficiente
def min_move_distance(x, y, min_distance=5):
    delta_x = abs(x - last_x)
    delta_y = abs(y - last_y)
    if delta_x > min_distance or delta_y > min_distance:
        return True
    return False


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

                # Coordenadas da tela
                x = int(index_tip.x * screen_w)
                y = int(index_tip.y * screen_h)

                # Suavizar o movimento do mouse
                smoothed_x, smoothed_y = smooth_move(x, y)

                # Limitar o movimento do mouse
                limited_x, limited_y = limit_movement(smoothed_x, smoothed_y)

                # Aplicar o filtro de suavização com média
                smoothed_x, smoothed_y = apply_smoothing_filter(limited_x, limited_y)

                # Limitar a velocidade do movimento
                speed_limited_x, speed_limited_y = limit_mouse_speed(smoothed_x, smoothed_y)

                # Verificar se o movimento é grande o suficiente
                if min_move_distance(speed_limited_x, speed_limited_y):
                    pyautogui.moveTo(speed_limited_x, speed_limited_y)

                # Detectar o gesto de "clicar" (polegar e indicador próximos)
                if abs(thumb_tip.x - index_tip.x) < 0.03 and abs(thumb_tip.y - index_tip.y) < 0.03:
                    pyautogui.click()

                # Detectar o gesto de "duplo clique" (polegar e indicador se tocando duas vezes)
                if abs(thumb_tip.x - index_tip.x) < 0.03 and abs(thumb_tip.y - index_tip.y) < 0.03:
                    pyautogui.doubleClick()

        # Mostrar a imagem na tela
        cv2.imshow('Hand Tracking - Mouse Control', frame)

        # Fechar a janela pressionando 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
