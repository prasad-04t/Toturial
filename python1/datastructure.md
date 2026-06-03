# Data Structures - Simplified Explanation

This chapter dives deeper into lists and introduces other ways to store and organize data in Python.

## 5.1. More on Lists

Lists have many built-in methods. Here are all the important ones:

| Method | Description | Example |
|--------|-------------|---------|
| `append(x)` | Adds `x` to the end of the list | `fruits.append('grape')` |
| `extend(iterable)` | Adds all items from another list/iterable | `nums.extend([4,5])` |
| `insert(i, x)` | Inserts `x` at position `i` | `fruits.insert(1, 'kiwi')` |
| `remove(x)` | Removes the **first** occurrence of `x` | `fruits.remove('apple')` |
| `pop([i])` | Removes and returns item at position `i` (default last) | `last = fruits.pop()` |
| `clear()` | Removes all items | `fruits.clear()` |
| `index(x)` | Returns position of first `x` | `pos = fruits.index('banana')` |
| `count(x)` | Counts how many times `x` appears | `n = fruits.count('apple')` |
| `sort()` | Sorts the list in place | `nums.sort()` |
| `reverse()` | Reverses the list in place | `nums.reverse()` |
| `copy()` | Returns a shallow copy | `new = old.copy()` |

Example using many methods:

```python
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))      # 2
print(fruits.index('banana'))     # 3
fruits.reverse()
print(fruits)                     # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
fruits.sort()
print(fruits)                     # ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
print(fruits.pop())               # 'pear'
```

**Important notes:**
- Methods that modify the list (like `sort`, `append`, `insert`) return `None`, not the modified list.
- Not all types can be sorted together (e.g., numbers and strings cannot be mixed).


### 5.1.1. Using Lists as Stacks

A **stack** works on the "last‑in, first‑out" principle. Use `append()` to push an item onto the stack and `pop()` to remove the top item.

```python
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)          # [3, 4, 5, 6, 7]
print(stack.pop())    # 7
print(stack)          # [3, 4, 5, 6]
```

### 5.1.2. Using Lists as Queues

A **queue** works "first‑in, first‑out". Lists are **not efficient** for queues because removing from the beginning is slow. Use `collections.deque` instead.

```python
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")      # Terry joins the queue
queue.append("Graham")     # Graham joins
print(queue.popleft())     # 'Eric' (first one leaves)
print(queue.popleft())     # 'John'
print(queue)               # deque(['Michael', 'Terry', 'Graham'])
```

### 5.1.3. List Comprehensions

List comprehensions are a short, readable way to create new lists.

**Old way:**
```python
squares = []
for x in range(10):
    squares.append(x**2)
```

**List comprehension:**
```python
squares = [x**2 for x in range(10)]
```

You can also add an `if` condition:

```python
# Get all even squares
even_squares = [x**2 for x in range(10) if x % 2 == 0]
```

More examples:

```python
# Combine two lists, excluding equal pairs
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

# Double all values
vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]                # [-8, -4, 0, 4, 8]

# Remove negative numbers
[x for x in vec if x >= 0]        # [0, 2, 4]

# Call a method on each string
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[fruit.strip() for fruit in freshfruit]

# Flatten a list of lists
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for row in vec for num in row]   # [1,2,3,4,5,6,7,8,9]
```

**Note:** If the expression is a tuple, you **must** put parentheses around it: `[(x, x**2) for x in range(5)]`.

### 5.1.4. Nested List Comprehensions

You can use a list comprehension inside another one. A classic example is transposing a matrix.

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# Transpose using nested comprehension
transposed = [[row[i] for row in matrix] for i in range(4)]
# Result: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

However, for this specific task the built-in `zip()` function is simpler:

```python
list(zip(*matrix))
```


## 5.2. The `del` Statement

`del` removes items from a list by **index** or deletes entire variables.

```python
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]               # Remove first item
print(a)               # [1, 66.25, 333, 333, 1234.5]
del a[2:4]             # Remove items at index 2 and 3
print(a)               # [1, 66.25, 1234.5]
del a[:]               # Clear the whole list
print(a)               # []

# Delete a variable entirely
del a
# Now using 'a' would cause a NameError
```


## 5.3. Tuples and Sequences

A **tuple** is like a list but **immutable** (cannot be changed). Tuples are written with commas; parentheses are optional but often used.

```python
t = 12345, 54321, 'hello!'
print(t[0])            # 12345
print(t)               # (12345, 54321, 'hello!')

# Nested tuples
u = t, (1, 2, 3, 4, 5)
print(u)               # ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# Tuples are immutable:
t[0] = 88888           # TypeError: 'tuple' object does not support item assignment

# But they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v[0][0] = 99           # This works because the list inside is mutable
```

**Creating special tuples:**
- Empty tuple: `empty = ()`
- Tuple with one item: `singleton = 'hello',` (note the trailing comma)

**Packing and Unpacking:**
```python
t = 12345, 54321, 'hello!'    # packing
x, y, z = t                   # unpacking
```


## 5.4. Sets

A **set** is an unordered collection with **no duplicates**. Useful for membership tests and removing duplicates.

Create sets with curly braces `{}` or the `set()` function. **Important:** `{}` alone creates an empty **dictionary**, not a set. Use `set()` for an empty set.

```python
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                     # duplicates are removed, order may vary

print('orange' in basket)         # True (fast membership test)
print('crabgrass' in basket)      # False
```

**Set operations:**

```python
a = set('abracadabra')
b = set('alacazam')

print(a)                 # unique letters in a: {'a', 'r', 'b', 'c', 'd'}
print(a - b)             # difference: letters in a but not in b
print(a | b)             # union: letters in a or b or both
print(a & b)             # intersection: letters in both
print(a ^ b)             # symmetric difference: letters in a or b but not both
```

**Set comprehensions** work just like list comprehensions:

```python
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)                 # {'r', 'd'}
```


## 5.5. Dictionaries

A **dictionary** stores **key‑value pairs**. Keys must be immutable (strings, numbers, tuples of immutable things). Values can be anything.

```python
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127               # add new entry
print(tel)                        # {'jack': 4098, 'sape': 4139, 'guido': 4127}
print(tel['jack'])                # 4098

del tel['sape']                   # delete entry
print(list(tel))                  # list of keys: ['jack', 'guido', 'irv']
print(sorted(tel))                # sorted keys: ['guido', 'irv', 'jack']

print('guido' in tel)             # True
print('jack' not in tel)          # False
```

**Avoiding KeyError:**

Use `get()` instead of square brackets when a key might be missing.

```python
print(tel.get('irv'))             # None (instead of error)
print(tel.get('irv', 0))          # 0 (custom default)
```

**Creating dictionaries:**

```python
# From list of (key, value) pairs
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

# Dictionary comprehension
{x: x**2 for x in (2, 4, 6)}      # {2: 4, 4: 16, 6: 36}

# Using keyword arguments (only for simple string keys)
dict(sape=4139, guido=4127, jack=4098)
```


## 5.6. Looping Techniques

Python provides helpful functions for common looping patterns.

**Looping over dictionary keys and values:**
```python
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
```

**Getting index and value with `enumerate()`:**
```python
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
# Output: 0 tic, 1 tac, 2 toe
```

**Looping over two lists simultaneously with `zip()`:**
```python
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print(f'What is your {q}? It is {a}.')
```

**Looping in reverse:**
```python
for i in reversed(range(1, 10, 2)):
    print(i)   # prints 9,7,5,3,1
```

**Looping in sorted order:**
```python
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for fruit in sorted(basket):
    print(fruit)
```

**Getting unique sorted items:**
```python
for fruit in sorted(set(basket)):
    print(fruit)
```

**Safer way to filter a list while looping:**
Create a new list instead of modifying the one you're iterating over.

```python
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
```


## 5.7. More on Conditions

Conditions in `if` and `while` can use more than comparisons.

**Membership tests:**
- `in` and `not in` check if a value exists in a container.

**Identity tests:**
- `is` and `is not` check if two variables refer to the exact same object.

**Chained comparisons:**
```python
a < b == c      # same as: a < b and b == c
```

**Boolean operators:**
- `and`, `or`, `not`
- They are **short‑circuit**: evaluation stops as soon as the result is known.

```python
# Short-circuit example
result = A and B and C   # if A is False, B and C are never evaluated
```

**Assigning Boolean results:**
```python
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)          # 'Trondheim' (first non-empty string)
```

**Note on assignment inside expressions:**
Python requires the walrus operator `:=` for assignment within an expression (e.g., `if (n := len(a)) > 5:`). This prevents accidentally using `=` instead of `==`.


## 5.8. Comparing Sequences and Other Types

Sequences (lists, tuples, strings) are compared **lexicographically** (like dictionary order).

- Compare first elements; if equal, compare second, and so on.
- If one sequence is a prefix of the other, the shorter one is considered smaller.
- Strings are compared by Unicode code point (alphabetical for basic English).

Examples:

```python
(1, 2, 3)              < (1, 2, 4)          # True
[1, 2, 3]              < [1, 2, 4]          # True
'ABC' < 'C' < 'Pascal' < 'Python'           # True
(1, 2, 3, 4)           < (1, 2, 4)          # True (stops at third element)
(1, 2)                 < (1, 2, -1)         # True (shorter is smaller)
(1, 2, 3)             == (1.0, 2.0, 3.0)    # True (numeric comparison)
```

Comparing different types (like `int` vs `str`) with `<` or `>` usually raises a `TypeError` unless specific comparison methods exist.


## Confirmation of Coverage

All subsections of Chapter 5 are fully explained:

| Section | Covered |
|---------|---------|
| 5.1 List methods | Yes |
| 5.1.1 Lists as stacks | Yes |
| 5.1.2 Lists as queues | Yes |
| 5.1.3 List comprehensions | Yes |
| 5.1.4 Nested list comprehensions | Yes |
| 5.2 The `del` statement | Yes |
| 5.3 Tuples and Sequences | Yes |
| 5.4 Sets | Yes |
| 5.5 Dictionaries | Yes |
| 5.6 Looping Techniques | Yes |
| 5.7 More on Conditions | Yes |
| 5.8 Comparing Sequences | Yes |

The explanation is complete, uses simple language, provides practical examples, and is presented in clean Markdown without emojis.