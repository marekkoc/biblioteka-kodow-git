const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('recipes.db');

db.serialize(() => {
  db.run(`CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    ingredients TEXT,
    instructions TEXT,
    mood TEXT
  )`);

  // Dodajemy przykładowe przepisy
  const sampleRecipes = [
    {
      name: 'Comfort Mac and Cheese',
      ingredients: 'Makaron, ser, mleko, masło',
      instructions: 'Ugotuj makaron. Rozpuść ser z mlekiem. Połącz składniki.',
      mood: 'sad'
    },
    {
      name: 'Energetic Smoothie Bowl',
      ingredients: 'Banany, jagody, mleko migdałowe, granola',
      instructions: 'Zmiksuj owoce z mlekiem. Udekoruj granolą.',
      mood: 'happy'
    },
    // Możesz dodać więcej przepisów
  ];

  const stmt = db.prepare('INSERT OR IGNORE INTO recipes (name, ingredients, instructions, mood) VALUES (?, ?, ?, ?)');
  sampleRecipes.forEach(recipe => {
    stmt.run(recipe.name, recipe.ingredients, recipe.instructions, recipe.mood);
  });
  stmt.finalize();
});

module.exports = db; 