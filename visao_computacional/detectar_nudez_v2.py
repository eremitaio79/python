from nudenet import NudeDetector
import cv2
import os
import numpy as np

# Criando o detector
detector = NudeDetector()

# Caminho para a imagem
image_path = r'D:\Imagens\woman2.jpeg'  # Atualize o caminho conforme necessário

# Lista de extensões válidas
valid_extensions = {'.jpg', '.jpeg', '.png', '.bmp'}

# Verifica se o arquivo existe
if not os.path.exists(image_path):
    print(f"❌ Erro: O arquivo não foi encontrado. Verifique se o caminho está correto: {image_path}")

# Verifica se a extensão do arquivo é válida
elif not os.path.splitext(image_path)[1].lower() in valid_extensions:
    print(f"❌ Erro: Formato de arquivo inválido. Use imagens nos formatos: {', '.join(valid_extensions)}")

else:
    # Tenta carregar a imagem
    image = cv2.imread(image_path)

    if image is None:
        print(f"❌ Erro: Não foi possível carregar a imagem. O arquivo pode estar corrompido ou no formato errado.")
    else:
        try:
            # Detectando nudez na imagem
            result = detector.detect(image_path)

            # Lista de classes que indicam nudez explícita
            explicit_classes = ['FEMALE_BREAST_EXPOSED', 'FEMALE_GENITALIA_EXPOSED', 'BUTTOCKS_EXPOSED']

            # Variável de controle para nudez explícita
            contains_nudity = False

            print("✅ Resultados da Detecção:")

            for detection in result:
                class_name = detection['class']
                score = detection['score']
                x, y, w, h = detection['box']

                print(detection)

                # Se a classe estiver na lista e a pontuação for alta, aplicamos o desfoque
                if class_name in explicit_classes and score > 0.5:
                    contains_nudity = True

                    # Região de interesse (ROI) para desfoque
                    roi = image[y:y + h, x:x + w]
                    blurred_roi = cv2.GaussianBlur(roi, (99, 99), 30)
                    image[y:y + h, x:x + w] = blurred_roi

                    # Desenha o retângulo em volta da área censurada
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

                    # Exibe a porcentagem de nudez acima do retângulo
                    percentage_text = f"{int(score * 100)}%"
                    cv2.putText(image, percentage_text, (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            # Exibe a mensagem final em destaque
            print("\n" + "=" * 50)
            if contains_nudity:
                print("🚨 ESTA IMAGEM CONTÉM NUDEZ EXPLÍCITA 🚨")
            else:
                print("✅ ESTA IMAGEM NÃO CONTÉM NUDEZ ✅")
            print("=" * 50)

            # Exibe a imagem processada
            cv2.imshow("Imagem Processada", image)
            cv2.waitKey(0)  # Espera o usuário pressionar qualquer tecla
            cv2.destroyAllWindows()

        except Exception as e:
            print(f"❌ Erro ao processar a imagem: {e}")
