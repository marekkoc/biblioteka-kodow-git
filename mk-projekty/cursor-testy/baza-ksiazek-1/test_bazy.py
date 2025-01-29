import sys
import sqlite3

def sprawdz_baze():
    print(f"Wersja Pythona: {sys.version}")
    print(f"Wersja SQLite: {sqlite3.sqlite_version}")
    
    try:
        # Próba połączenia z bazą
        conn = sqlite3.connect('ksiazki.sqlite')
        print("\nPołączenie z bazą ksiazki.sqlite zostało ustanowione pomyślnie!")
        
        # Sprawdzenie tabel w bazie
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        print("\nDostępne tabele w bazie:")
        for table in tables:
            print(f"- {table[0]}")
            
    except sqlite3.Error as e:
        print(f"Wystąpił błąd podczas łączenia z bazą: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    sprawdz_baze() 