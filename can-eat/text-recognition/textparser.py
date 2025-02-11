import re
from typing import Dict, List, Optional

class ProductTextParser:
    def __init__(self):
        # Słownik kluczowych słów dla różnych sekcji
        self.keywords = {
            'nutritional_markers': [
                'nutrition facts', 'nutritional value', 'nutrition information',
                'næringsinformasjon', 'næringsinnhold', 'wartości odżywcze'
            ],
            'ingredient_markers': [
                'ingredients', 'ingredienser', 'składniki', 'contains'
            ],
            'allergen_markers': [
                'allergens', 'allergener', 'alergeny', 'może zawierać'
            ],
            'storage_markers': [
                'storage', 'oppbevaring', 'przechowywanie'
            ]
        }
        
        # Wyrażenia regularne dla różnych wartości
        self.patterns = {
            'weight': r'(\d+(?:\.\d+)?)\s*(g|kg|ml|l)',
            'energy': r'(\d+(?:\.\d+)?)\s*(kcal|kj)',
            'nutrients': r'(\d+(?:\.\d+)?)\s*(g|mg|µg|%)',
            'barcode': r'(\d{8,13})',
            'percentage': r'(\d+(?:\.\d+)?)\s*%'
        }

    def clean_text(self, text: str) -> str:
        """Oczyszcza tekst ze zbędnych znaków"""
        text = text.lower().strip()
        text = re.sub(r'\s+', ' ', text)
        return text

    def extract_nutritional_values(self, text_list: List[str]) -> Dict:
        """Wyodrębnia wartości odżywcze z tekstu"""
        nutrition_facts = {
            'per_100g': {
                'energy': '',
                'fats': {
                    'total': '',
                    'saturated': '',
                    'unsaturated': None,
                    'trans': None
                },
                'carbohydrates': {
                    'total': '',
                    'sugars': {
                        'total': '',
                        'simple': None,
                        'complex': None
                    },
                    'fiber': None,
                    'starch': None
                },
                'protein': '',
                'salt': ''
            }
        }

        # Flagi do śledzenia kontekstu
        in_nutrition_section = False
        current_nutrient = None

        for text in text_list:
            text = self.clean_text(text)
            
            # Sprawdzenie czy jesteśmy w sekcji wartości odżywczych
            if any(marker in text for marker in self.keywords['nutritional_markers']):
                in_nutrition_section = True
                continue

            if in_nutrition_section:
                # Energia
                energy_match = re.search(r'energy|energi|energia', text)
                if energy_match:
                    value_match = re.search(self.patterns['energy'], text)
                    if value_match:
                        nutrition_facts['per_100g']['energy'] = f"{value_match.group(1)} {value_match.group(2)}"

                # Tłuszcze
                fat_match = re.search(r'fat|fett|tłuszcz', text)
                if fat_match:
                    value_match = re.search(self.patterns['nutrients'], text)
                    if value_match:
                        nutrition_facts['per_100g']['fats']['total'] = f"{value_match.group(1)} {value_match.group(2)}"

                # Pozostałe składniki odżywcze...
                # [Tu dodajemy podobną logikę dla pozostałych składników]

        return nutrition_facts

    def extract_ingredients(self, text_list: List[str]) -> List[str]:
        """Wyodrębnia listę składników"""
        ingredients = []
        in_ingredients_section = False

        for text in text_list:
            text = self.clean_text(text)
            
            if any(marker in text for marker in self.keywords['ingredient_markers']):
                in_ingredients_section = True
                continue

            if in_ingredients_section:
                # Sprawdzenie czy nie weszliśmy w inną sekcję
                if any(marker in text for marker in 
                      self.keywords['nutritional_markers'] + 
                      self.keywords['allergen_markers'] + 
                      self.keywords['storage_markers']):
                    break
                
                # Dzielenie tekstu na składniki (zwykle oddzielone przecinkami)
                parts = text.split(',')
                ingredients.extend([part.strip() for part in parts if part.strip()])

        return ingredients

    def extract_allergens(self, text_list: List[str]) -> List[str]:
        """Wyodrębnia alergeny z tekstu"""
        allergens = []
        in_allergen_section = False

        for text in text_list:
            text = self.clean_text(text)
            
            if any(marker in text for marker in self.keywords['allergen_markers']):
                in_allergen_section = True
                continue

            if in_allergen_section:
                if any(marker in text for marker in 
                      self.keywords['nutritional_markers'] + 
                      self.keywords['ingredient_markers'] + 
                      self.keywords['storage_markers']):
                    break
                
                # Ekstrakcja alergenów (zwykle pisane wielkimi literami)
                allergen_matches = re.findall(r'\b[A-Z]+\b', text.upper())
                allergens.extend(allergen_matches)

        return allergens

    def extract_barcode(self, text_list: List[str]) -> Optional[str]:
        """Wyodrębnia kod kreskowy"""
        for text in text_list:
            barcode_match = re.search(self.patterns['barcode'], text)
            if barcode_match:
                return barcode_match.group(1)
        return None

    def categorize_product(self, text_list: List[str], ingredients: List[str]) -> List[str]:
        """Określa kategorie produktu na podstawie tekstu i składników"""
        categories = []
        
        # Podstawowe słowa kluczowe dla kategorii
        category_keywords = {
            'Dairy': ['milk', 'yogurt', 'cheese', 'cream'],
            'Beverages': ['drink', 'juice', 'water', 'beverage'],
            'Snacks': ['chips', 'snack', 'crackers'],
            # ... więcej kategorii
        }

        # Analiza tekstu i składników
        all_text = ' '.join(text_list + ingredients).lower()
        
        for category, keywords in category_keywords.items():
            if any(keyword in all_text for keyword in keywords):
                categories.append(category)

        return categories

    def parse_text(self, text_list: List[str]) -> Dict:
        """Główna funkcja parsująca tekst do struktury JSON"""
        parsed_data = {
            "product_name": "",
            "manufacturer": "",
            "store_chain": "",
            "weight_volume": "",
            "ingredients": [],
            "nutrition_facts": {},
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

        # Ekstrakcja podstawowych informacji
        parsed_data['ingredients'] = self.extract_ingredients(text_list)
        parsed_data['nutrition_facts'] = self.extract_nutritional_values(text_list)
        parsed_data['allergens'] = self.extract_allergens(text_list)
        parsed_data['barcode'] = self.extract_barcode(text_list)
        parsed_data['categories'] = self.categorize_product(text_list, parsed_data['ingredients'])

        # Szukanie nazwy produktu (zwykle największy tekst na opakowaniu)
        # Tu możemy dodać logikę wykrywania nazwy produktu

        return parsed_data