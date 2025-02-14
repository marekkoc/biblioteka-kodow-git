---
Utworzono: 2025-02-13T12:58:00
Zmodyfikowano: 2025-02-13T12:58:00
Źródło: Claude
tags: 
Katalog:
---

Token to ciąg znaków służący do uwierzytelniania i autoryzacji w aplikacjach. W kontekście bezpieczeństwa, możemy wyróżnić kilka typów tokenów:

1. Access Token - tymczasowy token używany do uwierzytelniania żądań API
2. Refresh Token - długoterminowy token służący do odświeżania access tokenów
3. JWT (JSON Web Token) - token zawierający zakodowane informacje o użytkowniku

Jeśli chodzi o przechowywanie tokenów, oto najlepsze praktyki:

W aplikacjach webowych:
- Access tokeny: przechowywać w pamięci aplikacji (zmiennych)
- Refresh tokeny: w httpOnly cookies
- Nigdy nie przechowywać w localStorage ze względu na podatność na ataki XSS

W aplikacjach backendowych:
- Używać zmiennych środowiskowych (.env)
- W przypadku Pythona można użyć bibliotek jak python-dotenv
- Przykład:

```python
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
```

W systemach produkcyjnych:
- Używać menedżerów sekretów (np. AWS Secrets Manager, HashiCorp Vault)
- Szyfrować tokeny przed zapisem do bazy danych
- Regularnie rotować tokeny

Nigdy nie należy:
- Commitować tokenów do repozytorium git
- Przechowywać w kodzie źródłowym
- Zapisywać w zwykłych plikach tekstowych

Czy chciałbyś poznać bardziej szczegółowe informacje na temat któregoś z tych aspektów?

---

Rozumiem Twoje wątpliwości. Postaram się to wyjaśnić krok po kroku w praktyczny sposób:

1. Podczas developmentu lokalnego:
```python
# 1. Utwórz plik .env w głównym katalogu projektu
API_TOKEN=twój_tajny_token_123

# 2. Dodaj .env do .gitignore
echo ".env" >> .gitignore

# 3. W kodzie używaj:
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('API_TOKEN')
```

2. Dla aplikacji produkcyjnej masz kilka opcji:

a) Na własnym serwerze:
- Użyj zmiennych środowiskowych systemu:
```bash
# Na serwerze Linux
export API_TOKEN=twój_tajny_token_123

# W pliku systemowym (np. /etc/environment lub ~/.bashrc)
API_TOKEN=twój_tajny_token_123
```

b) W chmurze:
- AWS: używaj AWS Secrets Manager
```python
import boto3

def get_secret():
    session = boto3.session.Session()
    client = session.client('secretsmanager')
    response = client.get_secret_value(SecretId='nazwa_twojego_sekretu')
    return response['SecretString']
```

- Heroku: używaj Config Vars (przez panel lub CLI)
```bash
heroku config:set API_TOKEN=twój_tajny_token_123
```

1. Dla aplikacji desktopowej:
- Możesz użyć systemowego keyring:
```python
import keyring

# Zapisz token
keyring.set_password("nazwa_twojej_aplikacji", "api_token", "twój_tajny_token_123")

# Odczytaj token
token = keyring.get_password("nazwa_twojej_aplikacji", "api_token")
```

2. Dla aplikacji mobilnej:
- Android: użyj EncryptedSharedPreferences
- iOS: użyj Keychain

Przykład prostego wzorca dla projektu:

```python
# config.py
import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.token = self._get_token()
    
    def _get_token(self):
        # Kolejność sprawdzania:
        # 1. Zmienne środowiskowe
        # 2. Plik .env
        # 3. Keyring (dla aplikacji desktopowej)
        token = os.getenv('API_TOKEN')
        if not token:
            try:
                import keyring
                token = keyring.get_password("twoja_aplikacja", "api_token")
            except:
                pass
        return token

# Użycie
config = Config()
api_token = config.token
```

Najważniejsze zasady:
3. W developmencie: używaj .env i upewnij się, że jest w .gitignore
4. W produkcji: używaj zmiennych środowiskowych lub menedżera sekretów
5. Dla aplikacji desktopowych: rozważ użycie systemowego keyring
6. NIGDY nie commituj tokenów do repozytorium
7. Zadbaj o backup tokenów w bezpiecznym miejscu (np. menedżer haseł)

Czy teraz jest to jaśniejsze? Jeśli masz konkretny przypadek użycia, mogę doradzić najlepsze rozwiązanie dla Twojej sytuacji.

---
Porównajmy szczegółowo rozwiązanie 1 (plik .env) i 2 (zmienne środowiskowe systemu):

**Rozwiązanie 1 - plik .env:**
```python
# Struktura projektu:
projekt/
  ├── .env            # Tu przechowujesz token
  ├── .gitignore      # Tu dodajesz ".env"
  ├── main.py
  └── requirements.txt # Dodajesz "python-dotenv"

# Zawartość .env:
API_TOKEN=twój_tajny_token_123

# Kod w Python:
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('API_TOKEN')
```

**Rozwiązanie 2 - zmienne środowiskowe:**
```bash
# W systemie Linux/Unix:
export API_TOKEN=twój_tajny_token_123

# Lub trwale w ~/.bashrc:
echo "export API_TOKEN=twój_tajny_token_123" >> ~/.bashrc
source ~/.bashrc

# W Windows (PowerShell):
$env:API_TOKEN = "twój_tajny_token_123"
# Lub przez Panel sterowania -> Zmienne środowiskowe

# Kod w Python (identyczny!):
import os
token = os.getenv('API_TOKEN')
```

**Zalety i wady każdego rozwiązania:**

Rozwiązanie 1 (.env):
+ Łatwe w konfiguracji dla zespołu (możesz dostarczyć .env.example)
+ Token jest związany z projektem
+ Działa tak samo na każdym systemie
- Musisz pamiętać o .gitignore
- Plik może zostać przypadkowo skopiowany
- Trzeba instalować dodatkową bibliotekę

Rozwiązanie 2 (zmienne środowiskowe):
+ Natywne wsparcie w systemie (nie potrzeba dodatkowych bibliotek)
+ Bezpieczniejsze - zmienna dostępna tylko dla danego użytkownika
+ Działa automatycznie po restarcie systemu (jeśli dodane do ~/.bashrc)
- Trudniejsze w konfiguracji dla zespołu
- Może być problematyczne przy wielu projektach (konflikty nazw)
- Różne sposoby konfiguracji na różnych systemach

**Moja rekomendacja:**
1. Dla developmentu lokalnego: użyj .env
   - Łatwiejsze w zarządzaniu dla zespołu
   - Możesz mieć różne pliki dla różnych środowisk
   - Przejrzysta dokumentacja w .env.example

2. Dla produkcji: użyj zmiennych środowiskowych
   - Bezpieczniejsze
   - Standardowe podejście w środowiskach produkcyjnych
   - Łatwiejsze w automatyzacji (CI/CD)

Przykład praktycznego podejścia łączącego oba rozwiązania:
```python
# config.py
import os
from dotenv import load_dotenv

def get_token():
    # Najpierw sprawdź zmienne środowiskowe
    token = os.getenv('API_TOKEN')
    
    if not token:
        # Jeśli nie znaleziono, spróbuj załadować z .env
        load_dotenv()
        token = os.getenv('API_TOKEN')
        
    if not token:
        raise ValueError("API_TOKEN nie został skonfigurowany!")
        
    return token
```

Czy któryś z tych aspektów wymaga dodatkowego wyjaśnienia?