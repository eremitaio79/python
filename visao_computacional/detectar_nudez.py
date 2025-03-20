from nudenet import NudeDetector
import cv2  # Para carregar a imagem e verificar o caminho

# Criando o detector
detector = NudeDetector()

# Caminho para a imagem
image_path = r'D:\Imagens\m2.jpg'  # Atualize o caminho conforme necessário

# Tentando carregar a imagem para verificar o caminho
image = cv2.imread(image_path)

if image is None:
    print(f"Erro: Não foi possível carregar a imagem. Verifique o caminho: {image_path}")
else:
    try:
        # Detectando nudez na imagem
        result = detector.detect(image_path)

        # Lista de classes que indicam nudez explícita
        explicit_classes = [
            'FEMALE_BREAST_EXPOSED', 'GENITALIA_EXPOSED', 'BUTTOCKS_EXPOSED'
        ]

        # Variável de controle para nudez explícita
        contains_nudity = False

        print("Resultados da Detecção:")
        for detection in result:
            class_name = detection['class']
            score = detection['score']
            print(detection)

            # Só consideramos nudez explícita se a classe estiver na lista e o score for alto
            if class_name in explicit_classes and score > 0.5:
                print(f"A detecção '{class_name}' tem alta probabilidade de ser nudez explícita.")
                contains_nudity = True

        # Exibir a mensagem final
        print("\n" + "=" * 50)
        if contains_nudity:
            print("***** ESTA IMAGEM CONTÉM NUDEZ EXPLÍCITA *****")
        else:
            print("***** ESTA IMAGEM NÃO CONTÉM NUDEZ *****")
        print("=" * 50)

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")
