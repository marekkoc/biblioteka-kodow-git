"""

Wątki w Pythonie

C: 2025.01.20
M: 2025.01.20
"""

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
        print(f" [Wątek 2] Iteracja {i + 1}")
        time.sleep(0.8)  # Inny czas oczekiwania

# Funkcja dla trzeciego wątku
def funkcja3():
    for i in range(5):
        print(f"  [Wątek 3] Iteracja {i + 1}")
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
