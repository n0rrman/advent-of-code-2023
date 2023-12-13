import numpy as np


def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
    except Exception as e:
        print("Something went wrong: ", e)

    return content


def process_input(input):
    data = [np.array([list(x) for x in matrix.splitlines()]) for matrix in input.split('\n\n')] 
    return data


def compare_mirror(table, threshold):
    length = len(table) 
    for idx in range(1, length):
        search_range = min(idx, length - idx, length // 2)
        upper_from = max(0, idx- search_range)
        upper_to = idx 
        lower_from = idx
        lower_to = min(length, idx+ search_range)
        if np.sum(table[upper_from: upper_to] != np.flipud(table[lower_from: lower_to])) == threshold:
            return idx
    return -1


def calc_part_one(data):
    val_sum = 0
    for table in data:
        val_vertical = max(0, compare_mirror(table, 0))
        val_horizontal = max(0, compare_mirror(table.T, 0))
        val_sum += val_vertical*100 + val_horizontal 

    return val_sum


def calc_part_two(data):
    val_sum = 0
    for table in data:
        val_vertical = max(0, compare_mirror(table, 1))
        val_horizontal = max(0, compare_mirror(table.T, 1))
        val_sum += val_vertical*100 + val_horizontal 

    return val_sum


def main():
    input = read_file('input.txt')
    data = process_input(input)

    part_one = calc_part_one(data)
    part_two = calc_part_two(data)

    print("Part one: {}\nPart two: {}".format(part_one, part_two))


if __name__ == "__main__":
    main()