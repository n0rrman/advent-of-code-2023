import numpy as np
import networkx as nx


def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
    except Exception as e:
        print("Something went wrong: ", e)

    return content


def process_input(input):
    data = [[val for val in line] for line in input.splitlines()] 
    return data


def calc_part_one(graph, start):
    paths = nx.single_source_dijkstra_path_length(graph, start)
    return np.max(np.array([*paths.values()]))


def calc_part_two(graph, start, data):
    connected_nodes = nx.descendants(graph, start)
    connected_nodes.add(start)

    y_max = max(node[0] for node in connected_nodes)
    x_max = max(node[1] for node in connected_nodes)

    grid = np.zeros((x_max+1, y_max+1), dtype=int)
    for node in connected_nodes:
        grid[node[1], node[0]] = 10

    start_node = [[(edge[0] - start[0], edge[1] - start[1]) for edge in edges][1] for edges in graph.edges(start)]
    type_convert = {
        "[(-1, 0), (1, 0)]" : '|',
        "[(1, 0), (-1, 0)]" : '|',
        "[(0, -1), (1, 0)]" : '7',
        "[(1, 0), (0, -1)]" : '7',
        "[(1, 0), (0, 1)]" : 'F',
        "[(0, 1), (1, 0)]" : 'F'
    }

    try:
        data[start[1]][start[0]]  = type_convert["{}".format(start_node)]
    except:
        data[start[1]][start[0]]  = '-'

    for y, row in enumerate(grid):
        inside = False
        for x, square in enumerate(row):
            if square == 10:
                changing = np.isin(data[y][x], ['|', '7', 'F'])
                inside = not inside if changing else inside
            elif inside: grid[y][x] = 1

    return np.sum(grid % 10)


def node_name(x, y):
    return (x, y)


def build_graph(data):
    G = nx.Graph()

    for y, line in enumerate(data):
        for x, e in enumerate(line):
            if e != '.':
                # Add node
                from_node = node_name(x,y)
                G.add_node(from_node)

                if e == 'S': start_node = from_node

                # Add right edge
                if (np.isin(data[y][x], ['S', '-', 'F', 'L'])) and (x+1 < len(line)) and (np.isin(data[y][x+1], ['S', '-', 'J', '7'])):
                    to_node = node_name(x+1, y)
                    G.add_edge(from_node, to_node)

                # Add bottom edge
                if (np.isin(data[y][x], ['S', '|', '7', 'F'])) and (y+1 < len(data)) and (np.isin(data[y+1][x], ['S', '|', 'L', 'J'])):
                    to_node = node_name(x, y+1)
                    G.add_edge(from_node, to_node)

    return G, start_node 


def main():
    input = read_file('input.txt')
    data = process_input(input)

    graph, start = build_graph(data)

    part_one = calc_part_one(graph, start)
    part_two = calc_part_two(graph, start, data)

    print("Part one: {}\nPart two: {}".format(part_one, part_two))


if __name__ == "__main__":
    main()