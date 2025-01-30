from PyQt5.QtWidgets import (QApplication, QMainWindow, QGraphicsView, QGraphicsScene, 
                           QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QInputDialog,
                           QFileDialog, QMessageBox, QLabel, QComboBox)
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPen, QBrush, QColor, QTransform, QPainter, QFontMetrics, QFont
import sys
import json

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        self.node_type = "default"  # Dodajemy typ węzła dla kolorowania

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def to_dict(self):
        return {
            'data': self.data,
            'node_type': self.node_type,
            'children': [child.to_dict() for child in self.children]
        }

    @classmethod
    def from_dict(cls, data_dict):
        node = cls(data_dict['data'])
        node.node_type = data_dict['node_type']
        for child_dict in data_dict['children']:
            child = cls.from_dict(child_dict)
            node.add_child(child)
        return node

class ZoomableGraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setRenderHint(QPainter.Antialiasing)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.ScrollHandDrag)

    def wheelEvent(self, event):
        zoom_factor = 1.15
        if event.angleDelta().y() > 0:
            self.scale(zoom_factor, zoom_factor)
        else:
            self.scale(1/zoom_factor, 1/zoom_factor)

class TreeGraphicsScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.min_width = 100  # Minimalna szerokość węzła
        self.height = 40      # Wysokość węzła
        self.padding = 20     # Dodatkowe miejsce na tekst
        self.level_height = 80
        self.min_node_distance = 120
        self.colors = {
            'root': QColor(128, 0, 0),
            'drink': QColor(150, 75, 75),
            'ingredient': QColor(75, 75, 150),
            'animal': QColor(75, 150, 75),
            'default': QColor(128, 128, 128)
        }

    def calculate_node_width(self, text):
        # Obliczanie szerokości na podstawie tekstu
        font_metrics = QFontMetrics(QFont())
        text_width = font_metrics.width(text)
        return max(self.min_width, text_width + self.padding)

    def draw_tree(self, node, x=0, y=0, level=0):
        color = self.colors.get(node.node_type, self.colors['default'])
        
        # Obliczanie szerokości węzła na podstawie tekstu
        node_width = self.calculate_node_width(node.data)
        
        # Rysowanie owalnego węzła
        self.addEllipse(x - node_width/2, y - self.height/2,
                    node_width, self.height,
                    QPen(Qt.black), QBrush(color))
        
        # Dodawanie tekstu
        text = self.addText(node.data)
        text.setDefaultTextColor(Qt.white)
        text_width = text.boundingRect().width()
        text_height = text.boundingRect().height()
        text.setPos(x - text_width/2, y - text_height/2)

        if node.children:
            # Obliczanie całkowitej szerokości potrzebnej dla wszystkich dzieci
            total_width = sum(self.calculate_node_width(child.data) for child in node.children)
            total_spacing = self.min_node_distance * (len(node.children) - 1)
            width = max(total_width + total_spacing, node_width)
            
            # Pozycja startowa dla pierwszego dziecka
            start_x = x - width/2
            
            for i, child in enumerate(node.children):
                child_width = self.calculate_node_width(child.data)
                # Obliczanie pozycji x dla dziecka
                if i == 0:
                    child_x = start_x + child_width/2
                else:
                    prev_child_width = self.calculate_node_width(node.children[i-1].data)
                    child_x = prev_x + prev_child_width/2 + self.min_node_distance + child_width/2
                
                child_y = y + self.level_height
                
                # Rysowanie linii do dziecka
                self.addLine(x, y + self.height/2,
                            child_x, child_y - self.height/2,
                            QPen(Qt.black))
                
                # Rekurencyjne rysowanie poddrzewa
                self.draw_tree(child, child_x, child_y, level+1)
                prev_x = child_x


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Norsk Ingredienser Tree")
        self.initUI()
        
    def initUI(self):
        # Główny widget i layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # Toolbar
        toolbar = QHBoxLayout()
        
        # Przyciski
        save_btn = QPushButton("Save Tree", self)
        save_btn.clicked.connect(self.saveTree)
        load_btn = QPushButton("Load Tree", self)
        load_btn.clicked.connect(self.loadTree)
        add_btn = QPushButton("Add Node", self)
        add_btn.clicked.connect(self.addNode)
        remove_btn = QPushButton("Remove Node", self)
        remove_btn.clicked.connect(self.removeNode)
        reset_view_btn = QPushButton("Reset View", self)
        reset_view_btn.clicked.connect(self.resetView)
        
        # Dodawanie przycisków do toolbara
        toolbar.addWidget(save_btn)
        toolbar.addWidget(load_btn)
        toolbar.addWidget(add_btn)
        toolbar.addWidget(remove_btn)
        toolbar.addWidget(reset_view_btn)
        
        # Dodawanie toolbara do głównego layoutu
        layout.addLayout(toolbar)
        
        # Widok drzewa
        self.view = ZoomableGraphicsView()
        self.scene = TreeGraphicsScene()
        self.view.setScene(self.scene)
        layout.addWidget(self.view)
        
        # Tworzenie drzewa
        self.root = self.create_full_tree()
        self.draw_tree()
        
        self.resize(1400, 1000)

    def create_full_tree(self):
        root = TreeNode("G Alkohol")
        root.node_type = "root"

        # G Alkohol, som drikke
        alkohol_drikke = TreeNode("G Alkohol, som drikke")
        alkohol_drikke.node_type = "drink"
        root.add_child(alkohol_drikke)

        # Brennevin
        brennevin = TreeNode("G Brennevin")
        brennevin.node_type = "drink"
        alkohol_drikke.add_child(brennevin)

        # Liker
        liker = TreeNode("G Liker")
        brennevin.add_child(liker)
        for name in ["Appelsinliker", "Kirsebærlikor", "Likor, deklarert", "Marachino"]:
            node = TreeNode(name)
            liker.add_child(node)

        # Rom
        rom = TreeNode("G Rom")
        brennevin.add_child(rom)
        for name in ["Brun rom", "Hvit rom", "Rom, deklarert", "Gin", "Vodka", "Whisky"]:
            node = TreeNode(name)
            rom.add_child(node)

        # Cider
        cider = TreeNode("G Cider")
        alkohol_drikke.add_child(cider)
        for name in ["Cider, deklarert", "Eplecider", "Pærecider"]:
            node = TreeNode(name)
            cider.add_child(node)

        # Hetvin
        hetvin = TreeNode("G Hetvin")
        alkohol_drikke.add_child(hetvin)
        for name in ["Hetvin, deklarert", "Madeira", "Portvin", "Sherry"]:
            node = TreeNode(name)
            hetvin.add_child(node)

        # Øl
        ol = TreeNode("G Øl")
        alkohol_drikke.add_child(ol)
        for name in ["Fatøl", "Juleøl", "Øl, deklarert"]:
            node = TreeNode(name)
            ol.add_child(node)

        # Vin
        vin = TreeNode("G Vin")
        alkohol_drikke.add_child(vin)
        vin.add_child(TreeNode('"Rusbrus"'))
        for name in ["Eplevin", "Hvitvin", "Rødvin", "Vin, deklarert"]:
            node = TreeNode(name)
            vin.add_child(node)

        # G Alkohol, som ingrediens
        alkohol_ingrediens = TreeNode("G Alkohol, som ingrediens")
        alkohol_ingrediens.node_type = "ingredient"
        root.add_child(alkohol_ingrediens)

        # Brennevin som ingrediens
        brennevin_ing = TreeNode("G Brennevin, som ingrediens")
        alkohol_ingrediens.add_child(brennevin_ing)
        ingrediens_list = [
            "Brandy, som ingrediens",
            "Brennevin, som ingrediens, deklarert",
            "Etanol, som ingrediens",
            "Kirsebærvin, som ingrediens",
            "Madeira, som ingrediens",
            "Marachino, som ingrediens",
            "Mirin, som ingrediens",
            "Rom, som ingrediens",
            "Sherry, som ingrediens"
        ]
        for name in ingrediens_list:
            node = TreeNode(name)
            brennevin_ing.add_child(node)

        # Øl som ingrediens
        ol_ing = TreeNode("G Øl, som ingrediens")
        alkohol_ingrediens.add_child(ol_ing)
        ol_ing.add_child(TreeNode("Mørkt øl, som ingrediens"))
        ol_ing.add_child(TreeNode("Øl, som ingrediens, deklarert"))

        # Vin som ingrediens
        vin_ing = TreeNode("G Vin, som ingrediens")
        alkohol_ingrediens.add_child(vin_ing)
        hvitvin_ing = TreeNode("Hvitvin, som ingrediens")
        vin_ing.add_child(hvitvin_ing)
        hvitvin_ing.add_child(TreeNode("Hvitvinekstrakt"))
        
        for name in ["Chablis, som ingrediens", "Risvin, som ingrediens", 
                    "Rødvin, som ingrediens", "Vin, som ingrediens, deklarert"]:
            node = TreeNode(name)
            vin_ing.add_child(node)

        # Bløtdyr
        blotdyr = TreeNode("G Bløtdyr")
        blotdyr.node_type = "animal"
        root.add_child(blotdyr)

        # Skjell
        skjell = TreeNode("G Skjell")
        blotdyr.add_child(skjell)
        for name in ["Akkar", "Blekksprut", "Bløtdyr, deklarert", "Snegler"]:
            node = TreeNode(name)
            skjell.add_child(node)

        # Østers
        osters = TreeNode("G Østers")
        skjell.add_child(osters)
        for name in ["Blåskjell", "Kamskjell", "O-skjell", "Skjell, deklarert", 
                    "Østers, deklarert", "Østersekstrakt"]:
            node = TreeNode(name)
            osters.add_child(node)

        # Egg
        egg = TreeNode("G Egg")
        egg.node_type = "animal"
        root.add_child(egg)

        # Div. animalsk
        egg.add_child(TreeNode("G Div. animalsk"))

        # Hønseegg
        honseegg = TreeNode("G (Hønse)egg")
        egg.add_child(honseegg)
        
        # Egg components
        for name in ["Egg, deklarert", "Eggehvite", "Eggeplomme"]:
            node = TreeNode(name)
            honseegg.add_child(node)
            if "hvite" in name:
                node.add_child(TreeNode("Eggehvitepulver"))
            elif "plomme" in name:
                node.add_child(TreeNode("Eggeplommepulver"))
            elif "deklarert" in name:
                node.add_child(TreeNode("Eggepulver"))

        # Vaktelegg
        vaktelegg = TreeNode("G Vaktelegg")
        egg.add_child(vaktelegg)
        for name in ["Eggehvite", "Eggeplomme", "Vaktelegg, deklarert"]:
            node = TreeNode(name)
            vaktelegg.add_child(node)

        return root

    def draw_tree(self):
        self.scene.clear()
        self.scene.draw_tree(self.root)
        self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

    def saveTree(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Tree", "", "JSON files (*.json)")
        if filename:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.root.to_dict(), f, ensure_ascii=False, indent=2)

    def loadTree(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Load Tree", "", "JSON files (*.json)")
        if filename:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.root = TreeNode.from_dict(data)
                self.draw_tree()

    def addNode(self):
        text, ok = QInputDialog.getText(self, 'Add Node', 'Enter node name:')
        if ok and text:
            # Tutaj można dodać logikę dodawania nowego węzła
            pass

    def removeNode(self):
        # Tutaj można dodać logikę usuwania węzła
        pass

    def resetView(self):
        self.view.setTransform(QTransform())
        self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())