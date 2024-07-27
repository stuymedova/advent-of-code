import os


def main(input_file):
    number_of_points = 0
    with open(input_file) as file:
        for line in file:
            line = line.rstrip('/n')
            if len(line) == 0:
                continue
            _, line = line.split(':')
            winning_numbers, numbers_we_have = line.split('|')
            winning_numbers = set(map(lambda x: int(x), winning_numbers.split()))
            numbers_we_have = set(map(lambda x: int(x), numbers_we_have.split()))
            intersection_length = len(set.intersection(winning_numbers, numbers_we_have))
            number_of_points += 2 ** (intersection_length - 1) if intersection_length > 0 else 0
    return number_of_points


if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(dirname, 'input.txt')
    res = main(file_path)
    print(res)
