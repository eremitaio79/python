import cv2
import mediapipe as mp
import pyautogui
import time

# Inicializa o MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Captura de vídeo
cap = cv2.VideoCapture(0)

# Dicionário de gestos para letras (Apenas exemplo, precisa treinar modelos para reconhecer cada gesto)
gestures_to_letters = {
    "thumbs_up": "A",
    "index_up": "B",
    "fist": "C",
}

# Controle de tempo entre digitação para evitar repetição
last_gesture_time = 0
gesture_cooldown = 1.0  # Tempo mínimo entre detecções (segundos)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Espelha a imagem
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Pegando posições dos dedos principais
            index_tip = hand_landmarks.landmark[8]  # Indicador
            thumb_tip = hand_landmarks.landmark[4]  # Polegar

            # Exemplo de detecção de gesto simples (ajuste conforme necessário)
            if thumb_tip.y < index_tip.y:  # Se o polegar estiver acima do indicador (exemplo)
                detected_gesture = "thumbs_up"
            else:
                detected_gesture = None

            # Verifica o tempo para evitar repetições
            current_time = time.time()
            if detected_gesture in gestures_to_letters and current_time - last_gesture_time > gesture_cooldown:
                last_gesture_time = current_time  # Atualiza o tempo da última detecção

                # Obtém a letra correspondente ao gesto
                letter = gestures_to_letters[detected_gesture]
                print(f"Letra detectada: {letter}")
                pyautogui.write(letter)  # Escreve a letra no Notepad

    cv2.imshow("Libras para Notepad", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
