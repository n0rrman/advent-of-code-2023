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
    symbols = set()

    for row in data:
        for e in row:
            if (not str.isnumeric(e)) & (e != '.'):
                symbols.add(e)

    return data, list(symbols)


def calc_part_one(data, symbols):

    num = 0
    is_valid = False
    multiply = False

    total = 0

    for y, row in enumerate(data):
        for x, e in enumerate(row):
            if str.isnumeric(e):
                num *= 10 if multiply else 1
                multiply = True
                num += int(e)
                is_valid = is_valid | np.isin(data[max(y-1,0):min(y+1,len(data))+1, max(x-1,0):min(x+1, len(row))+1], symbols).any()

            else:
                total += num if is_valid else 0
                num = 0
                multiply = False
                is_valid = False
                
        total += num if is_valid else 0
        num = 0
        multiply = False
        is_valid = False

    return total


def find_number(data, y, x):
    start_index = x
    end_index = x+1
    char = data[y, x]
    if (char == '.') | (char == '*'):
        return None;
    
    while start_index - 1 >= 0:
        try:
            int("".join(data[y, start_index-1:end_index]))
            start_index -= 1
        except:
            break

    while end_index + 1 <= len(data[0]):
        try:
            int("".join(data[y, start_index:end_index+1]))
            end_index += 1
        except:
            break

    return int("".join(data[y, start_index: end_index]));


def calc_part_two(data):
    sum = 0;
    gear_locations = np.where(data == '*')

    for location in zip(gear_locations[0], gear_locations[1]):
        connected_numbers = set()
        y, x = location

        for i in range(max(y-1, 0), min(y+1, len(data))+1):
            for j in range(max(x-1, 0), min(x+1, len(data[0]))+1):
                connected_numbers.add(find_number(data, i, j))

        filtered_numbers = list(filter(None, connected_numbers))
        if len(filtered_numbers) >= 2:
            sum += filtered_numbers[0] * filtered_numbers[1]

    return sum


def main():
    input = read_file('input.txt')
    data, symbols = process_input(input)

    part_one = calc_part_one(data, symbols)
    part_two = calc_part_two(data)

    print("Part one: {}\nPart two: {}".format(part_one, part_two))


if __name__ == "__main__":
    main()