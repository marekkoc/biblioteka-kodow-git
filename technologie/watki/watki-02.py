"""

Wątki w Pythonie

C: 2025.01.20
M: 2025.01.20
"""

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
