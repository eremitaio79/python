import cv2
import mediapipe as mp
import math

# Inicializando o MediaPipe para rastreamento de pose e mãos
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

pose = mp_pose.Pose()
hands = mp_hands.Hands()


# Função para calcular o ângulo entre três pontos
def calcular_angulo(p1, p2, p3):
    # Calculando os vetores
    v1 = (p1.x - p2.x, p1.y - p2.y)
    v2 = (p3.x - p2.x, p3.y - p2.y)

    # Produto escalar
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]

    # Magnitudes dos vetores
    mag_v1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
    mag_v2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)

    # Cálculo do ângulo em radianos
    cos_angle = dot_product / (mag_v1 * mag_v2)
    angle_rad = math.acos(cos_angle)

    # Convertendo para graus
    angle_deg = math.degrees(angle_rad)

    return angle_deg


# Função para desenhar o arco de um ângulo
def desenhar_arco(frame, p1, p2, p3, angulo):
    # Convertendo as coordenadas para o tamanho da imagem
    center = (int(p2.x * frame.shape[1]), int(p2.y * frame.shape[0]))

    # Definindo os raios dos arcos
    raio_interno = int(0.05 * frame.shape[0])
    raio_externo = int(0.1 * frame.shape[0])

    # Desenhando o arco (utilizando o ângulo em radianos)
    cv2.ellipse(frame, center, (raio_interno, raio_externo), 0, 0, angulo, (255, 0, 0), 2)


# Inicializando a câmera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertendo a imagem para RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processando a imagem para obter a pose
    resultados_pose = pose.process(frame_rgb)
    resultados_manos = hands.process(frame_rgb)

    # Desenhando as landmarks e conexões do corpo
    if resultados_pose.pose_landmarks:
        mp_drawing.draw_landmarks(frame, resultados_pose.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Coletando os pontos-chave da pose
        landmarks = resultados_pose.pose_landmarks.landmark

        # Exemplo de ângulo no braço (elbow): entre o ombro, cotovelo e pulso
        angulo_cotovelo = calcular_angulo(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER],
                                          landmarks[mp_pose.PoseLandmark.LEFT_ELBOW],
                                          landmarks[mp_pose.PoseLandmark.LEFT_WRIST])

        print(f"Ângulo no cotovelo esquerdo: {angulo_cotovelo:.2f}°")

        cotovelo_coords = (int(landmarks[mp_pose.PoseLandmark.LEFT_ELBOW].x * frame.shape[1]),
                           int(landmarks[mp_pose.PoseLandmark.LEFT_ELBOW].y * frame.shape[0]))

        cv2.putText(frame, f"{angulo_cotovelo:.2f}°", cotovelo_coords, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        desenhar_arco(frame, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER],
                      landmarks[mp_pose.PoseLandmark.LEFT_ELBOW],
                      landmarks[mp_pose.PoseLandmark.LEFT_WRIST], angulo_cotovelo)

        angulo_joelho = calcular_angulo(landmarks[mp_pose.PoseLandmark.LEFT_HIP],
                                        landmarks[mp_pose.PoseLandmark.LEFT_KNEE],
                                        landmarks[mp_pose.PoseLandmark.LEFT_ANKLE])

        print(f"Ângulo no joelho esquerdo: {angulo_joelho:.2f}°")

        joelho_coords = (int(landmarks[mp_pose.PoseLandmark.LEFT_KNEE].x * frame.shape[1]),
                         int(landmarks[mp_pose.PoseLandmark.LEFT_KNEE].y * frame.shape[0]))

        cv2.putText(frame, f"{angulo_joelho:.2f}°", joelho_coords, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        desenhar_arco(frame, landmarks[mp_pose.PoseLandmark.LEFT_HIP],
                      landmarks[mp_pose.PoseLandmark.LEFT_KNEE],
                      landmarks[mp_pose.PoseLandmark.LEFT_ANKLE], angulo_joelho)

    if resultados_manos.multi_hand_landmarks:
        for hand_landmarks in resultados_manos.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('Body and Hand Tracking with Angles', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
