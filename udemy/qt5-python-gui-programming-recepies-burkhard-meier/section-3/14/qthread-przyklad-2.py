import sys
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QTimer, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QProgressBar, QTextEdit, QSlider, QLabel, QWidget, QHBoxLayout


class WorkerThread(QThread):
    """
    Wątek ładowania paska postępu.
    """
    progress_changed = pyqtSignal(int)  # Emituje wartość postępu
    work_finished = pyqtSignal()  # Informuje o zakończeniu pracy

    def __init__(self):
        super().__init__()
        self.is_running = True
        self.speed = 50  # Domyślna szybkość (ms)

    def run(self):
        progress = 0
        while self.is_running and progress <= 100:
            self.progress_changed.emit(progress)
            self.msleep(self.speed)  # Kontrolowanie szybkości ładowania
            progress += 1

        if progress > 100:
            self.work_finished.emit()  # Informacja o zakończeniu pracy

    def stop(self):
        self.is_running = False
        self.quit()
        self.wait()

    def set_speed(self, speed):
        """
        Ustawia szybkość ładowania (niższa wartość = szybsze ładowanie).
        """
        self.speed = max(1, speed)


class TimerThread(QThread):
    """
    Wątek odliczania czasu.
    """
    time_updated = pyqtSignal(str)  # Emituje aktualny czas jako tekst

    def __init__(self):
        super().__init__()
        self.is_running = True

    def run(self):
        seconds = 0
        while self.is_running:
            mins, secs = divmod(seconds, 60)
            self.time_updated.emit(f"{mins:02}:{secs:02}")
            self.sleep(1)
            seconds += 1

    def stop(self):
        self.is_running = False
        self.quit()
        self.wait()


class MainWindow(QMainWindow):
    """
    Główne okno aplikacji.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zaawansowana wielowątkowość w PyQt5")

        # Layout i widżety
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Pasek postępu
        self.progress_bar = QProgressBar()
        self.layout.addWidget(self.progress_bar)

        # Szybkość ładowania
        self.slider_label = QLabel("Szybkość: 50 ms")
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setMinimum(10)
        self.slider.setMaximum(500)
        self.slider.setValue(50)
        self.layout.addWidget(self.slider_label)
        self.layout.addWidget(self.slider)

        # Przyciski
        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.save_logs_button = QPushButton("Zapisz logi do pliku")
        self.stop_button.setEnabled(False)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)

        # Logi zdarzeń
        self.logs = QTextEdit()
        self.logs.setReadOnly(True)
        self.layout.addWidget(self.logs)

        # Timer
        self.timer_label = QLabel("Czas: 00:00")
        self.layout.addWidget(self.timer_label)

        # Wątki
        self.worker_thread = WorkerThread()
        self.timer_thread = TimerThread()

        # Połączenia sygnałów
        self.start_button.clicked.connect(self.start_worker)
        self.stop_button.clicked.connect(self.stop_worker)
        self.save_logs_button.clicked.connect(self.save_logs)
        self.worker_thread.progress_changed.connect(self.update_progress)
        self.worker_thread.work_finished.connect(self.worker_finished)
        self.timer_thread.time_updated.connect(self.update_timer)
        self.slider.valueChanged.connect(self.update_speed)

    @pyqtSlot()
    def start_worker(self):
        """
        Uruchamia wątek ładowania i odliczania czasu.
        """
        if not self.worker_thread.isRunning():
            self.worker_thread.is_running = True
            self.worker_thread.start()
            self.timer_thread.is_running = True
            self.timer_thread.start()
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)
            self.logs.append("Rozpoczęto ładowanie...")

    @pyqtSlot()
    def stop_worker(self):
        """
        Zatrzymuje wątek ładowania i odliczania czasu.
        """
        self.worker_thread.stop()
        self.timer_thread.stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.logs.append("Zatrzymano ładowanie.")

    @pyqtSlot(int)
    def update_progress(self, value):
        """
        Aktualizuje wartość progressBar na podstawie sygnału z wątku.
        """
        self.progress_bar.setValue(value)

    @pyqtSlot()
    def worker_finished(self):
        """
        Informuje o zakończeniu pracy.
        """
        self.logs.append("Ładowanie zakończone.")
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    @pyqtSlot(str)
    def update_timer(self, time_str):
        """
        Aktualizuje licznik czasu.
        """
        self.timer_label.setText(f"Czas: {time_str}")

    @pyqtSlot(int)
    def update_speed(self, value):
        """
        Aktualizuje szybkość ładowania na podstawie suwaka.
        """
        self.worker_thread.set_speed(value)
        self.slider_label.setText(f"Szybkość: {value} ms")

    @pyqtSlot()
    def save_logs(self):
        """
        Zapisuje logi do pliku.
        """
        with open("logs.txt", "w") as file:
            file.write(self.logs.toPlainText())
        self.logs.append("Logi zapisane do pliku logs.txt.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())