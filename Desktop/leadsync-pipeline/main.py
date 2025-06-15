import os
from utils import extract_text_from_pdf, clean_text, save_clean_text, annotate_image

def run_pipeline():
    # Procesar PDFs
    raw_pdf_dir = "data/raw_pdfs"
    for pdf in os.listdir(raw_pdf_dir):
        if pdf.endswith(".pdf"):
            pdf_path = os.path.join(raw_pdf_dir, pdf)
            print(f"Procesando PDF: {pdf}")
            raw_text = extract_text_from_pdf(pdf_path)
            cleaned = clean_text(raw_text)
            save_clean_text(cleaned, pdf.replace(".pdf", ".txt"))

    # Procesar imágenes
    raw_img_dir = "data/raw_images"
    for img in os.listdir(raw_img_dir):
        if img.lower().endswith((".png", ".jpg", ".jpeg")):
            print(f"Anotando imagen: {img}")
            annotate_image(os.path.join(raw_img_dir, img))

if __name__ == "__main__":
    run_pipeline()
