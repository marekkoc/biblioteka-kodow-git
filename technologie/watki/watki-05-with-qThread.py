"""

Wątki w Pythonie

C: 2025.01.20
M: 2025.01.20
"""

import sys
import time
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLCDNumber
from PyQt5.QtCore import QThread, pyqtSignal


class CounterThread(QThread):
    # Sygnał do przesyłania wartości licznika do GUI
    updated = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.running = False  # Flaga kontrolująca działanie wątku

    def run(self):
        count = 0
        while self.running:
            count += 1
            self.updated.emit(count)  # Emitowanie sygnału z wartością licznika
            time.sleep(0.5)

    def stop(self):
        self.running = False
        self.wait()  # Czekaj, aż wątek zakończy działanie


class Licznik(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wielowątkowość z QThread")
        self.setGeometry(100, 100, 400, 300)

        # Layouty
        self.main_layout = QVBoxLayout()
        self.counters_layout = QHBoxLayout()
        self.buttons_layout = QHBoxLayout()

        # Liczniki i kontrolki
        self.lcd1 = QLCDNumber(self)
        self.lcd2 = QLCDNumber(self)
        self.lcd3 = QLCDNumber(self)
        self.counters_layout.addWidget(self.lcd1)
        self.counters_layout.addWidget(self.lcd2)
        self.counters_layout.addWidget(self.lcd3)

        # Przyciski sterujące
        self.button1 = QPushButton("Start/Stop Wątek 1", self)
        self.button2 = QPushButton("Start/Stop Wątek 2", self)
        self.button3 = QPushButton("Start/Stop Wątek 3", self)
        self.buttons_layout.addWidget(self.button1)
        self.buttons_layout.addWidget(self.button2)
        self.buttons_layout.addWidget(self.button3)

        # Dodanie layoutów do głównego
        self.main_layout.addLayout(self.counters_layout)
        self.main_layout.addLayout(self.buttons_layout)
        self.setLayout(self.main_layout)

        # Utworzenie wątków
        self.threads = [CounterThread() for _ in range(3)]

        # Połączenie przycisków z funkcjami
        self.button1.clicked.connect(lambda: self.toggle_thread(0, self.lcd1))
        self.button2.clicked.connect(lambda: self.toggle_thread(1, self.lcd2))
        self.button3.clicked.connect(lambda: self.toggle_thread(2, self.lcd3))

    def toggle_thread(self, thread_index, lcd):
        thread = self.threads[thread_index]
        if thread.isRunning():
            thread.stop()  # Zatrzymujemy wątek
        else:
            thread.running = True  # Ustawiamy flagę na True
            thread.updated.connect(lcd.display)  # Podłączamy sygnał do wyświetlacza
            thread.start()  # Uruchamiamy wątek


if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = Licznik()
    okno.show()
    sys.exit(app.exec_())
