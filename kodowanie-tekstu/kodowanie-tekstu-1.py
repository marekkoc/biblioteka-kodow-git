"""
Czesc projektu: Program do kodowanie tekstu

C: 2024.10.27
M: 2024.10.27
"""

import numpy as np
import matplotlib.pyplot as plt

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from datetime import datetime

plt.close('all')

# Zmienne globalne
text_o = "marekkoc.github.io"

# ALFABET: Małe litery
lowercase = ''.join(chr(i) for i in range(97, 123))
# ALFABET: Wielkie litery
uppercase = ''.join(chr(i) for i in range(65, 91))


bg_color = 0
#text_color = np.random.randint(210,255)
text_color = 255


# za pomoca pahtlib.Path
home_folder =  Path.home()
save_folder = home_folder / 'Desktop' / "edits"
filename = "kodowanie-1.raw"

#################################################
###  Meta dane ###
rows, cols, slices = 256, 256, 256

current_datetime = datetime.now()
date = current_datetime.strftime("%Y-%m-%d")
hour = current_datetime.strftime("%H:%M:%S")

kompresja = None
szum = None
#################################################


#np_arr = np.random.randint(0,180, size=(rows,cols),dtype=np.uint8)
np_arr = np.zeros(shape=(rows,cols),dtype=np.uint8)

# numpy -> pil
pil_arr = Image.fromarray(np_arr)

# Tworzenie rysunku z PIL
draw = ImageDraw.Draw(pil_arr)
font4 = ImageFont.truetype("timesbi.ttf", 20)
draw.text((10, 20), str(lowercase), font=font4, fill=text_color)

# pil -> numpy
np_arr = np.array(pil_arr)

# obliczanie sredniej szerokosci liter
a = np_arr.max(0)
b= np.where(a>50, 1, 0)
av = b.sum() / len(lowercase)

a = np_arr.max(0)
if 0:
    plt.figure()
    plt.stem(a)




if 0:
    plt.figure()
    plt.imshow(np_arr, cmap=plt.cm.gray)
plt.show()
