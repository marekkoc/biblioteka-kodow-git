#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 11:12:11 2024

@author: marek

Image editor

1h58min

C: 2024.10.18
M: 2024.10.25
"""

import os
# 1. Main imports
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QComboBox,\
                                                    QListWidget, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter, ImageEnhance

# 2.Main application and settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("PhotoQt")
main_window.resize(2500,1900)

# 3. all widgets and app elemtnes
btn_folder = QPushButton("Folder")
file_list = QListWidget()
btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
btn_mirror = QPushButton("Mirror")
btn_sharpness = QPushButton("Sharpness")
btn_gray = QPushButton("Gray")
btn_saturation = QPushButton("Saturation")
btn_contrast = QPushButton("Contrast")
btn_blur = QPushButton("Blur")

#Dropdown box
filter_box = QComboBox()
filter_box.addItem("Oryginal")
filter_box.addItems(["Left", "Right", "Mirror","Sharpness","Gray", "Saturation", "Contrast", "Blur"])

picture_box = QLabel("Image will appear here")

# 4. Design
master_layout = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QHBoxLayout()

col1.addWidget(btn_folder)
col1.addWidget(file_list)
col1.addWidget(filter_box)
col1.addWidget(btn_left)

col1.addWidget(btn_right)
col1.addWidget(btn_mirror)
col1.addWidget(btn_sharpness)
col1.addWidget(btn_gray)
col1.addWidget(btn_saturation)
col1.addWidget(btn_contrast)
col1.addWidget(btn_blur)

col2.addWidget(picture_box)


master_layout.addLayout(col1, 20)
master_layout.addLayout(col2, 80)

main_window.setLayout(master_layout)

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


class Editor():
    def __init__(self):
        self.image = None
        self.original = None
        self.filename = None
        self.save_folder = "edits/"

    def load_image(self, filename):
        self.filename = filename
        fullname = os.path.join(working_directory, self.filename)
        self.image = Image.open(fullname)
        self.original = self.image.copy()

    def save_image(self):
        path = os.path.join(working_directory, self.save_folder)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)

    def show_image(self, path):
        picture_box.hide()
        image = QPixmap(path)
        w, h = picture_box.width(), picture_box.height()
        image = image.scaled(w,h,Qt.KeepAspectRatio)
        picture_box.setPixmap(image)
        picture_box.show()
    
    def gray(self):
        self.image = self.image.convert("L")
        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.filename)
        self.show_image(image_path)

    def left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.filename)
        self.show_image(image_path)

    def right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.filename)
        self.show_image(image_path)
    
    def mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.filename)
        self.show_image(image_path)
    
    def sharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.filename)
        self.show_image(image_path)

    def blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.filename)
        self.show_image(image_path)

    def color(self):
        self.image = ImageEnhance.Color(self.image).enhance(1.2)
        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.filename)
        self.show_image(image_path)

    def contrast(self):
        self.image = ImageEnhance.Contrast(self.image).enhance(1.2)
        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.filename)
        self.show_image(image_path)

    def apply_filter(self, filter_name):
        if filter_name == "Oryginal":
            self.image = self.original.copy()
        else:
            mapping = {
                "Gray" : lambda image: image.convert("L"),
                "Saturation" : lambda image: ImageEnhance.Color(image).enhance(1.2),
                "Left" : lambda image: image.transpose(Image.ROTATE_90),
                "Right" : lambda image: image.transpose(Image.ROTATE_270),
                "Mirror" :lambda image: image.transpose(Image.FLIP_LEFT_RIGHT),
                "Sharpness" : lambda image: image.filter(ImageFilter.SHARPEN),
                "Contrast" : lambda image: ImageEnhance.Contrast(image).enhance(1.2),
                "Blur" : lambda image: image.filter(ImageFilter.BLUR)
            }
            filter_function = mapping.get(filter_name)
            if filter_function:
                self.image = filter_function(self.image)
                self.save_image()
                image_path = os.path.join(working_directory, self.save_folder, self.filename)
                self.show_image(image_path)
            pass 
        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.filename)
        self.show_image(image_path)

def handle_filter():
    if file_list.currentRow() >= 0:
        select_filter = filter_box.currentText()
        main.apply_filter(select_filter)


def displayImage():
    if file_list.currentRow() >= 0:
        filename = file_list.currentItem().text()
        main.load_image(filename)
        main.show_image(os.path.join(working_directory, main.filename))


main = Editor()

# 5. Events
btn_folder.clicked.connect(getWorkDirectory)
file_list.currentRowChanged.connect(displayImage)
btn_gray.clicked.connect(main.gray)
btn_left.clicked.connect(main.left)
btn_right.clicked.connect(main.right)
btn_mirror.clicked.connect(main.mirror)
btn_sharpness.clicked.connect(main.sharpen)
btn_blur.clicked.connect(main.blur)
btn_saturation.clicked.connect(main.color)
btn_contrast.clicked.connect(main.contrast)
filter_box.currentTextChanged.connect(handle_filter)

# 6. show and run our app
main_window.show()
app.exec_()
