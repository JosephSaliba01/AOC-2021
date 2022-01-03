from aocd import lines
from aocd import submit
from aocd import get_data

get_data(day=3)


gamma = ""
epsilon = ""
for k in [''.join([num[i] for num in lines]) for i in range(0, len(lines[0]))]:
    if k.count('1') > k.count('0'):
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

submit(answer=(int(gamma, 2) * int(epsilon, 2)), day=3, part='a')


def f1(arr, num):
    if (len(arr) == 1):
        return arr[0]
    else:
        arr_T = [''.join([n[i] for n in arr])
                 for i in range(0, len(arr[0]))]

        most_common_bit = '1' if arr_T[num].count(
            '1') >= arr_T[num].count('0') else '0'

        new_arr = [s for s in arr if s[num] == most_common_bit]

        print(new_arr)

        return f1(new_arr, num+1)


def f2(arr, num):
    if (len(arr) == 1):
        return arr[0]
    else:
        arr_T = [''.join([n[i] for n in arr])
                 for i in range(0, len(arr[0]))]

        least_common_bit = '0' if arr_T[num].count(
            '1') >= arr_T[num].count('0') else '1'

        new_arr = [s for s in arr if s[num] == least_common_bit]

        print(new_arr)

        return f2(new_arr, num+1)


submit(answer=(int(f1(lines, 0), 2) * int(f2(lines, 0), 2)), day=3, part='b')
