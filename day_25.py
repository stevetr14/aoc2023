import matplotlib.pyplot as plt
import networkx as nx

from utils import parse_input


def part_one():
    lines = parse_input("day_25.txt")
    total = 1

    components = dict()

    for line in lines:
        component, connected = line.split(": ")
        components[component] = connected.split(" ")

    g = nx.Graph()
    g.add_nodes_from(components.keys())

    for k, v in components.items():
        g.add_edges_from(([k, n] for n in v))

    # Visualise the connected points
    # nx.draw(g)
    # plt.show()

    # Remove the connected wires with eye-balling technique
    g.remove_edge("bnv", "rpd")
    g.remove_edge("ttv", "ztc")
    g.remove_edge("vfh", "bdj")

    for item in list(nx.connected_components(g)):
        total *= len(item)

    print("Part 1: ", total)


def part_two():
    lines = parse_input("test.txt")
    total = 0

    print("Part 2: ", total)


if __name__ == "__main__":
    part_one()
    # part_two()
