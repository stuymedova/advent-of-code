import sys
import os


def main():
    data = handle_input()
    sum = get_cards_count(data)
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


def get_cards_count(data):
    cards = [1 for _ in range(len(data))]
    for i, line in enumerate(data):
        _, line = line.split(':')
        winning_numbers, numbers_we_have = line.split('|')
        winning_numbers = set(map(lambda x: int(x), winning_numbers.split()))
        numbers_we_have = set(map(lambda x: int(x), numbers_we_have.split()))
        intersection_length = len(set.intersection(winning_numbers, numbers_we_have))
        for j in range(1, intersection_length + 1):
            cards[i + j] += 1 * cards[i]
    return sum(cards)


if __name__ == '__main__':
    main()
