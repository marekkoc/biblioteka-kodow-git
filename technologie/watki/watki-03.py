"""

Wątki w Pythonie

C: 2025.01.20
M: 2025.01.20
"""
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
