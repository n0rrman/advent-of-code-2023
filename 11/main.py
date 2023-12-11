import numpy as np


def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
    except Exception as e:
        print("Something went wrong: ", e)

    return content


def process_input(input):
    data = [[val for val in line] for line in input.splitlines()] 
    return np.array(data)


def calc_part_one(data):
    row_empty = np.nonzero(np.all(data == '.', axis=1))[0]
    col_empty = np.nonzero(np.all(data.T == '.', axis=1))[0] 

    galaxy_location = np.where(data == '#')
    galaxy_map = []

    sum_distance = 0

    for galaxy in zip(galaxy_location[0], galaxy_location[1]):
        from_y = np.sum(row_empty < galaxy[0]) + galaxy[0]
        from_x = np.sum(col_empty < galaxy[1]) + galaxy[1]
        galaxy_map.append((from_y, from_x))

        for to_star in galaxy_map[:-1]:
            sum_distance += abs(to_star[0] - from_y) + abs(to_star[1] - from_x)

    return sum_distance

    
def calc_part_two(data):
    row_empty = np.nonzero(np.all(data == '.', axis=1))[0]
    col_empty = np.nonzero(np.all(data.T == '.', axis=1))[0] 

    galaxy_location = np.where(data == '#')
    galaxy_map = []

    sum_distance = 0

    for galaxy in zip(galaxy_location[0], galaxy_location[1]):
        from_y = np.sum(row_empty < galaxy[0])*(1000000-1) + galaxy[0]
        from_x = np.sum(col_empty < galaxy[1])*(1000000-1) + galaxy[1]
        galaxy_map.append((from_y, from_x))

        for to_star in galaxy_map[:-1]:
            sum_distance += abs(to_star[0] - from_y) + abs(to_star[1] - from_x)

    return sum_distance


def main():
    input = read_file('input.txt')
    data = process_input(input)

    part_one = calc_part_one(data)
    part_two = calc_part_two(data)

    print("Part one: {}\nPart two: {}".format(part_one, part_two))


if __name__ == "__main__":
    main()