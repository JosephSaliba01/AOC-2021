from aocd import submit
from aocd import get_data

get_data(day=2)

from aocd import lines

x = 0
y = 0
for arg in [line.split() for line in lines]:
    if (arg[0][0] == 'd'):
        y += int(arg[1])
    elif (arg[0][0] == 'u'):
        y -= int(arg[1])
    else:
        x += int(arg[1])

# submit(day=2, part='a', answer=x * y)

aim = 0
x2 = 0
y2 = 0
for arg in [line.split() for line in lines]:
    if (arg[0][0] == 'd'):
        aim += int(arg[1])
    elif (arg[0][0] == 'u'):
        aim -= int(arg[1])
    else:
        x2 += int(arg[1])
        y2 += aim * int(arg[1])

submit(day=2, part='b', answer=x2 * y2)
