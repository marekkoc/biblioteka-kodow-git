import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class BibliotekaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteka - System Zarządzania")
        
        # Połączenie z bazą danych
        try:
            self.conn = sqlite3.connect('ksiazki.sqlite')
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            messagebox.showerror("Błąd", f"Nie można połączyć z bazą danych: {e}")
            
        # Tworzenie interfejsu
        self.create_widgets()
        
    def create_widgets(self):
        # Frame na przyciski
        button_frame = ttk.Frame(self.root, padding="10")
        button_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Przyciski
        ttk.Button(button_frame, text="Pokaż wszystkie książki", 
                  command=self.pokaz_ksiazki).grid(row=0, column=0, pady=5)
        ttk.Button(button_frame, text="Dodaj książkę", 
                  command=self.dodaj_ksiazke).grid(row=1, column=0, pady=5)
        
        # Lista książek
        self.tree = ttk.Treeview(self.root, columns=('ID', 'Tytuł', 'Autor'), show='headings')
        self.tree.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=5)
        
        # Nagłówki kolumn
        self.tree.heading('ID', text='ID')
        self.tree.heading('Tytuł', text='Tytuł')
        self.tree.heading('Autor', text='Autor')
        
    def pokaz_ksiazki(self):
        # Czyszczenie obecnej listy
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        try:
            self.cursor.execute("SELECT * FROM ksiazki")
            for row in self.cursor.fetchall():
                self.tree.insert('', 'end', values=row)
        except sqlite3.Error as e:
            messagebox.showerror("Błąd", f"Nie można pobrać książek: {e}")
            
    def dodaj_ksiazke(self):
        # Okno dodawania książki
        dodaj_okno = tk.Toplevel(self.root)
        dodaj_okno.title("Dodaj nową książkę")
        
        ttk.Label(dodaj_okno, text="Tytuł:").grid(row=0, column=0, pady=5, padx=5)
        tytul_entry = ttk.Entry(dodaj_okno)
        tytul_entry.grid(row=0, column=1, pady=5, padx=5)
        
        ttk.Label(dodaj_okno, text="Autor:").grid(row=1, column=0, pady=5, padx=5)
        autor_entry = ttk.Entry(dodaj_okno)
        autor_entry.grid(row=1, column=1, pady=5, padx=5)
        
        def zapisz():
            tytul = tytul_entry.get()
            autor = autor_entry.get()
            try:
                self.cursor.execute("INSERT INTO ksiazki (tytul, autor) VALUES (?, ?)", 
                                  (tytul, autor))
                self.conn.commit()
                messagebox.showinfo("Sukces", "Książka została dodana!")
                dodaj_okno.destroy()
                self.pokaz_ksiazki()
            except sqlite3.Error as e:
                messagebox.showerror("Błąd", f"Nie można dodać książki: {e}")
        
        ttk.Button(dodaj_okno, text="Zapisz", command=zapisz).grid(row=2, column=0, 
                                                                  columnspan=2, pady=10)

def main():
    root = tk.Tk()
    app = BibliotekaGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 