import numpy as np


def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
    except Exception as e:
        print("Something went wrong: ", e)

    return content


def process_input(input):
    data = np.array([list(x) for x in input.splitlines()])
    return data


def calc_part_one(data):
    value = 0 
    for i, row in enumerate(data.T):
        section_start = 0
        num_O = 0
        for i, rock in enumerate(row):
            length = len(row)
            if rock == 'O':
                num_O += 1
            if rock == '#':
                value += sum(list(range(length +1 -section_start - num_O , length +1 - section_start)))
                section_start = i + 1
                num_O = 0

        value += sum(list(range(length +1 - section_start - num_O , length +1 - section_start)))

    return value


def calc_part_two(data):
    return 2


def main():
    input = read_file('input.txt')
    data = process_input(input)

    part_one = calc_part_one(data)
    part_two = calc_part_two(data)

    print("Part one: {}\nPart two: {}".format(part_one, part_two))


if __name__ == "__main__":
    main()