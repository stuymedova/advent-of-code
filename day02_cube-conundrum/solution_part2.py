import sys
import os


def main():
    data = handle_input()
    sum = get_sum_of_power_of_min_sets(data)
    print(sum)


def handle_input():
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(
        dirname,
        sys.argv[1] if len(sys.argv) == 2 else 'input.txt'
    )
    data = []
    with open(file_path) as file:
        for line in file:
            line = line.rstrip('\n')
            if len(line) == 0:
                continue
            data.append(line)
    return data


def get_sum_of_power_of_min_sets(data):
    sum = 0
    for line in data:
        max_cubes = {'red': 0, 'green': 0, 'blue': 0}
        revealed_sets = (line.split(': ')[1]).split('; ')
        for revealed_set in revealed_sets:
            cubes = revealed_set.split(', ')
            for cube in cubes:
                quantity, color = cube.split(' ')
                max_cubes[color] = max(max_cubes[color], int(quantity))
        sum += max_cubes['red'] * max_cubes['green'] * max_cubes['blue']
    return sum


if __name__ == '__main__':
    main()
