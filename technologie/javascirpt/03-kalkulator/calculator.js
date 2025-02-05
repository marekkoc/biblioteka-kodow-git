let wyswietlacz = document.getElementById('display');

function dodajDoWyswietlacza(wartosc) {
    wyswietlacz.value += wartosc;
}

function wyczyscWyswietlacz() {
    wyswietlacz.value = '';
}

function usunOstatni() {
    wyswietlacz.value = wyswietlacz.value.slice(0, -1);
}

function oblicz() {
    try {
        // eval() nie jest zalecane w produkcji, ale użyjemy dla prostoty przykładu
        wyswietlacz.value = eval(wyswietlacz.value);
    } catch (error) {
        wyswietlacz.value = 'Błąd';
        setTimeout(wyczyscWyswietlacz, 1000);
    }
}

// Obsługa klawiatury
document.addEventListener('keydown', (event) => {
    if (event.key >= '0' && event.key <= '9' || 
        event.key === '+' || event.key === '-' || 
        event.key === '*' || event.key === '/' || 
        event.key === '.' || event.key === '(' || 
        event.key === ')') {
        dodajDoWyswietlacza(event.key);
    } else if (event.key === 'Enter') {
        oblicz();
    } else if (event.key === 'Backspace') {
        usunOstatni();
    } else if (event.key === 'Escape') {
        wyczyscWyswietlacz();
    }
});