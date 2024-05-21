def solution(input_file):
    sum_of_min_set_powers = 0
    with open(input_file) as file:
        for line in file:
            line = line.rstrip('\n')
            if len(line) == 0:
                continue
            max_cubes = {'red': 0, 'green': 0, 'blue': 0}
            revealed_sets = (line.split(': ')[1]).split('; ')
            for revealed_set in revealed_sets:
                cubes = revealed_set.split(', ')
                for cube in cubes:
                    quantity, color = cube.split(' ')
                    max_cubes[color] = max(max_cubes[color], int(quantity))
            power = max_cubes['red'] * max_cubes['green'] * max_cubes['blue']
            sum_of_min_set_powers += power
    return sum_of_min_set_powers


file_path = 'input.txt'
res = solution(file_path)
print(res)
