#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 11:12:11 2024

@author: marek

Image editor: 3h32min - 3h42min

Zastosowanie funkcji labmda do wszystkich operacji przetwarzanie obrazów.
Zrefaktoryzowano z pomoca CursorAI i Claude AI.


C: 2024.10.18
M: 2025.02.10
"""

from typing import Dict, List, Callable, Optional
from enum import Enum
from dataclasses import dataclass
import os
from pathlib import Path

# Grupowanie importów według funkcjonalności
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QPushButton, 
    QLabel, 
    QComboBox,
    QListWidget, 
    QVBoxLayout, 
    QHBoxLayout, 
    QFileDialog,
    QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter, ImageEnhance

# Stałe
WINDOW_TITLE = "PhotoQt"
WINDOW_SIZE = (2500, 1900)
SUPPORTED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.svg'}
SAVE_DIRECTORY = "edits"  # Bez żadnych ścieżek, tylko nazwa katalogu

class ImageTransformation(Enum):
    ORIGINAL = "Original"
    GRAY = "Gray"
    SATURATION = "Saturation"
    LEFT = "Left"
    RIGHT = "Right"
    MIRROR = "Mirror"
    SHARPNESS = "Sharpness"
    CONTRAST = "Contrast"
    BLUR = "Blur"

@dataclass
class ImageTransformations:
    """Klasa przechowująca wszystkie transformacje obrazu"""
    @staticmethod
    def get_transformations() -> Dict[str, Callable[[Image.Image], Image.Image]]:
        return {
            ImageTransformation.GRAY.value: lambda image: image.convert("L"),
            ImageTransformation.SATURATION.value: lambda image: ImageEnhance.Color(image).enhance(1.2),
            ImageTransformation.LEFT.value: lambda image: image.transpose(Image.ROTATE_90),
            ImageTransformation.RIGHT.value: lambda image: image.transpose(Image.ROTATE_270),
            ImageTransformation.MIRROR.value: lambda image: image.transpose(Image.FLIP_LEFT_RIGHT),
            ImageTransformation.SHARPNESS.value: lambda image: image.filter(ImageFilter.SHARPEN),
            ImageTransformation.CONTRAST.value: lambda image: ImageEnhance.Contrast(image).enhance(1.2),
            ImageTransformation.BLUR.value: lambda image: image.filter(ImageFilter.BLUR)
        }

class ImageEditor:
    def __init__(self):
        self.image: Optional[Image.Image] = None
        self.original: Optional[Image.Image] = None
        self.filename: Optional[str] = None
        self.working_directory: Path = Path.cwd()  # Inicjalizacja bieżącym katalogiem
        self.transformations = ImageTransformations.get_transformations()

    def load_image(self, filename: str, working_directory: Path) -> None:
        try:
            self.filename = filename
            # Konwertujemy ścieżkę na absolutną
            self.working_directory = Path(working_directory).resolve()
            image_path = self.working_directory / filename
            print(f"Ładowanie obrazu z: {image_path}")  # Debugging
            self.image = Image.open(image_path)
            self.original = self.image.copy()
        except Exception as e:
            print(f"Błąd ładowania: {e}")
            raise

    def save_image(self) -> Path:
        try:
            # Tworzymy katalog edits w bieżącym katalogu roboczym
            save_path = self.working_directory / SAVE_DIRECTORY
            save_path.mkdir(exist_ok=True)
            
            # Zapisujemy plik
            full_path = save_path / self.filename
            print(f"Próba zapisu do: {full_path}")  # Debugging
            self.image.save(full_path)
            return full_path
        except Exception as e:
            print(f"Błąd zapisu: {e}")
            raise

    def transform_image(self, transformation_name: str) -> Optional[Path]:
        if not self.image:
            return None

        if transformation_name == ImageTransformation.ORIGINAL.value:
            self.image = self.original.copy()
        else:
            transform_func = self.transformations.get(transformation_name)
            if transform_func:
                self.image = transform_func(self.image)

        return self.save_image()

class PhotoQtGUI:
    def __init__(self):
        self.app = QApplication([])
        self.editor = ImageEditor()
        self.main_window = QWidget()
        self.main_window.setWindowTitle(WINDOW_TITLE)
        self.main_window.resize(*WINDOW_SIZE)
        self.setup_ui()

    def setup_ui(self) -> None:
        self.create_widgets()
        self.create_buttons()
        self.setup_layouts()
        self.connect_signals()

    def create_widgets(self) -> None:
        self.btn_folder = QPushButton("Wybierz folder")
        self.file_list = QListWidget()
        
        # Konfiguracja panelu ze zdjęciem
        self.image_label = QLabel()
        self.image_label.setMinimumSize(800, 600)
        self.image_label.setStyleSheet("""
            QLabel {
                background-color: #f0f0f0;
                border: 1px solid #ccc;
            }
        """)
        self.image_label.setAlignment(Qt.AlignCenter)
        # Dodajemy politykę skalowania
        self.image_label.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        
        self.filter_box = QComboBox()
        self.filter_box.addItems([transform.value for transform in ImageTransformation])

    def create_buttons(self) -> None:
        # Tworzenie przycisków dla każdej transformacji
        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setContentsMargins(20, 10, 20, 10)  # Marginesy dla przycisków
        self.buttons_layout.setSpacing(10)  # Odstęp między przyciskami
        
        for transform in ImageTransformation:
            button_name = f'btn_{transform.value.lower()}'
            button = QPushButton(transform.value)
            button.setMinimumWidth(100)  # Minimalna szerokość przycisku
            button.setStyleSheet("""
                QPushButton {
                    padding: 8px 15px;
                    background-color: #ffffff;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #f0f0f0;
                }
            """)
            setattr(self, button_name, button)
            self.buttons_layout.addWidget(button)

    def setup_layouts(self) -> None:
        # Główny kontener - układ pionowy
        main_vertical = QVBoxLayout()
        
        # Kontener na główną zawartość (lista plików + zdjęcie)
        content_layout = QHBoxLayout()
        
        # Lewy panel
        left_panel = QVBoxLayout()
        left_panel.addWidget(self.btn_folder)
        left_panel.addWidget(self.file_list)
        left_panel.addWidget(self.filter_box)
        
        left_widget = QWidget()
        left_widget.setLayout(left_panel)
        left_widget.setFixedWidth(300)
        
        # Dodawanie lewego panelu i zdjęcia do głównej zawartości
        content_layout.addWidget(left_widget)
        content_layout.addWidget(self.image_label, stretch=1)
        
        # Kontener na przyciski na dole
        bottom_panel = QWidget()
        bottom_panel.setMinimumHeight(80)  # Wysokość panelu z przyciskami
        bottom_panel.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                border-top: 1px solid #ddd;
            }
        """)
        bottom_panel.setLayout(self.buttons_layout)
        
        # Dodawanie wszystkiego do głównego układu
        content_widget = QWidget()
        content_widget.setLayout(content_layout)
        
        main_vertical.addWidget(content_widget, stretch=1)
        main_vertical.addWidget(bottom_panel)
        
        self.main_window.setLayout(main_vertical)

    def connect_signals(self) -> None:
        self.btn_folder.clicked.connect(self.get_work_directory)
        self.file_list.currentRowChanged.connect(self.display_image)
        self.filter_box.currentTextChanged.connect(self.handle_filter)

        # Poprawione podłączanie przycisków transformacji
        for transform in ImageTransformation:
            button_name = f'btn_{transform.value.lower()}'
            if hasattr(self, button_name):
                button = getattr(self, button_name)
                # Używamy partial aby zachować wartość transform.value w momencie tworzenia połączenia
                from functools import partial
                button.clicked.connect(partial(self.apply_transformation, transform.value))

    def apply_transformation(self, transform_name: str) -> None:
        """Nowa metoda do obsługi transformacji"""
        if self.editor.image:
            self.editor.transform_image(transform_name)
            self.update_display()

    def get_work_directory(self) -> None:
        directory = QFileDialog.getExistingDirectory(self.main_window, "Wybierz folder")
        if directory:
            # Konwertujemy ścieżkę na obiekt Path i rozwiązujemy wszystkie symlinki
            path = Path(directory).resolve()
            print(f"Wybrany katalog: {path}")  # Debugging
            self.editor.working_directory = path
            self.update_file_list()

    def update_file_list(self) -> None:
        try:
            self.file_list.clear()
            for file in os.listdir(self.editor.working_directory):
                if Path(file).suffix.lower() in SUPPORTED_EXTENSIONS:
                    self.file_list.addItem(file)
        except Exception as e:
            print(f"Błąd aktualizacji listy: {e}")

    def display_image(self, index: int) -> None:
        try:
            if index >= 0:
                filename = self.file_list.item(index).text()
                self.editor.load_image(filename, self.editor.working_directory)
                self.update_display()
        except Exception as e:
            print(f"Błąd podczas wyświetlania obrazu: {e}")

    def update_display(self) -> None:
        try:
            if self.editor.image:
                # Konwersja obrazu PIL do QPixmap
                image_path = self.editor.save_image()
                if image_path.exists():
                    pixmap = QPixmap(str(image_path))
                    if not pixmap.isNull():
                        # Pobieramy aktualny rozmiar label'a
                        label_size = self.image_label.size()
                        
                        # Skalujemy obraz do rozmiaru label'a, zachowując proporcje
                        scaled_pixmap = pixmap.scaled(
                            label_size.width(),
                            label_size.height(),
                            Qt.KeepAspectRatio,
                            Qt.SmoothTransformation
                        )
                        
                        self.image_label.setPixmap(scaled_pixmap)
                        # Wymuszamy przerysowanie
                        self.image_label.repaint()
                        
                        print(f"Załadowano obraz: {image_path}")
                        print(f"Rozmiar label'a: {label_size.width()}x{label_size.height()}")
                        print(f"Rozmiar pixmap: {scaled_pixmap.width()}x{scaled_pixmap.height()}")
                    else:
                        print("Błąd: Nie udało się utworzyć pixmap")
                else:
                    print(f"Błąd: Plik {image_path} nie istnieje")
        except Exception as e:
            print(f"Błąd podczas aktualizacji wyświetlania: {e}")

    def handle_filter(self, filter_name: str) -> None:
        if self.editor.image:
            self.editor.transform_image(filter_name)
            self.update_display()

    def run(self) -> None:
        self.main_window.show()
        self.app.exec_()

#########################
### All functionality ###
#########################

working_directory = ""

# filter the files and extentions
def filter(files, extentions):
    results = []

    for file in files:
        for ext in extentions:
            if file.lower().endswith(ext):
                results.append(file)
    return results

# Get the current work directory
def getWorkDirectory():
    global working_directory

    working_directory = QFileDialog.getExistingDirectory()
    extentions = ['.jpg', '.jpeg', '.png', '.svg' ]
    filenames = filter(os.listdir(working_directory), extentions)
    file_list.clear()
    for filename in filenames:
        file_list.addItem(filename)

def handle_filter():
    if file_list.currentRow() >= 0:
        select_filter = filter_box.currentText()
        main.apply_filter(select_filter)

def displayImage():
    if file_list.currentRow() >= 0:
        filename = file_list.currentItem().text()
        main.load_image(filename, Path(working_directory))
        main.show_image(os.path.join(working_directory, main.filename))

# Uruchomienie aplikacji
if __name__ == "__main__":
    app = PhotoQtGUI()
    app.run()
