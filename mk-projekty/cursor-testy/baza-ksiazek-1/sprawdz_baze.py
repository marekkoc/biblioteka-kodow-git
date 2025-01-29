import sys
import sqlite3

def main():
    # Sprawdzamy wersje
    print(f"Wersja Pythona: {sys.version}")
    print(f"Wersja SQLite: {sqlite3.version}")
    print(f"Wersja SQLite (biblioteka): {sqlite3.sqlite_version}")
    
    try:
        # Próba połączenia z bazą
        conn = sqlite3.connect('ksiazki.sqlite')
        print("\nUdało się połączyć z bazą ksiazki.sqlite!")
        
        # Sprawdzamy zawartość bazy
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tabele = cursor.fetchall()
        
        if tabele:
            print("\nZnalezione tabele:")
            for tabela in tabele:
                print(f"- {tabela[0]}")
        else:
            print("\nBrak tabel w bazie danych.")
            
    except sqlite3.Error as e:
        print(f"\nBłąd podczas połączenia z bazą: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    main() 