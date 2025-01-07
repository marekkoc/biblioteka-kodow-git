---
Utworzono: 2024-11-25T08:58:00
Zmodyfikowano: 2024-11-25T08:58:00
Źródło: chatGPT
tags:
---

**Zasada Open-Closed Principle (OCP)** jest jedną z zasad SOLID w programowaniu obiektowym. Mówi ona, że:

> Moduły, klasy i funkcje powinny być **otwarte na rozszerzanie**, ale **zamknięte na modyfikacje**.

### Co to oznacza?

- **Otwarte na rozszerzanie**: Możesz dodawać nową funkcjonalność do klasy lub modułu, bez konieczności zmieniania istniejącego kodu.
- **Zamknięte na modyfikacje**: Istniejący kod nie powinien być zmieniany, aby uniknąć wprowadzania nowych błędów lub problemów.

Zasada ta zachęca do pisania kodu, który jest łatwy do rozbudowy bez ingerowania w już istniejące rozwiązania, co zwiększa stabilność systemu i jego łatwość w utrzymaniu.

---

### Przykład łamiący zasadę OCP

Załóżmy, że mamy klasę, która obsługuje różne rodzaje płatności:

```python
class PaymentProcessor:
    def process_payment(self, payment_type, amount):
        if payment_type == "credit_card":
            print(f"Processing credit card payment of {amount}")
        elif payment_type == "paypal":
            print(f"Processing PayPal payment of {amount}")
        else:
            raise ValueError("Unsupported payment type")
```

Dodanie nowego typu płatności wymaga zmiany metody `process_payment`, co łamie zasadę OCP.

---

### Poprawny przykład zgodny z OCP

Możemy zastosować polimorfizm, aby otworzyć system na nowe typy płatności, ale zamknąć go na modyfikacje istniejącego kodu:

```python
from abc import ABC, abstractmethod

# Abstrakcyjna klasa bazowa
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Konkretne implementacje dla różnych metod płatności
class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")

# Klasa używająca polimorfizmu
class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process_payment(self, amount):
        self.payment_method.process_payment(amount)

# Użycie:
credit_card = CreditCardPayment()
paypal = PayPalPayment()

processor = PaymentProcessor(credit_card)
processor.process_payment(100)

processor = PaymentProcessor(paypal)
processor.process_payment(200)
```

---

### Wyjaśnienie kodu:

1. Klasa `PaymentMethod` jest abstrakcyjna i definiuje interfejs, który muszą implementować wszystkie konkretne metody płatności.
2. Dodanie nowej metody płatności (np. `BitcoinPayment`) wymaga tylko utworzenia nowej klasy, która dziedziczy z `PaymentMethod`, bez konieczności modyfikowania istniejącego kodu.
3. Klasa `PaymentProcessor` działa ogólnie z dowolną implementacją `PaymentMethod`, dzięki czemu jest bardziej elastyczna i zgodna z zasadą OCP.