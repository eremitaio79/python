import cv2

# Algoritmo de rastreio.
rastreador = cv2.TrackerCSRT_create()

# Imagem de input para rastreio. Neste teste será usado o vídeo race.mp4.
video = cv2.VideoCapture('fly1.mp4')

# A variável ok vai retornar true/false para o retorno do primeiro frame do vídeo armazenado na variável frame.
ok, frame = video.read()

# Será passado para a variável bbox (boundbox) o primeiro frame do vídeo.
# ROI = Region Of Interest.
bbox = cv2.selectROI(frame)
# print(bbox)

ok = rastreador.init(frame, bbox)
# print(ok)

while True:
    ok, frame = video.read()
    # print(ok)
    if not ok:
        break
    ok, bbox = rastreador.update(frame)
    print(bbox)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2, 1)
    else:
        cv2.putText(frame, 'Erro no rastreio', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Rastreamento', frame)

    if cv2.waitKey(1) & 0XFF  == 27: # Esc
        break

# if cv2.waitKey(0) & 0xFF == ord('q'):
#     exit()  # Encerra o programa corretamente
