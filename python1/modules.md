# Modules - Simplified Explanation

This chapter explains how to organize your Python code into reusable files called modules, and how to structure larger projects using packages.


## 6.1. What is a Module?

A **module** is simply a Python file (with a `.py` extension) containing functions, variables, and other code. Modules let you:

- Reuse code across multiple programs without copying and pasting.
- Keep your program organized by splitting it into logical pieces.

### Creating and Using a Module

Suppose you create a file named `fibo.py` with this content:

```python
# Fibonacci numbers module

def fib(n):
    """Print Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """Return Fibonacci series up to n as a list."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

Now in the Python interpreter, you can import and use the module:

```python
import fibo

fibo.fib(1000)          # Calls the fib function from fibo module
print(fibo.fib2(100))   # Calls fib2 function
print(fibo.__name__)    # The module knows its own name: 'fibo'
```

**Important:** When you `import fibo`, you do **not** directly get access to `fib` or `fib2`. You must prefix them with the module name: `fibo.fib`.

You can assign a function to a local name for convenience:

```python
fib = fibo.fib
fib(500)
```


## 6.1.1. More on Modules

### Module Execution

- A module can contain both function definitions and executable statements (like initializing variables).
- Statements inside a module run **only once**, the first time the module is imported anywhere.
- Each module has its **own namespace** (a separate set of variable names). This prevents name conflicts.

### Different Ways to Import

| Import Style | Example | How to Use |
|--------------|---------|------------|
| Import whole module | `import fibo` | `fibo.fib(100)` |
| Import specific names | `from fibo import fib, fib2` | `fib(100)` directly |
| Import everything (not recommended) | `from fibo import *` | `fib(100)` directly |
| Import with alias | `import fibo as fib` | `fib.fib(100)` |
| Import specific name with alias | `from fibo import fib as fibonacci` | `fibonacci(100)` |

**Warning:** `from module import *` is discouraged because it clutters your namespace and can overwrite existing names. It's sometimes used in interactive sessions for quick typing.

### Reloading a Module

Modules are cached after the first import. If you edit a module and want to reload it without restarting Python, use:

```python
import importlib
importlib.reload(module_name)
```


## 6.1.2. Executing Modules as Scripts

You can make a module act as both an importable library and a standalone script. Add this at the end of your file:

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

Now you can run it from the command line:

```bash
python fibo.py 50
```

The code inside the `if` block runs only when the file is executed directly (not imported). This is a common pattern for testing or providing a command-line interface.


## 6.1.3. The Module Search Path

When you `import spam`, Python searches for `spam.py` in the following order:

1. **Built-in modules** (like `sys`, `math`).
2. Directories listed in `sys.path`, which includes:
   - The directory containing the script you ran (or the current directory).
   - Directories from the `PYTHONPATH` environment variable.
   - Standard library directories (including `site-packages`).

You can view and modify `sys.path`:

```python
import sys
print(sys.path)               # Show current search path
sys.path.append('/my/modules') # Add a new directory
```

## 6.1.4. "Compiled" Python Files (`.pyc`)

To speed up loading, Python saves compiled bytecode versions of modules in the `__pycache__` folder. For example, `spam.py` becomes `__pycache__/spam.cpython-313.pyc`.

- This happens automatically; you don't need to do anything.
- `.pyc` files are platform-independent.
- Python recompiles the `.pyc` file if the source `.py` file has changed.

**Notes for advanced users:**
- The `-O` and `-OO` command-line flags can remove `assert` statements and docstrings to reduce file size.
- Running from a `.pyc` file is **not faster** than running from `.py`; it only loads faster.


## 6.2. Standard Modules

Python comes with a rich **standard library** of modules. Some notable ones:

- `sys`: System-specific parameters and functions.
- `os`: Operating system interfaces.
- `math`: Mathematical functions.
- `datetime`: Date and time handling.

Example with `sys`:

```python
import sys
print(sys.ps1)      # Primary prompt string: '>>> '
print(sys.ps2)      # Secondary prompt: '... '
sys.ps1 = 'C> '     # Change the prompt (interactive mode only)
```

You can also modify the module search path via `sys.path.append()`.


## 6.3. The `dir()` Function

`dir()` lists all names defined in a module or the current namespace.

```python
import fibo
print(dir(fibo))        # Shows '__name__', 'fib', 'fib2'

a = [1, 2, 3]
print(dir())            # Lists names you've defined: 'a', 'fibo', etc.
```

To see **built-in** names (like `print`, `len`, `Exception`), look in the `builtins` module:

```python
import builtins
print(dir(builtins))
```


## 6.4. Packages

A **package** is a collection of modules organized in directories. Packages use dotted module names (e.g., `sound.effects.echo`).

### Example Package Structure

```
sound/                      Top-level package
    __init__.py             (Can be empty)
    formats/                Subpackage
        __init__.py
        wavread.py
        wavwrite.py
        ...
    effects/                Subpackage
        __init__.py
        echo.py
        surround.py
        ...
    filters/                Subpackage
        __init__.py
        equalizer.py
        ...
```

### The `__init__.py` File

- Required (unless using namespace packages) to tell Python that the directory is a package.
- Can be empty or contain initialization code.
- Can define `__all__` to control what `from package import *` imports.

### Importing from a Package

```python
# Import a submodule with full path
import sound.effects.echo
sound.effects.echo.echofilter(input, output)

# Import a submodule without package prefix
from sound.effects import echo
echo.echofilter(input, output)

# Import a specific function directly
from sound.effects.echo import echofilter
echofilter(input, output)
```


### 6.4.1. Importing `*` from a Package

`from sound.effects import *` does **not** automatically import all submodules. The package author controls what gets imported by defining `__all__` in `__init__.py`:

```python
# In sound/effects/__init__.py
__all__ = ["echo", "surround", "reverse"]
```

If `__all__` is not defined, `import *` imports whatever names are already in the package's namespace (including previously imported submodules).

**Best practice:** Avoid `import *` in production code; be explicit about what you import.


### 6.4.2. Intra-package References

Inside a package, you can use **absolute imports** (preferred) or **relative imports**.

**Absolute import:**
```python
# In sound/filters/vocoder.py
from sound.effects import echo
```

**Relative import (using dots):**
- `.` means current package.
- `..` means parent package.

```python
# In sound/effects/surround.py
from . import echo              # same package
from .. import formats          # parent package (sound)
from ..filters import equalizer # sibling package
```

**Important:** Relative imports only work inside packages. The main script of an application should use absolute imports.


### 6.4.3. Packages in Multiple Directories

A package's `__path__` attribute holds a list of directories where submodules can be found. You can modify it to extend the package across multiple locations (rarely used).

```python
# Inside __init__.py
__path__.append('/additional/modules')
```


## Confirmation of Coverage

| Section | Covered |
|---------|---------|
| 6. Modules introduction | Yes |
| 6.1 More on modules (import styles, namespaces) | Yes |
| 6.1.1 Executing modules as scripts | Yes |
| 6.1.2 Module search path | Yes |
| 6.1.3 Compiled Python files | Yes |
| 6.2 Standard modules | Yes |
| 6.3 The `dir()` function | Yes |
| 6.4 Packages | Yes |
| 6.4.1 Importing `*` from a package | Yes |
| 6.4.2 Intra-package references | Yes |
| 6.4.3 Packages in multiple directories | Yes |

The explanation is complete, uses simple language with practical examples, and is formatted in clean Markdown without emojis.