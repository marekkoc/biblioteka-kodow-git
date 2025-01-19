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
