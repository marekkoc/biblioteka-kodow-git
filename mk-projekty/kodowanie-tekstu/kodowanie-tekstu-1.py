"""
Czesc projektu: Program do kodowanie tekstu

C: 2024.10.27
M: 2024.10.28
"""

from pathlib import Path
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont



plt.close('all')

################################################################
### ZMIENNE GLOBALNE ###

# Tekst ktory bedzie zakodowany
text_o = "marekkoc.github.io"




bg_color = 0
#text_color = np.random.randint(210,255)
text_color = 255

################################################################
### SCIEZKI DOSTEPU ###
# Katalog domowy
home_folder =  Path.home()
# Katalog do zapusu danych wynikowych
save_folder = home_folder / 'Desktop' / "edits"
# Domyslna nazwa pliku do zapisu
filename = "kodowanie-1.raw"

################################################################
###  META DANE DO ZAPISU OBRAZU CAPTCHA###
rows, cols, slices = 256, 256, 256

current_datetime = datetime.now()
date = current_datetime.strftime("%Y-%m-%d")
hour = current_datetime.strftime("%H:%M:%S")

kompresja = None
szum = None
################################################################
### FUNKCJE POMOCNICZE ###
def average_font_letter_size(font_name="timesbi.ttf", font_size=20, image_shape=(100,100)):
    """
    Wyznacza srednia szerokosc i wysokosc litery w wybranej czcionce.

    W zaleznosci od kroju czcionki oraz od jej wielkosci, szerokosc i wysokosc liter jest rozna. Dlatego wazne abysmy wiedzieli jak szeroka i jak wysoka jest srednie litera z danej czcionki. Jet to wazne, poniewaz w zaleznosci od dlugosci tekstu ktory chcemy zapisac w obrazie, musimy zaalokowac odpowiedni rozmiar obrazka, tak aby zmiescily sie wszystkie litery oraz aby zostalo jeszcze troche miejsca po bokach.

    Text color : white (255)
    Background color : black (0)

    To-do:
        1. Prepare for loop for both lowercase and uppercase
        2. Prepare for loop for different font_size
        3. Think over what to
            a) plot (eg. mip of images ?), plot of average_widht and average_height vs font_size
            b) dictionary with

    Args:
        font_name (string): Font name.
        font_size (int): Font size.
        image_shape (list[int]): Temp. image shape.

    Plots
        Plot average_widht vs. font size and average_heihgt vs font_size
    Returns
    --List (float): average_widht and average_height of the letter


    C: 2024.10.28
    M: 2020.10.28
    """

    # ALFABET: Małe litery
    lowercase = ''.join(chr(i) for i in range(97, 123))
    # ALFABET: Wielkie litery
    uppercase = ''.join(chr(i) for i in range(65, 91))

    # numpy array
    np_arr = np.zeros(shape=image_shape, dtype=np.uint8)
    # numpy -> pil
    pil_arr = Image.fromarray(np_arr)
    # Tworzenie rysunku z PIL
    draw = ImageDraw.Draw(pil_arr)
    font4 = ImageFont.truetype(font_name, font_size)
    draw.text((10, 40), str(lowercase), font=font4, fill=255)

    # pil -> numpy
    np_arr = np.array(pil_arr)

    # obliczanie sredniej szerokosci liter
    av_width = np_arr.max(0)
    b= np.where(av_width>255, 1, 0)
    av = b.sum() / len(lowercase)

    a = np_arr.max(0)
    if 1:
        plt.figure()
        plt.stem(av_width)

    if 1:
        plt.figure()
        plt.imshow(np_arr, cmap=plt.cm.gray)
    plt.show()

average_font_letter_size()
