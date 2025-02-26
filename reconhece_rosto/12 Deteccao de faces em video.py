import cv2

def redim(img, largura):
    alt = int(img.shape[0] / img.shape[1] * largura)
    return cv2.resize(img, (largura, alt), interpolation=cv2.INTER_AREA)

cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
df = cv2.CascadeClassifier(cascade_path)

if df.empty():
    print("Erro: Arquivo XML do classificador não encontrado!")
    exit()

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Erro: Não foi possível acessar a câmera!")
    exit()

while True:
    sucesso, frame = camera.read()
    if not sucesso:
        print("Erro: Não foi possível capturar o frame da câmera.")
        break

    frame = redim(frame, 320)
    frame_pb = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = df.detectMultiScale(frame_pb, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20))

    frame_temp = frame.copy()
    for (x, y, lar, alt) in faces:
        cv2.rectangle(frame_temp, (x, y), (x + lar, y + alt), (0, 255, 255), 2)


    cv2.imshow("Localizando rostos...", redim(frame_temp, 640))

    # s para encerrar
    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

# Liberar recursos
camera.release()
cv2.destroyAllWindows()
