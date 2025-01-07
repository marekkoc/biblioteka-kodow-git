---
Utworzono: 2024-10-26T18:29:00
Zmodyfikowano: 2024-10-26T18:29:00
Źródło: 
tags:
---
# 1.Opis projektu

1. Hasła mogą być generowane w zaszumionym obrazie 3D. Gdyby obraz był bez szumu, to możemy go zakodować np. za pomoca ciąglu RL.
2. Poszczególne litery będą zapisane na różnej głębokości i w kolejnych blokach obrazu
3. Wyswietlenie hasla będzie mozliwe za pomoca funkcji MIP
4. haslo będzie przechowywane jako np plik JSON w którym najpierw będą:
	1. meta dane:
		1. data utworzenia
		2. data ostatniego otwarcia
		3. data modyfikacji???
		4. rozmiar obrazu
		5. do czego jest to haslo np bonito.pl
		6. rozmiar obrazu
	2.  obraz 3D który może być zakodoany (jesli bedzi bez szumu) metodą RL
5. Program będzie rodzajem przeglądarki 3D z dodakowymi opcjami:
	1. wyslwetlenie MIP
	2. dodanie szumu do MIP
	3. zapis MIP do pliku np w formacie png
