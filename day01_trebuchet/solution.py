spelled_out_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
spelled_out_digits_dict = {
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

def get_first_digit(str):
    for i in range(len(str)):
        char = str[i]
        if char.isdigit():
            return char
        for spelled_out_digit in spelled_out_digits:
            if str.startswith(spelled_out_digit, i):
                return spelled_out_digits_dict[spelled_out_digit]

def get_last_digit(str):
    for i in range(len(str) - 1, -1, -1):
        char = str[i]
        if char.isdigit():
            return char
        for spelled_out_digit in spelled_out_digits:
            if str[:i].endswith(spelled_out_digit):
                return spelled_out_digits_dict[spelled_out_digit]

def solution(input_file):
    sum = 0
    with open(input_file) as file:
        for line in file:
            first_digit = get_first_digit(line)
            last_digit = get_last_digit(line)
            if first_digit and last_digit:
                sum += int(first_digit + last_digit)
    return sum

file_path = 'input.txt'
res = solution(file_path)
print(res)
