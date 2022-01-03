from aocd import get_data
from aocd import submit

get_data(day=5)

from aocd import lines

'''
lines = []
with open("example_input.txt", 'r') as f:
    for line in f:
        lines += [line.rstrip()]
'''


def part1():
    count_of_overlap = 0

    def print_grid():
        for line in grid:
            print(line)

    def get_max_points():
        max_x = 0
        max_y = 0
        for line in lines:
            points = line.split(" -> ")
            x0 = int(points[0].split(",")[0])
            x1 = int(points[1].split(",")[0])
            y0 = int(points[0].split(",")[1])
            y1 = int(points[1].split(",")[1])

            max_x = max(max_x, x0, x1)
            max_y = max(max_y, y0, y1)

        return (max_x, max_y)

    max_values = get_max_points()

    # grid = [[0]*(max_values[0]+1)]*(max_values[1]+1)
    grid = [[0 for x in range(max_values[0] + 1)]
            for y in range(max_values[1] + 1)]

    for line in lines:
        points = line.split(" -> ")
        x0 = int(points[0].split(",")[0])
        x1 = int(points[1].split(",")[0])
        y0 = int(points[0].split(",")[1])
        y1 = int(points[1].split(",")[1])

        #print(f"Adding: {x0}->{x1} | {y0}->{y1}")

        if (x0 == x1 or y0 == y1):

            if (x0 != x1):  # change across horizontal
                i = y0
                for j in range(min(x0, x1), max(x0, x1) + 1):
                    grid[i][j] += 1
                    if (grid[i][j] == 2):
                        count_of_overlap += 1
            else:  # change across vertical
                j = x0
                for i in range(min(y0, y1), max(y0, y1) + 1):
                    grid[i][j] += 1
                    if (grid[i][j] == 2):
                        count_of_overlap += 1

        # print_grid()

    print(f'\nFinal Grid:')
    print_grid()

    print(f'Overlap Count: {count_of_overlap}')
    # submit(day=5, part="a", answer=count_of_overlap)


def part2():
    count_of_overlap = 0

    def print_grid():
        for line in grid:
            print(line)

    def get_max_points():
        max_x = 0
        max_y = 0
        for line in lines:
            points = line.split(" -> ")
            x0 = int(points[0].split(",")[0])
            x1 = int(points[1].split(",")[0])
            y0 = int(points[0].split(",")[1])
            y1 = int(points[1].split(",")[1])

            max_x = max(max_x, x0, x1)
            max_y = max(max_y, y0, y1)

        return (max_x, max_y)

    def path(num1, num2):
        while (num1 != num2):
            yield num1
            if num1 < num2:
                num1 += 1
            else:
                num1 -= 1
        yield num1

    max_values = get_max_points()

    grid = [[0 for _ in range(max_values[0] + 1)]
            for _ in range(max_values[1] + 1)]

    for line in lines:
        points = line.split(" -> ")
        x0 = int(points[0].split(",")[0])
        x1 = int(points[1].split(",")[0])
        y0 = int(points[0].split(",")[1])
        y1 = int(points[1].split(",")[1])

        if (y0 == y1):  # change across horizontal
            i = y0
            for j in range(min(x0, x1), max(x0, x1) + 1):
                grid[i][j] += 1
                if (grid[i][j] == 2):
                    count_of_overlap += 1
        elif (x0 == x1):  # change across vertical
            j = x0
            for i in range(min(y0, y1), max(y0, y1) + 1):
                grid[i][j] += 1
                if (grid[i][j] == 2):
                    count_of_overlap += 1
        else:
            for j, i in zip(path(x0, x1), path(y0, y1)):
                grid[i][j] += 1
                if (grid[i][j] == 2):
                    count_of_overlap += 1

    # print(f'\nFinal Grid:')
    # print_grid()

    print(f'Overlap Count: {count_of_overlap}')
    submit(day=5, part="b", answer=count_of_overlap)


part2()
