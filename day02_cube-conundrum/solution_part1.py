import os


def main(input_file):
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    sum_of_possible_games_ids = 0
    with open(input_file) as file:
        for line in file:
            line = line.rstrip('\n')
            if len(line) == 0:
                continue
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
            sum_of_possible_games_ids += game_id
    return sum_of_possible_games_ids


if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(dirname, 'input.txt')
    res = main(file_path)
    print(res)
