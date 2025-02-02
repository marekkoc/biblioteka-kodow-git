// skrypt2.js - skrypt przyjmujący argumenty z linii komend
// Uruchomienie: node skrypt2.js argument1 argument2
const args = process.argv.slice(2); // pierwsze dwa argumenty to node i nazwa skryptu

console.log('Przekazane argumenty:', args);
