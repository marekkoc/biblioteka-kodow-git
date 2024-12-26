def zaokr(x: float):
  if x >= 0:
    if x - x // 1 >= 0.5:
      return x // 1 + 1
    else:
      return x // 1
  else:
    return - zaokr(-x)

print(zaokr(2.33))
print(zaokr(2.93))
print(zaokr(-2.33))
print(zaokr(-2.93))
print(zaokr(0))
