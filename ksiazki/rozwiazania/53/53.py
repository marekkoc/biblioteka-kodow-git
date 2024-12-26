from random import randint

def los():
  start = 1
  koniec = 1000
  while start < 1000:
    start = randint(start, koniec)
    yield start

print(list(los()))
