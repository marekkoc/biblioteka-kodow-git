def doPodwojenia(x: float):
  print(x, '->', end=' ')
  if x >= 0:
    return x // 1 + (x - x // 1) * 2
  else:
    return -(x // -1) - (-x - (x // -1)) * 2

# przykłady
print(doPodwojenia(3.22), doPodwojenia(3.6), doPodwojenia(-2.17), doPodwojenia(-2.99),
      doPodwojenia(0.1), doPodwojenia(-0.1), doPodwojenia(0))
