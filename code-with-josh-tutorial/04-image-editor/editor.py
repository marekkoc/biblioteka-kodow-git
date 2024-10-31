"""
Image Editor class - setup.

Created: 2024.10.28
Modified: 2024.10.28
"""
# Importy systemowe
import os
# Imoporty zewnetrzne, srodowiska
from PIL import Image, ImageFilter, ImageEnhance
from PyQt5.QtGui import QPixmap

# Importy moich modulow i klas

class Editor():
    """
    Manipulate 2D images.


    C: 2024.10.28
    M: 2024.10.28
    """
    
    def __init__(self, save_folder_name='edits/'):
        """
        Params:
        -----------
        image_folder (str): path with image to process
        save_folder (str): path to folder where processed images are saved. Default: edits

        C: 2024.10.28
        M: 2024.10.28
        """
        self.image = None
        self.original = None

        self.file_name = None
        self.image_folder_name =  "Desktop"
        self.image_full_path = '/home/marek/Desktop'        
        
        self.save_folder_name = save_folder_name
        self.save_folder_path = os.path.join(self.image_folder_name, self.save_folder_name)
        self.save_full_image_path = None

    def load_image(self, filename):
        self.file_name = filename
        self.image_full_path = os.path.join(self.image_folder_name, self.file_name)
        self.image = Image.open(self.image_full_path)
        self.original = self.image.copy()
        self.save_full_image_path = os.paht.join(self.save_folder_path, filename)

    def save_image(self):
        if not (os.path.exists(self.save_folder_path) or os.path.isdir(self.save_folder_path)):
            os.mkdir(self.save_folder_path)
        self.image.save(self.save_full_image_path)


    def show_image(self, path, picture_box):
        picture_box.hide()
        image = QPixmap(path)
        w, h = picture_box.width(), picture_box.height()
        image = image.scaled(w, h, Qt.KeepAspectRatio)
        picture_box.setPixmap(image)
        picture_box.show()
 
    def transformImage(self, transformation):
        transformations = {
                "Gray" : lambda image: image.convert("L"),
                "Saturation" : lambda image: ImageEnhance.Color(image).enhance(1.2),
                "Left" : lambda image: image.transpose(Image.ROTATE_90),
                "Right" : lambda image: image.transpose(Image.ROTATE_270),
                "Mirror" :lambda image: image.transpose(Image.FLIP_LEFT_RIGHT),
                "Sharpness" : lambda image: image.filter(ImageFilter.SHARPEN),
                "Contrast" : lambda image: ImageEnhance.Contrast(image).enhance(1.2),
                "Blur" : lambda image: image.filter(ImageFilter.BLUR)
            }
        transform_function = transformations.get(transformation)
        if transform_function:
            self.image = transform_function(self.image)
            self.save_image()

        self.save_image()
        image_path = os.path.join(self.image_folder_name, self.save_folder_name, self.file_name)
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
                image_path = os.path.join(self.image_folder_name, self.save_folder_name, self.file_name)
                self.show_image(image_path)
            pass 
        self.save_image()
        image_path = os.path.join(self.image_folder_name, self.save_folder_name, self.file_name)
        self.show_image(image_path)


if __name__ == '__main__':
    print("hello")

