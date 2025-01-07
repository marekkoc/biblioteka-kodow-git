---
Utworzono: 2024-12-17T07:06:00
Zmodyfikowano: 2024-12-18T07:07:00
Źródło: chatGPT
tags:
  - "#Duck-typing"
Katalog:
---

Tak, istnieje określenie na takie zjawisko w programowaniu. Nazywa się ono **duck typing** lub **strukturalny polimorfizm** w zależności od kontekstu i języka programowania.

### Wyjaśnienie:
- **Duck typing** to podejście charakterystyczne dla języków dynamicznych, takich jak Python czy Ruby. Opiera się na zasadzie *"If it looks like a duck and quacks like a duck, then it is a duck"*. Oznacza to, że nie ma znaczenia, z jakiej klasy pochodzi obiekt – jeśli posiada metodę o danej nazwie (i da się ją wywołać), to jest uznawany za odpowiedni.  
  **Przykład w Pythonie**:
   ```python
   class Kot:
       def dzwiek(self):
           print("Miau")

   class Pies:
       def dzwiek(self):
           print("Hau")

   def wydaj_dzwiek(zwierze):
       zwierze.dzwiek()

   kot = Kot()
   pies = Pies()

   wydaj_dzwiek(kot)  # Miau
   wydaj_dzwiek(pies) # Hau
   ```
   Oba obiekty mają metodę `dzwiek()`, więc funkcja `wydaj_dzwiek` działa niezależnie od ich klas.

- **Strukturalny polimorfizm** występuje w językach, które sprawdzają zgodność na podstawie struktury obiektu, a nie jego typu czy hierarchii dziedziczenia. Typowym przykładem jest Go (język programowania), który wspiera tzw. **interfejsy oparte na strukturze**.

### Podsumowanie:
- Jeśli obiekty różnych klas mają metody o tej samej nazwie i są używane w taki sam sposób, można mówić o **duck typing** lub **strukturalnym polimorfizmie**.
- Różni się to od klasycznego polimorfizmu opartego na dziedziczeniu, gdzie metody są dziedziczone przez wspólną hierarchię klas.