import sys
import os


def main():
    data = handle_input()
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    sum = get_sum_of_game_ids(data, max_cubes)
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


def get_sum_of_game_ids(data, max_cubes):
    sum = 0
    for line in data:
        is_game_impossible = False
        game_prefix, rest = line.split(': ')
        game_id = int(game_prefix.split(' ')[1])
        revealed_sets = rest.split('; ')
        for revealed_set in revealed_sets:
            cubes = revealed_set.split(', ')
            for cube in cubes:
                quantity, color = cube.split(' ')
                if int(quantity) > max_cubes[color]:
                    is_game_impossible = True
                    break
            if is_game_impossible:
                break
        if is_game_impossible:
            continue
        sum += game_id
    return sum


if __name__ == '__main__':
    main()
