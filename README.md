# SnakesUtils

SnakesUtils supports conversion from [SNAKES](https://snakes.ibisc.univ-evry.fr/) to data structures.
As a result, Petri nets can be handled easily!
It is used in academia.

## Getting Started

### Installing

```python
% pip install snakes-utils
```

### Example

A very simple example. [notebook example here.](https://github.com/kanekou/snakes_utils/blob/main/examples/example.ipynb)

```py
from snakes.nets import *
import snakes_utils

# create petri nets
n = PetriNet('sample')
n.add_place(Place('p0', [1]))
n.add_place(Place('p1', [1]))
n.add_transition(Transition('t0'))
n.add_transition(Transition('t1'))
n.add_input('p0', 't0', Variable('x'))
n.add_output('p1', 't0', Variable('x'))
n.add_input('p1', 't1', Variable('x'))

su = snakes_utils.Basic(n)

# Outputs the guard conditions for transitions.
print(su.guards)
# {'t0': 'True', 't1': 'True'}

# Outputs input transitions for a place.
print(su.posttrans_place_map)
# {'p0': ['t0'], 'p1': ['t1']}

```

### Prerequisites

- Python :: 3.x

  We have already confirmed the operation of version `3.7`.
  Other versions are also expected to work, but we have not been able to confirm.

## Running the tests

```python
% python3 -m unittest
```

## Supported specific topologies

In addition to basic Petri nets, specific topologies are supported.
More commonly, the Basic class will be easier to use.

- Job Shop Scheduling Problem(jss)

## Contributing

Welcome!

## Versioning

We use pypi for versioning. For the versions available, see the tags on this repository.

## API Reference

### class `Basic`

Basic class deals with simple Petri nets.

#### Method `__init__(self, n)`

Initialize the instance of Basic Class, that convert snakes model into a data structure.

```python
su = snakes_utils.Basic(n)
```

##### Call API

- `n`: SNAKES net model

#### Method `places(self)`

Return a list of places.

```python
su = snakes_utils.Basic(n)
print(su.places)
# [<place>,...]
```

#### Method `trans(self)`

Return a list of transitions.

```python
su = snakes_utils.Basic(n)
print(su.trans)
# [<transition>,...]
```

#### Method `guard(self)`

Return the guard conditions for the transition.

```python
su = snakes_utils.Basic(n)
print(su.guard)
# { <transition>: <guard>,... }
```

#### Method `preplaces_trans_map(self)`

Return the place behind the transition.

```python
su = snakes_utils.Basic(n)
print(su.preplaces_trans_map)
# { <transiton>: <place>,... }
```

#### Method `postplaces_trans_map(self)`

Return the place in front of the transition.

```python
su = snakes_utils.Basic(n)
print(su.postplaces_trans_map)
# { <transiton>: <place>,... }
```

#### Method `pretrans_place_map(self)`

Return the transition behind the place.

```python
su = snakes_utils.Basic(n)
print(su.pretrans_place_map)
# { <place>: <transition>,... }
```

#### Method `posttrans_place_map(self)`

Return the transition in front of the place.

```python
su = snakes_utils.Basic(n)
print(su.posttrans_place_map)
# { <place>: <transition>,... }
```

### class Scheduling

Scheduling problem, one of the combinatorial optimization problems is handled by Petri nets.

#### Method `__init__(self, n, rflag='r')`

Initialize the instance of Scheduling Class, that convert snakes model into a data structure.

```python
su = snakes_utils.Basic(n)
```

##### Call API

- `n`: SNAKES net model
- `rflag`: Resource Flag how to distinguish the resource place from places. **Only the first and only one character can be inserted.**

#### Method `places(self)`

Return a list of places.

```python
su = snakes_utils.Scheduling(n)
print(su.places)
# [<place>,...]
```

#### Method `trans(self)`

Return a list of transitions.

```python
su = snakes_utils.Scheduling(n)
print(su.trans)
# [<transition>,...]
```

#### Method `resources(self)`

Return a list of resources information. Use only for jss.

```python
su = snakes_utils.Scheduling(n)
print(su.resources)
# [<resource>,...]
```

#### Method `preplaces_trans_map(self, resource=False)`

Return the place behind the transition.

```python
su = snakes_utils.Scheduling(n)
print(su.preplaces_trans_map)
# { <transiton>: <place>,... }
```

##### Call API

- `bool resouce`: Include resouce transition.

#### Method `postplaces_trans_map(self, resource=False)`

Return the place in front of the transition.

```python
su = snakes_utils.Scheduling(n)
print(su.postplaces_trans_map)
# { <transiton>: <place>,... }
```

##### Call API

- `bool resouce`: Include resouce transition.

#### Method `pretrans_place_map(self)`

Return the transition behind the place.

```python
su = snakes_utils.Scheduling(n)
print(su.pretrans_place_map)
# { <place>: <transition>,... }
```

#### Method `posttrans_place_map(self)`

Return the transition in front of the place.

```python
su = snakes_utils.Scheduling(n)
print(su.posttrans_place_map)
# { <place>: <transition>,... }
```

#### Method `trans_resource_map(self)`

Return a set of transitions that need resources. Use only for jss.

```python
su = snakes_utils.Scheduling(n)
print(su.trans_resource_map)
# {<resource>: {<transition>, ...}, ...},
```

#### Method `resources_trans_map(self)`

Return a set of machines that need transitions. Use only for jss.

```python
su = snakes_utils.Scheduling(n)
print(su.resources_trans_map)
# {<transition>: {<resource>, ...}, ...},
```

#### Method `pt(self)`

Return the processing time for each operation. Use only for jss.

```python
su = snakes_utils.Scheduling(n)
print(su.pt)
# {<transition>: <processing time>,...},
```

#### Method `jobs(self)`

Return operations for each jobs. The job number is determined dynamically. Use only for jss.

```python
su = snakes_utils.Scheduling(n)
print(su.jobs)
# { job_number: [trans_id,...],... }
```

## Reference site

- https://snakes.ibisc.univ-evry.fr/
- https://github.com/fpom/snakes

## License

The source code is licensed LGPL.

(C) 2021-2022 Kohei Kaneshima

This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with this library; If not, see <https://www.gnu.org/licenses/>.
