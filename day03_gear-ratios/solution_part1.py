import sys
import os


def main():
    data = handle_input()
    sum = get_sum_of_part_numbers(data)
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
            if len(line) == 0:
                continue
            data.append(line)
    return data


def get_sum_of_part_numbers(matrix):
    sum = 0
    for i, line in enumerate(matrix):
        cur_number = ''
        has_symbol_adjacent = False
        for j, char in enumerate(line):
            if char.isdigit():
                cur_number += char
                if not has_symbol_adjacent and has_symbol_adjacent_to(matrix, i, j):
                    has_symbol_adjacent = True
            else:
                if cur_number and has_symbol_adjacent:
                    sum += int(cur_number)
                cur_number = ''
                has_symbol_adjacent = False
    return sum


def has_symbol_adjacent_to(matrix, i, j):
    symbols = set('*#+$=&%/@-')
    # rotating in a circle clockwise starting from the top
    deviations = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    for k, l in deviations:
        try:
            if matrix[i + k][j + l] in symbols:
                return True
        except IndexError:
            continue
    return False


if __name__ == '__main__':
    main()
