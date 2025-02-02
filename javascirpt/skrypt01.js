// skrypt1.js - prosty skrypt listujący pliki w katalogu
const fs = require('fs');

// Listowanie plików w bieżącym katalogu
fs.readdir('./', (err, files) => {
    if (err) {
        console.error('Błąd:', err);
        return;
    }
    console.log('Pliki w katalogu:');
    files.forEach(file => console.log(file));
});
