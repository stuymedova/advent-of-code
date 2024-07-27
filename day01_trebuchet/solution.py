import sys
import os


spelled_out_digits = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def main():
    data = handle_input()
    sum = sum_calibration_values(data)
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


def sum_calibration_values(data):
    sum = 0
    for line in data:
        first_digit = get_first_digit(line)
        last_digit = get_last_digit(line)
        if first_digit and last_digit:
            sum += int(first_digit + last_digit)
    return sum


def get_first_digit(str):
    for i in range(len(str)):
        char = str[i]
        if char.isdigit():
            return char
        for spelled_out_digit in spelled_out_digits.keys():
            if str.startswith(spelled_out_digit, i):
                return spelled_out_digits[spelled_out_digit]


def get_last_digit(str):
    for i in range(len(str) - 1, -1, -1):
        char = str[i]
        if char.isdigit():
            return char
        for spelled_out_digit in spelled_out_digits.keys():
            if str[:i].endswith(spelled_out_digit):
                return spelled_out_digits[spelled_out_digit]


if __name__ == '__main__':
    main()
