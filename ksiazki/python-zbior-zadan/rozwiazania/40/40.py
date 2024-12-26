poz1, poz2 = 0, -1
imie = input('Podaj swoje imię: ')
for literka in imie:
  if literka in 'aeyuioAEYUIO':
    print(imie)
    poz1, poz2 = poz2, poz1
    imie = imie[::-1]
