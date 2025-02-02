class Zadanie {
    constructor(tytul, priorytet = "normalny") {
        this.id = Date.now(); // unikalny identyfikator
        this.tytul = tytul;
        this.priorytet = priorytet;
        this.ukonczone = false;
        this.dataUtworzenia = new Date();
    }

    zakonczZadanie() {
        this.ukonczone = !this.ukonczone; // przełączanie stanu
    }

    pobierzStatus() {
        return this.ukonczone ? "Zakończone" : "W trakcie";
    }
}