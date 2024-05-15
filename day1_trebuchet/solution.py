def get_first_digit(str):
    for char in str:
        if char.isdigit():
            return char

def get_last_digit(str):
    for char in reversed(str):
        if char.isdigit():
            return char

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
