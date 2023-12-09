import numpy as np
import networkx as nx
import math
from itertools import product


def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
    except Exception as e:
        print("Something went wrong: ", e)

    return content


def chars_to_val(chars):
    num_0 = (ord(chars[0]) - ord('A')) * (ord('Z') - ord('A') + 1)**2
    num_1 = (ord(chars[1]) - ord('A')) * (ord('Z') - ord('A') + 1)
    num_2 = (ord(chars[2]) - ord('A'))
    return int(num_0 + num_1 + num_2)


def process_input(input):
    move_order = list(map(lambda x: 0 if x == 'L' else 1, list(input.splitlines()[0])))

    char_network = [line.replace(' = (', ';').replace(', ', ';').replace(')', '').split(';') for line in input.splitlines()[2:]]
    num_network = np.array([[chars_to_val(chars) for chars in row] for row in char_network])

    network = {}
    for val, l, r in num_network:
        network[val] = (l, r)

    return move_order, network


def find_end(move_order, network, index, from_val, to_val):
    idx = index
    current = from_val
    start = True

    while start | (not current == to_val):
        start = False
        next_move = move_order[idx % len(move_order)]
        current = network[current][next_move]
        idx += 1

    return idx


def calc_part_one(move_order, network):
    start = chars_to_val('AAA')
    end = chars_to_val('ZZZ')
    return find_end(move_order, network, 0, start, end)


def ends_with(char, idx):
    return idx % (ord('Z') - ord('A') +1) == ((ord(char)-ord('A')))


def build_graph(network):
    G = nx.DiGraph()
    for k, v in network.items(): 
        G.add_node(k)
        G.add_edge(k, v[0])
        G.add_edge(k, v[1])

    return G 


def calc_part_two(move_order, network):
    current = [idx for idx in list(network.keys()) if ends_with('A', idx)]
    end = [idx for idx in list(network.keys()) if ends_with('Z', idx)]

    reachable_ends = []
    G = build_graph(network)
    reachable_ends = [[start, end] for start, end in product(current, end) if nx.has_path(G, start, end)]

    for start, end in product(current, end):
        if nx.has_path(G, start, end):
            reachable_ends.append([start, end])

    cycles = []
    for nodes in reachable_ends:
        start = nodes[0]
        end = nodes[1]
        index = find_end(move_order, network, 0, start, end)
        cycles.append(index)  

    return math.lcm(*cycles)


def main():
    input = read_file('input.txt')
    mo, net = process_input(input)

    part_one = calc_part_one(mo, net)
    part_two = calc_part_two(mo, net)

    print("Part one: {}\nPart two: {}".format(part_one, part_two))


if __name__ == "__main__":
    main()