
import numpy as np
from math import lcm

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
    for row in data.T:
        section_start = 0
        num_O = 0
        for idx, rock in enumerate(row):
            length = len(row)
            if rock == 'O':
                num_O += 1
            if rock == '#':
                value += sum(list(range(length +1 -section_start - num_O , length +1 - section_start)))
                section_start = idx + 1
                num_O = 0
        value += sum(list(range(length +1 - section_start - num_O , length +1 - section_start)))
    return value


def tilt_dish(dish, direciton):
    if direciton == 'N':
        temp_dish = dish.T
    if direciton == 'S':
        temp_dish = np.fliplr(dish.T)
    if direciton == 'W':
        temp_dish = dish
    if direciton == 'E':
        temp_dish = np.fliplr(dish)

    new_table = []
    for row in temp_dish:
        num_O = 0
        num_space = 0
        new_row = np.array([])
        for i, rock in enumerate(row):
            if rock == 'O':
                num_O += 1
            if rock == '.':
                num_space += 1
            if rock == '#':
                new_row = np.append(new_row, [['O']*num_O + ['.']*num_space + ['#']]) 
                num_O = 0
                num_space = 0

        new_row = np.append(new_row, [['O']*num_O + ['.']*num_space])
        new_table.append(new_row)

    if direciton == 'N':
        tilted_dish = np.array(new_table).T
    if direciton == 'S':
        tilted_dish = np.fliplr(new_table).T 
    if direciton == 'W':
        tilted_dish = np.array(new_table)
    if direciton == 'E':
        tilted_dish = np.fliplr(new_table)

    return tilted_dish



def calc_part_two(data):
    cycles = dict()
    # history = dict()
    # prev_vals = dict()

    limit = 100
    spins = 0
    # memory = pd.DataFrame()
    # for index in range(1, spins+1):
    while limit > 0:
        # # key = hash(np.array2string(data))
        spins += 1 
        # print('')
        # print(data)
        # print('')
        # if key in cache:
        #     data = cache[key]
        # else:

        # if True:
        
            # print(index)
        north = tilt_dish(data, 'N')
        west = tilt_dish(north, 'W')
        south = tilt_dish(west, 'S')
        east = tilt_dish(south, 'E')
        data = east

            # cache[key] = data

            # val = 0
        val = sum((idx + 1) * np.count_nonzero(row == 'O') for idx, row in enumerate(data[::-1]))

        # print(spins, val)
        if val in cycles:

            (prev_val, cycle, i) = cycles[val]
            # print(prev_val, cycle, spins)
            # prev_prev, prev_val = prev_vals[val]
            
            if (lcm(spins - prev_val, cycle) == cycle):
                # cycles2[val] = cycle
                # real_cycles[val] = (spins%(spins-prev_val), spins-prev_val)
                limit -= 1
            else:
                # limit = 50
                # print(spins, val, " changed")
                # cycles[val] = (spins, spins%(spins-prev_val), spins - prev_val)
                cycles[val] = (spins, lcm(spins - prev_val, cycle), i+1)
                # print(val)
                # history.setdefault(val, {})[val] = val
                # print(val, prev_val, spins, cycles[val])
                # prev_vals[val] = (prev_val, spins)

            # limit -= 1
            # print(spins, prev_val, cycle)

        elif spins > 200:            
            cycles[val] = (spins, 1, 0) 
            # print(val)
            # cache[val] = index
        # if index > 100:
        #    memory[key] =  1

    # print(real_cycles)
    # print(cycles2)
    # print(prev_vals)
    print(cycles) 


    # for k, (val, mod, cycle) in cycles.items():
    #     print(val, mod, cycle)
    #     if 1000000000 % cycle == mod:
    #         print(k) 


    # print(cache)
    return 2


def main():
    input = read_file('input.txt')
    data = process_input(input)

    part_one = calc_part_one(data)

    part_two = calc_part_two(data)

    print("Part one: {}\nPart two: {}".format(part_one, part_two))


if __name__ == "__main__":
    main()