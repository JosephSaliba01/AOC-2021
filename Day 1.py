from aocd import numbers
from aocd import submit


c1 = 0
for i in range(1, len(numbers)):
    if (numbers[i] > numbers[i-1]):
        c1 += 1
c2 = 0
for i in range(3, len(numbers)):
    if (numbers[i] > numbers[i-3]):
        c2 += 1

submit(c1, part="a", day=1)
submit(c2, part="b", day=1)

