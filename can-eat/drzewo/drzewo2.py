from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QBrush, QColor
import sys

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

class TreeGraphicsScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.node_radius = 20
        self.level_height = 60
        self.min_node_distance = 100
        self.colors = {
            'root': QColor(128, 0, 0),  # ciemny czerwony
            'branch': QColor(150, 75, 75),  # jaśniejszy czerwony
            'leaf': QColor(175, 100, 100)   # najjaśniejszy czerwony
        }

    def draw_tree(self, node, x=0, y=0, level=0):
        # Wybierz kolor w zależności od poziomu w drzewie
        if level == 0:
            color = self.colors['root']
        elif not node.children:
            color = self.colors['leaf']
        else:
            color = self.colors['branch']

        # Rysuj węzeł
        self.addEllipse(x-self.node_radius, y-self.node_radius, 
                       self.node_radius*2, self.node_radius*2, 
                       QPen(Qt.black), QBrush(color))
        
        # Dodaj tekst
        text = self.addText(str(node.data))
        text.setDefaultTextColor(Qt.white)
        text.setPos(x - text.boundingRect().width()/2, 
                   y - text.boundingRect().height()/2)

        if node.children:
            width = max(len(node.children) * self.min_node_distance, self.min_node_distance)
            start_x = x - width/2

            for i, child in enumerate(node.children):
                child_x = start_x + (width/(len(node.children)-1 if len(node.children) > 1 else 1)) * i
                child_y = y + self.level_height
                
                self.addLine(x, y, child_x, child_y, QPen(Qt.black))
                self.draw_tree(child, child_x, child_y, level+1)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Alkohol og andre ingredienser")
        
        self.view = QGraphicsView()
        self.scene = TreeGraphicsScene()
        self.view.setScene(self.scene)
        
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Tworzenie struktury drzewa
        root = TreeNode("G Alkohol")
        
        # Pierwsza główna gałąź - G Alkohol, som drikke
        alkohol_drikke = TreeNode("G Alkohol, som drikke")
        root.add_child(alkohol_drikke)

        # Dodawanie dzieci do G Alkohol, som drikke
        brennevin = TreeNode("G Brennevin")
        cider = TreeNode("G Cider")
        hetvin = TreeNode("G Hetvin")
        ol = TreeNode("G Øl")
        vin = TreeNode("G Vin")

        for node in [brennevin, cider, hetvin, ol, vin]:
            alkohol_drikke.add_child(node)

        # Dodawanie kolejnych poziomów...
        # (Tu dodałbym resztę struktury, ale dla czytelności pokazuję tylko fragment)

        # Wizualizacja
        self.scene.draw_tree(root)
        self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(1200, 800)
    window.show()
    sys.exit(app.exec_())