import operator

slowa = dict()
znaki = dict()
with open('121_dane.txt', 'r', encoding='utf-8') as f:
  for ln in f:
    for slowo in ln.strip().split(' '):
      slowa.setdefault(slowo, 0)
      slowa[slowo] += 1
      for znak in slowo:
        znaki.setdefault(znak, 0)
        znaki[znak] += 1
slowa = dict(sorted(slowa.items(), key=operator.itemgetter(1)))
znaki = dict(sorted(znaki.items(), key=operator.itemgetter(1), reverse=True))

min_slowa = min(slowa.values())
max_znaki = max(znaki.values())

print('Słowa, które wystąpiły najmniejszą ilość razy:')
print(dict(filter(lambda item: item[1] == min_slowa, slowa.items())))

print('Znaki, które wystąpiły największą ilość razy:')
print(dict(filter(lambda item: item[1] == max_znaki, znaki.items())))
