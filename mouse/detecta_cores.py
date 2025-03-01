# import cv2
# import numpy as np
#
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#     lower_red = np.array([0, 120, 70])
#     upper_red = np.array([10, 255, 255])
#     mask = cv2.inRange(hsv, lower_red, upper_red)
#
#     result = cv2.bitwise_and(frame, frame, mask=mask)
#
#     cv2.imshow("Original", frame)
#     cv2.imshow("Detecção de Cor", result)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()




# import cv2
# import numpy as np
#
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#     # Faixa de cor para detectar branco
#     lower_white = np.array([0, 0, 200])   # Valores mínimos para branco
#     upper_white = np.array([180, 30, 255]) # Valores máximos para branco
#
#     mask = cv2.inRange(hsv, lower_white, upper_white)
#
#     # Encontra contornos nos objetos brancos
#     contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area > 500:  # Filtra pequenos ruídos
#             x, y, w, h = cv2.boundingRect(cnt)
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Desenha o retângulo
#             cv2.putText(frame, "Branco", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#
#     cv2.imshow("Detecção de Objetos Brancos", frame)
#     cv2.imshow("Máscara Branca", mask)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()




import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Faixa de cor para detectar laranja
    lower_orange = np.array([10, 100, 100])   # Valores mínimos para laranja
    upper_orange = np.array([25, 255, 255])   # Valores máximos para laranja

    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    # Encontra contornos nos objetos laranjas
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:  # Filtra pequenos ruídos
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Desenha o retângulo
            cv2.putText(frame, "Laranja", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Detecção de Objetos Laranja", frame)
    cv2.imshow("Máscara Laranja", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
