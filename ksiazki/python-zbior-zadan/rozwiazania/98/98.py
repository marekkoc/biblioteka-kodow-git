def uporzadkujNapisy(s1, s2):
  s1 = s1.lower()
  s2 = s2.lower()
  # lambda poniżej zwróci pozycję znaku w alfabecie!
  # zakładamy poprawność napisów s1, s2 (brak innych znaków)
  alfapoz = lambda znak: 'aąbcćdeęfghijklłmnńoóprsśtuwxyzźż'.find(znak)
  for poz in range(0, min(len(s1), len(s2))):
    if alfapoz(s1[poz]) < alfapoz(s2[poz]):
      return (s1, s2)
    elif alfapoz(s1[poz]) > alfapoz(s2[poz]):
      return (s2, s1)
  if len(s1) > len(s2):
    return (s2, s1)
  return (s1, s2)

print(uporzadkujNapisy('abc', 'ABCcc'))  # zmienię i tak na małe
print(uporzadkujNapisy('rower', 'złość'))
print(uporzadkujNapisy('śliwka', 'ślimak'))
print(uporzadkujNapisy('szczur', 'szczaw'))
print(uporzadkujNapisy('kabanosy', 'kabanos'))
print(uporzadkujNapisy('kąśliwość', 'kasza'))
