class Punkt:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def wzor(self, p):
    a = p.x - self.x
    b = - self.y * p.x + self.y * self.x
    c = p.y - self.y
    d = p.y * self.x - self.y * self.x
    """
    liczby a,b,c i d wyprowadzam ze wzoru: 
    (y−self.y) * (p.x−self.x) − (p.y−self.y) * (x−self.x) = 0
    y*p.x - y*self.x - self.y*p.x + self.y * self.x - (x* p.y - p.y*self.x - self.y * x + self.y*self.x) = 0
    y* (p.x-self.x) - self.y*p.x + self.y * self.x  - x*p.y + p.y*self.x + self.y*x - self.y*self.x = 0
    y* (p.x-self.x) - self.y*p.x + self.y * self.x  - x * (p.y - self.y) + p.y*self.x - self.y*self.x = 0
    y*a + b -x*c + d = 0
    y*a = x*c - b - d
    y = x*c/a + (-b -d)/a 
    """
    # a teraz już zwracam napis ze wzorem
    znak = ' + '
    if -b - d < 0:
      znak = ''
    try:
      return 'y = ' + str(round(c / a, 2)) + '*x' + znak + str(
        round((-b - d) / a, 2))
    except (ZeroDivisionError):
      return 'Prawdopodobny błąd dzielenia przez zero! Prosta jest prostopadła do osi X. ' + 'Brak wzoru.\n'

# (cy−yA)(xB−xA)−(yB−yA)(cx−xA)==0
# wzór funkcji dla dwóch punktów, a i b. Punkt c spełnia powyższą
# równość, gdy leży na prostej utworzonej z punktów: a i b.
def CzyCnaProstejAB(a: Punkt, b: Punkt, c: Punkt):
  return ((c.y - a.y) * (b.x - a.x) - (b.y - a.y) * (c.x - a.x) == 0)

def CzyPunktyNaJednejLinii(a: Punkt, b: Punkt, c: Punkt):
  """
  Testujemy, czy punkty: czy punkt c leży na linii utworzonej z punktów: a i b.
  Kombinacje a, c, b oraz b, c, a nie muszą być sprawdzane, zwracam jednak
  uwagę na fakt, że prostą mogą tworzyć inne dwa punkty.
  """
  return (
      CzyCnaProstejAB(a, b, c)
      or CzyCnaProstejAB(a, c, b)
      or CzyCnaProstejAB(b, c, a))

print(CzyPunktyNaJednejLinii(Punkt(0, 0), Punkt(10, 10), Punkt(5, 5)))
print(CzyPunktyNaJednejLinii(Punkt(0, 0), Punkt(10, 10), Punkt(1, -1)))
print(CzyPunktyNaJednejLinii(Punkt(0, 0), Punkt(10, 10), Punkt(-1, -1)))
print(CzyPunktyNaJednejLinii(Punkt(-1, -1), Punkt(10, 10), Punkt(0, 0)))
print(CzyPunktyNaJednejLinii(Punkt(0, 0), Punkt(0, 5), Punkt(2, 0)))
print(CzyPunktyNaJednejLinii(Punkt(0, 0), Punkt(0, 5), Punkt(0, 2)))

print()

print('Wzór funkcji:', Punkt(0, 0).wzor(Punkt(5, 5)))  # y = x
print('Wzór funkcji:', Punkt(0, 20).wzor(Punkt(0, 0)))  # nie powinno być wzoru
print('Wzór funkcji:', Punkt(-2, -7).wzor(Punkt(2, 1)))  # y = 2x - 3
