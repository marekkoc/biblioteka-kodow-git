"""
Czesc projektu: Program do kodowanie tekstu

Plik wygenerowano za pomoca chatGPT

C: 2024.10.27
M: 2024.10.27
"""



from PIL import Image, ImageDraw, ImageFont
import random
import string
import os
from pathlib import Path

# za pomoca os
home_folder1 =  os.path.expanduser("~")
# za pomoca pahtlib.Path
home_folder =  Path.home()
save_folder = home_folder / 'Desktop' / "edits"
filename = 'captcha-tekst.png'

# Funkcja generująca losowy tekst CAPTCHA
def generate_captcha_text(length=5):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Funkcja generująca obraz CAPTCHA z tekstem
def generate_captcha_image(captcha_text):
    # Ustawienia rozmiaru obrazu
    width, height = 640, 480
    background_color = (255, 255, 255)  # Białe tło
    text_color = (0, 0, 0)              # Czarny tekst

    # Tworzenie nowego obrazu
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Czcionka systemowa lub domyślna
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except IOError:
        font = ImageFont.load_default()

    # Rysowanie tekstu na środku obrazu
    text_width, text_height = draw.textsize(captcha_text, font=font)
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    draw.text((text_x, text_y), captcha_text, font=font, fill=text_color)

    # Dodanie zakłóceń: linii i punktów
    for _ in range(10):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        line_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.line((x1, y1, x2, y2), fill=line_color, width=2)

    for _ in range(50000):
        dot_x = random.randint(0, width)
        dot_y = random.randint(0, height)
        dot_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.point((dot_x, dot_y), fill=dot_color)

    # Zapisz obraz CAPTCHA do pliku
    image.save(save_folder / filename)
    print("Generated CAPTCHA saved as captcha_custom.png")

# Przykład użycia
captcha_text = generate_captcha_text()
generate_captcha_image(captcha_text)
print(f"Generated CAPTCHA text: {captcha_text}")

