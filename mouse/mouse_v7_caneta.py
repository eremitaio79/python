import cv2
import numpy as np
import pyautogui

# Obtém o tamanho da tela
screen_w, screen_h = pyautogui.size()

# Captura de vídeo
cap = cv2.VideoCapture(0)

# Define o intervalo de cor da ponta da caneta (Ajuste conforme necessário)
lower_color = np.array([100, 150, 0])   # Azul (exemplo)
upper_color = np.array([140, 255, 255]) # Azul

# Suavização para evitar instabilidade
kernel = np.ones((5, 5), np.uint8)

# Inicializa última posição para suavizar o movimento
last_x, last_y = 0, 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Espelha a imagem
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Converte para HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Cria a máscara para detectar a cor da caneta
    mask = cv2.inRange(hsv, lower_color, upper_color)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Encontra contornos
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Pega o maior contorno (provavelmente a caneta)
        largest_contour = max(contours, key=cv2.contourArea)

        if cv2.contourArea(largest_contour) > 500:
            # Obtém a posição da caneta
            x, y, w_rect, h_rect = cv2.boundingRect(largest_contour)
            pen_x, pen_y = x + w_rect // 2, y + h_rect // 2

            # Suaviza o movimento
            smooth_x = int(0.7 * last_x + 0.3 * pen_x)
            smooth_y = int(0.7 * last_y + 0.3 * pen_y)

            last_x, last_y = smooth_x, smooth_y

            # Move o mouse
            pyautogui.moveTo(smooth_x * screen_w / w, smooth_y * screen_h / h, duration=0.05)

            # Exibe um ponto onde a caneta está detectada
            cv2.circle(frame, (pen_x, pen_y), 10, (0, 255, 0), -1)

    # Mostra a saída
    cv2.imshow("Controle do Mouse com Caneta", frame)

    # Pressione "q" para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
