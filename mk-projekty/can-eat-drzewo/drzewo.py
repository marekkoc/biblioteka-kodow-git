# Struktura danych pozostaje taka sama
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

# Wizualizacja drzewa używając QTreeWidget
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem

class TreeVisualizer(QTreeWidget):
    def __init__(self):
        super().__init__()
        self.setHeaderLabel("Tree Structure")
    
    def add_tree(self, node, parent=None):
        if parent is None:
            item = QTreeWidgetItem(self)
        else:
            item = QTreeWidgetItem(parent)
        
        item.setText(0, str(node.data))
        
        for child in node.children:
            self.add_tree(child, item)

# Graficzna wizualizacja drzewa
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QBrush, QColor

class TreeGraphicsScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.node_radius = 30
        self.level_height = 100
        self.min_node_distance = 80

    def draw_tree(self, node, x=0, y=0, level=0):
        # Rysuj węzeł
        self.addEllipse(x-self.node_radius, y-self.node_radius, 
                       self.node_radius*2, self.node_radius*2, 
                       QPen(Qt.black), QBrush(Qt.white))
        
        # Dodaj tekst
        text = self.addText(str(node.data))
        text.setPos(x - text.boundingRect().width()/2, 
                   y - text.boundingRect().height()/2)

        # Rysuj dzieci
        if node.children:
            width = len(node.children) * self.min_node_distance
            start_x = x - width/2
            
            for i, child in enumerate(node.children):
                child_x = start_x + i * self.min_node_distance
                child_y = y + self.level_height
                
                # Rysuj linię do dziecka
                self.addLine(x, y, child_x, child_y, QPen(Qt.black))
                
                # Rekurencyjnie rysuj poddrzewo
                self.draw_tree(child, child_x, child_y, level+1)

# Główne okno aplikacji
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tree Visualizer")
        
        # Utworzenie widoku
        self.view = QGraphicsView()
        self.scene = TreeGraphicsScene()
        self.view.setScene(self.scene)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        
        # Centralny widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Przykładowe drzewo
        root = TreeNode("Root")
        child1 = TreeNode("Child 1")
        child2 = TreeNode("Child 2")
        root.add_child(child1)
        root.add_child(child2)
        
        # Wizualizacja
        self.scene.draw_tree(root)

# Uruchomienie aplikacji
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())