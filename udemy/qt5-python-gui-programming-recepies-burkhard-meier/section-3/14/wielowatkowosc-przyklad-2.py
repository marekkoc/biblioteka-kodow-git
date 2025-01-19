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