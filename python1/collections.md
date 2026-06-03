# collections — Container Datatypes - Simplified Explanation

The `collections` module provides specialized container types that extend the built-in `list`, `dict`, `set`, and `tuple`. These are designed to solve common programming problems more efficiently and readably.


## Overview of Specialized Containers

| Container | Purpose |
|-----------|---------|
| `namedtuple()` | Tuple with named fields for better readability |
| `deque` | Double-ended queue; fast appends/pops from both ends |
| `ChainMap` | Combine multiple dictionaries into a single view |
| `Counter` | Count occurrences of items |
| `OrderedDict` | Dictionary that remembers insertion order (less needed since Python 3.7) |
| `defaultdict` | Dictionary that provides default values for missing keys |
| `UserDict` | Wrapper for easier dictionary subclassing |
| `UserList` | Wrapper for easier list subclassing |
| `UserString` | Wrapper for easier string subclassing |


## namedtuple() – Tuples with Named Fields

`namedtuple()` creates tuple subclasses where you can access fields by name instead of index.

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)

print(p[0])           # 11 (indexing still works)
print(p.x)            # 11 (access by name)
print(p)              # Point(x=11, y=22)

x, y = p              # unpack like a regular tuple
```

**Useful methods:**

```python
# Create from iterable
t = [11, 22]
p = Point._make(t)

# Convert to dictionary
p._asdict()           # {'x': 11, 'y': 22}

# Create a new instance with changes
p._replace(x=33)      # Point(x=33, y=22)

# List field names
Point._fields         # ('x', 'y')
```

**With default values:**

```python
Account = namedtuple('Account', ['type', 'balance'], defaults=[0])
acc = Account('premium')
print(acc)            # Account(type='premium', balance=0)
```


## deque – Double-Ended Queue

`deque` (pronounced "deck") supports fast O(1) appends and pops from both ends, unlike lists where `pop(0)` is slow.

```python
from collections import deque

d = deque('ghi')               # deque(['g', 'h', 'i'])
d.append('j')                  # add to right
d.appendleft('f')              # add to left
print(d)                       # deque(['f', 'g', 'h', 'i', 'j'])

print(d.pop())                 # 'j' (remove from right)
print(d.popleft())             # 'f' (remove from left)
```

**Bounded length (useful for history/tail):**

```python
d = deque(maxlen=3)
d.extend([1, 2, 3, 4, 5])      # only keeps last 3 items
print(d)                       # deque([3, 4, 5])
```

**Rotation:**

```python
d = deque('abcde')
d.rotate(2)                    # rotate right by 2
print(d)                       # deque(['d', 'e', 'a', 'b', 'c'])
d.rotate(-1)                   # rotate left by 1
```


## ChainMap – Combine Multiple Dictionaries

`ChainMap` links several dictionaries so they act as one. Lookups search dictionaries in order; writes affect only the first dictionary.

```python
from collections import ChainMap

defaults = {'color': 'red', 'user': 'guest'}
cli_args = {'user': 'john'}
env_vars = {'color': 'blue'}

combined = ChainMap(cli_args, env_vars, defaults)
print(combined['user'])        # 'john' (from cli_args)
print(combined['color'])       # 'blue' (from env_vars)
```

**Creating child contexts (like nested scopes):**

```python
parent = ChainMap({'a': 1, 'b': 2})
child = parent.new_child()     # new empty dict at front
child['a'] = 99
print(child['a'])              # 99 (from child)
print(parent['a'])             # 1  (unchanged)

print(child.parents)           # ChainMap({'a': 1, 'b': 2})
```


## Counter – Count Hashable Objects

`Counter` is a dictionary subclass for counting. Missing keys return `0` instead of raising `KeyError`.

```python
from collections import Counter

# Create counters
c = Counter('abracadabra')
print(c)                       # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# Most common elements
print(c.most_common(2))        # [('a', 5), ('b', 2)]

# Access missing key
print(c['z'])                  # 0 (no error)

# Update counts
c.update('aaaa')
print(c['a'])                  # 9

# Subtract counts (can become negative)
c.subtract({'a': 10})
print(c['a'])                  # -1
```

**Mathematical operations (for positive counts):**

```python
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

print(c1 + c2)   # Counter({'a': 4, 'b': 3})   (add counts)
print(c1 - c2)   # Counter({'a': 2})           (subtract, drop non-positive)
print(c1 & c2)   # Counter({'a': 1, 'b': 1})   (minimum)
print(c1 | c2)   # Counter({'a': 3, 'b': 2})   (maximum)
```

**Useful methods:**

```python
c.total()                        # sum of all counts
list(c)                          # unique elements
c.clear()                        # reset
```


## defaultdict – Dictionary with Default Values

`defaultdict` returns a default value for missing keys instead of raising `KeyError`. You provide a factory function (like `list`, `int`, `set`).

```python
from collections import defaultdict

# Group items by key
s = [('yellow', 1), ('blue', 2), ('yellow', 3)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d)   # defaultdict(list, {'yellow': [1, 3], 'blue': [2]})

# Counting (like Counter)
s = 'mississippi'
d = defaultdict(int)
for ch in s:
    d[ch] += 1
print(d)   # defaultdict(int, {'m': 1, 'i': 4, 's': 4, 'p': 2})

# Custom default using lambda
d = defaultdict(lambda: '<missing>')
d['name'] = 'John'
print(d['name'])      # 'John'
print(d['age'])       # '<missing>'
```


## OrderedDict – Order-Sensitive Dictionary

Before Python 3.7, regular `dict` didn't guarantee insertion order. `OrderedDict` was created for that purpose. It still has extra methods for reordering.

```python
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(list(od))                # ['a', 'b', 'c']

# Move to end
od.move_to_end('b')
print(list(od))                # ['a', 'c', 'b']

# Move to beginning
od.move_to_end('b', last=False)
print(list(od))                # ['b', 'a', 'c']

# Pop from either end
od.popitem(last=True)          # pops ('c', 3)  (LIFO)
od.popitem(last=False)         # pops ('b', 1)  (FIFO)
```

**Equality:** `OrderedDict` considers order when comparing with another `OrderedDict`, but ignores order when comparing with regular `dict`.


## UserDict, UserList, UserString – Wrappers for Subclassing

These classes wrap the built-in types, making it easier to subclass and override behavior. The underlying data is accessible via the `.data` attribute.

```python
from collections import UserDict

class MyDict(UserDict):
    def __setitem__(self, key, value):
        print(f'Setting {key} = {value}')
        super().__setitem__(key, value)

d = MyDict()
d['a'] = 1   # prints "Setting a = 1"
```

Similarly, `UserList` wraps a list, and `UserString` wraps a string. They are useful when you want to customize built-in behavior without dealing with the complexities of subclassing `dict` or `list` directly.


## Summary Table

| Class | Best Used For |
|-------|---------------|
| `namedtuple` | Lightweight data records with named fields |
| `deque` | Fast queue/stack operations from both ends |
| `ChainMap` | Layered configuration (defaults, environment, CLI) |
| `Counter` | Counting occurrences and multiset operations |
| `OrderedDict` | Dictionaries where order matters for equality/reordering |
| `defaultdict` | Avoiding key errors and grouping data |
| `UserDict/List/String` | Customizing built-in containers |

All these types are imported from `collections`. They are part of Python's standard library and require no external installation.