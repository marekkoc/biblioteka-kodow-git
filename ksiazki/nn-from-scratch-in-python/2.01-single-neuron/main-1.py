import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class NeuronApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Symulator Neuronu")
        self.root.geometry("800x600")
        
        # Parametry neuronu
        self.weights = [0.0, 0.0, 0.0]  # Wagi
        self.bias = 0.0                 # Bias
        self.inputs = [0.0, 0.0, 0.0]   # Wejścia
        self.activation_function = "sigmoid"  # Domyślna funkcja aktywacji
        
        self.create_widgets()
        self.update_output()
        
    def create_widgets(self):
        # Ramka główna
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Konfiguracja siatki, aby elementy skalowały się z oknem
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)
        
        # Ramka dla parametrów
        param_frame = ttk.LabelFrame(main_frame, text="Parametry neuronu", padding="10")
        param_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        # Konfiguracja siatki dla param_frame
        param_frame.columnconfigure(0, weight=1)  # Kolumna z etykietami
        param_frame.columnconfigure(1, weight=3)  # Kolumna ze sliderami - większa waga
        param_frame.columnconfigure(2, weight=1)  # Kolumna z wartościami
        
        # Styl dla większych sliderów
        style = ttk.Style()
        style.configure("Thick.Horizontal.TScale", sliderthickness=25)  # Zwiększenie wysokości slidera
        
        # Przechowywanie referencji do wszystkich etykiet
        self.labels = {}
        
        # Wagi
        self.labels["wagi_header"] = ttk.Label(param_frame, text="Wagi:", font=("Arial", 12, "bold"))
        self.labels["wagi_header"].grid(row=0, column=0, sticky=tk.W, pady=10)
        
        self.weight_vars = []
        self.weight_sliders = []
        
        for i in range(3):
            weight_var = tk.DoubleVar(value=0.0)
            self.weight_vars.append(weight_var)
            
            self.labels[f"w{i+1}"] = ttk.Label(param_frame, text=f"w{i+1}:", font=("Arial", 11))
            self.labels[f"w{i+1}"].grid(row=i+1, column=0, sticky=tk.W, pady=5)
            
            weight_slider = ttk.Scale(param_frame, from_=-5.0, to=5.0, orient=tk.HORIZONTAL, 
                                     variable=weight_var, command=lambda _,i=i: self.update_weight(i),
                                     style="Thick.Horizontal.TScale")
            weight_slider.grid(row=i+1, column=1, sticky=tk.EW, pady=5, padx=10)
            self.weight_sliders.append(weight_slider)
            
            weight_label = ttk.Label(param_frame, text="0.0", font=("Arial", 11))
            weight_label.grid(row=i+1, column=2, sticky=tk.W, padx=5, pady=5)
            setattr(self, f"weight_label_{i}", weight_label)
        
        # Bias
        self.labels["bias_header"] = ttk.Label(param_frame, text="Bias:", font=("Arial", 12, "bold"))
        self.labels["bias_header"].grid(row=4, column=0, sticky=tk.W, pady=10)
        
        self.bias_var = tk.DoubleVar(value=0.0)
        bias_slider = ttk.Scale(param_frame, from_=-5.0, to=5.0, orient=tk.HORIZONTAL, 
                               variable=self.bias_var, command=self.update_bias,
                               style="Thick.Horizontal.TScale")
        bias_slider.grid(row=4, column=1, sticky=tk.EW, pady=5, padx=10)
        self.bias_label = ttk.Label(param_frame, text="0.0", font=("Arial", 11))
        self.bias_label.grid(row=4, column=2, sticky=tk.W, padx=5, pady=5)
        
        # Wejścia
        self.labels["inputs_header"] = ttk.Label(param_frame, text="Wejścia:", font=("Arial", 12, "bold"))
        self.labels["inputs_header"].grid(row=5, column=0, sticky=tk.W, pady=10)
        
        self.input_vars = []
        self.input_sliders = []
        
        for i in range(3):
            input_var = tk.DoubleVar(value=0.0)
            self.input_vars.append(input_var)
            
            self.labels[f"x{i+1}"] = ttk.Label(param_frame, text=f"x{i+1}:", font=("Arial", 11))
            self.labels[f"x{i+1}"].grid(row=i+6, column=0, sticky=tk.W, pady=5)
            
            input_slider = ttk.Scale(param_frame, from_=0.0, to=1.0, orient=tk.HORIZONTAL, 
                                    variable=input_var, command=lambda _,i=i: self.update_input(i),
                                    style="Thick.Horizontal.TScale")
            input_slider.grid(row=i+6, column=1, sticky=tk.EW, pady=5, padx=10)
            self.input_sliders.append(input_slider)
            
            input_label = ttk.Label(param_frame, text="0.0", font=("Arial", 11))
            input_label.grid(row=i+6, column=2, sticky=tk.W, padx=5, pady=5)
            setattr(self, f"input_label_{i}", input_label)
        
        # Funkcja aktywacji
        self.labels["activation_header"] = ttk.Label(param_frame, text="Funkcja aktywacji:", font=("Arial", 12, "bold"))
        self.labels["activation_header"].grid(row=9, column=0, sticky=tk.W, pady=10)
        
        self.activation_var = tk.StringVar(value=self.activation_function)
        activation_combo = ttk.Combobox(param_frame, textvariable=self.activation_var, 
                                       values=["sigmoid", "tanh", "relu", "liniowa"],
                                       font=("Arial", 11))
        activation_combo.grid(row=9, column=1, sticky=tk.EW, pady=5, padx=10)
        activation_combo.bind("<<ComboboxSelected>>", self.update_activation)
        
        # Wyjście
        self.labels["output_header"] = ttk.Label(param_frame, text="Wyjście:", font=("Arial", 12, "bold"))
        self.labels["output_header"].grid(row=10, column=0, sticky=tk.W, pady=10)
        
        self.output_label = ttk.Label(param_frame, text="0.0", font=("Arial", 14, "bold"))
        self.output_label.grid(row=10, column=1, sticky=tk.W, pady=10)
        
        # Ramka dla wizualizacji
        viz_frame = ttk.LabelFrame(main_frame, text="Wizualizacja neuronu", padding="10")
        viz_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
        # Konfiguracja siatki dla viz_frame
        viz_frame.columnconfigure(0, weight=1)
        viz_frame.rowconfigure(0, weight=1)
        
        # Wizualizacja neuronu
        self.fig, self.ax = plt.subplots(figsize=(6, 5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=viz_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
        
        # Dodanie obsługi zmiany rozmiaru okna
        self.root.bind("<Configure>", self.on_window_resize)
        
        self.draw_neuron()
        
    def on_window_resize(self, event):
        # Aktualizacja wykresu przy zmianie rozmiaru okna
        if hasattr(self, 'fig') and event.widget == self.root:
            self.draw_neuron()
            
            # Aktualizacja rozmiaru sliderów i czcionek
            window_width = self.root.winfo_width()
            if window_width > 100:  # Zabezpieczenie przed zbyt małymi wartościami
                # Dostosowanie stylu sliderów do rozmiaru okna
                slider_height = max(20, int(window_width / 40))
                style = ttk.Style()
                style.configure("Thick.Horizontal.TScale", sliderthickness=slider_height)
                
                # Dostosowanie rozmiaru czcionek
                font_size = max(10, int(window_width / 80))
                bold_font_size = max(12, int(window_width / 70))
                title_font_size = max(14, int(window_width / 60))
                
                # Aktualizacja czcionek dla etykiet wag
                for i in range(3):
                    getattr(self, f"weight_label_{i}").config(font=("Arial", font_size))
                    self.labels[f"w{i+1}"].config(font=("Arial", font_size))
                
                # Aktualizacja czcionek dla etykiet wejść
                for i in range(3):
                    getattr(self, f"input_label_{i}").config(font=("Arial", font_size))
                    self.labels[f"x{i+1}"].config(font=("Arial", font_size))
                
                # Aktualizacja czcionki dla etykiety bias
                self.bias_label.config(font=("Arial", font_size))
                
                # Aktualizacja czcionek dla nagłówków sekcji
                for key in ["wagi_header", "bias_header", "inputs_header", "activation_header", "output_header"]:
                    self.labels[key].config(font=("Arial", bold_font_size, "bold"))
                
                # Aktualizacja czcionki dla etykiety wyjścia
                self.output_label.config(font=("Arial", bold_font_size, "bold"))
                
                # Aktualizacja czcionki dla comboboxa
                for child in self.root.winfo_children():
                    if isinstance(child, ttk.Frame):
                        for frame in child.winfo_children():
                            if isinstance(frame, ttk.LabelFrame):
                                # Aktualizacja czcionki dla tytułów ramek
                                style.configure('TLabelframe.Label', font=('Arial', title_font_size, 'bold'))
                                
                                # Szukanie comboboxa
                                for widget in frame.winfo_children():
                                    if isinstance(widget, ttk.Combobox):
                                        widget.config(font=("Arial", bold_font_size))
        
    def update_weight(self, index):
        value = self.weight_vars[index].get()
        self.weights[index] = value
        getattr(self, f"weight_label_{index}").config(text=f"{value:.2f}")
        self.update_output()
        self.draw_neuron()
        
    def update_bias(self, value):
        self.bias = self.bias_var.get()
        self.bias_label.config(text=f"{self.bias:.2f}")
        self.update_output()
        self.draw_neuron()
        
    def update_input(self, index):
        value = self.input_vars[index].get()
        self.inputs[index] = value
        getattr(self, f"input_label_{index}").config(text=f"{value:.2f}")
        self.update_output()
        self.draw_neuron()
        
    def update_activation(self, event):
        self.activation_function = self.activation_var.get()
        self.update_output()
        
    def apply_activation(self, x):
        if self.activation_function == "sigmoid":
            return 1 / (1 + np.exp(-x))
        elif self.activation_function == "tanh":
            return np.tanh(x)
        elif self.activation_function == "relu":
            return max(0, x)
        else:  # liniowa
            return x
        
    def update_output(self):
        # Obliczenie wyjścia neuronu
        net = np.dot(self.weights, self.inputs) + self.bias
        output = self.apply_activation(net)
        self.output_label.config(text=f"{output:.4f}")
        
    def draw_neuron(self):
        self.ax.clear()
        
        # Dostosowanie rozmiaru czcionki do rozmiaru okna
        window_width = self.root.winfo_width()
        base_font_size = max(10, int(window_width / 80))
        
        # Rysowanie neuronu
        neuron_circle = plt.Circle((0.5, 0.5), 0.2, fill=True, color='lightblue', alpha=0.7)
        self.ax.add_patch(neuron_circle)
        
        # Wejścia
        input_positions = [(0.1, 0.3), (0.1, 0.5), (0.1, 0.7)]
        for i, pos in enumerate(input_positions):
            self.ax.plot(pos[0], pos[1], 'ro', markersize=10)
            self.ax.text(pos[0]-0.05, pos[1], f'x{i+1}', fontsize=base_font_size)
            
            # Linia wagi z grubością proporcjonalną do wagi
            weight = self.weights[i]
            width = abs(weight) / 2
            if width < 0.5:
                width = 0.5
            color = 'green' if weight >= 0 else 'red'
            self.ax.plot([pos[0], 0.5], [pos[1], 0.5], color=color, linewidth=width*1.5)
            self.ax.text((pos[0] + 0.5)/2, (pos[1] + 0.5)/2, f'{weight:.2f}', 
                        fontsize=base_font_size, 
                        bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=1))
        
        # Bias
        self.ax.text(0.5, 0.8, f'bias: {self.bias:.2f}', 
                    fontsize=base_font_size+2, 
                    bbox=dict(facecolor='lightyellow', alpha=0.7, edgecolor='none', pad=2))
        
        # Wyjście
        self.ax.plot(0.9, 0.5, 'bo', markersize=10)
        self.ax.text(0.95, 0.5, 'y', fontsize=base_font_size+2)
        self.ax.plot([0.7, 0.9], [0.5, 0.5], 'b-', linewidth=3)
        
        # Funkcja aktywacji
        self.ax.text(0.5, 0.2, f'f: {self.activation_function}', 
                    fontsize=base_font_size+2,
                    bbox=dict(facecolor='lightgreen', alpha=0.7, edgecolor='none', pad=2))
        
        # Dodanie tytułu z wartością wyjścia
        output = float(self.output_label.cget("text"))
        self.ax.set_title(f'Wyjście: {output:.4f}', fontsize=base_font_size+4)
        
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.axis('off')
        
        # Dostosowanie układu wykresu
        self.fig.tight_layout()
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = NeuronApp(root)
    root.mainloop()
