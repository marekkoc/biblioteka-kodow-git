"""
Czesc projektu: Program do kodowanie tekstu

Plik wygenerowano za pomoca chatGPT

C: 2024.10.27
M: 2024.10.27
"""


import numpy as np
import matplotlib.pyplot as plt
import os 
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# za pomoca os
home_folder1 =  os.path.expanduser("~")
# za pomoca pahtlib.Path
home_folder =  Path.home()
save_folder = home_folder / 'Desktop' / "edits"
filename = 'randomowy-tekst.png'

# Ustawienia obrazu
width, height = 200, 100
background_color = 255  # biały
text_color = 0          # czarny

# Tworzenie pustej macierzy (wypełniona kolorem tła)
image_array = np.full((height, width), background_color, dtype=np.uint8)
image = Image.fromarray(image_array)

# Tworzenie rysunku z PIL
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()  # Można też użyć czcionki TrueType (ImageFont.truetype)

# Dodanie tekstu do obrazu
text = "Hello, NumPy!"
text_x, text_y = 20, 40  # Pozycja tekstu na obrazie
draw.text((text_x, text_y), text, font=font, fill=text_color)

# Konwersja obrazu PIL z powrotem do macierzy NumPy
image_array_with_text = np.array(image)

# Wyświetlenie wyniku
plt.imshow(image_array_with_text, cmap=plt.cm.gray)
plt.show()

print(save_folder)
image.save(save_folder / filename)

