// skrypt3.js - przykład skryptu przetwarzającego plik
const fs = require('fs').promises; // wersja z promises dla async/await

async function przetworzPlik(sciezka) {
    try {
        const dane = await fs.readFile(sciezka, 'utf8');
        const linie = dane.split('\n');
        console.log(`Liczba linii: ${linie.length}`);
        console.log(`Pierwsza linia: ${linie[0]}`);
    } catch (err) {
        console.error('Błąd podczas czytania pliku:', err);
    }
}

przetworzPlik('przyklad.txt');
