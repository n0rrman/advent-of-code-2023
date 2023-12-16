import numpy as np
import sys

sys.setrecursionlimit(10000)


def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
    except Exception as e:
        print("Something went wrong: ", e)

    return content


def process_input(input):
    data = [list(line) for line in input.splitlines()]
    return data


def traverse_map(map, move, visited, cache):
    x, y, direction = move

    if x < 0 or y < 0 or y >= len(map) or x >= len(map[0]):
        return

    if move in cache:
        return 

    cache.add(move)
    visited[y, x] = 1
    tile = map[y][x]

    if tile == '|':
        traverse_map(map, (x, y+1, 'U'), visited, cache)
        traverse_map(map, (x, y-1, 'D'), visited, cache)

    if tile == '-':
        traverse_map(map, (x+1, y, 'R'), visited, cache)
        traverse_map(map, (x-1, y, 'L'), visited, cache)
    
    if tile == '\\':
        if direction == 'R': traverse_map(map, (x, y+1, 'U'), visited, cache)
        if direction == 'L': traverse_map(map, (x, y-1, 'D'), visited, cache)
        if direction == 'U': traverse_map(map, (x+1, y, 'R'), visited, cache)
        if direction == 'D': traverse_map(map, (x-1, y, 'L'), visited, cache)
    
    if tile == '/':
        if direction == 'R': traverse_map(map, (x, y-1, 'D'), visited, cache)
        if direction == 'L': traverse_map(map, (x, y+1, 'U'), visited, cache)
        if direction == 'U': traverse_map(map, (x-1, y, 'L'), visited, cache)
        if direction == 'D': traverse_map(map, (x+1, y, 'R'), visited, cache)

    if tile == '.':
        if direction == 'R':
            traverse_map(map, (x+1, y, 'R'), visited, cache)
        if direction == 'L':
            traverse_map(map, (x-1, y, 'L'), visited, cache)
        if direction == 'U':
            traverse_map(map, (x, y+1, 'U'), visited, cache)
        if direction == 'D':
            traverse_map(map, (x, y-1, 'D'), visited, cache)


def calc_visited_nodes(map, starting):
    cache = set()
    visited = np.zeros(np.array(map).shape, dtype=int)
    traverse_map(map, starting, visited, cache)
    return np.sum(visited)


def calc_part_one(map):
    starting = (0, 0, 'R')
    return calc_visited_nodes(map, starting)


def calc_part_two(map):
    max_val = 0
    for x in range(len(map[0])):    
        max_val = max(max_val, calc_visited_nodes(map, (x, 0, 'U')))
        max_val = max(max_val, calc_visited_nodes(map, (x, len(map)-1, 'D')))

    for y in range(len(map)):    
        max_val = max(max_val, calc_visited_nodes(map, (0, y, 'L')))
        max_val = max(max_val, calc_visited_nodes(map, (len(map[0])-1, y, 'R')))
        
    return max_val


def main():
    input = read_file('input.txt')
    data = process_input(input)

    part_one = calc_part_one(data)
    part_two = calc_part_two(data)

    print("Part one: {}\nPart two: {}".format(part_one, part_two))


if __name__ == "__main__":
    main()