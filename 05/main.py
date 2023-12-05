import numpy as np


def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
    except Exception as e:
        print("Something went wrong: ", e)

    return content


def process_input(input):
    data = input.split('\n\n')
    seeds = np.array([int(val) for val in data[0].split(':')[1].strip().split(' ')])
    transforms = [[[int(number) for number in numbers.split(' ')] 
                   for numbers in transform.split(':')[1].strip().split('\n')]
                     for transform in data[1:]]
    return seeds, transforms 


def transform_all(input_pairs, table):
    output_pairs = np.array([])
    for value_start, value_end in zip(input_pairs[::2], input_pairs[1::2]):
        output_pairs = np.append(output_pairs, transform(value_start, value_end, table)) 

    return output_pairs


def transform(start, end, table):
    for transform_vals in table:
        transform_start = transform_vals[1]
        tranform_end = transform_vals[1] + transform_vals[2] - 1
        if (start >= transform_start) & (start <= tranform_end):
            if (end > tranform_end):
                return np.append((np.array([start, tranform_end]) - (transform_vals[1]-transform_vals[0])), transform(tranform_end+1, end, table))
            else:
                return np.array([start, end]) - (transform_vals[1]-transform_vals[0])

    return np.array([start, end])

 
def calc_part_one(seeds, transforms):
    locations = np.array([])

    for seed in seeds:
        soil = transform(seed, seed, transforms[0])
        fertilizer = transform(*soil, transforms[1])
        water = transform(*fertilizer, transforms[2])
        light = transform(*water, transforms[3])
        temperature = transform(*light, transforms[4])
        humidity = transform(*temperature, transforms[5])
        location = transform(*humidity, transforms[6])
        
        locations = np.append(locations, location[::2])

    return int(locations.min())  


def calc_part_two(seeds, transforms):
    locations = np.array([])

    for seed_start, seed_range in zip(seeds[::2], seeds[1::2]):
        soil = transform_all([seed_start, seed_start+seed_range], transforms[0])
        fertilizer = transform_all(soil, transforms[1])
        water = transform_all(fertilizer, transforms[2])
        light = transform_all(water, transforms[3])
        temperature = transform_all(light, transforms[4])
        humidity = transform_all(temperature, transforms[5])
        location = transform_all(humidity, transforms[6])
        
        locations = np.append(locations, location[::2])
    
    return int(locations.min())  


def main():
    input = read_file('input.txt')
    seeds, transforms = process_input(input)

    part_one = calc_part_one(seeds, transforms)
    part_two = calc_part_two(seeds, transforms)

    print("Part one: {}\nPart two: {}".format(part_one, part_two))


if __name__ == "__main__":
    main()