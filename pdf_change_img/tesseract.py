import pytesseract

# Defina o caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Verifique a versão do Tesseract
try:
    print(pytesseract.get_tesseract_version())
except pytesseract.TesseractNotFoundError as e:
    print("Erro: Tesseract não encontrado. Verifique o caminho de instalação.")
