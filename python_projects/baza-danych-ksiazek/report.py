class Report:
    def __init__(self, ksiazki):
        self._ksiazki = ksiazki

    def generuj_raport(self, sort_by='id'):
        formaty_wyswietlania = {
            'tytul': "Tytuł: {tytul}, Autor: {autor}, Rok: {rok}, ID: {id}",
            'autor': "Autor: {autor}, Tytuł: {tytul}, Rok: {rok}, ID: {id}",
            'rok': "Rok: {rok}, Autor: {autor}, Tytuł: {tytul}, ID: {id}",
            'id': "ID: {id}, Autor: {autor}, Tytuł: {tytul}, Rok: {rok}"
        }

        print(f"Sortowanie książek po: {sort_by}")
        print("--------------------------------")
        
        sort_by = sort_by if sort_by in formaty_wyswietlania else 'id'
        self._ksiazki.sort(key=lambda x: x[sort_by])
        
        format_linii = formaty_wyswietlania[sort_by]
        for ksiazka in self._ksiazki:
            print(format_linii.format(**ksiazka))








