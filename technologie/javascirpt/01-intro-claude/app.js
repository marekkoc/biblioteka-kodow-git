const menadzerZadan = {
    zadania: [],
    
    dodajZadanie() {
        const input = document.getElementById('taskInput');
        const priority = document.getElementById('priorityInput');
        
        if (input.value.trim() !== '') {
            const zadanie = new Zadanie(input.value, priority.value);
            this.zadania.push(zadanie);
            this.pokazZadania();
            input.value = ''; // czyszczenie pola
        }
    },

    usunZadanie(id) {
        this.zadania = this.zadania.filter(zadanie => zadanie.id !== id);
        this.pokazZadania();
    },

    przełączStatus(id) {
        const zadanie = this.zadania.find(z => z.id === id);
        if (zadanie) {
            zadanie.zakonczZadanie();
            this.pokazZadania();
        }
    },

    pokazZadania() {
        const taskList = document.getElementById('taskList');
        taskList.innerHTML = ''; // czyszczenie listy

        this.zadania.forEach(zadanie => {
            const taskDiv = document.createElement('div');
            taskDiv.className = `task-item ${zadanie.ukonczone ? 'task-done' : ''} ${zadanie.priorytet === 'wysoki' ? 'high-priority' : ''}`;
            
            taskDiv.innerHTML = `
                <span onclick="menadzerZadan.przełączStatus(${zadanie.id})">
                    ${zadanie.tytul} (${zadanie.priorytet})
                </span>
                <button onclick="menadzerZadan.usunZadanie(${zadanie.id})">Usuń</button>
            `;
            
            taskList.appendChild(taskDiv);
        });
    }
};

// Dodajemy obsługę klawisza Enter
document.getElementById('taskInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        menadzerZadan.dodajZadanie();
    }
});