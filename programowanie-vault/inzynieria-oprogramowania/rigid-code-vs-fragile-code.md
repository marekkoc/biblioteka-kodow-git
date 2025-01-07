---
Utworzono: 2024-11-06T14:45:00
Zmodyfikowano: 2024-11-06T14:45:00
Źródło: 
tags:
---

Pojęcia **"rigid code"** i **"fragile code"** odnoszą się do problemów ze strukturą kodu, które mogą utrudniać rozwój projektu oraz wprowadzanie zmian. Oto ich znaczenie:

1. **Rigid Code**:
   - Kod, który jest trudny do zmiany. Jest on mało elastyczny i wymaga modyfikacji w wielu miejscach, nawet gdy wprowadza się drobne zmiany.
   - Taki kod zazwyczaj **ma wiele zależności** (moduły i klasy są ze sobą mocno powiązane), co powoduje, że zmiana jednego elementu wymaga modyfikacji także w innych, zależnych częściach kodu.
   - Kod o charakterze "rigid" utrudnia wprowadzanie nowych funkcjonalności, a dodawanie ich może powodować błąd w istniejącym kodzie.
   - Powoduje to, że projekt staje się kosztowny w utrzymaniu, a sam kod jest bardziej narażony na błędy i niespójności.

2. **Fragile Code**:
   - Kod, który łatwo się psuje przy wprowadzaniu zmian. **Jest podatny na błędy**, ponieważ każda zmiana (nawet drobna) może nieoczekiwanie wpłynąć na inne części systemu.
   - Kod może być kruchy, jeśli opiera się na dużej liczbie nieprzewidywalnych zależności lub jeśli jest napisany w sposób trudny do zrozumienia i testowania.
   - Taki kod często zawiera **ukryte zależności** i powiązania, przez co zmiana jednego miejsca może powodować problemy w innym, pozornie niepowiązanym module.
   - Kod "fragile" jest ryzykowny przy modyfikacjach, ponieważ zmiany mogą wymagać wielu poprawek i testowania w całym systemie, co zwiększa ryzyko wprowadzenia nowych błędów.

Oba te rodzaje problematycznego kodu są źródłem frustracji dla programistów, którzy muszą pracować nad jego rozwojem lub utrzymaniem. Dlatego dobre praktyki programistyczne, takie jak **stosowanie wzorców projektowych, zasady SOLID** oraz **refaktoryzacja**, są kluczowe, aby uniknąć tworzenia kodu, który jest albo sztywny (rigid), albo kruchy (fragile).