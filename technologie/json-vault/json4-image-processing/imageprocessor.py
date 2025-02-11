import easyocr
import cv2
import json
from textparser import ProductTextParser

class ProductImageProcessor:
    def __init__(self, languages=['en', 'pl', 'no']):
        self.reader = easyocr.Reader(languages)
        self.json_template = {
            "product_name": "",
            "manufacturer": "",
            "store_chain": "",
            "weight_volume": "",
            "ingredients": [],
            "nutrition_facts": {
                "per_100g": {
                    "energy": "",
                    "fats": {
                        "total": "",
                        "saturated": "",
                        "unsaturated": None,
                        "trans": None
                    },
                    "carbohydrates": {
                        "total": "",
                        "sugars": {
                            "total": "",
                            "simple": None,
                            "complex": None
                        },
                        "fiber": None,
                        "starch": None
                    },
                    "protein": "",
                    "salt": ""
                }
            },
            "vitamins_and_minerals": {},
            "allergens": [],
            "barcode": "",
            "expiry_date": None,
            "storage_conditions": None,
            "country_of_origin": "",
            "categories": [],
            "price": None,
            "notes": ""
        }

    def preprocess_image(self, image_path):
        """Preprocesses image for better OCR results"""
        # Wczytaj obraz
        image = cv2.imread(str(image_path))
        
        # Konwertuj do skali szarości
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Zastosuj binaryzację adaptacyjną
        binary = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
        )
        
        # Usuń szum
        denoised = cv2.fastNlMeansDenoising(binary)
        
        return denoised

    def extract_text(self, image):
        """Extracts text from preprocessed image using EasyOCR"""
        results = self.reader.readtext(image)
        return [text[1] for text in results]

    def extract_barcode(self, image):
        """Extracts barcode from image"""
        # Tutaj możemy dodać specyficzną logikę do wykrywania kodów kreskowych
        # np. używając biblioteki pyzbar
        pass

    def parse_nutrition_facts(self, text_list):
        """Parses nutrition facts from text"""
        nutrition_facts = self.json_template["nutrition_facts"]["per_100g"].copy()
        
        for text in text_list:
            # Tutaj dodamy logikę do parsowania wartości odżywczych
            # np. przy użyciu wyrażeń regularnych
            pass
        
        return nutrition_facts

    def process_image(self, image_path):
        """Main method to process image and return structured data"""
        # Preprocessuj obraz
        processed_image = self.preprocess_image(image_path)
        
        # Wyodrębnij tekst
        text_list = self.extract_text(processed_image)
        
        # Przygotuj dane JSON
        product_data = self.json_template.copy()
        
        # Parsuj tekst
        parser = ProductTextParser()
        product_data = parser.parse_text(text_list)
        
        return product_data

    def save_to_json(self, data, output_path):
        """Saves processed data to JSON file"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)