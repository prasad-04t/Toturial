# More Control Flow Tools - Simplified Explanation

This section explains how to control the flow of your Python programs using conditions, loops, and functions.


## 4.1. `if` Statements

The `if` statement lets you execute code only when a condition is true. You can add `elif` (else if) for additional conditions and `else` for a fallback.

```python
x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
```

**Key points:**
- You can have zero or more `elif` blocks.
- The `else` block is optional.
- `elif` avoids deeply nested `if` statements.


## 4.2. `for` Statements

Python's `for` loop iterates over items of any sequence (like a list or string) in order. It does **not** require a counter variable like in C or Pascal.

```python
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
```

Output:
```
cat 3
window 6
defenestrate 12
```

**Warning:** Do not modify a collection while iterating over it directly. Instead, iterate over a copy or create a new collection.

```python
# Iterate over a copy
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
```

## 4.3. The `range()` Function

`range()` generates a sequence of numbers, useful when you need to loop a specific number of times.

```python
for i in range(5):
    print(i)
```
Output: `0 1 2 3 4`

**Customizing `range`:**

| Example | Result |
|---------|--------|
| `list(range(5, 10))` | `[5, 6, 7, 8, 9]` |
| `list(range(0, 10, 3))` | `[0, 3, 6, 9]` |
| `list(range(-10, -100, -30))` | `[-10, -40, -70]` |

**Looping with indices** (though `enumerate()` is often better):

```python
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
```

**Note:** `range()` returns an **iterable** object, not a list. It generates numbers on the fly, saving memory.

```python
sum(range(4))   # 0 + 1 + 2 + 3 = 6
```


## 4.4. `break` and `continue` Statements

- `break` exits the innermost loop immediately.
- `continue` skips the rest of the current iteration and moves to the next.

```python
# break example: find factors
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
```
Output:
```
4 equals 2 * 2
6 equals 2 * 3
8 equals 2 * 4
9 equals 3 * 3
```

```python
# continue example: separate even/odd
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")
```

## 4.5. `else` Clauses on Loops

A loop can have an `else` block that runs **only if the loop finishes without a `break`**. This is often used for searching.

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # No factor found
        print(n, 'is a prime number')
```

Output:
```
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
...
```

**Important:** The `else` belongs to the `for` loop, **not** the `if` statement.


## 4.6. `pass` Statements

`pass` does nothing. It acts as a placeholder where syntax requires a statement but you have nothing to do yet.

```python
while True:
    pass  # Wait for keyboard interrupt (Ctrl+C)
```

Common uses:
- Minimal class definition: `class MyEmptyClass: pass`
- Stub function: `def initlog(*args): pass`

Some programmers use `...` (ellipsis) as a placeholder instead of `pass`.

## 4.7. `match` Statements

`match` compares a value against patterns, similar to `switch` in other languages but much more powerful. It can also extract parts of the value into variables.

**Basic literal matching:**

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:          # wildcard (default)
            return "Something's wrong"
```

**Combining literals with `|`:**

```python
case 401 | 403 | 404:
    return "Not allowed"
```

**Unpacking tuples:**

```python
# point is (x, y)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
```

**Matching class instances:**

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

match point:
    case Point(x=0, y=0):
        print("Origin")
    case Point(x=0, y=y):
        print(f"Y={y}")
    case Point(x=x, y=0):
        print(f"X={x}")
    case Point():
        print("Somewhere else")
```

**Adding guards with `if`:**

```python
match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print("Not on the diagonal")
```

**Other features:**
- Sequence patterns support extended unpacking: `[x, y, *rest]`
- Mapping patterns extract dictionary values: `{"bandwidth": b, "latency": l}`
- Capture subpatterns with `as`: `case (Point(x1, y1), Point(x2, y2) as p2)`
- Named constants must be dotted (e.g., `Color.RED`) to avoid being treated as capture variables.

## 4.8. Defining Functions

Use `def` to create a reusable block of code.

```python
def fib(n):    # Print Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)   # Call the function
```

**Key concepts:**
- The first string in a function is a **docstring** (used for documentation).
- Variables inside a function are **local**; they don't affect global variables unless declared `global`.
- Functions without `return` return `None`.

**Returning a value:**

```python
def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```


## 4.9. More on Defining Functions

### 4.9.1. Default Argument Values

You can provide default values for parameters. If a value is omitted when calling, the default is used.

```python
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```

**Important warning:** Default values are evaluated **only once**. This can cause surprises with mutable defaults like lists:

```python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))   # [1]
print(f(2))   # [1, 2]   (same list reused!)
```

To avoid this, use `None` as default and create a new list inside the function:

```python
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```

### 4.9.2. Keyword Arguments

You can call functions by naming the parameters. This improves readability and allows you to skip optional arguments.

```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# Valid calls
parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000000, action='VOOOOOM')
parrot('a million', 'bereft of life', 'jump')
```

**Invalid calls:**
- Missing required argument.
- Positional argument after a keyword argument.
- Duplicate value for the same argument.
- Unknown keyword argument.

**Arbitrary keyword arguments with `**kwargs`:**

```python
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    for arg in arguments:
        print(arg)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
```

- `*arguments` collects extra positional arguments into a tuple.
- `**keywords` collects extra keyword arguments into a dictionary.

### 4.9.3. Special Parameters: `/` and `*`

You can restrict how arguments are passed.

- **Positional-only** (before `/`): cannot be passed by keyword.
- **Keyword-only** (after `*`): must be passed by keyword.

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    pass
```

**Examples:**

```python
def standard_arg(arg): pass          # either position or keyword
def pos_only_arg(arg, /): pass       # only position
def kwd_only_arg(*, arg): pass       # only keyword
def combined(pos_only, /, standard, *, kwd_only): pass
```

**Why use this?**
- Positional-only: parameter names don't matter to the caller; prevents breaking changes if names change.
- Keyword-only: forces clarity when calling.

### 4.9.4. Arbitrary Argument Lists (`*args`)

A function can accept any number of positional arguments using `*args`.

```python
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
```

Any parameters after `*args` become **keyword-only**.

```python
def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")          # 'earth/mars/venus'
concat("earth", "mars", "venus", sep=".") # 'earth.mars.venus'
```

### 4.9.5. Unpacking Argument Lists

Use `*` to unpack a list/tuple into positional arguments, and `**` to unpack a dictionary into keyword arguments.

```python
args = [3, 6]
list(range(*args))   # equivalent to range(3, 6)

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
```

### 4.9.6. Lambda Expressions

Lambdas are small anonymous functions defined with `lambda`. They are limited to a single expression.

```python
# Return a function that adds n
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)   # 42
f(1)   # 43
```

Common use: sorting with a custom key.

```python
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])   # sort by second item
```

### 4.9.7. Documentation Strings (Docstrings)

Write a triple‑quoted string right after the `def` line. First line: short summary. Blank line, then details.

```python
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)
```

### 4.9.8. Function Annotations

You can optionally add type hints using `:` and `->`. They are stored in `__annotations__` but don't enforce anything.

```python
def f(ham: str, eggs: str = 'eggs') -> str:
    return ham + ' and ' + eggs

print(f.__annotations__)
# {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
```


## 4.10. Intermezzo: Coding Style (PEP 8)

Follow these conventions to make your code readable:

- Use **4 spaces** per indentation level (no tabs).
- Limit lines to **79 characters**.
- Separate functions and classes with **blank lines**.
- Put comments on their own line when possible.
- Use **docstrings** for functions, classes, and modules.
- Use spaces around operators and after commas: `a = f(1, 2) + g(3, 4)`
- Naming: `UpperCamelCase` for classes, `lowercase_with_underscores` for functions and variables.
- Use `self` as the first method parameter name.
- Stick to **UTF-8** or ASCII encoding; avoid non‑ASCII characters in identifiers.

## Confirmation of Coverage

All topics from the original Chapter 4 are included:

| Section | Covered |
|---------|---------|
| 4.1 `if` statements | Yes |
| 4.2 `for` statements | Yes |
| 4.3 `range()` function | Yes |
| 4.4 `break` and `continue` | Yes |
| 4.5 `else` on loops | Yes |
| 4.6 `pass` statement | Yes |
| 4.7 `match` statement | Yes |
| 4.8 Defining functions | Yes |
| 4.9.1 Default argument values | Yes |
| 4.9.2 Keyword arguments | Yes |
| 4.9.3 Special parameters (`/`, `*`) | Yes |
| 4.9.4 Arbitrary argument lists (`*args`) | Yes |
| 4.9.5 Unpacking argument lists | Yes |
| 4.9.6 Lambda expressions | Yes |
| 4.9.7 Documentation strings | Yes |
| 4.9.8 Function annotations | Yes |
| 4.10 Coding style (PEP 8) | Yes |

The explanation is complete, simplified, and presented in clean Markdown without emojis.