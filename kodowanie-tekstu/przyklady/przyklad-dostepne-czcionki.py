import os

def list_fonts(directory):
    fonts = []
    # Przechodzimy przez pliki w danym katalogu
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.ttf', '.otf')):  # Sprawdzamy, czy plik jest czcionką
                fonts.append(os.path.join(root, file))
    return fonts

# Typowe lokalizacje czcionek
font_dirs = [
    "/usr/share/fonts/",          # Linux
    "~/.fonts/",                 # Linux (użytkownik)
    "C:\\Windows\\Fonts\\",      # Windows
    "/Library/Fonts/",           # macOS
    "~/Library/Fonts/"           # macOS (użytkownik)
]

# Zbieranie czcionek z wszystkich lokalizacji
available_fonts = []
for dir in font_dirs:
    expanded_dir = os.path.expanduser(dir)  # Rozwiń '~' do katalogu domowego
    if os.path.exists(expanded_dir):
        available_fonts.extend(list_fonts(expanded_dir))

# Wyświetlenie dostępnych czcionek
for font in available_fonts:
    print(font)
