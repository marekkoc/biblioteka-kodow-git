---
Utworzono: 2024-10-20T17:00:00
Zmodyfikowano: 2024-10-20T17:00:00
Źródło: chatGPT
tags:
---

Aby połączyć kilka repozytoriów Git w jedno i umieścić je jako podkatalogi w jednym repozytorium, można użyć funkcji **submodules** lub **subtree**. Poniżej przedstawię dwa podejścia:

### 1. Metoda z użyciem **Git Submodules**

Git Submodules pozwala na osadzenie jednego repozytorium w innym, zachowując niezależność każdego z nich. To dobry wybór, jeśli chcesz, aby podrepozytoria były zarządzane oddzielnie, ale dostępne w jednym głównym repozytorium.

#### Kroki:

1. **Utwórz nowe, główne repozytorium** lub przejdź do istniejącego:
   ```bash
   git init main-repo
   cd main-repo
   ```

2. **Dodaj istniejące repozytoria jako submoduły**:
   ```bash
   git submodule add <URL_repo1> subfolder1
   git submodule add <URL_repo2> subfolder2
   git submodule add <URL_repo3> subfolder3
   ```

   Na przykład:
   ```bash
   git submodule add https://github.com/user/repo1.git repo1
   git submodule add https://github.com/user/repo2.git repo2
   git submodule add https://github.com/user/repo3.git repo3
   ```

3. **Zatwierdź zmiany w głównym repozytorium**:
   ```bash
   git add .
   git commit -m "Dodano repozytoria jako submoduły"
   ```

4. **Aktualizacja submodułów**: Aby zaktualizować submoduły w przyszłości, musisz pobrać nowe zmiany w ich własnych repozytoriach:
   ```bash
   git submodule update --remote --merge
   ```

**Zalety:**
- Niezależność repozytoriów.
- Możliwość aktualizowania każdego subrepozytorium osobno.
  
**Wady:**
- Większa złożoność zarządzania.
- Musisz ręcznie aktualizować submoduły.

### 2. Metoda z użyciem **Git Subtree**

Git Subtree pozwala na integrację zawartości jednego repozytorium bez dodawania dodatkowej złożoności zarządzania. Wszystkie repozytoria są w pełni zintegrowane w głównym repozytorium.

#### Kroki:

1. **Utwórz nowe repozytorium** lub przejdź do istniejącego:
   ```bash
   git init main-repo
   cd main-repo
   ```

2. **Dodaj istniejące repozytoria jako poddrzewa**:
   - Najpierw dodaj repozytorium jako zdalne:
     ```bash
     git remote add repo1 https://github.com/user/repo1.git
     git remote add repo2 https://github.com/user/repo2.git
     git remote add repo3 https://github.com/user/repo3.git
     ```

   - Pobierz zawartość każdego repozytorium:
     ```bash
     git fetch repo1
     git fetch repo2
     git fetch repo3
     ```

   - Scal repozytoria jako podkatalogi:
     ```bash
     git subtree add --prefix=subfolder1 repo1 main
     git subtree add --prefix=subfolder2 repo2 main
     git subtree add --prefix=subfolder3 repo3 main
     ```

   - Na przykład, jeśli chcesz dodać repozytorium `repo1` do folderu `repo1` w swoim głównym repozytorium:
     ```bash
     git subtree add --prefix=repo1 https://github.com/user/repo1.git main
     ```

3. **Zatwierdź zmiany**:
   ```bash
   git add .
   git commit -m "Dodano repozytoria jako subtree"
   ```

4. **Aktualizacja subtree**:
   Aby zaktualizować podrepozytoria, można użyć:
   ```bash
   git subtree pull --prefix=subfolder1 repo1 main
   ```

**Zalety:**
- Prostsza integracja niż submoduły.
- Cała historia repozytorium jest przenoszona do głównego repozytorium.
  
**Wady:**
- Trudniejsza do aktualizacji i synchronizacji w porównaniu do submodułów, ale bardziej intuicyjna w użyciu.

### Którą metodę wybrać?

- Jeśli chcesz, aby każde repozytorium było oddzielnym projektem, łatwym do zaktualizowania i zarządzanym niezależnie — wybierz **Submodules**.
- Jeśli chcesz połączyć repozytoria na stałe, jako jedną całość, i nie potrzebujesz często aktualizować podrepozytoriów — wybierz **Subtree**.