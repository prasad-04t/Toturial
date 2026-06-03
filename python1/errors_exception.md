# Errors and Exceptions - Simplified Explanation

This chapter explains the different types of errors in Python, how to handle them gracefully, and how to create your own error types.


## 8.1. Syntax Errors

A **syntax error** occurs when Python cannot understand your code because it violates the language's grammar rules.

```python
while True print('Hello world')
```

Python shows:
```
  File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax
```

The parser points to where it detected the problem, though the actual fix may be earlier (here, a missing colon `:` before `print`).


## 8.2. Exceptions

An **exception** is an error that occurs during execution, even if the syntax is correct.

Common examples:

```python
10 * (1/0)          # ZeroDivisionError: division by zero
4 + spam*3          # NameError: name 'spam' is not defined
'2' + 2             # TypeError: can only concatenate str (not "int") to str
```

When an exception occurs, Python prints:
- The **exception type** (e.g., `ZeroDivisionError`)
- A **detail message** explaining what happened
- A **traceback** showing the sequence of function calls leading to the error


## 8.3. Handling Exceptions

Use `try` and `except` to catch and handle exceptions instead of letting the program crash.

### Basic Structure

```python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")
```

**How it works:**
1. Code in `try` block runs.
2. If no exception occurs, `except` is skipped.
3. If a matching exception occurs, the `except` block runs.
4. If an unmatched exception occurs, it propagates upward.

### Multiple `except` Clauses

You can catch different exceptions separately:

```python
try:
    # some code
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Cannot divide by zero")
except (RuntimeError, TypeError, NameError):
    print("One of several errors occurred")
```

### Exception Hierarchy

Exceptions are classes. An `except` clause catches the named class and any subclass of it.

```python
class B(Exception): pass
class C(B): pass
class D(C): pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
# Output: B, C, D
```

Order matters: put more specific exceptions first.

### Accessing Exception Details

Capture the exception instance with `as`:

```python
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))       # <class 'Exception'>
    print(inst.args)        # ('spam', 'eggs')
    print(inst)             # ('spam', 'eggs')
    x, y = inst.args
    print('x =', x)         # x = spam
    print('y =', y)         # y = eggs
```

### Catching All Exceptions (Use with Caution)

`Exception` catches most exceptions, but avoid being too broad unless necessary.

```python
try:
    # risky code
except Exception as err:
    print(f"Unexpected error: {err}")
    raise   # Re-raise after logging
```

### The `else` Clause

`else` runs only if no exception occurred in the `try` block. This separates normal code from error-handling code.

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('Cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

### Exceptions in Called Functions

Handlers catch exceptions raised inside functions called from the `try` block.

```python
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
```

## 8.4. Raising Exceptions

Use `raise` to deliberately trigger an exception.

```python
raise NameError('HiThere')
```

You can pass an exception class (instantiated automatically) or an instance:

```python
raise ValueError   # equivalent to raise ValueError()
```

### Re-raising Exceptions

Inside an `except` block, `raise` alone re-raises the current exception.

```python
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
```m



## 8.5. Exception Chaining

When an exception occurs while handling another exception, Python automatically chains them.

```python
try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")
```

The traceback shows both exceptions with "During handling...".

### Explicit Chaining with `from`

Use `raise ... from exc` to explicitly state that one exception caused another.

```python
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
```

### Disabling Chaining

Use `from None` to suppress the automatic chaining:

```python
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None
```



## 8.6. User-defined Exceptions

Create your own exception types by subclassing `Exception` (or its subclasses).

```python
class MyCustomError(Exception):
    """Raised when something specific goes wrong."""
    pass
```

Convention: Exception class names usually end with "Error".



## 8.7. Defining Clean-up Actions (`finally`)

The `finally` clause always executes, whether an exception occurred or not. It's ideal for releasing resources (closing files, network connections).

```python
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
```

Output:
```
Goodbye, world!
Traceback (most recent call last):
  ...
KeyboardInterrupt
```

**Important rules:**
- `finally` runs after `try`, `except`, and `else`, but before the exception propagates.
- If `finally` contains `return` or `break`, it overrides any exception or return from `try`. (This is discouraged and triggers a warning in Python 3.14+.)

Example with return override:

```python
def bool_return():
    try:
        return True
    finally:
        return False

print(bool_return())   # False
```

Complete example:

```python
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)   # result is 2.0 \n executing finally clause
divide(2, 0)   # division by zero! \n executing finally clause
divide("2", "1") # executing finally clause (then raises TypeError)
```

---

## 8.8. Predefined Clean-up Actions (`with` Statement)

Many objects (like files) provide built-in clean-up via the `with` statement. This ensures resources are released automatically, even if errors occur.

Without `with`:
```python
for line in open("myfile.txt"):
    print(line, end="")
# File remains open indefinitely (bad practice)
```

With `with`:
```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
# File is automatically closed
```

`with` works with any object that defines context manager methods (like `__enter__` and `__exit__`).

---

## 8.9. Raising and Handling Multiple Unrelated Exceptions

Sometimes you need to report several errors at once (e.g., when multiple parallel tasks fail). Use `ExceptionGroup`.

```python
def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)

f()
```

Output shows a group with two sub-exceptions.

### Catching Specific Exceptions in a Group with `except*`

Use `except*` to handle only certain types of exceptions from a group, leaving others to propagate.

```python
def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup(
                "group2",
                [OSError(3), RecursionError(4)]
            )
        ]
    )

try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")
```

Note: Exceptions inside a group must be instances, not types.

### Practical Pattern for Collecting Exceptions

```python
excs = []
for test in tests:
    try:
        test.run()
    except Exception as e:
        excs.append(e)

if excs:
    raise ExceptionGroup("Test Failures", excs)
```



## 8.10. Enriching Exceptions with Notes

Use `add_note()` to attach additional context to an exception after it has been caught. Notes appear in the traceback.

```python
try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
    raise
```

Traceback includes:
```
TypeError: bad type
Add some information
Add some more information
```

### Example: Adding Context to Grouped Exceptions

```python
def f():
    raise OSError('operation failed')

excs = []
for i in range(3):
    try:
        f()
    except Exception as e:
        e.add_note(f'Happened in Iteration {i+1}')
        excs.append(e)

raise ExceptionGroup('We have some problems', excs)
```

Each sub-exception in the group will display its specific note.

---

## Confirmation of Coverage

| Section | Covered |
|---------|---------|
| 8.1 Syntax Errors | Yes |
| 8.2 Exceptions | Yes |
| 8.3 Handling Exceptions (`try`/`except`/`else`) | Yes |
| 8.4 Raising Exceptions | Yes |
| 8.5 Exception Chaining (`from`, `from None`) | Yes |
| 8.6 User-defined Exceptions | Yes |
| 8.7 Defining Clean-up Actions (`finally`) | Yes |
| 8.8 Predefined Clean-up Actions (`with`) | Yes |
| 8.9 Exception Groups (`ExceptionGroup`, `except*`) | Yes |
| 8.10 Enriching Exceptions with Notes (`add_note`) | Yes |

The explanation is complete, uses simple language with practical examples, and is formatted in clean Markdown without emojis.