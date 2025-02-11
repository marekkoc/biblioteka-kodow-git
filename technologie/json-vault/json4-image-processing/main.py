
import cv2
import pytesseract
import json
from pathlib import Path
import numpy as np
from PIL import Image
import easyocr
import json

from imageprocessor import ProductImageProcessor


# dla tekstu w różnych językach
reader = easyocr.Reader(['en', 'pl', 'no'])  # możemy dodać więcej języków jeśli potrzeba

# Przykład użycia
if __name__ == "__main__":
    current_dir: Path = Path.cwd()
    products_dir = current_dir.parent / 'produkt-1'

    # Ścieżka do folderu ze zdjęciami
    processor = ProductImageProcessor()
    
    # Ścieżka do folderu ze zdjęciami
    image_folder = Path("product_images")
    output_folder = Path("processed_data")
    output_folder.mkdir(exist_ok=True)
    
    # Przetwórz wszystkie zdjęcia w folderze
    for image_path in image_folder.glob("*.JPEG"):
        product_data = processor.process_image(image_path)
        output_path = output_folder / f"{image_path.stem}.json"
        processor.save_to_json(product_data, output_path)