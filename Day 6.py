"""Day 6."""
from aocd import get_data, submit

get_data(day=6)

from aocd import lines

"""Part a."""
NUM_DAYS = 80
population = list(map(int, lines[0].split(",")))


def update_population(population):
    num_of_newborn = 0
    for i in range(0, len(population)):
        if (population[i] == 0):
            num_of_newborn += 1
            population[i] = 6
        else:
            population[i] -= 1
    population += ([8] * num_of_newborn)
    return population


'''
for _ in range(NUM_DAYS):
    population = update_population(population)
'''

# print(len(population))

"""Part b."""
population = list(map(int, lines[0].split(",")))


def total_fish(day, cache={}):
    if (day < 7):
        return 1
    if day not in cache:
        cache[day] = total_fish(day - 7) + total_fish(day - 9)
    return cache[day]


sum_of_all_populations = sum([total_fish(256 + 6 - d) for d in population])

submit(day=6, part='b', answer=sum_of_all_populations)
