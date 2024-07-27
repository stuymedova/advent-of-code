import os


def main(input_file):
    matrix = []
    with open(input_file) as file:
        for line in file:
            line = line.rstrip('/n')
            if len(line) == 0:
                continue
            matrix.append(line)
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
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(dirname, 'input.txt')
    res = main(file_path)
    print(res)
