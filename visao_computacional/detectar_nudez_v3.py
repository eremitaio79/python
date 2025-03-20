from nudenet import NudeDetector
import cv2

# Criando o detector
detector = NudeDetector()

# Inicializa a webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro ao abrir a webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar frame")
        break

    # Converte para RGB para a NudeNet
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Tenta detectar nudez
    try:
        detections = detector.detect(frame_rgb)
    except Exception as e:
        print("Erro na detecção:", e)
        detections = []

    # Filtrar apenas partes íntimas (opcional)
    print("Detecções:", detections)

    if detections:
        message = "Nudez detectada"
        color = (0, 0, 255)  # Vermelho
    else:
        message = "Nenhuma nudez detectada"
        color = (0, 255, 0)  # Verde

    # Percorre as detecções e desenha retângulos vermelhos borrados
    for detection in detections:
        x1, y1, x2, y2 = map(int, detection["box"])
        label = detection.get("class", "Desconhecido")  # Parte do corpo detectada

        # Verifica se as coordenadas são válidas
        if x2 > x1 and y2 > y1:
            roi = frame[y1:y2, x1:x2]

            # Verifica se o ROI não está vazio antes de aplicar o blur
            if roi.size != 0:
                blurred_roi = cv2.GaussianBlur(roi, (99, 99), 30)
                frame[y1:y2, x1:x2] = blurred_roi

            # Desenha o retângulo vermelho
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

            # Exibe o nome da parte do corpo detectada
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

    # Exibe a mensagem na tela
    cv2.putText(frame, message, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)

    # Exibe a imagem com as detecções
    cv2.imshow("Webcam com NudeNet", frame)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
