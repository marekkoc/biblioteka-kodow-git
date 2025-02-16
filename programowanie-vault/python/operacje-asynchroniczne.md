---
Utworzono: 2025-02-15T11:27:00
Zmodyfikowano: 2025-02-15T11:27:00
Źródło: 
tags: 
Katalog:
---

Postaram się wyjaśnić operacje asynchroniczne w Pythonie w przystępny sposób.

Operacje asynchroniczne pozwalają na wykonywanie zadań "w tle", bez blokowania głównego wątku programu. Wyobraź sobie, że jesteś w restauracji:

Podejście synchroniczne (tradycyjne):
```python
def zamow_obiad():
    przygotuj_zupe()  # czekamy 10 minut
    przygotuj_drugie_danie()  # czekamy 20 minut
    przygotuj_deser()  # czekamy 5 minut
    # Całkowity czas oczekiwania: 35 minut
```

Podejście asynchroniczne:
```python
async def zamow_obiad():
    zupa = await przygotuj_zupe()  # rozpoczynamy przygotowanie zupy
    drugie = await przygotuj_drugie_danie()  # w międzyczasie rozpoczynamy drugie danie
    deser = await przygotuj_deser()  # rozpoczynamy deser
    # Zadania wykonują się współbieżnie, całkowity czas może być krótszy
```

W Pythonie mamy do tego specjalną składnię:
- `async def` - definicja funkcji asynchronicznej
- `await` - oczekiwanie na zakończenie operacji asynchronicznej
- `asyncio` - biblioteka do obsługi operacji asynchronicznych

Praktyczny przykład - pobieranie danych z kilku źródeł jednocześnie:

```python
import asyncio
import aiohttp  # asynchroniczna biblioteka HTTP

async def pobierz_dane(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = [
        'http://api.example.com/data1',
        'http://api.example.com/data2',
        'http://api.example.com/data3'
    ]
    
    # Pobieramy dane równolegle
    tasks = [pobierz_dane(url) for url in urls]
    wyniki = await asyncio.gather(*tasks)
    
    return wyniki

# Uruchamiamy
asyncio.run(main())
```

Kluczowe korzyści:
1. Lepsze wykorzystanie zasobów - podczas oczekiwania na I/O (np. sieć, dysk) program może wykonywać inne zadania
2. Większa responsywność aplikacji - główny wątek nie jest blokowany
3. Lepsza skalowalność - możemy obsłużyć więcej równoczesnych operacji

Warto pamiętać, że:
- Asynchroniczność nie oznacza wielowątkowości - wszystko działa w jednym wątku
- Najlepiej sprawdza się dla operacji I/O-bound (sieć, dysk)
- Dla operacji CPU-bound lepiej użyć wielowątkowości (threading) lub wieloprocesowości (multiprocessing)

Czy chciałbyś, żebym rozwinął któryś z tych aspektów lub pokazał więcej przykładów?

# Tak, poprosze. Potrzebuje wiecej wyjasnien i przykładów asynchroincznosci bo to jest zuepłnie nowy temat dla mnie. Gdzie to stosowac? Jak? Co jeszcze o tym powinienem wiedziec? Co jest ważne?

Dobrze, rozszerzę temat i pokażę więcej praktycznych przykładów.

1. Gdzie stosować asynchroniczność:
```python
# DOBRE zastosowania async:
- Aplikacje webowe (FastAPI, aiohttp)
- Operacje na bazach danych (aiosqlite, asyncpg)
- Scrapowanie stron internetowych
- Pobieranie plików
- Obsługa websocketów
- API klienty

# NIE WARTO używać async dla:
- Ciężkich obliczeń matematycznych
- Przetwarzania obrazów
- Kompresji danych
- Operacji na dużych tablicach numpy
```

Przykład praktyczny - scraper stron www:
```python
import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def pobierz_tytul(session, url):
    try:
        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            return soup.title.text
    except Exception as e:
        return f"Błąd dla {url}: {str(e)}"

async def main():
    urls = [
        'http://python.org',
        'http://pypi.org',
        'http://github.com'
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [pobierz_tytul(session, url) for url in urls]
        tytuly = await asyncio.gather(*tasks)
        
    for url, tytul in zip(urls, tytuly):
        print(f"{url}: {tytul}")

asyncio.run(main())
```

2. Obsługa błędów w async:
```python
async def bezpieczna_operacja():
    try:
        async with timeout(5):  # limit czasu wykonania
            await długa_operacja()
    except asyncio.TimeoutError:
        print("Operacja trwała zbyt długo!")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
```

1. Przykład z bazą danych (asyncpg - PostgreSQL):
```python
import asyncpg

async def pobierz_dane():
    conn = await asyncpg.connect(
        user='user',
        password='password',
        database='dbname',
        host='localhost'
    )
    
    # Wykonaj kilka zapytań równolegle
    async with conn.transaction():
        zapytania = [
            conn.fetch("SELECT * FROM users"),
            conn.fetch("SELECT * FROM orders"),
            conn.fetch("SELECT * FROM products")
        ]
        users, orders, products = await asyncio.gather(*zapytania)
    
    await conn.close()
    return users, orders, products
```

2. FastAPI - przykład asynchronicznego API:
```python
from fastapi import FastAPI
from typing import List

app = FastAPI()

@app.get("/dane/{user_id}")
async def pobierz_dane_uzytkownika(user_id: int):
    # Równoległe pobieranie różnych typów danych
    profil = await pobierz_profil(user_id)
    zamowienia = await pobierz_zamowienia(user_id)
    preferencje = await pobierz_preferencje(user_id)
    
    return {
        "profil": profil,
        "zamowienia": zamowienia,
        "preferencje": preferencje
    }
```

Ważne koncepcje do zapamiętania:

3. Event Loop:
```python
# Event loop to serce asyncio
import asyncio

async def main():
    # Twoje zadania

# Metoda 1 - prosta
asyncio.run(main())

# Metoda 2 - większa kontrola
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
```

4. Tasks vs. Coroutines:
```python
async def zadanie():
    await asyncio.sleep(1)
    return "Gotowe"

# Utworzenie task
task = asyncio.create_task(zadanie())

# Oczekiwanie na wynik
wynik = await task
```

5. Asynchroniczne konteksty (async with):
```python
class AsyncResource:
    async def __aenter__(self):
        # Inicjalizacja zasobu
        print("Rozpoczynam")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # Sprzątanie
        print("Kończę")

async def main():
    async with AsyncResource():
        await some_operation()
```

Najważniejsze wskazówki:

6. Nie mieszaj sync i async:
```python
# ŹLE:
async def funkcja():
    time.sleep(1)  # blokujące!

# DOBRZE:
async def funkcja():
    await asyncio.sleep(1)  # nie-blokujące
```

7. Uważaj na blokujące operacje:
```python
# Jeśli musisz użyć blokującej funkcji:
async def funkcja():
    wynik = await asyncio.to_thread(blocking_function)
```

8. Używaj async for dla asynchronicznych iteratorów:
```python
async for item in async_iterator:
    await process_item(item)
```

9. Pamiętaj o obsłudze zamykania zasobów:
```python
async def main():
    try:
        async with aiohttp.ClientSession() as session:
            # operacje
    finally:
        # sprzątanie
```

Czy któryś z tych aspektów chciałbyś, żebym bardziej szczegółowo wyjaśnił?

# TAk, podaj proszę wiecej przykładów na scrapowanie stron www

Pokażę kilka praktycznych przykładów scrapowania stron z użyciem asyncio i aiohttp.

1. Podstawowy scraper z obsługą limitu równoczesnych połączeń:

```python
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from typing import List
import logging

class AsyncScraper:
    def __init__(self, max_concurrent_requests=10):
        self.semaphore = asyncio.Semaphore(max_concurrent_requests)
        self.session = None
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()
    
    async def fetch_page(self, url: str) -> str:
        async with self.semaphore:  # Limit równoczesnych połączeń
            try:
                async with self.session.get(url) as response:
                    if response.status == 200:
                        return await response.text()
                    logging.error(f"Błąd {response.status} dla {url}")
                    return ""
            except Exception as e:
                logging.error(f"Wyjątek dla {url}: {str(e)}")
                return ""

    async def scrape_articles(self, urls: List[str]):
        tasks = [self.fetch_page(url) for url in urls]
        pages = await asyncio.gather(*tasks)
        
        results = []
        for url, html in zip(urls, pages):
            if html:
                soup = BeautifulSoup(html, 'html.parser')
                article = {
                    'url': url,
                    'title': soup.find('h1').text.strip() if soup.find('h1') else 'Brak tytułu',
                    'content': soup.find('article').text.strip() if soup.find('article') else 'Brak treści'
                }
                results.append(article)
        return results

async def main():
    urls = [
        'https://python.org/news',
        'https://pypi.org/project/aiohttp',
        # ... więcej URLi
    ]
    
    async with AsyncScraper(max_concurrent_requests=5) as scraper:
        articles = await scraper.scrape_articles(urls)
        for article in articles:
            print(f"URL: {article['url']}")
            print(f"Tytuł: {article['title']}\n")

if __name__ == "__main__":
    asyncio.run(main())
```

2. Scraper z paginacją i zapisem do pliku:

```python
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import json
import aiofiles

class PaginatedScraper:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = None
        self.results = []

    async def init_session(self):
        self.session = aiohttp.ClientSession(
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        )

    async def close_session(self):
        if self.session:
            await self.session.close()

    async def get_page_count(self) -> int:
        async with self.session.get(f"{self.base_url}/page/1") as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            # Przykładowa logika znajdowania liczby stron
            pagination = soup.find('div', class_='pagination')
            if pagination:
                return int(pagination.find_all('a')[-2].text)
            return 1

    async def scrape_page(self, page_num: int):
        url = f"{self.base_url}/page/{page_num}"
        async with self.session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            
            items = soup.find_all('div', class_='item')
            page_results = []
            
            for item in items:
                data = {
                    'title': item.find('h2').text.strip() if item.find('h2') else '',
                    'price': item.find('span', class_='price').text.strip() if item.find('span', class_='price') else '',
                    'description': item.find('p', class_='description').text.strip() if item.find('p', class_='description') else ''
                }
                page_results.append(data)
            
            return page_results

    async def save_results(self, filename: str):
        async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
            await f.write(json.dumps(self.results, ensure_ascii=False, indent=2))

    async def run(self):
        await self.init_session()
        try:
            page_count = await self.get_page_count()
            tasks = [self.scrape_page(i) for i in range(1, page_count + 1)]
            results = await asyncio.gather(*tasks)
            
            # Spłaszczenie listy wyników
            self.results = [item for sublist in results for item in sublist]
            
            # Zapis do pliku
            await self.save_results('wyniki.json')
            
        finally:
            await self.close_session()

async def main():
    scraper = PaginatedScraper('https://example.com/products')
    await scraper.run()

if __name__ == "__main__":
    asyncio.run(main())
```

1. Scraper z kolejką zadań i postępem:

```python
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from asyncio import Queue
from tqdm import tqdm
import time

class QueuedScraper:
    def __init__(self, num_workers=5):
        self.queue = Queue()
        self.num_workers = num_workers
        self.session = None
        self.results = []
        self.pbar = None

    async def worker(self, worker_id: int):
        while True:
            try:
                url = await self.queue.get()
                if url is None:  # Sygnał zakończenia
                    break

                async with self.session.get(url) as response:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    
                    # Przykładowe wyciąganie danych
                    data = {
                        'url': url,
                        'title': soup.find('title').text if soup.find('title') else '',
                        'timestamp': time.time()
                    }
                    self.results.append(data)
                    
                    self.pbar.update(1)
                    await asyncio.sleep(1)  # Opóźnienie między requestami
            
            except Exception as e:
                print(f"Błąd w worker {worker_id}: {str(e)}")
            finally:
                self.queue.task_done()

    async def run(self, urls: list):
        self.session = aiohttp.ClientSession()
        self.pbar = tqdm(total=len(urls))

        # Dodaj URLe do kolejki
        for url in urls:
            await self.queue.put(url)

        # Uruchom workery
        workers = []
        for i in range(self.num_workers):
            worker = asyncio.create_task(self.worker(i))
            workers.append(worker)

        # Dodaj sygnały zakończenia
        for _ in range(self.num_workers):
            await self.queue.put(None)

        # Czekaj na zakończenie wszystkich workerów
        await asyncio.gather(*workers)
        await self.session.close()
        self.pbar.close()

async def main():
    urls = [
        'https://python.org',
        'https://docs.python.org',
        'https://pypi.org',
        # ... więcej URLi
    ]

    scraper = QueuedScraper(num_workers=3)
    await scraper.run(urls)
    
    # Wyświetl wyniki
    for result in scraper.results:
        print(f"URL: {result['url']}")
        print(f"Tytuł: {result['title']}")
        print(f"Timestamp: {result['timestamp']}\n")

if __name__ == "__main__":
    asyncio.run(main())
```

Każdy z tych przykładów pokazuje inne podejście do scrapowania:
2. Pierwszy przykład koncentruje się na bezpiecznym pobieraniu z limitem równoczesnych połączeń
3. Drugi pokazuje jak obsłużyć paginację i zapisywać wyniki do pliku
4. Trzeci wykorzystuje kolejkę zadań i pokazuje postęp

Ważne aspekty do zapamiętania przy scrapowaniu:
- Zawsze dodawaj opóźnienia między requestami
- Używaj User-Agent w nagłówkach
- Obsługuj błędy i timeout
- Limituj liczbę równoczesnych połączeń
- Zapisuj wyniki na bieżąco (nie trzymaj wszystkiego w pamięci)

Chciałbyś, żebym rozwinął któryś z tych aspektów lub pokazał jeszcze inne przykłady?

#  Podaj mi 3-4 praktycze przykłady scrpawoania, coś w miarę prostego, jakieś praktyczne zastosowania, bo to tez jest dla mnie nowy temat


Pokażę Ci 4 praktyczne i względnie proste przykłady scrapowania:

1. Pobieranie cen produktów z e-sklepu:

```python
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import csv

async def scrape_product_prices():
    # Lista produktów do śledzenia
    products = [
        'https://www.sklep.pl/product1',
        'https://www.sklep.pl/product2',
        'https://www.sklep.pl/product3'
    ]
    
    async with aiohttp.ClientSession() as session:
        async def get_price(url):
            try:
                async with session.get(url) as response:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    # Dostosuj selektor do konkretnego sklepu
                    price = soup.find('span', class_='price').text.strip()
                    name = soup.find('h1', class_='product-name').text.strip()
                    return {'name': name, 'price': price, 'url': url}
            except Exception as e:
                print(f"Błąd dla {url}: {e}")
                return None

        results = await asyncio.gather(*[get_price(url) for url in products])
        results = [r for r in results if r]  # Usuń None

        # Zapisz wyniki do CSV
        with open('ceny.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['name', 'price', 'url'])
            writer.writeheader()
            writer.writerows(results)

asyncio.run(scrape_product_prices())
```

2. Pobieranie najnowszych artykułów z portalu informacyjnego:

```python
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from datetime import datetime

async def scrape_news():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://example-news.com') as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            
            # Znajdź wszystkie artykuły na stronie głównej
            articles = soup.find_all('article', class_='news-item')
            
            news_list = []
            for article in articles[:10]:  # Weź 10 najnowszych
                title = article.find('h2').text.strip()
                link = article.find('a')['href']
                date = article.find('time').text.strip()
                
                news_list.append({
                    'title': title,
                    'link': link,
                    'date': date
                })
            
            # Zapisz do pliku z datą
            current_date = datetime.now().strftime('%Y-%m-%d')
            with open(f'news_{current_date}.txt', 'w', encoding='utf-8') as f:
                for news in news_list:
                    f.write(f"Tytuł: {news['title']}\n")
                    f.write(f"Link: {news['link']}\n")
                    f.write(f"Data: {news['date']}\n")
                    f.write("-" * 50 + "\n")

asyncio.run(scrape_news())
```

1. Pobieranie ofert pracy z portalu:

```python
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import json

async def scrape_job_offers():
    keywords = ['python', 'javascript', 'java']
    
    async with aiohttp.ClientSession() as session:
        async def get_jobs_for_keyword(keyword):
            url = f'https://example-jobs.com/search?q={keyword}'
            async with session.get(url) as response:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                
                jobs = []
                for job in soup.find_all('div', class_='job-offer'):
                    jobs.append({
                        'title': job.find('h3').text.strip(),
                        'company': job.find('span', class_='company').text.strip(),
                        'salary': job.find('span', class_='salary').text.strip(),
                        'keyword': keyword
                    })
                return jobs

        all_jobs = await asyncio.gather(*[get_jobs_for_keyword(kw) for kw in keywords])
        # Spłaszcz listę wyników
        flat_jobs = [job for jobs in all_jobs for job in jobs]
        
        # Zapisz do JSON
        with open('oferty_pracy.json', 'w', encoding='utf-8') as f:
            json.dump(flat_jobs, f, ensure_ascii=False, indent=2)

asyncio.run(scrape_job_offers())
```

2. Pobieranie pogody dla różnych miast:

```python
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

async def scrape_weather():
    cities = ['warsaw', 'krakow', 'gdansk', 'wroclaw', 'poznan']
    
    async with aiohttp.ClientSession() as session:
        async def get_weather(city):
            url = f'https://example-weather.com/{city}'
            try:
                async with session.get(url) as response:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    
                    temp = soup.find('span', class_='temperature').text.strip()
                    conditions = soup.find('div', class_='conditions').text.strip()
                    
                    return {
                        'city': city,
                        'temperature': temp,
                        'conditions': conditions,
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M')
                    }
            except Exception as e:
                print(f"Błąd dla {city}: {e}")
                return None

        weather_data = await asyncio.gather(*[get_weather(city) for city in cities])
        weather_data = [w for w in weather_data if w]  # Usuń None
        
        # Zapisz do Excel używając pandas
        df = pd.DataFrame(weather_data)
        df.to_excel(f'pogoda_{datetime.now().strftime("%Y%m%d")}.xlsx', index=False)

asyncio.run(scrape_weather())
```

Kilka ważnych wskazówek przy scrapowaniu:

3. Zawsze sprawdź politykę strony (robots.txt) i warunki użytkowania
4. Dodaj opóźnienia między requestami:
```python
await asyncio.sleep(1)  # 1 sekunda między requestami
```

5. Używaj właściwych nagłówków:
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}
session = aiohttp.ClientSession(headers=headers)
```

6. Zapisuj dane regularnie na wypadek błędów:
```python
# Co 10 elementów zapisuj do pliku
if len(results) % 10 == 0:
    save_checkpoint(results)
```

Chciałbyś, żebym któryś z tych przykładów rozwinął lub pokazał, jak można je zmodyfikować do konkretnych potrzeb?

# nie, na razie dziekuje. Wrocmy jedanak do poprzedniego watkiu NIE WARTO używać async dla:
 - Ciężkich obliczeń matematycznych 
- Przetwarzania obrazów - Kompresji danych
 - Operacji na dużych tablicach numpy

co warto stosowac w tych przypadkach, podaj prosze przyklady

W przypadku operacji obliczeniowo intensywnych (CPU-bound) najlepiej wykorzystać wielowątkowość (threading) lub wieloprocesowość (multiprocessing). Oto przykłady:

1. Przetwarzanie obrazów z użyciem multiprocessing:

```python
from multiprocessing import Pool
from PIL import Image
import os

def process_image(image_path):
    # Otwórz obraz
    with Image.open(image_path) as img:
        # Przykładowe operacje
        img = img.resize((800, 600))
        img = img.convert('L')  # Konwersja do skali szarości
        
        # Zapisz wynik
        output_path = f"processed_{os.path.basename(image_path)}"
        img.save(output_path)
        return output_path

def process_multiple_images(image_paths):
    # Utworzenie puli procesów
    with Pool() as pool:
        # Mapowanie funkcji na wszystkie obrazy
        results = pool.map(process_image, image_paths)
    return results

# Użycie:
images = ['image1.jpg', 'image2.jpg', 'image3.jpg']
processed = process_multiple_images(images)
```

2. Obliczenia numeryczne z NumPy używając multiprocessing:

```python
import numpy as np
from multiprocessing import Pool

def heavy_calculation(matrix):
    # Przykładowe obliczenia
    result = np.linalg.svd(matrix)
    eigenvalues = np.linalg.eigvals(matrix)
    return {'svd': result, 'eigenvalues': eigenvalues}

def process_matrices(matrices):
    with Pool() as pool:
        results = pool.map(heavy_calculation, matrices)
    return results

# Użycie:
matrices = [np.random.rand(1000, 1000) for _ in range(5)]
results = process_matrices(matrices)
```

1. Kompresja danych z threading:

```python
import zlib
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

def compress_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    compressed = zlib.compress(data, level=9)
    
    output_path = str(file_path) + '.gz'
    with open(output_path, 'wb') as f:
        f.write(compressed)
    return output_path

def compress_multiple_files(file_paths, max_workers=4):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(compress_file, file_paths))
    return results

# Użycie:
files = ['data1.txt', 'data2.txt', 'data3.txt']
compressed_files = compress_multiple_files(files)
```

2. Złożone obliczenia matematyczne z wykorzystaniem obu podejść:

```python
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
import numpy as np
from scipy import optimize

def complex_optimization(params):
    # Przykładowa funkcja do optymalizacji
    def objective(x):
        return np.sum(np.sin(x) * np.cos(x ** 2) + x ** 2)
    
    result = optimize.minimize(objective, params, method='Nelder-Mead')
    return result.x

def parallel_calculations(parameter_sets):
    # Dla bardzo intensywnych obliczeń używamy multiprocessing
    with Pool() as pool:
        results = pool.map(complex_optimization, parameter_sets)
    return results

def mixed_parallel_processing(data_chunks):
    # Przykład mieszanego podejścia
    def process_chunk(chunk):
        # Obliczenia na jednym chunku danych
        processed = np.fft.fft2(chunk)
        filtered = np.fft.ifft2(processed)
        return filtered.real
    
    # Używamy ThreadPoolExecutor dla operacji I/O
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Ale właściwe obliczenia wykonujemy w osobnych procesach
        with Pool() as pool:
            results = []
            for chunk in data_chunks:
                # Wstępne przetwarzanie w wątkach
                future = executor.submit(process_chunk, chunk)
                # Główne obliczenia w osobnych procesach
                result = pool.apply_async(complex_optimization, (future.result(),))
                results.append(result)
            
            # Zbieramy wszystkie wyniki
            final_results = [r.get() for r in results]
    
    return final_results

# Użycie:
data = [np.random.rand(100) for _ in range(10)]
results = parallel_calculations(data)
```

3. Przetwarzanie dużych zbiorów danych z pandas:

```python
import pandas as pd
from multiprocessing import Pool
import numpy as np

def process_chunk(chunk):
    # Przykładowe obliczenia na chunku danych
    result = chunk.groupby('category').agg({
        'value': ['mean', 'std', 'sum'],
        'count': 'count'
    })
    return result

def parallel_dataframe_processing(df, chunk_size=10000):
    # Dzielimy DataFrame na chunki
    chunks = [df[i:i+chunk_size] for i in range(0, len(df), chunk_size)]
    
    # Przetwarzamy chunki równolegle
    with Pool() as pool:
        results = pool.map(process_chunk, chunks)
    
    # Łączymy wyniki
    final_result = pd.concat(results)
    return final_result

# Użycie:
df = pd.DataFrame({
    'category': np.random.choice(['A', 'B', 'C'], size=100000),
    'value': np.random.randn(100000),
    'count': np.random.randint(1, 100, size=100000)
})

result = parallel_dataframe_processing(df)
```

Główne zasady:

4. Użyj multiprocessing gdy:
- Masz obliczenia intensywne procesorowo
- Operacje są niezależne od siebie
- Dane można łatwo podzielić na części

5. Użyj threading gdy:
- Operacje zawierają dużo I/O
- Potrzebujesz współdzielić pamięć między wątkami
- Masz ograniczenia w zasobach systemowych

6. Użyj połączenia obu gdy:
- Masz mieszane operacje (I/O i CPU)
- Potrzebujesz elastycznego zarządzania zasobami
- Pracujesz z dużymi zbiorami danych

Chciałbyś, żebym któryś z tych przykładów rozwinął lub pokazał inne zastosowania?