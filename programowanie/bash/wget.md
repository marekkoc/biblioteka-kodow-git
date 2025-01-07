---
Utworzono: 2024-10-20T12:17:00
Zmodyfikowano: 2024-10-20T12:17:00
Źródło: chatGPT
tags:
---

# Pobieranie strony za pomocą komendy *wget*

Aby pobrać stronę internetową za pomocą `wget`, łącznie z załącznikami (np. obrazkami, plikami CSS, JavaScript itp.), do 3 poziomu zagnieżdżenia (czyli linkami wewnętrznymi prowadzącymi do kolejnych stron), możesz skorzystać z następującej komendy:

```bash
wget -r -l 3 -k -p -E -H -D example.com https://example.com
```

**Wyjaśnienie opcji:**

- `-r` – włącza tryb rekurencyjny, który pozwala na pobieranie stron wraz z linkami prowadzącymi do innych stron.
- `-l 3` – określa maksymalną głębokość zagnieżdżenia (tutaj 3 poziomy).
- `-k` – zmienia linki na stronie tak, aby działały lokalnie po pobraniu (tzw. konwersja linków).
- `-p` – pobiera wszystkie zasoby niezbędne do poprawnego wyświetlenia strony, np. obrazki, pliki CSS, JavaScript itp.
- `-E` – zmienia rozszerzenie pobranych plików HTML na `.html`, co jest przydatne, gdy np. serwer nie dodaje rozszerzenia.
- `-H` – pozwala na pobieranie zasobów z różnych domen (jeśli są zewnętrzne linki do np. plików obrazków).
- `-D example.com` – ogranicza pobieranie zasobów do określonej domeny (tutaj: `example.com`), co pomaga uniknąć pobierania zasobów spoza interesującej nas strony. Zmień to na właściwą domenę.

Zastąp `https://example.com` adresem strony, którą chcesz pobrać.