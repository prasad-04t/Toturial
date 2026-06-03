# Python Fundamentals for Automation Testing Engineers

## Introduction

Python is one of the most widely used languages in test automation due to its simplicity, readability, and extensive ecosystem of testing frameworks (pytest, Selenium, Appium, etc.). A solid grasp of Python’s core concepts—variables, operators, and keywords—is essential for writing robust, maintainable automation code. 

---

## 1. Variables in Python

### 1.1 What Are Variables?

In Python, variables are named storage locations that hold data which can be referenced and manipulated during program execution. Unlike statically typed languages (e.g., Java, C++), Python is **dynamically typed**—the type of a variable is inferred from the value assigned to it, and the same variable can hold different types over its lifetime.

```python
x = 5                # x is an integer
name = "Samantha"    # name is a string
print(x)
print(name)
```

Output:
```
5
Samantha
```

### 1.2 Rules for Naming Variables

To use variables effectively, follow Python’s naming rules:

- Variable names can contain only letters, digits, and underscores (`_`).
- They **cannot start with a digit**.
- Names are case‑sensitive (`myVar` and `myvar` are different).
- Avoid using Python keywords (see Section 3) as variable names.

**Valid names**  
```python
age = 21
_colour = "lilac"
total_score = 90
```

**Invalid names**  
```python
1name = "Error"      # Starts with a digit
class = 10           # 'class' is a reserved keyword
user-name = "Doe"    # Contains a hyphen
```

### 1.3 Assigning Values to Variables

#### Basic Assignment  
The `=` operator assigns a value to a variable.

```python
x = 5
y = 3.14
z = "Hi"
```

#### Dynamic Typing  
A variable can be reassigned to a value of a different type.

```python
x = 10
x = "Now a string"   # No error
```

### 1.4 Multiple Assignments

#### Same Value to Multiple Variables  
```python
a = b = c = 100
print(a, b, c)   # 100 100 100
```

#### Different Values in One Line  
```python
x, y, z = 1, 2.5, "Python"
print(x, y, z)   # 1 2.5 Python
```

### 1.5 Type Casting (Type Conversion)

Python provides built‑in functions to convert between data types.

```python
s = "10"
n = int(s)          # n = 10

cnt = 5
f = float(cnt)      # f = 5.0

age = 25
s2 = str(age)       # s2 = "25"

print(n)            # 10
print(f)            # 5.0
print(s2)           # 25
```

### 1.6 Determining the Type of a Variable

Use `type()` to inspect the type of any variable.

```python
n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
b = True

print(type(n))    # <class 'int'>
print(type(f))    # <class 'float'>
print(type(s))    # <class 'str'>
print(type(li))   # <class 'list'>
print(type(d))    # <class 'dict'>
print(type(b))    # <class 'bool'>
```

### 1.7 Concept of Object Reference

In Python, variables are **references** to objects, not containers that hold values directly.

```python
x = 5
```

When `x = 5` is executed, Python creates an integer object with value `5` and makes `x` reference it.

If we assign `y = x`:
```python
y = x
```

Both `x` and `y` now reference the **same** integer object (shared reference).  

Now reassign `x`:
```python
x = 'Geeks'
```

A new string object `'Geeks'` is created, and `x` now references it. `y` continues to reference the original `5` object.

If we later assign `y = "Computer"`, another new object is created, and `y` references it. The original `5` object may be garbage collected if no references remain.

**Key points:**
- Variables hold references, not the objects themselves.
- Multiple variables can reference the same object.
- Reassigning one variable does not affect others referencing the same object.

### 1.8 Deleting a Variable

The `del` keyword removes a variable from the namespace, freeing its reference to the object.

```python
x = 10
del x
print(x)   # NameError: name 'x' is not defined
```

### 1.9 Practical Examples in Automation

#### Example 1: Storing Test Configuration
```python
base_url = "https://api.example.com"
timeout = 30
retry_count = 3
```

#### Example 2: Swapping Test Data
```python
a, b = 5, 10
a, b = b, a   # Swaps values without a temporary variable
print(a, b)   # 10 5
```

#### Example 3: Counting Characters in a String
```python
word = "Python"
length = len(word)
print("Length of the word:", length)   # 6
```

#### Example 4: Using Type Casting in API Testing
```python
response_body = '{"status": "success", "code": 200}'
data = json.loads(response_body)
status_code = int(data["code"])   # Ensure numeric type for comparison
```

---

## 2. Operators in Python

Operators are special symbols that perform operations on values (operands). Python provides a rich set of operators, many of which are frequently used in test automation.

### 2.1 Arithmetic Operators

Used for mathematical calculations.

| Operator | Description          | Example       | Result  |
|----------|----------------------|---------------|---------|
| `+`      | Addition             | `15 + 4`      | `19`    |
| `-`      | Subtraction          | `15 - 4`      | `11`    |
| `*`      | Multiplication       | `15 * 4`      | `60`    |
| `/`      | Division (float)     | `15 / 4`      | `3.75`  |
| `//`     | Floor division       | `15 // 4`     | `3`     |
| `%`      | Modulus (remainder)  | `15 % 4`      | `3`     |
| `**`     | Exponentiation       | `15 ** 4`     | `50625` |

**Note:** In Python 3, `/` always returns a float. Use `//` for integer division.

### 2.2 Comparison Operators

Return `True` or `False`. Essential for assertions.

| Operator | Description             | Example          |
|----------|-------------------------|------------------|
| `>`      | Greater than            | `13 > 33` → `False` |
| `<`      | Less than               | `13 < 33` → `True`  |
| `==`     | Equal to                | `13 == 33` → `False`|
| `!=`     | Not equal to            | `13 != 33` → `True` |
| `>=`     | Greater than or equal to| `13 >= 33` → `False`|
| `<=`     | Less than or equal to   | `13 <= 33` → `True` |

### 2.3 Logical Operators

Combine boolean expressions.

| Operator | Description | Example                 |
|----------|-------------|-------------------------|
| `and`    | Logical AND | `True and False` → `False` |
| `or`     | Logical OR  | `True or False` → `True`    |
| `not`    | Logical NOT | `not True` → `False`        |

**Precedence:** `not` > `and` > `or`

### 2.4 Bitwise Operators

Operate on integers at the bit level. While less common in high‑level automation, they are occasionally used in low‑level protocols or flags.

| Operator | Description          | Example   |
|----------|----------------------|-----------|
| `&`      | Bitwise AND          | `10 & 4` → `0`  |
| `|`      | Bitwise OR           | `10 | 4` → `14` |
| `^`      | Bitwise XOR          | `10 ^ 4` → `14` |
| `~`      | Bitwise NOT          | `~10` → `-11`   |
| `<<`     | Left shift           | `10 << 2` → `40`|
| `>>`     | Right shift          | `10 >> 2` → `2` |

### 2.5 Assignment Operators

Assign values, often with an operation.

| Operator | Example   | Equivalent to |
|----------|-----------|---------------|
| `=`      | `a = 10`  |               |
| `+=`     | `a += 5`  | `a = a + 5`   |
| `-=`     | `a -= 5`  | `a = a - 5`   |
| `*=`     | `a *= 5`  | `a = a * 5`   |
| `/=`     | `a /= 5`  | `a = a / 5`   |
| `//=`    | `a //= 5` | `a = a // 5`  |
| `%=`     | `a %= 5`  | `a = a % 5`   |
| `**=`    | `a **= 5` | `a = a ** 5`  |
| `<<=`    | `a <<= 2` | `a = a << 2`  |
| `>>=`    | `a >>= 2` | `a = a >> 2`  |
| `&=`     | `a &= 5`  | `a = a & 5`   |
| `|=`     | `a |= 5`  | `a = a | 5`   |
| `^=`     | `a ^= 5`  | `a = a ^ 5`   |

### 2.6 Identity Operators

Compare whether two variables reference the same object (memory location).

| Operator | Description                    | Example                 |
|----------|--------------------------------|-------------------------|
| `is`     | True if both refer to same object | `a is b`             |
| `is not` | True if they refer to different objects | `a is not b` |

**Important:** `is` checks identity, `==` checks equality. In automation, use `is` only for singletons like `None`, `True`, `False`.

```python
a = [1, 2]
b = [1, 2]
print(a == b)   # True (same content)
print(a is b)   # False (different objects)

c = a
print(a is c)   # True (same object)
```

### 2.7 Membership Operators

Test whether a value is present in a sequence (list, tuple, string, dict, etc.).

| Operator | Description                    | Example                       |
|----------|--------------------------------|-------------------------------|
| `in`     | True if value found in sequence | `"admin" in roles`            |
| `not in` | True if value not found         | `"guest" not in roles`        |

### 2.8 Ternary Operator (Conditional Expression)

A compact way to write simple if‑else statements.

```python
value = true_value if condition else false_value
```

Example:
```python
a, b = 10, 20
min_val = a if a < b else b
print(min_val)   # 10
```

### 2.9 Precedence and Associativity

When multiple operators appear in an expression, **precedence** determines which operations are performed first. Operators with higher precedence are evaluated before those with lower precedence. **Associativity** determines the order of evaluation when operators have the same precedence (left‑to‑right or right‑to‑left).

**Example – Precedence:**
```python
expr = 10 + 20 * 30   # * has higher precedence than +, so 20*30 first
print(expr)           # 610, not 900
```

**Example – Associativity:**
```python
print(100 / 10 * 10)   # left‑to‑right: (100/10)=10, then 10*10=100.0
print(5 - 2 + 3)       # left‑to‑right: 5-2=3, then 3+3=6
print(5 - (2 + 3))     # parentheses override: 5 - 5 = 0
print(2 ** 3 ** 2)     # exponentiation is right‑associative: 2 ** (3**2) = 2**9 = 512
```

### 2.10 Automation‑Specific Use Cases

- **Assertions with comparison operators:**
  ```python
  assert response.status_code == 200, "Unexpected status code"
  assert len(elements) > 0, "No elements found"
  ```

- **Conditional test execution with logical operators:**
  ```python
  if environment == "production" and test_type == "destructive":
      pytest.skip("Destructive tests not allowed in production")
  ```

- **Membership tests for expected values:**
  ```python
  if user_role in {"admin", "manager"}:
      grant_permissions()
  ```

- **Ternary for simple assignments:**
  ```python
  timeout = 30 if environment == "staging" else 60
  ```

- **Identity checks with `None`:**
  ```python
  if element is None:
      raise ElementNotFoundError("Element not present")
  ```

---

## 3. Keywords in Python

### 3.1 What Are Keywords?

Keywords are reserved words that are part of Python’s syntax. They have special meanings and **cannot** be used as identifiers (variable names, function names, class names, etc.).

#### List of All Keywords
```python
import keyword
print(keyword.kwlist)
```

Output:
```
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

### 3.2 Identifying Keywords

- **Syntax highlighting** in IDEs (e.g., PyCharm, VS Code) displays keywords in a distinct color.
- **SyntaxError:** Attempting to use a keyword as a variable name raises an error.

```python
for = 10   # SyntaxError: invalid syntax
```

### 3.3 Categories of Keywords

| Category               | Keywords |
|------------------------|----------|
| Value Keywords         | `True`, `False`, `None` |
| Operator Keywords      | `and`, `or`, `not`, `is`, `in` |
| Control Flow           | `if`, `elif`, `else`, `for`, `while`, `break`, `continue`, `pass`, `try`, `except`, `finally`, `raise`, `assert` |
| Function & Class       | `def`, `return`, `lambda`, `yield`, `class` |
| Context Management     | `with`, `as` |
| Import & Module        | `import`, `from` |
| Scope & Namespace      | `global`, `nonlocal` |
| Async Programming      | `async`, `await` |

### 3.4 Keywords vs Identifiers vs Variables

| Concept      | Description                                                                 | Examples                         |
|--------------|-----------------------------------------------------------------------------|----------------------------------|
| **Keywords** | Reserved words with fixed meaning; cannot be used as names.                 | `if`, `else`, `while`            |
| **Identifiers** | Names given to variables, functions, classes, etc. Must follow naming rules. | `test_login`, `retry_count`      |
| **Variables** | A specific kind of identifier that holds a value.                           | `timeout = 10`                   |

### 3.5 Common Pitfalls in Automation

- Using a keyword as a variable name leads to `SyntaxError`:
  ```python
  class = "LoginTest"   # Error
  ```
  **Solution:** Use alternative names like `test_class` or `class_name`.

- Confusing `is` with `==` (both are keywords but have different meanings). Use `is` for identity (especially with `None`, `True`, `False`) and `==` for value equality.

- Overlooking that `assert` is a keyword and cannot be used as a variable name (though it is rarely needed).

### 3.6 Best Practices for Naming in Automation

- Use descriptive names: `driver`, `wait_time`, `test_data_file`.
- Follow PEP 8 conventions: `snake_case` for variables and functions, `CamelCase` for classes.
- Avoid single‑letter names except for very short loops (`i`, `j`).
- Prefix internal or private variables with a single underscore (by convention).
- Use all‑caps for constants: `DEFAULT_TIMEOUT = 30`.

---

## 4. Conclusion

Mastering Python’s variables, operators, and keywords is foundational for any automation testing engineer. These core elements are used in every test script—from reading configuration data and handling dynamic values to writing assertions and controlling test flow. By understanding the nuances of variable references, operator precedence, and the distinction between keywords and identifiers, you will write more reliable, maintainable, and professional automation code.

Keep this guide as a reference, and always apply best practices: use meaningful names, avoid keyword clashes, and leverage the right operators for clarity and correctness. With these skills, you are well‑equipped to build robust automation frameworks that stand up to real‑world demands.