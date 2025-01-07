
![[figs/Python-Programmer-How-to-build-a-web-app-in-python-complete-roadmap.png]]

#Python-programmer #Web-App


Kompletna mapa drogowa do zbudowania **aplikacji webowej** w Pythonie wraz z najlepszymi materiałami i linkami do stron i do kursów polecana w filmie [# How to build a web app in python. Complete roadmap and learning materials...](https://www.youtube.com/watch?v=tELWnKCVd9k) aby stworzyć kompletną **Aplikację internetową**

**Web App** (Web Application) - **Aplikacja internetowa** - (chat) jest to program który działa w przeglądarce internetowej i nie wymaga instalacji na urządzeniu użytkownika ponieważ jest dostępny za pomocą internetu. 

==Uczymy się przez robienie -- Learn by doing== nie uczymy się przez czytanie tutoriali i książek. Zawsze uczymy się przez robienie! ==Uczymy się przez praktykę== Gdy będziemy tylko czytać, to w pewnym momencie nasza nauka zwolni, bo musimy robić. Gdy mamy projekt, to on daje nam siłę napędową do rozwiązania napotkanych problemów, chcemy go kontynuować i pokonać napotkane przeszkody! Projekt w swojej istocie powoduje ==wypelnianie luk w naszej wiedzy== bo zmusza nas do dojścia do stanu w którym będzie ukończony i w którym będzie on działał. A nasza chęć ukończenia projektu podtrzymuje naszą ==motywację== do nauki i kontynuowania. Dlatego ten sposób nauki jest bardzo dobry.

Zatem, jeśli mam pomysł na zrobienie strony internetowej to powinienem ją zrobić, powinienem zacząć nad nią pracować, bo dzięki temu bardzo dużo się nauczę.

## Mapa drogowa
Ta mapa zawiera wszystkie rzeczy, które powinienem wiedzieć aby zbudować gotową aplikację internetową od początku do końca, aby była ona działająca i kompletna.


### 1. HTML, CSS

Aplikacja musi mieć strukturę, musi byś wyświetlana,  możliwość interakcji zatem musi zawierać przyciski oraz ładny wygląd. Zatem wszystko musi mieć szkielet. 

Na stronie domowej **Mozilla** ([**MDN Web docs**](https://developer.mozilla.org/en-US/)) są bardzo dobre materiały źródłowe do nauki **HTML**a i **Css**a. ([referencje](https://developer.mozilla.org/en-US/docs/Web#web_technology_references)) Jest to bardzo dobre źródło informacji o wielu internetowych technologiach. Tutaj powinniśmy zacząć czytać i zdobywać informację.  Nie powinienem czytać wszystkiego, tylko rzeczy które mnie interesują, ale zdecydowanie powinienem przeczytać:
1. HTML** - jest całkiem łatwy do nauczenie się, do załapania o co w nimi chodzi. 
2. **CSS** - jest bardzo obszerny i można poświęcić/stracić dużo czasu na jego naukę, ale powinniśmy nauczyć się tylko tyle ile go potrzebujemy do naszej strony. Zatem musimy mieć już jakąś wizję naszej strony.

###  2. Bootstrap

. **[Bootstrap](https://getbootstrap.com/)** - jest to struktura (framework) dla CSS ([getting started](https://getbootstrap.com/docs/5.3/getting-started/introduction/)) Powinniśmy przeczytać wstęp i trochę dokumentacji. Znając już trochę HTML i CSS zrozumiemy więcej z Bootstrap. Jest też spora strona z [przykadami](https://getbootstrap.com/docs/5.3/examples/). 
   
### 3. Python 

Dodajemy trochę **back-end funkcjonalności do naszej aplikacji** zatem uczymy się Pythona. Zatem tę część aplikacji, która działa po stronie serwera i jest niewidzialna dla użytkownika piszemy w języku Python. 

Back-end: część serwerowa, zaplecze aplikacji
- zarządzanie bazami danych,
- logikę aplikacji,
- obsługę żądań od strony klienta (front-end),
- autoryzację i uwierzytelnianie,
- integracje z zewnętrznymi API.


Technologie używane w back-endzie to często języki programowania takie jak: Java, Python, PHP, Node.js, Ruby, oraz bazy danych jak MySQL, PostgreSQL, MongoDB.

Dla kogoś kto zupełnie nie zna Python dobrym początkiem jest: Python tutorial na oficjalnej stronie Pythona.
[Sugerowane sekcje](https://docs.python.org/release/3.12.6/tutorial/index.html): 
- 1 do 10 do klas i dziedziczenia włącznie.
- 12: Środowiska wirtualne

### 4. Framework internetowy (web framework)

**Web framework (framework internetowy)** to zestaw narzędzi, bibliotek i reguł, które pomagają w tworzeniu aplikacji internetowych. Ułatwia on pracę deweloperom, automatyzując i upraszczając wiele zadań związanych z tworzeniem stron czy aplikacji webowych, takich jak routing, obsługa zapytań HTTP, zarządzanie sesjami, autoryzacja czy praca z bazami danych.

Frameworki webowe mogą dotyczyć zarówno front-endu (część widoczna dla użytkownika), jak i back-endu (część serwerowa). Oto przykłady popularnych frameworków:

**Front-end:**
- React – biblioteka JavaScript stworzona przez Facebooka do budowania interfejsów użytkownika.
- Angular – framework rozwijany przez Google, używany do budowania dynamicznych aplikacji jednostronicowych (SPA).
- Vue.js – lekki framework JavaScript, łatwy w nauce, idealny do mniejszych projektów oraz dużych aplikacji SPA.
  
**Back-end:**
- Django (Python) – potężny framework o wysokim poziomie abstrakcji, który oferuje wiele wbudowanych narzędzi do szybkiego tworzenia aplikacji.
- Express (Node.js) – minimalistyczny i elastyczny framework do tworzenia serwerów i API.
- Ruby on Rails (Ruby) – framework typu full-stack, który zapewnia wszystkie narzędzia do tworzenia aplikacji internetowych z naciskiem na prostotę i produktywność.
- Spring (Java) – bardzo popularny framework dla aplikacji webowych w ekosystemie Javy, oferujący bogate wsparcie dla aplikacji enterprise.
- Laravel (PHP) – nowoczesny framework dla PHP, który znacznie upraszcza budowanie aplikacji webowych.
  
Frameworki pozwalają programistom skupić się na logice aplikacji, zamiast na implementowaniu podstawowych funkcji, takich jak obsługa żądań HTTP, co przyspiesza proces tworzenia aplikacji.

Popularne Frameworki to:
1. Flask - ten framework jest rekomendowany w tym materiale ponieważ jest na jego temat dużo dokumentacji, jest łatwy do nauki a jednocześnie ma duże możliwości. Jest modułowy, zatem można go łatwo rozbudowywać. 
3. Django
4. FastAPI

####  4.1 Flask - materialy

 1. Na początek dobry jest tutorial [Corey'ego Shafera na YT](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH). To jest najlepszy tutorial dla początkujących. 
 2. Można też kupić książkę: Flask Framework Cookbook. Over 80 proven recepies.. Shallabh Aggarwal
 3. [The Flask Mega tutorial ](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by Miguel Grinberg
 4. Hackers and slackers:  [Build Flask Apps](https://hackersandslackers.com/series/build-flask-apps/)
 5. [Dokumentacja Flask](https://flask.palletsprojects.com/en/3.0.x/):  [Tutorial](https://flask.palletsprojects.com/en/3.0.x/tutorial/)

### 5. Bazy danych 
1. Bazy danych. Nie wiem jaka strone on pokazywal: może ta: 
	1. SQLAlhemy
	2. flask storyng data
2. [Full stack python]( https://www.fullstackpython.com/flask.html) 


==NIE SZUKAJ WIĘCEJ ŹRÓDEŁ. TE ŹRÓDŁA W ZUPEŁNOŚCI WYSTARCZĄ. ZACZNIJ PRACOWAĆ I PISAĆ STRONĘ. INACZEJ WPADNIESZ W PUŁAPKĘ CIĄGŁEGO SZUKANIA!!!==


