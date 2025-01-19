"""

C: 2025.01.16
M: 2025.01.17
"""


import sys
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QProgressBar, QWidget


class WorkerThread(QThread):
    """
    Klasa reprezentująca wątek roboczy. Wykonuje zadania w tle.
    """
    progress_changed = pyqtSignal(int)  # Emituje postęp (0-100)
    work_stopped = pyqtSignal()  # Emituje sygnał po zatrzymaniu pracy

    def __init__(self):
        super().__init__()
        self.is_running = True  # Flaga sterująca działaniem wątku

    def run(self):
        """
        Główna funkcja wykonywana w wątku.
        """
        progress = 0
        while self.is_running and progress <= 100:
            self.progress_changed.emit(progress)  # Emitowanie wartości postępu
            self.msleep(50)  # Spowolnienie działania (50 ms)
            progress += 1

        if not self.is_running:
            self.work_stopped.emit()  # Emitowanie sygnału zatrzymania

    def stop(self):
        """
        Zatrzymuje wątek.
        """
        self.is_running = False
        self.quit()
        self.wait()


class MainWindow(QMainWindow):
    """
    Główne okno aplikacji.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wielowątkowość w PyQt5")

        # Layout i widżety
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.progress_bar = QProgressBar()
        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.stop_button.setEnabled(False)  # Na początku "Stop" jest niedostępny

        self.layout.addWidget(self.progress_bar)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)

        # Wątek roboczy
        self.worker_thread = WorkerThread()

        # Połączenia sygnałów
        self.start_button.clicked.connect(self.start_worker)
        self.stop_button.clicked.connect(self.stop_worker)
        self.worker_thread.progress_changed.connect(self.update_progress)
        self.worker_thread.work_stopped.connect(self.on_worker_stopped)

    @pyqtSlot()
    def start_worker(self):
        """
        Uruchamia wątek roboczy.
        """
        if not self.worker_thread.isRunning():
            self.worker_thread.is_running = True
            self.worker_thread.start()
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)

    @pyqtSlot()
    def stop_worker(self):
        """
        Zatrzymuje wątek roboczy.
        """
        self.worker_thread.stop()

    @pyqtSlot(int)
    def update_progress(self, value):
        """
        Aktualizuje wartość progressBar na podstawie sygnału z wątku.
        """
        self.progress_bar.setValue(value)

    @pyqtSlot()
    def on_worker_stopped(self):
        """
        Przywraca interfejs po zatrzymaniu wątku.
        """
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.progress_bar.reset()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
