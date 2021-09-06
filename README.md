# SnakesUtils

SnakesUtils supports conversion from [SNAKES](https://snakes.ibisc.univ-evry.fr/) to data structures.
As a result, Petri nets can be handled easily!
It is used in academia.

## Example

A very simple example. [Here's the actual code in jupyter notebook.](https://github.com/kanekou/snakes2ds/blob/main/examples/test_snakes.ipynb)

```py
import snakes.plugins
snakes.plugins.load("gv", "snakes.nets", "nets")
from nets import *
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
print(su.guards)
# {'t0': 'True', 't1': 'True'}

print(su.posttrans_place_map)
# {'p0': ['t0'], 'p1': ['t1']}

```

## Supported specific topologies.

In addition to basic Petri nets, specific topologies are supported.

- Job Shop Scheduling Problem(jss)

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

## Reference site

- https://snakes.ibisc.univ-evry.fr/
- https://github.com/fpom/snakes

## License

The source code is licensed MIT, see LICENSE.txt.
