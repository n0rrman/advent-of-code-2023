
def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
    except Exception as e:
        print("Something went wrong: ", e)

    return content

def process_input(input):
    data = [x.split(': ')[1].replace(';', ',').split(', ') for x in input.splitlines()]
    return data


def calc_part_one(data):
    max_red = 12
    max_green = 13
    max_blue = 14

    index = 1
    pos_sum = 0

    possible = True;

    for row in data:
        for e in row:
            val, color = e.split()
            if color == "red": possible &= int(val) <= max_red
            if color == "green": possible &= int(val) <= max_green
            if color == "blue": possible &= int(val) <= max_blue
        if possible:
            pos_sum += index

        possible = True
        index += 1

    return pos_sum



def calc_part_two(data):
    max_red = 0 
    max_green = 0
    max_blue = 0

    sum = 0

    for row in data:
        for e in row:
            val, color = e.split()
            if color == "red": max_red = max(max_red, int(val))
            if color == "green": max_green = max(max_green, int(val))
            if color == "blue": max_blue = max(max_blue, int(val))

        sum += max_red * max_green * max_blue
        max_red = 0
        max_green = 0
        max_blue = 0

    return sum


def main():
    input = read_file('input.txt')
    data = process_input(input)

    part_one = calc_part_one(data)
    part_two = calc_part_two(data)

    print("Part one: {}\nPart two: {}".format(part_one, part_two))


if __name__ == "__main__":
    main()