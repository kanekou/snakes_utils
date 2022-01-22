# Copyright (c) 2021 Kohei Kaneshima (kanekou)
# This software is released under the MIT License, see LICENSE.txt.

# Extract the topology of Petri nets as the adjacency list.
def extract_graph_topology(n, trans, post=False):
    topology = {}
    for t in trans:
        topology[t] = list(n.transition(f'{t}').post.keys()) if post else list(
            n.transition(f'{t}').pre.keys())
    return topology
