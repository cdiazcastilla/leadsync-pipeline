import fitz  # PyMuPDF
import os
import re
import cv2
import pytesseract
from PIL import Image

# 1. Extraer texto de PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# 2. Limpiar texto
def clean_text(text):
    text = re.sub(r"\n+", " ", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()

# 3. Guardar texto limpio
def save_clean_text(text, filename, output_dir="data/cleaned_text"):
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
        f.write(text)

# 4. Anotar imagen (simulado con pytesseract)
def annotate_image(image_path, output_dir="data/annotated_images"):
    os.makedirs(output_dir, exist_ok=True)

    # Ruta al ejecutable de Tesseract OCR en tu sistema
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    image = cv2.imread(image_path)
    boxes = pytesseract.image_to_boxes(image)

    for b in boxes.splitlines():
        b = b.split(' ')
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(image, (x, image.shape[0]-y), (w, image.shape[0]-h), (0, 255, 0), 2)

    annotated_path = os.path.join(output_dir, os.path.basename(image_path))
    cv2.imwrite(annotated_path, image)
