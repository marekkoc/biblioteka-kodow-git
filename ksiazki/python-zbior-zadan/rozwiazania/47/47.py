from random import randint

# sposób 1 z randint
n = randint(0, 1000) / 1000
print(n)

# sposób 2 na podstawie upływającego czasu w nanosekundach
import time

n = (time.time_ns() % 1001) / 1000
print(n)
