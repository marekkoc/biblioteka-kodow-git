import sys
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton,
    QProgressBar, QTextEdit, QSlider, QLabel, QWidget, QListWidget, QLineEdit, QGroupBox, QListWidgetItem
)


class WorkerThread(QThread):
    """
    Wątek roboczy dla paska postępu.
    """
    progress_changed = pyqtSignal(int)  # Emituje wartość postępu
    work_finished = pyqtSignal(str)  # Informuje o zakończeniu pracy

    def __init__(self, task_name):
        super().__init__()
        self.task_name = task_name
        self.is_running = True
        self.speed = 50  # Domyślna szybkość

    def run(self):
        progress = 0
        while self.is_running and progress <= 100:
            self.progress_changed.emit(progress)
            self.msleep(self.speed)
            progress += 1

        if progress > 100:
            self.work_finished.emit(self.task_name)

    def stop(self):
        self.is_running = False
        self.quit()
        self.wait()

    def set_speed(self, speed):
        self.speed = max(1, speed)


class MainWindow(QMainWindow):
    """
    Główne okno aplikacji.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zaawansowana wielowątkowość z dynamicznymi zadaniami")

        # Layout główny
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Logi zdarzeń
        self.logs = QTextEdit()
        self.logs.setReadOnly(True)
        self.layout.addWidget(self.logs)

        # Sekcja zarządzania zadaniami
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Nazwa zadania...")
        self.add_task_button = QPushButton("Dodaj zadanie")
        self.layout.addWidget(self.task_input)
        self.layout.addWidget(self.add_task_button)

        # Lista zadań
        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        # Przycisk zapisania logów
        self.save_logs_button = QPushButton("Zapisz logi do pliku")
        self.layout.addWidget(self.save_logs_button)

        # Sygnały
        self.add_task_button.clicked.connect(self.add_task)
        self.save_logs_button.clicked.connect(self.save_logs)

        # Przechowywanie wątków
        self.task_threads = {}

    def add_task(self):
        """
        Dodaje nowe zadanie do listy.
        """
        task_name = self.task_input.text().strip()
        if not task_name:
            self.logs.append("Nie można dodać pustego zadania!")
            return

        # Sprawdź, czy zadanie już istnieje
        if task_name in self.task_threads:
            self.logs.append(f"Zadanie '{task_name}' już istnieje!")
            return

        # Utwórz element listy
        task_item = QListWidgetItem(task_name)
        self.task_list.addItem(task_item)

        # Utwórz widżet dla paska postępu i przycisków sterujących
        task_widget = QWidget()
        task_layout = QHBoxLayout(task_widget)
        progress_bar = QProgressBar()
        progress_bar.setValue(0)
        task_layout.addWidget(progress_bar)

        start_button = QPushButton("Start")
        stop_button = QPushButton("Stop")
        reset_button = QPushButton("Reset")
        remove_button = QPushButton("Usuń")
        task_layout.addWidget(start_button)
        task_layout.addWidget(stop_button)
        task_layout.addWidget(reset_button)
        task_layout.addWidget(remove_button)

        # Dodaj widżet do elementu listy
        self.task_list.setItemWidget(task_item, task_widget)

        # Stwórz nowy wątek
        task_thread = WorkerThread(task_name)
        self.task_threads[task_name] = (task_thread, progress_bar)

        # Podłącz sygnały
        task_thread.progress_changed.connect(progress_bar.setValue)
        task_thread.work_finished.connect(self.task_finished)
        start_button.clicked.connect(lambda: self.start_task(task_name))
        stop_button.clicked.connect(lambda: self.stop_task(task_name))
        reset_button.clicked.connect(lambda: self.reset_task(task_name, progress_bar))
        remove_button.clicked.connect(lambda: self.remove_task(task_name))

        self.logs.append(f"Dodano zadanie: {task_name}")
        self.task_input.clear()

    def start_task(self, task_name):
        """
        Uruchamia zadanie.
        """
        if task_name in self.task_threads:
            task_thread, _ = self.task_threads[task_name]
            if not task_thread.isRunning():
                task_thread.is_running = True
                task_thread.start()
                self.logs.append(f"Rozpoczęto zadanie: {task_name}")

    def stop_task(self, task_name):
        """
        Zatrzymuje zadanie.
        """
        if task_name in self.task_threads:
            task_thread, _ = self.task_threads[task_name]
            task_thread.stop()
            self.logs.append(f"Zatrzymano zadanie: {task_name}")

    def reset_task(self, task_name, progress_bar):
        """
        Resetuje zadanie.
        """
        self.stop_task(task_name)
        progress_bar.setValue(0)
        self.logs.append(f"Zresetowano zadanie: {task_name}")

    def remove_task(self, task_name):
        """
        Usuwa zadanie z listy.
        """
        if task_name in self.task_threads:
            self.stop_task(task_name)
            del self.task_threads[task_name]

            # Usuń element z listy
            for i in range(self.task_list.count()):
                if self.task_list.item(i).text() == task_name:
                    self.task_list.takeItem(i)
                    break

            self.logs.append(f"Usunięto zadanie: {task_name}")

    @pyqtSlot(str)
    def task_finished(self, task_name):
        """
        Informuje o zakończeniu zadania.
        """
        self.logs.append(f"Zadanie zakończone: {task_name}")

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
