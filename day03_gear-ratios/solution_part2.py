import sys
import os


def main():
    data = handle_input()
    sum = get_sum_of_gear_ratios(data)
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


def get_sum_of_gear_ratios(matrix):
    sum = 0
    gear_candidates = find_gear_candidates(matrix)
    for i, j in gear_candidates:
        num = get_adjacent_numbers(matrix, i, j)
        if len(num) != 2:
            continue
        sum += num[0] * num[1]
    return sum


def find_gear_candidates(matrix):
    coordinates = []
    gear_candidate = '*'
    for i, line in enumerate(matrix):
        for j, char in enumerate(line):
            if matrix[i][j] == gear_candidate:
                coordinates.append([i, j])
    return coordinates


def get_adjacent_numbers(matrix, i, j):
    adjacent_digit_coordinates = get_adjacent_digits_coordinates(matrix, i, j)
    number_start_coordinates = set(
        map(lambda x: get_start_coordinates(matrix, *x), adjacent_digit_coordinates))
    return list(map(lambda x: get_number_by_start_coordinates(matrix, *x), number_start_coordinates))


def get_adjacent_digits_coordinates(matrix, i, j):
    matches = []
    # rotating in a circle clockwise starting from the top
    deviations = [[-1, 0], [-1, 1], [0, 1], [1, 1],
                  [1, 0], [1, -1], [0, -1], [-1, -1]]
    for k, l in deviations:
        try:
            if matrix[i + k][j + l].isdigit():
                matches.append([i + k, j + l])
        except IndexError:
            continue
    return matches


def get_start_coordinates(matrix, i, j):
    while j != 0 and matrix[i][j - 1].isdigit():
        j -= 1
    return i, j


def get_number_by_start_coordinates(matrix, i, j):
    number = ''
    while j != len(matrix[i]) and matrix[i][j].isdigit():
        number += matrix[i][j]
        j += 1
    return int(number)


if __name__ == '__main__':
    main()
