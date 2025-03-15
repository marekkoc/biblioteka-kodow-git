"""
Czesc projektu: Program do kodowanie tekstu

Plik wygenerowano za pomoca chatGPT

Aby zadzialal ten kod musialem zainstalowac czcionki:

sudo apt install ttf-mscorefonts-installer


C: 2024.10.27
M: 2024.10.27
"""



from PIL import Image, ImageDraw, ImageFont

# Tworzymy obraz
img = Image.new('RGB', (600, 800), color = (73, 109, 137))
draw = ImageDraw.Draw(img)

# Ustawiamy czcionkę domyślną (bez ładowania pliku)
font0 = ImageFont.load_default()
draw.text((10, 10), "Hello World!", font=font0, fill=(255, 255, 255))

font1 = ImageFont.truetype("arial.ttf", 80)  # Arial lub inna dostępna czcionka
font2 = ImageFont.truetype("Comic_Sans_MS_Bold.ttf", 80)  # Arial lub inna dostępna czcionka
font3 = ImageFont.truetype("Courier_New_Bold.ttf", 80)  # Arial lub inna dostępna czcionka
font4 = ImageFont.truetype("timesbi.ttf", 80)  # Arial lub inna dostępna czcionka

#draw.text((30, 100), "Hello World!", font=font, fill=(255, 255, 255))
draw.text((30, 100), "Hello World!", font=font1, fill=(255, 255, 255))
draw.text((30, 200), "Hello World!", font=font2, fill=(255, 255, 255))
draw.text((30, 300), "Hello World!", font=font3, fill=(255, 255, 255))
draw.text((30, 400), "Hello World!", font=font4, fill=(255, 255, 255))


img.show()
