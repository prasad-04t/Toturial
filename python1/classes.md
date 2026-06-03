# Classes - Simplified Explanation

This chapter explains how to create your own data types in Python using **classes**. Classes bundle together data (attributes) and functions (methods) that operate on that data. They support object-oriented programming features like inheritance and encapsulation.


## 9.1. A Word About Names and Objects

In Python, multiple names can refer to the same object. This is called **aliasing**. For immutable types (numbers, strings, tuples), it’s harmless. But for mutable objects like lists and dictionaries, changes through one name affect all other names.

```python
a = [1, 2, 3]
b = a          # b is an alias for the same list
b.append(4)
print(a)       # [1, 2, 3, 4]   Both see the change
```

This is efficient: passing an object to a function only passes a reference, not a full copy. Functions can modify the original object.


## 9.2. Python Scopes and Namespaces

Before diving into classes, you need to understand where Python looks for names.

### Namespaces

A **namespace** is a mapping from names to objects. Examples:
- Built-in names (e.g., `print`, `len`)
- Global names in a module
- Local names inside a function
- Attributes of an object

Names in different namespaces don't conflict. You can have a function `max` in two different modules, and you distinguish them by the module name: `mymodule.max` vs `yourmodule.max`.

### Scopes

A **scope** defines where a namespace is directly accessible. Python searches for a name in this order:

1. **Local scope** – inside the current function.
2. **Enclosing functions** – from inner to outer (nonlocal).
3. **Global scope** – module level.
4. **Built-in scope** – Python's predefined names.

By default, assigning to a name creates a local variable. To modify a variable from an outer scope, use `global` (for module-level) or `nonlocal` (for enclosing function scope).

### Example: `global` and `nonlocal`

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)      # test spam
    do_nonlocal()
    print("After nonlocal assignment:", spam)   # nonlocal spam
    do_global()
    print("After global assignment:", spam)     # nonlocal spam

scope_test()
print("In global scope:", spam)                 # global spam
```

Output:
```
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```

Notice:
- `do_local()` didn't change `scope_test`'s `spam` because it created a new local variable.
- `do_nonlocal()` changed the `spam` in `scope_test`.
- `do_global()` changed the module-level `spam`.

---

## 9.3. A First Look at Classes

### 9.3.1. Class Definition Syntax

```python
class ClassName:
    """Optional docstring."""
    # Statements (usually method definitions)
    pass
```

The class definition must be executed before it has any effect (just like `def`). Inside the class body, a new namespace is created and used as the local scope.

### 9.3.2. Class Objects

After the class definition finishes, a **class object** is created. You can do two things with it:

- **Attribute references**: `ClassName.attribute`
- **Instantiation**: `ClassName()` creates a new instance.

```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

print(MyClass.i)        # 12345
print(MyClass.f)        # <function MyClass.f at ...>
print(MyClass.__doc__)  # 'A simple example class'
```

#### Instantiation and `__init__()`

Calling a class creates an empty instance. To initialize it with data, define the special method `__init__()`.

```python
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)   # 3.0 -4.5
```

### 9.3.3. Instance Objects

Instance objects only understand **attribute references**. Two kinds exist:

- **Data attributes** (instance variables) – created when first assigned.
- **Methods** – functions that belong to the instance.

```python
x = MyClass()
x.counter = 1           # create a data attribute
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)        # 16
del x.counter           # delete it
```

### 9.3.4. Method Objects

When you call a method like `x.f()`, Python automatically passes the instance as the first argument. By convention, this parameter is named `self`.

```python
x = MyClass()
x.f()            # equivalent to MyClass.f(x)
```

You can store a method for later use:

```python
xf = x.f
print(xf())      # 'hello world'
```

**How it works:** When you access `x.f`, Python creates a **method object** that packages the instance `x` and the function `MyClass.f`. When you call that method object, it prepends the instance to the argument list and calls the function.

### 9.3.5. Class and Instance Variables

- **Class variables** are shared by all instances.
- **Instance variables** are unique to each instance.

```python
class Dog:
    kind = 'canine'          # class variable

    def __init__(self, name):
        self.name = name     # instance variable

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)   # 'canine'  (shared)
print(e.kind)   # 'canine'  (shared)
print(d.name)   # 'Fido'    (unique)
print(e.name)   # 'Buddy'   (unique)
```

**Pitfall with mutable class variables:**

```python
class Dog:
    tricks = []              # WRONG: one list shared by all dogs

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)   # ['roll over', 'play dead'] (shared accidentally)
```

Correct design: initialize mutable attributes in `__init__`.

```python
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []     # each dog gets its own list

    def add_trick(self, trick):
        self.tricks.append(trick)
```

---

## 9.4. Random Remarks

- If an attribute exists in both instance and class, the **instance attribute takes precedence**.
- No true private variables; use a single leading underscore `_internal` to signal "internal use, don't touch."
- `self` is just a convention; you could name it anything, but stick to `self` for readability.
- Any function object assigned to a class attribute becomes a method.

```python
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1
    def g(self):
        return 'hello world'
    h = g
```

Now `C.f`, `C.g`, and `C.h` are all methods.

- Methods can call other methods via `self.methodname()`.

---

## 9.5. Inheritance

A class can inherit attributes and methods from a base class.

```python
class DerivedClassName(BaseClassName):
    # new or overridden methods
```

If an attribute isn't found in the derived class, Python searches the base class (and further up the chain).

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

d = Dog()
print(d.speak())   # Woof! (overridden)
```

### Calling Base Class Methods

You can explicitly call a base class method:

```python
class Dog(Animal):
    def speak(self):
        base_sound = Animal.speak(self)
        return f"{base_sound} and Woof!"
```

Python provides two built-in functions for inheritance checks:

- `isinstance(obj, class)` – returns `True` if `obj` is an instance of `class` or a subclass.
- `issubclass(cls1, cls2)` – returns `True` if `cls1` is a subclass of `cls2`.

### 9.5.1. Multiple Inheritance

A class can inherit from multiple base classes:

```python
class Derived(Base1, Base2, Base3):
    pass
```

Python uses a **method resolution order (MRO)** that ensures each base class is visited only once, in a consistent order. For simple cases, think of it as depth-first, left-to-right search.

---

## 9.6. Private Variables

Python doesn't enforce private variables. The convention is to prefix with `_` for "protected" (internal use).

**Name mangling:** Any identifier with at least two leading underscores and at most one trailing underscore (e.g., `__spam`) is textually replaced with `_classname__spam`. This helps avoid accidental name clashes in subclasses.

```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)     # becomes _Mapping__update

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update               # private copy

class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)
```

Even with mangling, you can still access `_Mapping__update` if you really need to (e.g., for debugging).

---

## 9.7. Odds and Ends

### Dataclasses (Simpler Classes)

For simple data containers, use the `@dataclass` decorator (Python 3.7+). It automatically generates `__init__`, `__repr__`, and other methods.

```python
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

john = Employee('john', 'computer lab', 1000)
print(john.dept)   # 'computer lab'
```

### Duck Typing

Python doesn't require formal inheritance. If an object has the required methods (e.g., `read` and `readline`), it can be used where a file is expected.

### Method Object Attributes

A method object stores:
- `method.__self__` – the instance.
- `method.__func__` – the original function.

---

## 9.8. Iterators

Many Python objects are **iterable**: you can loop over them with `for`. Behind the scenes, `for` calls `iter()` to get an **iterator**, then repeatedly calls `next()` on that iterator until `StopIteration` is raised.

```python
s = 'abc'
it = iter(s)
print(next(it))   # 'a'
print(next(it))   # 'b'
print(next(it))   # 'c'
# next(it) would raise StopIteration
```

### Creating Your Own Iterator

Define `__iter__()` (returns self) and `__next__()` (returns next item or raises `StopIteration`).

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

for char in Reverse('spam'):
    print(char)
# Output: m a p s (each on a new line)
```

---

## 9.9. Generators

Generators are a simpler way to create iterators. Write a function with `yield` instead of `return`. The function's state is automatically saved between calls.

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)
# Output: f l o g
```

Generators automatically implement `__iter__()` and `__next__()`, and raise `StopIteration` when done.

---

## 9.10. Generator Expressions

For simple generators used immediately, use parentheses instead of brackets (like list comprehensions but with `()`).

```python
sum(i*i for i in range(10))                 # 285

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))         # 260

unique_words = set(word for line in page for word in line.split())

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))   # ['f', 'l', 'o', 'g']
```

Generator expressions are memory-efficient because they yield items one at a time instead of building a full list.

---

## Confirmation of Coverage

| Section | Covered |
|---------|---------|
| 9.1 Names and Objects (aliasing) | Yes |
| 9.2 Scopes and Namespaces | Yes |
| 9.2.1 Example | Yes |
| 9.3.1 Class Definition Syntax | Yes |
| 9.3.2 Class Objects | Yes |
| 9.3.3 Instance Objects | Yes |
| 9.3.4 Method Objects | Yes |
| 9.3.5 Class and Instance Variables | Yes |
| 9.4 Random Remarks | Yes |
| 9.5 Inheritance | Yes |
| 9.5.1 Multiple Inheritance | Yes |
| 9.6 Private Variables | Yes |
| 9.7 Odds and Ends (dataclasses) | Yes |
| 9.8 Iterators | Yes |
| 9.9 Generators | Yes |
| 9.10 Generator Expressions | Yes |

The explanation is complete, uses simple language with practical examples, and is formatted in clean Markdown without emojis.