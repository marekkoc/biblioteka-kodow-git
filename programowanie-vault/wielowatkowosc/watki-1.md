---
Utworzono: 2025-01-20T17:35:00
Zmodyfikowano: 2025-01-20T17:35:00
Źródło: chatGPT
tags: 
Katalog:
---

# Watki w Pythonie

Wielowątkowość w Pythonie polega na wykonywaniu wielu zadań równolegle w ramach jednego procesu. W Pythonie do tego celu najczęściej używamy modułu `threading`. Jednak warto pamiętać, że Python ma Global Interpreter Lock (GIL), który ogranicza jednoczesne wykonywanie wątków na jednym wątku CPU. Dlatego wielowątkowość w Pythonie jest szczególnie przydatna w przypadku operacji wejścia/wyjścia, a mniej przydatna do zadań intensywnych obliczeniowo.

Poniżej znajdziesz przykład programu, który tworzy trzy wątki wykonujące różne zadania. Każdy wątek będzie działał niezależnie i wykonywał swoją funkcję.

### Przykład z trzema wątkami

```python
import threading
import time

# Funkcja dla pierwszego wątku
def funkcja1():
    for i in range(5):
        print(f"[Wątek 1] Iteracja {i + 1}")
        time.sleep(1)  # Symulacja dłuższego zadania

# Funkcja dla drugiego wątku
def funkcja2():
    for i in range(5):
        print(f"[Wątek 2] Iteracja {i + 1}")
        time.sleep(0.8)  # Inny czas oczekiwania

# Funkcja dla trzeciego wątku
def funkcja3():
    for i in range(5):
        print(f"[Wątek 3] Iteracja {i + 1}")
        time.sleep(0.6)  # Jeszcze inny czas oczekiwania

# Tworzenie wątków
watki = []
watki.append(threading.Thread(target=funkcja1))
watki.append(threading.Thread(target=funkcja2))
watki.append(threading.Thread(target=funkcja3))

# Uruchamianie wątków
for watek in watki:
    watek.start()

# Oczekiwanie na zakończenie wszystkich wątków
for watek in watki:
    watek.join()

print("Wszystkie wątki zakończyły działanie.")
```

---

### Wyjaśnienie kodu

1. **Importowanie modułu `threading` i `time`**:
    
    - Moduł `threading` umożliwia tworzenie i zarządzanie wątkami.
    - Moduł `time` służy do symulacji opóźnień za pomocą funkcji `time.sleep()`.
2. **Definicja funkcji dla wątków**:
    
    - Każda funkcja symuluje zadanie, wypisując informacje o swojej iteracji w konsoli.
3. **Tworzenie wątków**:
    
    - Tworzymy listę wątków. Każdy wątek jest instancją klasy `threading.Thread`, a jego funkcja docelowa (`target`) to odpowiednia funkcja użytkownika (`funkcja1`, `funkcja2`, `funkcja3`).
4. **Uruchamianie wątków**:
    
    - Używamy `watek.start()` dla każdego wątku, co powoduje rozpoczęcie jego działania.
5. **Oczekiwanie na zakończenie wątków**:
    
    - Metoda `watek.join()` blokuje główny wątek programu do momentu zakończenia działania danego wątku.
6. **Końcowy komunikat**:
    
    - Po zakończeniu wszystkich wątków, główny wątek wyświetla komunikat.

---

### Przykładowe wyjście

Wyniki mogą być w różnej kolejności, ponieważ wątki działają równolegle:

```
[Wątek 1] Iteracja 1
[Wątek 2] Iteracja 1
[Wątek 3] Iteracja 1
[Wątek 3] Iteracja 2
[Wątek 2] Iteracja 2
[Wątek 1] Iteracja 2
...
Wszystkie wątki zakończyły działanie.
```

---

Jeśli masz pytania lub chcesz rozszerzyć przykład, daj znać! 😊

# watek.join() i Global Interpreter Lock (GIL)


### Wyjaśnienie `watek.join()`

Metoda `join()` w Pythonie jest używana do synchronizacji głównego wątku programu z wątkiem podrzędnym. Gdy wywołujesz `watek.join()`, główny wątek **zatrzymuje swoje działanie** i czeka, aż dany wątek podrzędny zakończy swoje zadanie.

---

#### Przykład działania `join()`

Wyobraź sobie, że w twoim programie tworzysz dwa wątki, a następnie chcesz, aby główny wątek wyświetlił komunikat dopiero po zakończeniu pracy obu wątków. Bez użycia `join()` główny wątek może zakończyć się wcześniej niż wątki podrzędne, co prowadzi do niepełnego działania programu.

Zastosowanie `join()` gwarantuje, że główny wątek poczeka na zakończenie działania wątków podrzędnych.

### Przykład z `join()`:

```python
import threading
import time

def funkcja():
    for i in range(3):
        print(f"[Wątek] Iteracja {i + 1}")
        time.sleep(1)

# Tworzymy wątek
watek = threading.Thread(target=funkcja)

# Uruchamiamy wątek
watek.start()

# Oczekiwanie na zakończenie wątku
watek.join()

print("Wątek zakończył działanie. Główny wątek kontynuuje.")
```

---

#### Co się dzieje w tym kodzie:

1. Wątek zaczyna swoje zadanie (`watek.start()`).
2. Główny wątek wywołuje `watek.join()`, więc **czeka**, aż funkcja w wątku zakończy wszystkie iteracje.
3. Dopiero po zakończeniu działania wątku, program kontynuuje wykonywanie dalszego kodu w głównym wątku i wyświetla komunikat `"Wątek zakończył działanie. Główny wątek kontynuuje."`.

Bez `join()`, komunikat z głównego wątku mógłby pojawić się przed zakończeniem działania wątku podrzędnego.

---

### Global Interpreter Lock (GIL) w Pythonie

GIL (Global Interpreter Lock) jest mechanizmem wbudowanym w interpreter CPython, który **zapewnia synchronizację** w wykonywaniu wątków.

---

#### Dlaczego istnieje GIL?

Python obsługuje dynamiczne zarządzanie pamięcią (np. garbage collector), co wymaga ochrony struktur pamięci przed równoczesnym dostępem. GIL:

1. **Chroni pamięć** w trakcie wykonywania kodu.
2. Zapobiega sytuacjom, w których dwa wątki jednocześnie modyfikują te same dane, co mogłoby prowadzić do niespójności danych.

---

#### Jak działa GIL?

1. GIL pozwala **tylko jednemu wątkowi** wykonywać kod Pythona w danej chwili, nawet na procesorach wielordzeniowych.
2. Wątek, który uzyska GIL, wykonuje swoje zadanie przez pewien czas (tzw. quantum czasu), a następnie GIL przechodzi do kolejnego wątku.

---

#### Problemy wynikające z GIL

- **Ograniczenie wielowątkowości na CPU**: W aplikacjach intensywnych obliczeniowo (np. przetwarzanie dużych ilości danych), GIL ogranicza wydajność, ponieważ tylko jeden wątek może korzystać z CPU w danej chwili.
- **Mniejsze korzyści na procesorach wielordzeniowych**: GIL sprawia, że Python nie w pełni wykorzystuje możliwości równoległego przetwarzania obliczeń na wielu rdzeniach.

---

#### Rozwiązania obejścia GIL:

1. **Użycie modułu `multiprocessing`**:
    
    - `multiprocessing` tworzy **osobne procesy**, które nie są ograniczone przez GIL (każdy proces ma swoją instancję interpretera Pythona).
    - Jest to bardziej efektywne w zadaniach obliczeniowych.
2. **Używanie bibliotek w językach niskopoziomowych**:
    
    - Biblioteki jak NumPy wykorzystują kod napisany w C/C++, który działa poza GIL.

---

#### Przykład działania GIL w wielowątkowości:

```python
import threading
import time

# Funkcja symulująca zadanie obliczeniowe
def obliczenia():
    x = 0
    for i in range(10**6):
        x += 1
    print(f"Zakończono obliczenia w wątku {threading.current_thread().name}")

# Tworzenie dwóch wątków
watek1 = threading.Thread(target=obliczenia)
watek2 = threading.Thread(target=obliczenia)

# Start obu wątków
start = time.time()
watek1.start()
watek2.start()

# Oczekiwanie na zakończenie wątków
watek1.join()
watek2.join()

end = time.time()
print(f"Czas wykonania: {end - start:.2f} sekund")
```

#### Wynik:

Wydajność obliczeń jest ograniczona, ponieważ GIL uniemożliwia równoległe wykonywanie kodu obliczeniowego w obu wątkach. Czas wykonania może być podobny do wykonania tych obliczeń w pojedynczym wątku.

---

Jeśli masz dodatkowe pytania, chętnie wyjaśnię! 😊

# Ten sam program z PyQt5

Poniżej znajdziesz kompletny przykład programu z wykorzystaniem **PyQt5**, który spełnia Twoje wymagania. Program tworzy trzy przyciski sterujące trzema wątkami. Każdy wątek ma osobny licznik, którego aktualna wartość jest wyświetlana na ekranie za pomocą kontrolki **QLCDNumber**.

### Kod programu

```python
import sys
import threading
import time
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLCDNumber


class Licznik(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wielowątkowość z PyQt5")
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

        # Stan wątków
        self.running_flags = [False, False, False]  # Flagi kontrolne dla każdego wątku
        self.threads = [None, None, None]  # Wątki

        # Połączenie przycisków z funkcjami
        self.button1.clicked.connect(lambda: self.toggle_thread(0, self.lcd1))
        self.button2.clicked.connect(lambda: self.toggle_thread(1, self.lcd2))
        self.button3.clicked.connect(lambda: self.toggle_thread(2, self.lcd3))

    def toggle_thread(self, thread_index, lcd):
        if self.running_flags[thread_index]:
            # Zatrzymaj wątek
            self.running_flags[thread_index] = False
            self.threads[thread_index].join()  # Czekamy na zakończenie wątku
            self.threads[thread_index] = None
        else:
            # Uruchom wątek
            self.running_flags[thread_index] = True
            self.threads[thread_index] = threading.Thread(
                target=self.run_counter, args=(thread_index, lcd), daemon=True
            )
            self.threads[thread_index].start()

    def run_counter(self, thread_index, lcd):
        count = 0
        while self.running_flags[thread_index]:
            count += 1
            lcd.display(count)  # Wyświetlenie wartości w liczniku
            time.sleep(0.5)  # Symulacja opóźnienia


if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = Licznik()
    okno.show()
    sys.exit(app.exec_())
```

---

### Wyjaśnienie działania programu

1. **Struktura GUI**:
    
    - **QLCDNumber**: Używane do wyświetlania aktualnej wartości licznika dla każdego wątku.
    - **QPushButton**: Trzy przyciski sterują wątkami (Start/Stop).
2. **Logika sterowania wątkami**:
    
    - Każdy wątek ma osobną flagę (`self.running_flags`), która kontroluje jego działanie.
    - Gdy przycisk jest wciśnięty:
        - Jeśli wątek działa, flaga jest ustawiana na `False`, co powoduje zatrzymanie wątku.
        - Jeśli wątek jest zatrzymany, tworzony jest nowy wątek i rozpoczyna działanie.
3. **Funkcja `run_counter`**:
    
    - Każdy wątek zwiększa swoją wartość licznika co 0.5 sekundy.
    - Wartość licznika jest wyświetlana na ekranie za pomocą metody `lcd.display(count)`.
4. **Metoda `join()`**:
    
    - Gdy wątek jest zatrzymywany, wywołujemy `join()`, aby upewnić się, że wątek zakończył działanie, zanim zostanie usunięty.
5. **Daemon threads**:
    
    - Wątki są oznaczone jako `daemon=True`, co oznacza, że zakończą swoje działanie automatycznie, gdy aplikacja zostanie zamknięta.

---

### Jak to działa?

- Po uruchomieniu programu pojawi się okno z trzema licznikami (kontrolki **QLCDNumber**) i trzema przyciskami.
- Kliknięcie przycisku `Start/Stop` dla konkretnego wątku spowoduje rozpoczęcie/zatrzymanie liczenia dla danego licznika.
- Wartości licznika będą się zwiększać co 0.5 sekundy, a wyniki będą wyświetlane w kontrolce LCD.

---

Jeśli potrzebujesz dalszych wyjaśnień lub modyfikacji, daj znać! 😊

# działanie funkcji toggle_thread ()

Funkcja `toggle_thread` w programie zarządza uruchamianiem i zatrzymywaniem konkretnego wątku. Przyjrzyjmy się jej krok po kroku:

```python
def toggle_thread(self, thread_index, lcd):
    if self.running_flags[thread_index]:
        # Zatrzymaj wątek
        self.running_flags[thread_index] = False
        self.threads[thread_index].join()  # Czekamy na zakończenie wątku
        self.threads[thread_index] = None
    else:
        # Uruchom wątek
        self.running_flags[thread_index] = True
        self.threads[thread_index] = threading.Thread(
            target=self.run_counter, args=(thread_index, lcd), daemon=True
        )
        self.threads[thread_index].start()
```

---

### Wyjaśnienie działania

#### Argumenty funkcji:

- **`thread_index`**: Numer (indeks) wątku w tablicach `self.threads` i `self.running_flags`.
- **`lcd`**: Obiekt `QLCDNumber`, który jest kontrolką przypisaną do licznika danego wątku.

---

### Logika funkcji:

#### 1. **Sprawdzenie stanu wątku**:

```python
if self.running_flags[thread_index]:
```

- Sprawdzamy flagę w tablicy `self.running_flags`, która informuje, czy dany wątek jest aktualnie uruchomiony.
    - `True`: Wątek działa.
    - `False`: Wątek jest zatrzymany.

---

#### 2. **Zatrzymanie wątku (jeśli działa)**:

```python
self.running_flags[thread_index] = False
self.threads[thread_index].join()
self.threads[thread_index] = None
```

- **`self.running_flags[thread_index] = False`**:
    - Ustawiamy flagę na `False`, co powoduje zatrzymanie pętli w funkcji `run_counter`.
- **`self.threads[thread_index].join()`**:
    - Czekamy, aż dany wątek zakończy swoje działanie. To gwarantuje, że wątek zakończy się całkowicie przed usunięciem jego obiektu.
- **`self.threads[thread_index] = None`**:
    - Usuwamy referencję do wątku, co pozwala na stworzenie nowego wątku w przyszłości.

---

#### 3. **Uruchomienie wątku (jeśli jest zatrzymany)**:

```python
self.running_flags[thread_index] = True
self.threads[thread_index] = threading.Thread(
    target=self.run_counter, args=(thread_index, lcd), daemon=True
)
self.threads[thread_index].start()
```

- **`self.running_flags[thread_index] = True`**:
    - Ustawiamy flagę na `True`, aby poinformować funkcję `run_counter`, że wątek powinien działać.
- **Tworzenie nowego wątku**:
    - Tworzymy instancję wątku z:
        - `target=self.run_counter`: Funkcja, którą wątek będzie wykonywać.
        - `args=(thread_index, lcd)`: Argumenty przekazywane do funkcji `run_counter`:
            - `thread_index`: Indeks wątku.
            - `lcd`: Kontrolka `QLCDNumber` do wyświetlania wartości licznika.
        - `daemon=True`: Oznacza, że wątek zakończy się automatycznie, gdy aplikacja zostanie zamknięta.
- **`self.threads[thread_index].start()`**:
    - Uruchamiamy wątek, który zaczyna wykonywać funkcję `run_counter`.

---

### Dlaczego `join()` jest potrzebne przy zatrzymywaniu wątku?

Bez `join()` główny wątek aplikacji (czyli GUI PyQt5) może kontynuować działanie, zanim wątek podrzędny zostanie w pełni zatrzymany. Może to prowadzić do problemów, takich jak:

- Wątek kontynuujący działanie po zamknięciu aplikacji.
- Błędy w zarządzaniu zasobami.

`join()` zapewnia, że główny wątek **czeka**, aż wątek podrzędny zakończy swoją pracę.

---

### Przykład działania funkcji `toggle_thread`:

1. Klikasz przycisk "Start/Stop Wątek 1".
    - Jeśli wątek 1 działa: zostaje zatrzymany, flaga zmienia się na `False`, a wątek kończy działanie.
    - Jeśli wątek 1 jest zatrzymany: zostaje utworzony nowy wątek, który zaczyna zliczać wartości w kontrolce `QLCDNumber`.

Jeśli coś wymaga dodatkowego objaśnienia, daj znać! 😊


# napisz teraz dokladnie ten sam program z pyQt5 ale z zastosowaniem QThread. Wyjasnij różnice napisz teraz dokladnie ten sam program z pyQt5 ale z zastosowaniem QThread. Wyjasnij różnice


Poniżej znajdziesz kompletną wersję programu, który wykorzystuje **QThread** zamiast klasycznego modułu `threading`. Wersja ta jest bardziej zgodna z filozofią PyQt, ponieważ **QThread** integruje zarządzanie wątkami z pętlą zdarzeń Qt, co pozwala uniknąć potencjalnych problemów z synchronizacją między GUI a wątkami.

---

### Kod programu z użyciem QThread

```python
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
```

---

### Wyjaśnienie kodu

#### **1. Użycie `QThread` zamiast `threading.Thread`**

- **QThread** to dedykowana klasa PyQt do zarządzania wątkami, która pozwala na komunikację między wątkiem a GUI za pomocą sygnałów i slotów.
- W naszym kodzie:
    - Klasa `CounterThread` dziedziczy po `QThread`.
    - Sygnał `updated` jest emitowany z wartością licznika, a GUI nasłuchuje tego sygnału i aktualizuje kontrolkę `QLCDNumber`.

---

#### **2. Funkcje `start` i `stop` w `QThread`**

- **`start()`**:
    - Wywołuje metodę `run()` w osobnym wątku.
- **`stop()`**:
    - Ustawia flagę `self.running` na `False`, co przerywa pętlę w metodzie `run`.
    - Wywołanie `self.wait()` zapewnia, że wątek zakończy swoje działanie przed kontynuacją programu.

---

#### **3. Synchronizacja za pomocą sygnałów**

- **Sygnał `updated`**:
    - Sygnały w PyQt umożliwiają bezpieczną komunikację między wątkami a główną pętlą GUI.
    - Wątek emituje sygnał `updated` z wartością licznika, a kontrolka LCD (przekazana jako `lcd`) wyświetla tę wartość.
- Dzięki tej metodzie unika się potencjalnych problemów z dostępem do wspólnych zasobów (np. GUI), co mogłoby się zdarzyć przy użyciu `threading.Thread`.

---

#### **4. Obsługa GUI**

- Główna logika zarządzania wątkami (start/stop) została przeniesiona do metody `toggle_thread`, co upraszcza kod.

---

### Różnice między `threading.Thread` a `QThread`

|**Cecha**|**`threading.Thread`**|**`QThread`**|
|---|---|---|
|**Integracja z PyQt**|Nie jest zoptymalizowane dla PyQt. Wymaga ręcznej synchronizacji z GUI.|Zapewnia wbudowaną integrację z sygnałami i slotami.|
|**Komunikacja z GUI**|Trzeba używać `queue` lub innych metod.|Używa sygnałów, co jest łatwiejsze i bezpieczniejsze.|
|**Zarządzanie zasobami**|Użytkownik musi ręcznie zarządzać wątkami i ich zakończeniem.|Metody takie jak `wait()` i `isRunning()` ułatwiają zarządzanie.|
|**Wydajność**|Działa niezależnie od frameworka.|Optymalizacja pod kątem aplikacji PyQt.|

---

### Główne zalety QThread

1. **Bezpieczeństwo GUI**:
    - Dzięki sygnałom i slotom GUI nie jest bezpośrednio manipulowane z wątku.
2. **Łatwość użycia**:
    - Zarządzanie wątkami i komunikacją jest bardziej intuicyjne.
3. **Lepsza integracja**:
    - QThread współpracuje z pętlą zdarzeń Qt, co jest idealne dla aplikacji PyQt.

---

Jeśli masz pytania lub chcesz coś zmodyfikować, daj znać! 😊