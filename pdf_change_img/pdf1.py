import fitz  # PyMuPDF para manipular PDFs
import cv2
import numpy as np
from PIL import Image
import io
import os

# Configurações
pasta_pdfs = r"D:\pyprojects\pdf_change_img\pdf_original"  # Pasta onde estão os PDFs
logotipos_referencia = [
    r"D:\pyprojects\pdf_change_img\logotipos\padrao1.png",
    r"D:\pyprojects\pdf_change_img\logotipos\padrao2.png",
    r"D:\pyprojects\pdf_change_img\logotipos\padrao3.png",
    r"D:\pyprojects\pdf_change_img\logotipos\padrao4.png",
    r"D:\pyprojects\pdf_change_img\logotipos\padrao5.png"
]
tolerancia_match = 0.8  # Tolerância para a correspondência de padrões (ajustável)

# Carrega os logotipos de referência para detecção
logos_ref = {}
for logotipo in logotipos_referencia:
    img = cv2.imread(logotipo, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Erro ao carregar a imagem de referência: {logotipo}")
    logos_ref[logotipo] = img

# Loop pelos PDFs na pasta
for arquivo in os.listdir(pasta_pdfs):
    if arquivo.endswith(".pdf"):
        pdf_path = os.path.join(pasta_pdfs, arquivo)
        doc = fitz.open(pdf_path)

        for page_num, page in enumerate(doc):
            imagens = page.get_images(full=True)  # Obtém todas as imagens

            for img_index, img in enumerate(imagens):
                xref = img[0]  # ID da imagem
                base_image = doc.extract_image(xref)
                image_data = base_image["image"]

                # Convertendo a imagem para OpenCV
                image_pil = Image.open(io.BytesIO(image_data))
                img_cv = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2GRAY)

                for logotipo, logo_ref in logos_ref.items():
                    # Usar OpenCV para encontrar o logotipo na imagem
                    result = cv2.matchTemplate(img_cv, logo_ref, cv2.TM_CCOEFF_NORMED)
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

                    # Verifica se a correspondência é suficientemente boa
                    if max_val >= tolerancia_match:
                        print(f"Logotipo encontrado ({logotipo}) na página {page_num + 1} do arquivo {arquivo}")

                        # Obtém a posição do logotipo encontrado
                        h, w = logo_ref.shape
                        top_left = max_loc
                        bottom_right = (top_left[0] + w, top_left[1] + h)

                        # Desenha um retângulo vermelho ao redor do logotipo encontrado
                        img_cv_color = cv2.cvtColor(img_cv, cv2.COLOR_GRAY2BGR)
                        cv2.rectangle(img_cv_color, top_left, bottom_right, (0, 0, 255), 3)

                        # Exibe a imagem no terminal
                        cv2.imshow(f"Logotipo detectado - {arquivo} (página {page_num + 1})", img_cv_color)
                        cv2.waitKey(500)  # Aguarda 500ms antes de processar a próxima
                        cv2.destroyAllWindows()

                        # Converte de volta para formato PIL para reinserir no PDF
                        img_pil_final = Image.fromarray(cv2.cvtColor(img_cv_color, cv2.COLOR_BGR2RGB))
                        img_byte_arr = io.BytesIO()
                        img_pil_final.save(img_byte_arr, format='PNG')

                        # Substitui a imagem no PDF
                        rect = page.get_image_rects(xref)[0]
                        page.insert_image(rect, stream=img_byte_arr.getvalue())

        # Salva o PDF atualizado
        pasta_saida = r"D:\pyprojects\pdf_change_img\pdf_alterado"
        os.makedirs(pasta_saida, exist_ok=True)  # Garante que a pasta de saída exista
        caminho_saida = os.path.join(pasta_saida, arquivo)

        doc.save(caminho_saida)
        doc.close()

# Mensagem de conclusão
print("Processo concluído com sucesso!")
