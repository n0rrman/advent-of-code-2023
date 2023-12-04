import numpy as np


def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
    except Exception as e:
        print("Something went wrong: ", e)

    return content


def process_input(input):
    winning_numbers = [] 
    numbers = []
    
    for line in input.splitlines():
        _, winning_number, number = line.replace(':', '|').split('|')
        winning_numbers.append(winning_number.strip().replace('  ', ' ').split(' '))
        numbers.append(number.strip().replace('  ', ' ').split(' '))

    return np.array(winning_numbers), np.array(numbers)


def calc_part_one(winning_numbers, numbers):
    sum = 0

    for i, row in enumerate(numbers):
        wins = np.isin(row, winning_numbers[i])
        num_wins = np.count_nonzero(wins)

        calc = 0 if num_wins == 0 else 2**(num_wins-1)
        sum += calc

    return sum


def scratch_card(winning_numbers, numbers, index):
    wins = np.isin(numbers[index], winning_numbers[index])
    num_wins = np.count_nonzero(wins)

    wins = [scratch_card(winning_numbers, numbers, card) for card in range(index+1, index+1+num_wins)]

    return 1 + sum(wins)


def calc_part_two(winning_numbers, numbers):
    wins = [scratch_card(winning_numbers, numbers, i) for i in range(len(numbers))]

    return sum(wins)


def main():
    input = read_file('input.txt')
    winning, numbers = process_input(input)

    part_one = calc_part_one(winning, numbers)
    part_two = calc_part_two(winning, numbers)

    print("Part one: {}\nPart two: {}".format(part_one, part_two))


if __name__ == "__main__":
    main()