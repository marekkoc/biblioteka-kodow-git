A = float(3.15)
B = float(11.89)

print(f'Obliczenia bez mnożenia: float A={A} * float B={B} = ', A / (1 / B))
print(A * B, ': test poprawności.')

A = float(8.76)
B = int(10)
S = A * B  # dla testu
print(f'Obliczenia bez mnożenia i dzielenia: float A={A} * int B={B} = ',
      end='')
suma = 0
while B > 0:
  suma += A
  B -= 1
print(round(suma, 5))
print(S, ':test poprawności.')
