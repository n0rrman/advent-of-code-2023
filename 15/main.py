import numpy as np


def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
    except Exception as e:
        print("Something went wrong: ", e)

    return content


def process_input(input):
    data = np.array(input.split(','))
    return data


def calc_hash(input_string):
    hash_val = 0 
    for char in input_string:
       hash_val = ((hash_val + ord(char)) * 17) % 256 

    return hash_val


def calc_part_one(data):
    return sum([calc_hash(entry) for entry in data])


def calc_part_two(data):
    focus_map = dict()

    for part in data:
        rm = part.find('-')
        eq = part.find('=')
        
        if rm > 0:
            id, val = part.split('-')
            hash = calc_hash(id)
            try:
                focus_map[hash].pop(id)  
            except:
                pass

        if eq > 0:
            id, val = part.split('=')
            hash = calc_hash(id)
            focus_map.setdefault(hash, {})[id] = int(val)  

    focusing_power = 0
    for box_num, box_vals in focus_map.items():
        for slot_num, (_, focal_length) in enumerate(box_vals.items()):
            focusing_power += (box_num+1) * (slot_num+1) * focal_length

    return focusing_power

def main():
    input = read_file('input.txt')
    data = process_input(input)

    part_one = calc_part_one(data)
    part_two = calc_part_two(data)

    print("Part one: {}\nPart two: {}".format(part_one, part_two))


if __name__ == "__main__":
    main()