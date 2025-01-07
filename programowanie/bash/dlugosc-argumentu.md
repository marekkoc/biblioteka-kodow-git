---
Utworzono: 2024-10-31T13:36:00
Zmodyfikowano: 2024-10-31T13:36:00
Źródło: chatGPT
tags:
---

W języku Bash długość argumentu można policzyć, używając składni `${#argument}`. Oto przykład:

```bash
#!/bin/bash

# Sprawdzamy, czy został podany argument
if [ -z "$1" ]; then
    echo "Podaj argument!"
    exit 1
fi

# Liczymy długość pierwszego argumentu
dlugosc=${#1}
echo "Długość argumentu to: $dlugosc"
```

Tutaj `${#1}` zwraca liczbę znaków w pierwszym argumencie przekazanym do skryptu.