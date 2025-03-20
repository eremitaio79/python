import cv2

# Usando o rastreador MOSSE, mais rápido e robusto para movimentos rápidos.
rastreador = cv2.TrackerMOSSE_create()

# Abrindo o vídeo.
video = cv2.VideoCapture('fly2.mp4')

# Leitura do primeiro frame.
ok, frame = video.read()

if not ok:
    print("Falha ao abrir o vídeo")
    exit()

# Seleção da região de interesse (ROI) no primeiro frame.
bbox = cv2.selectROI(frame, False)
ok = rastreador.init(frame, bbox)

# Suavização do movimento para melhorar a precisão
previous_bbox = None

while True:
    ok, frame = video.read()
    if not ok:
        break

    # Atualiza a posição da caixa delimitadora (bounding box).
    ok, bbox = rastreador.update(frame)

    if ok:
        # Se a posição atual for válida, suavizamos o movimento.
        if previous_bbox is not None:
            # Suaviza as mudanças usando uma média ponderada
            x = int((bbox[0] + previous_bbox[0]) / 2)
            y = int((bbox[1] + previous_bbox[1]) / 2)
            w = int((bbox[2] + previous_bbox[2]) / 2)
            h = int((bbox[3] + previous_bbox[3]) / 2)
            bbox = (x, y, w, h)

        # Atualiza a caixa delimitadora
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2, 1)
        previous_bbox = bbox  # Armazena a posição atual para suavização.

    else:
        cv2.putText(frame, 'Erro no rastreio', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Exibe o frame com o rastreamento.
    cv2.imshow('Rastreamento', frame)

    # Sai do loop se a tecla Esc for pressionada.
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Libera o vídeo e fecha as janelas.
video.release()
cv2.destroyAllWindows()
