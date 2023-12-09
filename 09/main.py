import numpy as np

def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
    except Exception as e:
        print("Something went wrong: ", e)

    return content



def process_input(input):
    data = [line.split(' ') for line in input.splitlines()] 
    return np.array(data).astype(int)


def get_next_val(line):
    if np.all([(val == 0) for val in line]):
        return 0

    next_line = [pair[1] - pair[0] for pair in zip(line[0:], line[1:])]
    next_val = get_next_val(next_line)
    
    return line[-1] + next_val

def calc_part_one(data):
    sum = 0
    for line in data:
        sum += get_next_val(line)
    return sum

def get_first_val(line):
    if np.all([(val == 0) for val in line]):
        return 0

    next_line = [pair[1] - pair[0] for pair in zip(line[0:], line[1:])]
    next_val = get_first_val(next_line)
    
    return line[0] - next_val

def calc_part_two(data):
    sum = 0
    for line in data:
        sum += get_first_val(line)
    return sum


def main():
    input = read_file('input.txt')
    data = process_input(input)

    part_one = calc_part_one(data)
    part_two = calc_part_two(data)

    print("Part one: {}\nPart two: {}".format(part_one, part_two))


if __name__ == "__main__":
    main()