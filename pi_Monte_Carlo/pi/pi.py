import random
from math import sqrt
import math


N = 100000000
n = 0

for i in range(N):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    if sqrt((x - 0.5) ** 2 + (y - 0.5) ** 2) <= 0.5:

        n += 1

print("lim  pi = ", 4 * n / N)
print("true pi = ", math.pi)





