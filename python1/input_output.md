# Input and Output - Simplified Explanation

This chapter covers how to display nicely formatted output and how to read from and write to files.

## 7.1. Fancier Output Formatting

You already know how to print values with `print()`. But often you need more control over how the output looks. Python offers several ways to format output.

### Three Main Formatting Approaches

1. **Formatted string literals (f-strings)** – modern and recommended.
2. **`str.format()` method** – flexible and widely used.
3. **Manual string operations** – for complete control.

Additionally, two useful functions for converting values to strings:
- `str()` – returns a human-readable version.
- `repr()` – returns a version meant for the interpreter (includes quotes, escapes).

```python
s = 'Hello, world.'
print(str(s))    # Hello, world.
print(repr(s))   # 'Hello, world.'

x = 10 * 3.25
y = 200 * 200
print('The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...')
# The value of x is 32.5, and y is 40000...
```

### 7.1.1. Formatted String Literals (f-strings)

Prefix a string with `f` or `F` and embed expressions inside `{ }`.

```python
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')   # Results of the 2016 Referendum
```

**Format specifiers** can be added after a colon `:` inside the braces.

```python
import math
print(f'The value of pi is approximately {math.pi:.3f}.')
# The value of pi is approximately 3.142.
```

**Minimum width** for aligning columns:

```python
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

# Sjoerd     ==>       4127
# Jack       ==>       4098
# Dcab       ==>       7678
```

**Conversion flags** `!a`, `!s`, `!r` apply `ascii()`, `str()`, or `repr()`:

```python
animals = 'eels'
print(f'My hovercraft is full of {animals!r}.')
# My hovercraft is full of 'eels'.
```

**Self-documenting expressions** using `=`:

```python
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')
# Debugging bugs='roaches' count=13 area='living room'
```


### 7.1.2. The String `format()` Method

Placeholders `{}` are replaced by arguments passed to `format()`.

```python
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# We are the knights who say "Ni!"
```

**Positional references** (0-based):

```python
print('{0} and {1}'.format('spam', 'eggs'))   # spam and eggs
print('{1} and {0}'.format('spam', 'eggs'))   # eggs and spam
```

**Keyword references**:

```python
print('This {food} is {adjective}.'.format(food='spam', adjective='horrible'))
# This spam is horrible.
```

**Combining positional and keyword**:

```python
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
# The story of Bill, Manfred, and Georg.
```

**Accessing dictionary values**:

```python
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

Or unpack the dictionary with `**`:

```python
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
```

**Aligning columns** with format specifiers:

```python
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# Output neatly aligned columns for numbers, squares, and cubes.
```


### 7.1.3. Manual String Formatting

String methods like `str.rjust()`, `str.ljust()`, and `str.center()` pad strings with spaces to a given width.

```python
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))

# Produces same aligned table as above.
```

**`str.zfill()`** pads a numeric string with leading zeros, respecting signs:

```python
'12'.zfill(5)      # '00012'
'-3.14'.zfill(7)   # '-003.14'
```


### 7.1.4. Old String Formatting (`%` operator)

An older style similar to C's `printf`. Use `%` with a format string and a tuple of values.

```python
import math
print('The value of pi is approximately %5.3f.' % math.pi)
# The value of pi is approximately 3.142.
```

This method is still supported but f-strings or `str.format()` are preferred for new code.


## 7.2. Reading and Writing Files

Use the `open()` function to work with files.

```python
f = open('workfile', 'w', encoding='utf-8')
```

**Arguments:**
- **filename** – string with the file name.
- **mode** – `'r'` (read, default), `'w'` (write, overwrites existing), `'a'` (append), `'r+'` (read/write).
- **encoding** – recommended to always specify `encoding='utf-8'` for text files.

**Binary mode:** Add `'b'` to mode (e.g., `'rb'`, `'wb'`) for non-text files like images or executables. Do not specify encoding in binary mode.

**Line endings:** In text mode, Python automatically converts platform-specific line endings (`\r\n` on Windows) to `\n` when reading, and back when writing.

### The `with` Statement (Best Practice)

Using `with` ensures the file is automatically closed, even if an error occurs.

```python
with open('workfile', encoding='utf-8') as f:
    read_data = f.read()

# File is closed automatically after the block
print(f.closed)   # True
```

Without `with`, you must manually call `f.close()`.


### 7.2.1. Methods of File Objects

Assume `f` is an open file object.

| Method | Description |
|--------|-------------|
| `f.read(size)` | Reads up to `size` characters/bytes. Without `size`, reads the whole file. Returns `''` at EOF. |
| `f.readline()` | Reads one line (including the newline `\n`). Returns `''` at EOF. |
| Looping over `f` | `for line in f:` iterates over lines efficiently. |
| `f.write(string)` | Writes the string to the file. Returns number of characters written. |
| `f.tell()` | Returns current position in file (bytes from start in binary mode). |
| `f.seek(offset, whence)` | Moves to new position. `whence`: `0` = start, `1` = current, `2` = end. |

**Examples:**

```python
# Read entire file
with open('workfile', encoding='utf-8') as f:
    print(f.read())

# Read line by line
with open('workfile', encoding='utf-8') as f:
    for line in f:
        print(line, end='')

# Write to file
with open('workfile', 'w', encoding='utf-8') as f:
    f.write('This is a test\n')

# Seeking in binary mode
f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5)          # Move to 6th byte
print(f.read(1))   # b'5'
f.seek(-3, 2)      # 3rd byte from end
print(f.read(1))   # b'd'
f.close()
```

**Important:** In text mode, `seek()` only works reliably with offsets returned by `tell()` or zero (beginning).

### 7.2.2. Saving Structured Data with `json`

Saving complex data like lists and dictionaries to a file manually is tedious. Python's `json` module handles this easily.

**Serializing (Python object → JSON string)**

```python
import json
x = [1, 'simple', 'list']
json_string = json.dumps(x)
print(json_string)   # '[1, "simple", "list"]'
```

**Writing JSON directly to a file:**

```python
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(x, f)
```

**Deserializing (JSON string → Python object)**

```python
with open('data.json', 'r', encoding='utf-8') as f:
    x = json.load(f)
print(x)   # [1, 'simple', 'list']
```

**Notes:**
- JSON files should use UTF-8 encoding.
- `json` works well with basic Python types (lists, dicts, strings, numbers, booleans, `None`).
- For more complex objects (like custom classes), additional steps are needed (see `json` module documentation).

**Alternative: `pickle` module** – can serialize almost any Python object but is Python-specific and **insecure** with untrusted data. Use `json` for cross-language data exchange.


## Confirmation of Coverage

| Section | Covered |
|---------|---------|
| 7.1 Fancier Output Formatting (intro, `str()` vs `repr()`) | Yes |
| 7.1.1 Formatted String Literals (f-strings) | Yes |
| 7.1.2 The String `format()` Method | Yes |
| 7.1.3 Manual String Formatting | Yes |
| 7.1.4 Old string formatting (`%`) | Yes |
| 7.2 Reading and Writing Files | Yes |
| 7.2.1 Methods of File Objects | Yes |
| 7.2.2 Saving structured data with `json` | Yes |

The explanation is complete, uses simple language with practical examples, and is formatted in clean Markdown without emojis.