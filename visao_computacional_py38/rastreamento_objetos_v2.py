import cv2
import random

# Lista para armazenar os rastreadores, bboxes e cores
rastreadores = []
bboxes = []
cores = []

# Carregar vídeo
video = cv2.VideoCapture('race.mp4')

# Ler o primeiro frame do vídeo
ok, frame = video.read()
if not ok or frame is None:
    print("Erro ao carregar o vídeo")
    exit()

# Criar uma janela para seleção de objetos
cv2.namedWindow("Selecione os objetos", cv2.WINDOW_NORMAL)

while True:
    # Criar uma cópia do frame para manter os retângulos anteriores visíveis
    frame_copy = frame.copy()

    # Desenhar os retângulos já selecionados
    for i, bbox in enumerate(bboxes):
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame_copy, (x, y), (x + w, y + h), cores[i], 2, 1)

    cv2.imshow("Selecione os objetos", frame_copy)

    # Pressione 'n' para adicionar um novo rastreador ou 'ENTER' para iniciar o vídeo
    key = cv2.waitKey(0) & 0xFF
    if key == 13:  # ENTER
        break
    elif key == ord('n'):  # Pressionar 'n' para adicionar um novo retângulo
        bbox = cv2.selectROI("Selecione os objetos", frame_copy, fromCenter=False, showCrosshair=True)

        # Se a seleção for vazia, ignorar
        if bbox == (0, 0, 0, 0):
            continue

        # Criar um novo rastreador
        rastreador = cv2.TrackerCSRT_create()
        rastreador.init(frame, bbox)

        # Adicionar à lista
        rastreadores.append(rastreador)
        bboxes.append(bbox)

        # Gerar uma cor aleatória para cada rastreador
        cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cores.append(cor)

cv2.destroyWindow("Selecione os objetos")

# Reiniciar o vídeo para começar do primeiro frame
video.set(cv2.CAP_PROP_POS_FRAMES, 0)

# Loop principal para rastreamento
while True:
    ok, frame = video.read()
    if not ok or frame is None:
        break

    # Atualizar todos os rastreadores
    for i, rastreador in enumerate(rastreadores):
        ok, bbox = rastreador.update(frame)
        if ok:
            (x, y, w, h) = [int(v) for v in bbox]
            cv2.rectangle(frame, (x, y), (x + w, y + h), cores[i], 2, 1)
        else:
            cv2.putText(frame, f'Erro no rastreio {i+1}', (50, 50 + (i * 30)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # Mostrar o vídeo com os rastreadores
    cv2.imshow('Rastreamento Múltiplo', frame)

    # Pressionar 'ESC' para sair
    if cv2.waitKey(30) & 0xFF == 27:
        break

video.release()
cv2.destroyAllWindows()
