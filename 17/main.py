import numpy as np
import collections

def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
    except Exception as e:
        print("Something went wrong: ", e)

    return content

def process_input(input):
    data = np.array([list(line) for line in input.splitlines()], dtype=int)
    return data



def calc_part_one(data):
    max_TTL = 3
    values = np.zeros(data.shape, dtype=int)+4201337
    # print(values)
    work = collections.deque([(0, 0, max_TTL, 'D'), (0, 0, max_TTL, 'R')])

    while work:
        
        print("hello")
        y, x, TTL, direction = work.pop()
        print(y,x)
        val = data[y, x]
        
        TTL_left = TTL-1 if direction == 'L' else max_TTL
        add_left = direction != 'R' and x > 0 and TTL_left
        add_left = add_left and values[y, x-1] > (val + values[y, x])

        TTL_right = TTL-1 if direction == 'R' else max_TTL
        add_right = direction != 'L' and y < (len(data[0])-1) and TTL_right
        add_right = add_right and values[y, x+1] > (val + values[y, x])
        
        TTL_up = TTL-1 if direction == 'U' else max_TTL
        add_up = direction != 'D' and y > 0 and TTL_up
        add_up = add_left and values[y+1, x] > (val + values[y, x])
        
        TTL_down = TTL-1 if direction == 'D' else max_TTL
        add_down = direction != 'U' and y < (len(data)-1) and TTL_down
        add_down = add_left and values[y-1, x] > (val + values[y, x])


        if add_left: print("left")
        if add_right: print("right")
        if add_up: print("up")
        if add_down: print("down")

        if add_left: 
            work.appendleft((y, x-1, TTL_left, 'L'))
            values[y, x-1] = val + data[y, x-1]
        if add_right: 
            work.appendleft((y, x+1, TTL_right, 'R'))
            values[y, x+1] = val + data[y, x+1]
        if add_up: 
            work.appendleft((y-1, x, TTL_up, 'U'))
            values[y-1, x] = val + data[y-1, x]
        if add_down: 
            work.appendleft((y+1, x, TTL_down, 'D'))
            values[y+1, x] = val + data [y+1, x]
        
        values[y, x] = val
        # print("val: ", val)
        # if values[y,x] < val:
        #     values[y,x] = val
    print(values)
    return values[len(data)-1, len(data[0])-1] 

def calc_part_two(data):
    return 2


def main():
    input = read_file('test_input.txt')
    data = process_input(input)


    part_one = calc_part_one(data)
    part_two = calc_part_two(data)

    print("Part one: {}\nPart two: {}".format(part_one, part_two))


if __name__ == "__main__":
    main()