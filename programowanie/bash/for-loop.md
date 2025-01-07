---
Utworzono: 2024-10-31T13:35:00
Zmodyfikowano: 2024-10-31T13:35:00
Źródło: chatGPT
tags:
---

W Bash składnia pętli `for` może przyjmować kilka różnych form, w zależności od tego, co chcemy osiągnąć. Oto podstawowe konstrukcje:

1. **Pętla `for` iterująca po liście elementów:**

   ```bash
   for item in item1 item2 item3; do
       echo "Przetwarzam $item"
   done
   ```

   Tutaj `item` przyjmuje wartość kolejnych elementów: `item1`, `item2`, `item3`.

2. **Pętla `for` z sekwencją liczb (korzysta z polecenia `seq`):**

   ```bash
   for i in $(seq 1 5); do
       echo "Liczba: $i"
   done
   ```

   Można też skorzystać z `{}` zamiast `seq`:

   ```bash
   for i in {1..5}; do
       echo "Liczba: $i"
   done
   ```

3. **Pętla `for` w stylu C (dla iteracji liczbowej z warunkiem i inkrementacją):**

   ```bash
   for (( i=0; i<5; i++ )); do
       echo "Indeks: $i"
   done
   ```

   Tutaj `i` zaczyna od `0` i zwiększa się o `1` aż do `4`.

4. **Pętla `for` iterująca po plikach w katalogu:**

   ```bash
   for file in /ścieżka/do/katalogu/*; do
       echo "Plik: $file"
   done
   ```

   W tym przypadku `for` iteruje po wszystkich plikach i folderach w zadanej ścieżce.

---

Każda z tych konstrukcji używa `do ... done` do oznaczenia bloku, który ma być wykonywany dla każdej iteracji pętli.