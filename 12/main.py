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



def calc_section(section, targets):
    # print( section, targets )
    # for target in targets:
    target = targets[0]
    # print("target:", target)
    arrangements = 0
    pattern = re.compile(r'\.*#{' + target + r'}\.*')
    # patterns = []   
    combo_array = [['#', '.'] if x == '?' else [x] for x in section]

    for x in itertools.product(*combo_array):
        if re.fullmatch(pattern, ''.join(x)):
            # print(target, section)
            print(x)
            arrangements += 1
        # print(section, target)

    return arrangements


def get_combos(spring_map, targets):
    print(spring_map, targets)

    prev_char = '.'

    # targets_list = [int(x) for x in targets.split(',')]

    if not targets:
        if (spring_map.count('#') > 0):
            return 0
        else:
            return 1
    
    next_num = targets.pop(0)

    # print(targets_list)
    # print(targets_list.pop(0))
    # print(targets_list)
    char = spring_map[:next_num]
    # char = spring_map.splice(0, next_num)splice
    print(char)
    if char == '#':
        return 1 + get_combos(spring_map[1:], targets[1:]) + get_combos(spring_map[1:], targets)
    if char == '?':
        return get_combos(spring_map[1:], targets) + get_combos(spring_map[1:], targets)
    if char == '.':
       return 1 

    return 0

def calc_part_two(data):
    part_two_data = [[(springs+'?')*4+springs, (vals+',')*4+vals] for springs, vals in data]
    return calc_part_one(part_two_data)

    # arrangements = 0
    # if data:
    #     line = data[0]*5

    #     spring_map = line[0]*5
    #     targets = [int(x) for x in line[1].split(',')]

    #     arrangements += get_combos(spring_map, targets)

    # return arrangements
    

def main():
    input = read_file('test_input.txt')
    data = process_input(input)

    part_one = calc_part_one(data)
    part_two = calc_part_two(data)

    print("Part one: {}\nPart two: {}".format(part_one, part_two))


if __name__ == "__main__":
    main()