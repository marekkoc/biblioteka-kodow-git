---
Utworzono: 2025-01-17T10:17:00
Zmodyfikowano: 2025-01-17T10:17:00
Źródło: chatGPT
tags: 
Katalog:
---
# Wersja podstawowa

Wielowątkowość w aplikacjach PyQt5 pozwala na wykonywanie długotrwałych zadań w tle, dzięki czemu interfejs użytkownika pozostaje responsywny. Qt oferuje klasy takie jak `QThread` i `QThreadPool` oraz pomocnicze mechanizmy, takie jak `QRunnable` i `QTimer`.

Poniżej znajduje się przykład prostej aplikacji, która:

1. **Zawiera `QProgressBar`, który ładuje się w tle.**
2. **Pozwala na uruchamianie i zatrzymywanie procesu ładowania za pomocą przycisków.**
3. **Używa `QThread` do uruchomienia procesu w tle, by interfejs użytkownika pozostał responsywny.**

---

### Kod aplikacji:

```python
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
```

---

### Wyjaśnienie kodu:

#### 1. **`WorkerThread` (klasa wątku roboczego):**

- Dziedziczy z `QThread`.
- Ma metodę `run`, która wykonuje kod w tle (np. symulowanie ładowania paska postępu).
- **Sygnały:**
    - `progress_changed` – emituje wartość postępu.
    - `work_stopped` – informuje o zatrzymaniu pracy.

#### 2. **Zarządzanie wątkiem:**

- Wątek jest uruchamiany przez `self.worker_thread.start()`.
- Zatrzymywany jest przez `self.worker_thread.stop()`, co ustawia flagę `is_running` na `False`.

#### 3. **Responsywny interfejs:**

- Wątek działa w tle, a interfejs użytkownika pozostaje responsywny, ponieważ `QThread` nie blokuje głównej pętli zdarzeń.

#### 4. **Progres Bar i przyciski:**

- **Start:** Uruchamia wątek i blokuje przycisk "Start".
- **Stop:** Zatrzymuje wątek, odblokowuje "Start" i resetuje `QProgressBar`.

#### 5. **Dlaczego `QThread` zamiast pętli w głównym wątku?**

- Wykonując długie zadania w głównym wątku (np. pętle `while`), blokujemy pętlę zdarzeń Qt, co powoduje zamrożenie interfejsu użytkownika.

---

### Jak to działa:

1. Kliknij **Start**, aby rozpocząć ładowanie paska w tle.
2. Kliknij **Stop**, aby zatrzymać pasek w bieżącym miejscu.
3. Pasek jest responsywny i nie zamraża aplikacji podczas działania.

Możesz rozbudować tę aplikację, np. dodając bardziej złożone zadania w tle. 😊

# Rozbudowana werjsa

Rozbudujmy aplikację, aby była bardziej funkcjonalna i interesująca! Dodamy następujące elementy:

1. **Zaawansowany pasek postępu** – możliwość wprowadzania szybkości ładowania za pomocą suwaka (`QSlider`).
2. **Wielowątkowość z priorytetami** – dodanie dodatkowego wątku roboczego symulującego inne zadanie (np. odliczanie czasu).
3. **Logi zdarzeń** – okno tekstowe (`QTextEdit`) wyświetlające logi działań aplikacji.
4. **Zapis do pliku** – możliwość zapisania logów do pliku.

---

### Kod aplikacji:

```python
import sys
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QTimer
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
        self.slider.setOrientation(QtCore.Qt.Horizontal)
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
```

---

### Nowe funkcjonalności:

1. **Suwak szybkości:**
    
    - Zmienia szybkość ładowania paska postępu (10 ms do 500 ms na krok).
    - Ustawia nową wartość w wątku roboczym.
2. **Drugi wątek (Timer):**
    
    - Odpowiada za odliczanie czasu w formacie MM:SS.
    - Odlicza czas w tle niezależnie od paska postępu.
3. **Logi zdarzeń:**
    
    - `QTextEdit` przechowuje informacje o działaniach użytkownika.
    - Przycisk zapisuje logi do pliku `logs.txt`.

---

### Jak to działa:

1. Suwak pozwala kontrolować szybkość ładowania paska w czasie rzeczywistym.
2. Timer działa równolegle, pokazując upływający czas.
3. Logi przechowują informacje o zdarzeniach i można je zapisać do pliku.

Możesz łatwo rozszerzyć aplikację o dodatkowe funkcjonalności, takie jak bardziej złożone zadania w tle czy kolejne wątki! 😊

# Zadanie 3

Dobrze, rozbudujmy aplikację jeszcze bardziej! Dodamy następujące funkcjonalności:

1. **Dynamiczna lista zadań** – Użytkownik może dodawać zadania (np. "Praca A", "Praca B") do listy. Każde zadanie będzie miało oddzielny pasek postępu i przyciski sterujące (start/stop/reset).
2. **Zakończenie pracy wątku** – Wyświetlanie komunikatu w logach, gdy dane zadanie zakończy swoje działanie.
3. **Usuwanie zadań** – Możliwość usunięcia zadania z listy.

---

### Kod aplikacji:

```python
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
```

---

### Nowe funkcjonalności:

1. **Dynamiczne zadania:**
    
    - Możesz dodawać zadania z oddzielnymi paskami postępu i kontrolami (start/stop/reset).
    - Zadania mogą działać jednocześnie w osobnych wątkach.
2. **Logi zdarzeń:**
    
    - Rejestrują działania, takie jak dodanie, uruchomienie, zatrzymanie czy usunięcie zadania.
3. **Usuwanie zadań:**
    
    - Możliwość usunięcia zadania razem z jego wątkiem i widżetami.
4. **Zapis logów:**
    
    - Logi mogą być zapisane do pliku `logs.txt`.

---

### Jak to działa:

1. Dynamicznie dodajesz zadania za pomocą pola tekstowego i przycisku.
2. Każde zadanie ma swój pasek postępu i przyciski sterujące.
3. Zadania działają w osobnych wątkach, co pozwala na równoległe wykonywanie.

To narzędzie może być bazą do jeszcze bardziej zaawansowanych aplikacji, takich jak zarządzanie zadaniami, procesami, czy nawet planowaniem pracy! 😊

# wielowatkowość bez qt

Wielowątkowość w Pythonie pozwala na wykonywanie wielu zadań równolegle w jednym procesie. Jest szczególnie przydatna w aplikacjach, które muszą obsługiwać wiele zadań na raz, takich jak operacje sieciowe, obsługa wejścia/wyjścia (I/O), czy zarządzanie wieloma klientami.

---

### Kluczowe pojęcia:

1. **Global Interpreter Lock (GIL)**:
    
    - W CPython (najpopularniejsza implementacja Pythona), jednocześnie może działać tylko jeden wątek w ramach jednego procesu, co ogranicza korzyści z wielowątkowości w zadaniach intensywnie wykorzystujących CPU.
    - W zadaniach I/O (np. pobieranie danych z internetu) wielowątkowość jest bardzo efektywna, ponieważ wątki mogą "czekać" na zakończenie operacji.
2. **Biblioteka `threading`**:
    
    - Umożliwia zarządzanie wątkami.
    - Każdy wątek działa jako osobna jednostka wykonawcza w ramach programu.
3. **Alternatywa: multiprocessing**:
    
    - Do zadań intensywnie obciążających CPU lepiej używać wielu procesów (biblioteka `multiprocessing`), ponieważ każdy proces ma własny GIL.

---

### Prosty przykład wielowątkowości w Pythonie:

#### Przykład 1: Użycie `threading` do operacji I/O (symulacja pobierania danych)

```python
import threading
import time

def download_data(thread_id, duration):
    """
    Funkcja symulująca pobieranie danych.
    """
    print(f"Thread-{thread_id} started downloading data.")
    time.sleep(duration)  # Symulacja pobierania danych
    print(f"Thread-{thread_id} finished downloading data after {duration} seconds.")

# Tworzymy wątki
threads = []
for i in range(5):
    thread = threading.Thread(target=download_data, args=(i, i + 1))
    threads.append(thread)

# Uruchamiamy wątki
for thread in threads:
    thread.start()

# Czekamy na zakończenie wszystkich wątków
for thread in threads:
    thread.join()

print("All threads have completed.")
```

---

### Jak działa powyższy kod?

1. Tworzymy funkcję `download_data`, która symuluje zadanie (np. pobieranie pliku) przez wywołanie `time.sleep()`.
2. Tworzymy pięć wątków, które wykonują tę funkcję równolegle z różnymi czasami trwania.
3. `thread.start()` uruchamia wątek.
4. `thread.join()` blokuje główny wątek programu do czasu, aż każdy z wątków zakończy działanie.

---

### Przykład 2: Licznik równoległy w wielu wątkach

```python
import threading

class CounterThread(threading.Thread):
    def __init__(self, thread_id, count_to):
        super().__init__()
        self.thread_id = thread_id
        self.count_to = count_to

    def run(self):
        """
        Kod wykonywany w wątku.
        """
        for i in range(1, self.count_to + 1):
            print(f"Thread-{self.thread_id} counting: {i}")

# Tworzymy wątki
threads = []
for i in range(3):
    thread = CounterThread(thread_id=i, count_to=5)
    threads.append(thread)

# Uruchamiamy wątki
for thread in threads:
    thread.start()

# Czekamy na zakończenie wszystkich wątków
for thread in threads:
    thread.join()

print("All counters have completed.")
```

---

### Wyjaśnienie drugiego przykładu:

1. **Klasa `CounterThread`**:
    
    - Dziedziczy po `threading.Thread` i implementuje logikę w metodzie `run()`.
    - Każdy wątek liczy do określonej liczby (`count_to`).
2. **Uruchamianie wątków**:
    
    - `start()` wywołuje metodę `run()` w osobnym wątku.
3. **Niezależne liczenie**:
    
    - Każdy wątek liczy równolegle, niezależnie od innych wątków.

---

### Ograniczenia `threading`:

- **Global Interpreter Lock (GIL):** W zadaniach CPU-bound (np. skomplikowane obliczenia) wielowątkowość nie przynosi korzyści. W takich przypadkach lepiej używać biblioteki `multiprocessing`.

---

### Kiedy używać wielowątkowości?

- Operacje I/O (sieć, pliki, baza danych).
- Obsługa wielu użytkowników w aplikacji sieciowej.
- Zadania, które mogą działać równolegle, nie wpływając na siebie.

Dzięki temu wątek główny aplikacji (np. interfejs użytkownika) pozostaje responsywny, a zadania w tle mogą być obsługiwane efektywnie. 😊