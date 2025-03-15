"""
Created: 2025.03.06
Modified: 2025.03.15
Author: MK
"""

class Quote:
    """
    Klasa reprezentująca pojedynczy cytat.

    Zawiera tekst, autora, id oraz liczbę obiektów.
    """
    # Zmienna klasowa do śledzenia liczby obiektów
    liczba_obiektow = 0
    
    def __init__(self, tekst: str, autor: str) -> None:
        self.tekst: str = tekst
        self.autor: str = autor
        # Zwiększamy licznik przy tworzeniu nowego obiektu
        Quote.liczba_obiektow += 1
        self.id = Quote.liczba_obiektow

    def __str__(self) -> str:
        """
        Zwraca tekstową reprezentację pojedynczego cytatu.
        """
        return f"{self.tekst} /{self.autor}/"    
   
    def __repr__(self) -> str:
        """
        Aby wyswetlic wymusic wywoalnie __str__ podczas wyswitalnia listy mott.
        """
        return self.__str__()
    
    def print_with_id(self) -> str:
        """
        Zwraca tekstową reprezentację pojedynczego cytatu.
        """
        return f"{self.id}) ** {self.tekst} **  -  {self.autor}"

    def to_dict(self) -> dict:
        """
        Konwertuje obiekt Cytat na słownik.
        """
        return {"tekst": self.tekst, "autor": self.autor}
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Quote':
        """
        Tworzy obiekt Quote z słownika.
        """
        return cls(data["tekst"], data["autor"])
    
    def __del__(self) -> None:
        """
        Destruktor obiektu - zmniejsza licznik obiektów przy usunięciu.
        """
        Quote.liczba_obiektow -= 1
    
    @classmethod
    def get_liczba_obiektow(cls) -> int:
        """
        Zwraca aktualną liczbę istniejących obiektów klasy Quote.
        """
        return cls.liczba_obiektow
    
    def __eq__(self, other: object) -> bool:
        """
        Porównuje dwa obiekty Quote.
        Zwraca True, jeśli tekst i autor są identyczne.
        """
        if not isinstance(other, Quote):
            return False
        return self.tekst == other.tekst and self.autor == other.autor
    
    def __lt__(self, other: 'Quote') -> bool:
        """
        Operator mniejszości (<).
        Porównuje dwa obiekty Quote na podstawie tekstu, a następnie autora.
        """
        if not isinstance(other, Quote):
            raise TypeError("Porównanie możliwe tylko z innym obiektem Quote")
        if self.tekst != other.tekst:
            return self.tekst < other.tekst
        return self.autor < other.autor
    
    def __gt__(self, other: 'Quote') -> bool:
        """
        Operator większości (>).
        Porównuje dwa obiekty Quote na podstawie tekstu, a następnie autora.
        """
        if not isinstance(other, Quote):
            raise TypeError("Porównanie możliwe tylko z innym obiektem Quote")
        if self.tekst != other.tekst:
            return self.tekst > other.tekst
        return self.autor > other.autor
    
    def __hash__(self) -> int:
        """
        Implementacja funkcji hash dla obiektu Quote.
        Umożliwia używanie obiektów Quote jako kluczy w słownikach i elementów zbiorów.
        """
        return hash((self.tekst, self.autor))


if __name__ == "__main__":
    quote: Quote  = Quote("Dupa lampa", "Violka")
    print(quote.print_with_id())
    print(f"Liczba obiektów: {quote.get_liczba_obiektow()}")
   

    
