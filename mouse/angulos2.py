import cv2
import mediapipe as mp
import math


# Função para calcular o ângulo entre três pontos
def calcular_angulo(p1, p2, p3):
    # Vetores p1 -> p2 e p2 -> p3
    vetor1 = [p1[0] - p2[0], p1[1] - p2[1]]
    vetor2 = [p3[0] - p2[0], p3[1] - p2[1]]

    # Produto escalar
    produto_escalar = vetor1[0] * vetor2[0] + vetor1[1] * vetor2[1]

    # Magnitudes
    mag_vetor1 = math.sqrt(vetor1[0] ** 2 + vetor1[1] ** 2)
    mag_vetor2 = math.sqrt(vetor2[0] ** 2 + vetor2[1] ** 2)

    # Cálculo do ângulo
    cos_angulo = produto_escalar / (mag_vetor1 * mag_vetor2)
    angulo = math.acos(cos_angulo)
    return math.degrees(angulo)  # Convertendo de radianos para graus


# Inicializando o MediaPipe e a câmera
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertendo a imagem para RGB e detectando as mãos
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = hands.process(frame_rgb)

    if resultados.multi_hand_landmarks:
        for landmarks in resultados.multi_hand_landmarks:
            # Coordenadas das articulações para calcular os ângulos dos dedos (exemplo com polegar e indicador)
            thumb_angle = calcular_angulo(
                [landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x,
                 landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y],
                [landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x,
                 landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y],
                [landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x,
                 landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y]
            )

            index_angle = calcular_angulo(
                [landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x,
                 landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y],
                [landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x,
                 landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y],
                [landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x,
                 landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y]
            )

            # Exibir os ângulos na tela
            cv2.putText(frame, f'Polegar: {thumb_angle:.2f}°', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, f'Indicador: {index_angle:.2f}°', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Desenhando as landmarks da mão
            mp.solutions.drawing_utils.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

    # Mostrar o frame com os ângulos
    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
