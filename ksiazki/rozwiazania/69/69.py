from random import randint

n = -1
with open('69_liczby10.txt', 'w', encoding='utf-8') as file:
  while n != 1000:
    n = randint(0, 1000)
    if n % 10 == 0:
      file.write(str(n) + '\n')
