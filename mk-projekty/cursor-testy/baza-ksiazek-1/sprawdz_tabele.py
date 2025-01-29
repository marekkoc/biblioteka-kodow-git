import sqlite3

def sprawdz_baze():
    try:
        conn = sqlite3.connect('ksiazki.sqlite')
        cursor = conn.cursor()
        
        # Sprawdź strukturę tabeli
        cursor.execute("PRAGMA table_info(ksiazki)")
        struktura = cursor.fetchall()
        print("\nStruktura tabeli 'ksiazki':")
        for kolumna in struktura:
            print(f"- {kolumna[1]} ({kolumna[2]})")
            
        # Sprawdź zawartość tabeli
        cursor.execute("SELECT * FROM ksiazki")
        rekordy = cursor.fetchall()
        print("\nZawartość tabeli 'ksiazki':")
        for rekord in rekordy:
            print(f"ID: {rekord[0]}, Tytuł: {rekord[1]}, Autor: {rekord[2]}")
            
    except sqlite3.Error as e:
        print(f"Błąd podczas sprawdzania bazy: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    sprawdz_baze() 