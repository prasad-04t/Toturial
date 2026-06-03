# Brief Tour of the Standard Library - Simplified Explanation

This chapter introduces some of the most useful modules that come included with Python. Think of them as pre-written tools that save you time and effort.

## 10.1. Operating System Interface (`os` and `shutil`)

The **`os`** module lets you interact with the operating system: get the current directory, change directories, run system commands.

```python
import os

print(os.getcwd())                  # Show current working directory
os.chdir('/server/accesslogs')      # Change directory
os.system('mkdir today')            # Run the 'mkdir' command
```

**Important:** Use `import os` rather than `from os import *`. The latter can cause confusion because `os.open()` is different from Python's built-in `open()` function.

The **`shutil`** module provides easier functions for everyday file and folder tasks:

```python
import shutil

shutil.copyfile('data.db', 'archive.db')       # Copy a file
shutil.move('/build/executables', 'installdir') # Move a folder
```

**Useful exploration tools:**
- `dir(os)` lists all functions in the `os` module.
- `help(os)` displays the documentation for the `os` module.


## 10.2. File Wildcards (`glob`)

The **`glob`** module finds files matching a pattern (like `*.py`).

```python
import glob

python_files = glob.glob('*.py')
print(python_files)   # e.g., ['primes.py', 'random.py', 'quote.py']
```

## 10.3. Command-Line Arguments (`sys.argv` and `argparse`)

Command-line arguments are stored in `sys.argv` as a list.

```python
# File: demo.py
import sys
print(sys.argv)
```

Running `python demo.py one two three` outputs:
```
['demo.py', 'one', 'two', 'three']
```

For more advanced argument handling (with flags, help messages, type checking), use **`argparse`**:

```python
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file'
)
parser.add_argument('filenames', nargs='+')          # One or more filenames required
parser.add_argument('-l', '--lines', type=int, default=10)  # Optional flag
args = parser.parse_args()

print(args.filenames)   # List of files
print(args.lines)       # Number of lines (default 10)
```

Run with: `python top.py --lines=5 alpha.txt beta.txt`


## 10.4. Error Output Redirection and Program Termination (`sys.stderr`, `sys.exit`)

Use `sys.stderr.write()` to print error messages separately from normal output (useful when regular output is redirected to a file).

```python
import sys

sys.stderr.write('Warning, log file not found starting a new one\n')
```

To end a program early, use `sys.exit()`.


## 10.5. String Pattern Matching (`re`)

The **`re`** module provides **regular expressions** for advanced text search and replace.

```python
import re

# Find all words starting with 'f'
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
# Returns: ['foot', 'fell', 'fastest']

# Replace duplicate words
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
# Returns: 'cat in the hat'
```

For simple tasks, string methods like `replace()` are easier:

```python
'tea for too'.replace('too', 'two')   # 'tea for two'
```


## 10.6. Mathematics (`math`, `random`, `statistics`)

### `math` – mathematical functions

```python
import math

print(math.cos(math.pi / 4))   # 0.7071067811865476
print(math.log(1024, 2))       # 10.0
```

### `random` – random numbers and choices

```python
import random

print(random.choice(['apple', 'pear', 'banana']))   # random fruit
print(random.sample(range(100), 10))                # 10 unique numbers
print(random.random())                              # float between 0.0 and 1.0
print(random.randrange(6))                          # integer from 0 to 5
```

### `statistics` – basic stats

```python
import statistics

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))       # 1.607...
print(statistics.median(data))     # 1.25
print(statistics.variance(data))   # 1.372...
```

For more advanced numerical work, see the **SciPy** project (scipy.org).


## 10.7. Internet Access (`urllib.request`, `smtplib`)

### Fetching web pages

```python
from urllib.request import urlopen

with urlopen('https://docs.python.org/3/') as response:
    for line in response:
        line = line.decode()            # Convert bytes to string
        if 'updated' in line:
            print(line.rstrip())
```

### Sending email (requires a local mail server)

```python
import smtplib

server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
    """To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
server.quit()
```


## 10.8. Dates and Times (`datetime`)

The **`datetime`** module handles dates and times.

```python
import datetime as dt

# Today's date
now = dt.date.today()
print(now)                              # e.g., 2003-12-02

# Formatting dates
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
# '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

# Date arithmetic
birthday = dt.date(1964, 7, 31)
age = now - birthday
print(age.days)                         # Number of days old
```


## 10.9. Data Compression (`zlib`, `gzip`, `zipfile`, `tarfile`)

Python supports many compression formats. Here's a simple example using `zlib`:

```python
import zlib

s = b'witch which has which witches wrist watch'
print(len(s))                     # 41

compressed = zlib.compress(s)
print(len(compressed))            # 37 (smaller)

original = zlib.decompress(compressed)
print(original)                   # b'witch which...'

print(zlib.crc32(s))              # Checksum: 226805979
```

Other modules like `zipfile` and `tarfile` handle archive files.


## 10.10. Performance Measurement (`timeit`, `profile`)

The **`timeit`** module compares the speed of small code snippets.

```python
from timeit import Timer

# Traditional swap
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# Tuple unpacking swap (slightly faster)
print(Timer('a,b = b,a', 'a=1; b=2').timeit())
```

For larger programs, the **`profile`** and **`pstats`** modules help identify slow parts.


## 10.11. Quality Control (`doctest`, `unittest`)

Writing tests ensures your code works as expected.

### `doctest` – tests inside docstrings

```python
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # Automatically runs the examples in docstrings
```

### `unittest` – more comprehensive test suites

```python
import unittest

class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

if __name__ == '__main__':
    unittest.main()
```


## 10.12. Batteries Included

Python's standard library is vast and includes modules for many common tasks. Some highlights:

| Module / Package | Purpose |
|------------------|---------|
| `xmlrpc.client`, `xmlrpc.server` | Remote procedure calls (no XML knowledge needed) |
| `email` | Build, parse, and manage email messages (including attachments) |
| `json` | Read and write JSON data (widely used for web APIs) |
| `csv` | Read and write CSV files (compatible with spreadsheets) |
| `xml.etree.ElementTree`, `xml.dom`, `xml.sax` | Process XML data |
| `sqlite3` | Lightweight database (no separate server required) |
| `gettext`, `locale`, `codecs` | Internationalization (i18n) support |

This "batteries included" philosophy means you can accomplish a lot without installing third-party libraries.


## Confirmation of Coverage

| Section | Covered |
|---------|---------|
| 10.1 Operating system interface (`os`, `shutil`) | Yes |
| 10.2 File wildcards (`glob`) | Yes |
| 10.3 Command-line arguments (`sys.argv`, `argparse`) | Yes |
| 10.4 Error output redirection and termination (`sys.stderr`, `sys.exit`) | Yes |
| 10.5 String pattern matching (`re`) | Yes |
| 10.6 Mathematics (`math`, `random`, `statistics`) | Yes |
| 10.7 Internet access (`urllib.request`, `smtplib`) | Yes |
| 10.8 Dates and times (`datetime`) | Yes |
| 10.9 Data compression (`zlib`) | Yes |
| 10.10 Performance measurement (`timeit`) | Yes |
| 10.11 Quality control (`doctest`, `unittest`) | Yes |
| 10.12 Batteries included (overview of packages) | Yes |

The explanation is complete, uses simple language with practical examples, and is formatted in clean Markdown without emojis.

---
# Brief Tour of the Standard Library — Part II - Simplified Explanation

This second tour covers more advanced modules that are especially useful for larger or professional Python projects.


## 11.1. Output Formatting

### `reprlib` – Abbreviated Displays

When printing large or deeply nested data structures, `reprlib` shows a shortened version instead of overwhelming the screen.

```python
import reprlib
data = set('supercalifragilisticexpialidocious')
print(reprlib.repr(data))   # "{'a', 'c', 'd', 'e', 'f', 'g', ...}"
```

### `pprint` – Pretty Printing

The "pretty printer" formats complex data structures with indentation and line breaks for readability.

```python
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width=30)
```

Output:
```
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
```

### `textwrap` – Formatting Paragraphs

Use `textwrap` to wrap text to a specific width, such as 40 characters.

```python
import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc, width=40))
```

### `locale` – Culture-Specific Formatting

`locale` formats numbers, currencies, and dates according to local conventions (e.g., commas for thousands).

```python
import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')
x = 1234567.8
print(locale.format_string("%d", x, grouping=True))   # '1,234,567'

conv = locale.localeconv()
print(locale.format_string("%s%.*f", (conv['currency_symbol'],
                                       conv['frac_digits'], x), grouping=True))
# '$1,234,567.80'
```


## 11.2. Templating (`string.Template`)

The `Template` class lets you create strings with placeholders that can be filled in later. This is useful for user-customizable output or mail merge.

Placeholders use `$` followed by an identifier, or `${identifier}` to separate from surrounding text. Use `$$` to output a literal `$`.

```python
from string import Template
t = Template('${village}folk send $$10 to $cause.')
result = t.substitute(village='Nottingham', cause='the ditch fund')
print(result)   # 'Nottinghamfolk send $10 to the ditch fund.'
```

If a placeholder is missing, `substitute()` raises a `KeyError`. Use `safe_substitute()` to leave missing placeholders unchanged.

```python
t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
print(t.safe_substitute(d))   # 'Return the unladen swallow to $owner.'
```

### Custom Delimiters

You can change the placeholder delimiter (e.g., to `%`) by subclassing `Template`.

```python
import time, os.path

class BatchRename(Template):
    delimiter = '%'

photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')
t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print(f'{filename} --> {newname}')
```


## 11.3. Working with Binary Data Record Layouts (`struct`)

The `struct` module converts between Python values and binary data (as `bytes` objects). It's used for reading/writing binary file formats.

Format codes:
- `H` – 2-byte unsigned integer
- `I` – 4-byte unsigned integer
- `<` – little-endian byte order

Example: Reading ZIP file headers without using the `zipfile` module.

```python
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to next header
```


## 11.4. Multi-threading (`threading`)

Threads allow a program to do multiple things at once. For example, a long file compression can run in the background while the main program stays responsive.

```python
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
```

### Coordination and the `queue` Module

Threads sharing data need careful synchronization. The `queue` module provides a safe way for threads to communicate. It's often better to have one thread manage a resource and other threads send requests via a queue.


## 11.5. Logging (`logging`)

The `logging` module provides a flexible system for recording messages from your program. Different levels indicate importance: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.

```python
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
```

Output (default shows WARNING and above):
```
WARNING:root:Warning:config file server.conf not found
ERROR:root:Error occurred
CRITICAL:root:Critical error -- shutting down
```

You can configure logging to write to files, send emails, or change format via configuration files without changing code.

---

## 11.6. Weak References (`weakref`)

Normally, as long as you have a reference to an object, it stays in memory. `weakref` lets you track an object without preventing it from being deleted. Useful for caches.

```python
import weakref, gc

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a          # weak reference, does not keep object alive
print(d['primary'])       # 10 (object still alive)

del a                     # remove the only strong reference
gc.collect()              # force garbage collection
print(d['primary'])       # KeyError: 'primary' (automatically removed)
```


## 11.7. Tools for Working with Lists

### `array` – Compact Homogeneous Arrays

`array` stores numbers more efficiently than a regular list (all items same type). Useful for large numeric data.

```python
from array import array
a = array('H', [4000, 10, 700, 22222])   # 'H' = unsigned short (2 bytes)
print(sum(a))            # 26932
print(a[1:3])            # array('H', [10, 700])
```

### `collections.deque` – Fast Double-Ended Queue

`deque` (pronounced "deck") supports fast appends and pops from both ends. Ideal for queues.

```python
from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())   # Handling task1
```

Example: Breadth-first search uses `deque` as a queue.

### `bisect` – Maintain Sorted Lists

`bisect` inserts items into a sorted list while keeping it sorted.

```python
import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)
# [(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
```

### `heapq` – Heap Queue (Priority Queue)

A heap keeps the smallest element at position 0, making it fast to repeatedly get the minimum.

```python
from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # rearrange into heap order
heappush(data, -5)                 # add new element
print([heappop(data) for i in range(3)])  # three smallest: [-5, 0, 1]
```


## 11.8. Decimal Floating-Point Arithmetic (`decimal`)

Binary floating-point (`float`) can produce rounding errors for decimal numbers (like `0.1`). The `Decimal` type is exact for base-10 arithmetic, making it ideal for financial applications.

```python
from decimal import Decimal

# Compare Decimal vs float for tax calculation
print(round(Decimal('0.70') * Decimal('1.05'), 2))   # Decimal('0.74')
print(round(0.70 * 1.05, 2))                         # 0.73
```

**Exact representation avoids binary floating-point surprises:**

```python
print(Decimal('1.00') % Decimal('.10'))   # Decimal('0.00')
print(1.00 % 0.10)                        # 0.09999999999999995

print(sum([Decimal('0.1')]*10) == Decimal('1.0'))   # True
print(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0)  # False
```

**Adjustable precision:**

```python
from decimal import getcontext
getcontext().prec = 36
print(Decimal(1) / Decimal(7))
# Decimal('0.142857142857142857142857142857142857')
```


## Confirmation of Coverage

| Section | Covered |
|---------|---------|
| 11.1 Output Formatting (`reprlib`, `pprint`, `textwrap`, `locale`) | Yes |
| 11.2 Templating (`string.Template`) | Yes |
| 11.3 Binary Data Record Layouts (`struct`) | Yes |
| 11.4 Multi-threading (`threading`) | Yes |
| 11.5 Logging (`logging`) | Yes |
| 11.6 Weak References (`weakref`) | Yes |
| 11.7 Tools for Working with Lists (`array`, `deque`, `bisect`, `heapq`) | Yes |
| 11.8 Decimal Floating-Point Arithmetic (`decimal`) | Yes |

The explanation is complete, uses simple language with practical examples, and is formatted in clean Markdown without emojis.