import re
import itertools


def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
    except Exception as e:
        print("Something went wrong: ", e)

    return content


def process_input(input):
    data = [x.split(' ') for x in input.splitlines()] 
    return data


def calc_part_one(data):
    arrangements = 0

    for line in data:
        spring_map = line[0]
        target = line[1].split(',')

        regex_ends = r'\.*'
        regex_padding = r'\.+'

        pattern = regex_ends + r'#{' + target[0] + r'}'
        for number in target[1:]:
            pattern += regex_padding + r'#{' + number + r'}'
        pattern += regex_ends

        spring_map_combos = [['#', '.'] if x == '?' else [x] for x in spring_map] 

        pattern = re.compile(pattern)
        matches = 0
        for x in itertools.product(*spring_map_combos):
            if re.fullmatch(pattern, ''.join(x)):
                matches += 1

        arrangements += matches
    return arrangements


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