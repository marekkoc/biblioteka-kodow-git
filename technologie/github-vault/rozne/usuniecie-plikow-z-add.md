---
Utworzono: 2025-02-17
Zmodyfikowano: 2025-02-17
Źródło: 
tags: 
Katalog:
---

# niechcacy dodalem kilka plkow do repozytorium github za pomoca git add. nie zrobilem jeszcze commitu. jak cofnac ta operacje?

Aby cofnąć operację `git add` (czyli usunąć pliki ze stagingu area), możesz użyć komendy:

```bash
git reset
```

Ta komenda usunie wszystkie pliki ze stagingu area (te, które zostały dodane przez `git add`).

Jeśli chcesz cofnąć `git add` tylko dla konkretnych plików, możesz użyć:

```bash
git reset NAZWA_PLIKU
```

Na przykład:
```bash
git reset plik1.txt
git reset folder/plik2.py
```

Możesz też sprawdzić status plików przed i po operacji używając:
```bash
git status
```