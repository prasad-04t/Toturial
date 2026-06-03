# An Informal Introduction to Python - Simplified Explanation

This document explains the basics of Python in simple words. You will learn how to use Python for calculations, work with text, store multiple items in lists, and write a small program.



## Understanding the Examples in This Document

- When you see lines starting with `>>>` or `...`, those are commands you type into Python.
- Lines without those prompts are what Python prints back as a result.
- The `#` symbol starts a comment. Comments are notes for humans; Python ignores them.

```python
# This is a comment
spam = 1  # This is also a comment
text = "# This is not a comment because it's inside quotes."
```


## 3.1. Using Python as a Calculator

You can use Python just like a calculator. Type a math expression, press Enter, and Python shows the answer.

### 3.1.1. Numbers

Python understands addition, subtraction, multiplication, and division.

| Operator | Meaning       | Example       | Result |
|----------|---------------|---------------|--------|
| `+`      | Addition      | `2 + 2`       | `4`    |
| `-`      | Subtraction   | `50 - 5*6`    | `20`   |
| `*`      | Multiplication| `5 * 3`       | `15`   |
| `/`      | Division (always gives decimal) | `8 / 5` | `1.6` |
| `//`     | Floor division (drops decimal) | `17 // 3` | `5` |
| `%`      | Remainder (modulo) | `17 % 3` | `2` |
| `**`     | Power         | `5 ** 2`      | `25`   |
| `()`     | Grouping      | `(50 - 5*6) / 4` | `5.0` |

**Important Notes:**

- Division with `/` always returns a number with a decimal point (a `float`).
- Use `//` to get an integer result without the decimal part.
- Use `%` to find the remainder after division.

**Variables**

You can store values in variables using the `=` sign.

```python
width = 20
height = 5 * 9
width * height   # Result: 900
```

If you try to use a variable that hasn't been given a value yet, Python shows an error.

**The Special `_` Variable**

In interactive mode, `_` holds the result of the last calculation.

```python
tax = 12.5 / 100
price = 100.50
price * tax        # Result: 12.5625
price + _          # Result: 113.0625 (adds last result)
round(_, 2)        # Result: 113.06
```

**Other Number Types**

Python also supports fractions, precise decimal numbers, and complex numbers (e.g., `3+5j`).


### 3.1.2. Text (Strings)

Text in Python is called a **string**. You can write strings inside single quotes `'...'` or double quotes `"..."`.

```python
'spam eggs'          # Using single quotes
"Paris rabbit"       # Using double quotes
'1975'               # Numbers inside quotes become text, not numbers
```

**Escaping Quotes**

If your text contains a quote, you have two options:

1. Put a backslash `\` before the quote inside the string.
2. Use the other type of quote around the whole string.

```python
'doesn\'t'           # Escaped single quote
"doesn't"            # Using double quotes around it
'"Yes," they said.'  # Single quotes around double quotes
```

**Special Characters**

The backslash `\` is also used for special characters like `\n` (new line) or `\t` (tab).

```python
s = 'First line.\nSecond line.'
print(s)
```

Output:
```
First line.
Second line.
```

**Raw Strings**

If you don't want `\` to be treated as special, put an `r` before the opening quote.

```python
print(r'C:\this\name')   # Prints exactly: C:\this\name
```

**Multi-line Strings**

Use three quotes `"""..."""` or `'''...'''` to write text that spans several lines.

```python
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```

**Joining and Repeating Strings**

- `+` joins strings together.
- `*` repeats a string.

```python
3 * 'un' + 'ium'      # Result: 'unununium'
```

If you write two string literals next to each other, Python automatically joins them (only works with literals, not variables).

```python
'Py' 'thon'           # Result: 'Python'
```

**Accessing Characters in a String**

Each character has a position number, starting from `0`.

```python
word = 'Python'
word[0]               # 'P' (first character)
word[5]               # 'n' (sixth character)
word[-1]              # 'n' (last character)
word[-2]              # 'o' (second last)
```

**Slicing (Getting Parts of a String)**

Use `word[start:end]` to get a substring. The start position is included, the end position is **not** included.

```python
word[0:2]             # 'Py'  (positions 0 and 1)
word[2:5]             # 'tho' (positions 2,3,4)
word[:2]              # 'Py'  (from start to position 2 excluded)
word[4:]              # 'on'  (from position 4 to end)
word[-2:]             # 'on'  (last two characters)
```

Think of the slice positions as the spaces *between* characters:

```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

**Strings Cannot Be Changed**

You cannot alter a string once created. To "change" it, you must make a new string.

```python
word[0] = 'J'         # ERROR! Strings are immutable.
'J' + word[1:]        # 'Jython' (creates a new string)
```

**Finding Length**

Use `len()` to find how many characters are in a string.

```python
len('supercalifragilisticexpialidocious')   # Result: 34
```


### 3.1.3. Lists

A **list** is a container that holds multiple items in order. You write a list using square brackets `[]` with commas between items.

```python
squares = [1, 4, 9, 16, 25]
```

**Indexing and Slicing Lists**

Works exactly like strings.

```python
squares[0]            # 1 (first item)
squares[-1]           # 25 (last item)
squares[-3:]          # [9, 16, 25] (last three items)
```

**Concatenation**

```python
squares + [36, 49, 64, 81, 100]   # Combines two lists
```

**Lists Are Mutable (Can Be Changed)**

Unlike strings, you can modify a list after creation.

```python
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64         # Fix the wrong value
cubes                 # [1, 8, 27, 64, 125]
```

**Adding Items**

Use `.append()` to add an item to the end.

```python
cubes.append(216)     # Adds 216 at the end
cubes.append(7 ** 3)  # Adds 343
cubes                 # [1, 8, 27, 64, 125, 216, 343]
```

**Important: Assignment Does Not Copy**

When you assign a list to a new variable, both variables point to the **same** list. Changing one changes the other.

```python
rgb = ["Red", "Green", "Blue"]
rgba = rgb
rgba.append("Alph")
print(rgb)            # ["Red", "Green", "Blue", "Alph"] (both changed)
```

To make a real copy, use slicing `[:]`.

```python
correct_rgba = rgba[:]   # Creates a new copy
correct_rgba[-1] = "Alpha"
print(rgba)           # Original remains unchanged
```

**Assigning to Slices**

You can replace parts of a list or even clear it entirely.

```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']   # Replace items at positions 2,3,4
letters[2:5] = []                # Remove those items
letters[:] = []                  # Clear the whole list
```

**Nested Lists**

A list can contain other lists.

```python
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]            # x is a list of two lists
x[0]                  # ['a', 'b', 'c']
x[0][1]               # 'b'
```

**Length of a List**

Use `len()` to find the number of items.

```python
len(['a', 'b', 'c', 'd'])   # Result: 4
```


## 3.2. First Steps Towards Programming

Now let's write a small program. This example prints the Fibonacci sequence (each number is the sum of the two before it) until the numbers exceed 10.

```python
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
```

Output:
```
0
1
1
2
3
5
8
```

**What This Program Teaches:**

**Multiple Assignment**

`a, b = 0, 1` sets `a` to `0` and `b` to `1` at the same time. Later, `a, b = b, a+b` calculates both new values before assigning them.

**The `while` Loop**

The loop runs as long as the condition `a < 10` is `True`. Python treats non‑zero numbers and non‑empty sequences as `True`; zero and empty sequences are `False`.

**Comparison Operators**

- `<`   less than
- `>`   greater than
- `==`  equal to
- `<=`  less than or equal
- `>=`  greater than or equal
- `!=`  not equal

**Indentation Matters**

The lines inside the `while` loop are indented (usually 4 spaces). This tells Python which statements belong to the loop. In interactive mode, press Enter twice on a blank line to end the loop.

**The `print()` Function**

`print()` shows values on the screen. You can print multiple things separated by commas, and Python adds a space between them.

```python
i = 256 * 256
print('The value of i is', i)   # Output: The value of i is 65536
```

**Changing the Line Ending**

By default, `print()` ends with a new line. You can change that with `end=`.

```python
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b
# Output: 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
```

This prints all numbers on one line separated by commas.
This concludes the informal introduction. You now know how to use Python for basic calculations, work with text and lists, and write a simple loop.