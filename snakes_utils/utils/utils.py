# (C) 2021-2022 Kohei Kaneshima

# This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version.

# This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with this library; If not, see <https://www.gnu.org/licenses/>.

# Extract the topology of Petri nets as the adjacency list.
def extract_graph_topology(n, trans, post=False):
    topology = {}
    for t in trans:
        topology[t] = list(n.transition(f'{t}').post.keys()) if post else list(
            n.transition(f'{t}').pre.keys())
    return topology
