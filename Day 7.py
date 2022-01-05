"""Day 7."""
from aocd import get_data, submit

get_data(day=7)

'''
lines = []
with open("example_input.txt", 'r') as f:
    for line in f:
        lines += [line.rstrip()]
'''


from aocd import lines

"""Part a."""
data = list(map(int, lines[0].split(",")))


def get_data_nudge_costs():
    total_costs = {}
    for num in set(data):
        total_costs[num] = 0

    for i in data:
        for j in set(data):
            total_costs[j] += get_cost(i, j)
    return total_costs


def get_cost(i, j):
    return abs(i - j)


# total_costs = get_data_nudge_costs()

# submit(day=7, part='a', answer=min(total_costs.values()))

"""Part b."""
data = list(map(int, lines[0].split(",")))


def get_data_nudge_costs():
    total_costs = {}
    for num in set(data):
        total_costs[num] = 0

    for i in data:
        for j in set(data):
            total_costs[j] += get_cost(i, j)
    return total_costs


def get_cost(i, j):
    return sum(range(1, abs(i - j) + 1))


total_costs = get_data_nudge_costs()

submit(day=7, part='b', answer=min(total_costs.values()))
