"""
Czesc projektu: Program do kodowanie tekstu

Plik wygenerowano za pomoca chatGPT

C: 2024.10.27
M: 2024.10.27
"""


from PIL import Image, ImageDraw

# Tworzymy obraz o białym tle
img = Image.new('RGB', (800, 800), 'white')
draw = ImageDraw.Draw(img)

# Rysujemy linię
draw.line((10, 10, 190, 10), fill="blue", width=3)

# Rysujemy prostokąt
draw.rectangle((10, 20, 190, 60), outline="red", fill="yellow")

# Dodajemy tekst
draw.text((10, 70), "Hello, ImageDraw!", fill="black")

# Wyświetlamy obraz
img.show()
