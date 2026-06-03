# Automation Testing with pytest: Comprehensive Guide for QA Engineers

## 1. Introduction

pytest is a powerful and widely adopted testing framework for Python that enables automation testing engineers to write simple, scalable, and maintainable tests. Its philosophy emphasizes readability, minimal boilerplate, and rich assertion introspection.

## 2. Installation and Setup

Ensure Python (3.8+) is installed on your system. Use `pip` to install pytest:

```bash
pip install -U pytest
```

Verify the installation by checking the version:

```bash
$ pytest --version
pytest 9.0.2
```

For project isolation, consider using a virtual environment (e.g., `venv` or `conda`).

## 3. Writing Your First Test

Create a file named `test_sample.py`. pytest discovers tests in files that follow the naming conventions `test_*.py` or `*_test.py`. Inside, define a test function prefixed with `test_`:

```python
# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
```

Run the test from the command line:

```bash
$ pytest
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-9.x.y, pluggy-1.x.y
rootdir: /home/sweet/project
collected 1 item

test_sample.py F                                                     [100%]

================================= FAILURES =================================
_______________________________ test_answer ________________________________

    def test_answer():
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_sample.py:6: AssertionError
========================= short test summary info ==========================
FAILED test_sample.py::test_answer - assert 4 == 5
============================ 1 failed in 0.12s =============================
```

The output shows the progress (`[100%]`) and a detailed failure report. The `assert` statement is all that is needed – pytest’s advanced assertion introspection automatically displays intermediate values, eliminating the need for JUnit-style assertion methods.

## 4. Running Tests and Test Discovery

By default, pytest runs all files matching `test_*.py` or `*_test.py` in the current directory and its subdirectories. You can also specify a particular file, directory, or test node:

```bash
pytest test_sample.py               # run a specific file
pytest tests/                       # run all tests in the tests directory
pytest -k "test_answer"             # run tests matching name
pytest -m "slow"                    # run tests marked with @pytest.mark.slow
```

Use the `-q` (quiet) flag for a more concise output:

```bash
$ pytest -q test_sysexit.py
.                                                                    [100%]
1 passed in 0.12s
```

Test discovery follows standard conventions:

- Test files: `test_*.py`, `*_test.py`
- Test classes: named `Test*` (with no `__init__` method)
- Test functions/methods: prefixed with `test_`

## 5. Assertions and Introspection

pytest relies on the built-in `assert` statement. When an assertion fails, pytest rewrites the assertion to provide context, showing the values of each sub‑expression. This eliminates the need for custom assertion helpers.

Example of a failing assertion with introspection:

```python
def test_introspection():
    a = 5
    b = 10
    assert a + b == 20
```

Failure output will include `assert 5 + 10 == 20` and the computed values.

## 6. Testing Exceptions

Use `pytest.raises()` as a context manager to verify that a specific exception is raised. This is especially useful for negative testing and validating error handling.

```python
# content of test_sysexit.py
import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
```

Run the test:

```bash
$ pytest -q test_sysexit.py
.                                                                    [100%]
1 passed in 0.12s
```

You can also match the exception message or access the exception object:

```python
with pytest.raises(ValueError, match=r".*invalid value.*"):
    process_data(-1)
```

## 7. Organizing Tests with Classes

Grouping tests into classes can improve organization, allow sharing of fixtures at class level, and enable applying markers to an entire class. pytest discovers test methods inside classes whose name starts with `Test` (and that do not have an `__init__` method).

```python
# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
```

Running this module:

```bash
$ pytest -q test_class.py
.F                                                                   [100%]
================================= FAILURES =================================
____________________________ TestClass.test_two ____________________________

self = <test_class.TestClass object at 0xdeadbeef0001>

    def test_two(self):
        x = "hello"
>       assert hasattr(x, "check")
E       AssertionError: assert False
E        +  where False = hasattr('hello', 'check')

test_class.py:8: AssertionError
========================= short test summary info ==========================
FAILED test_class.py::TestClass::test_two - AssertionError: assert False
1 failed, 1 passed in 0.12s
```

**Important:** Each test in a class gets its own instance of the class, ensuring test isolation. Attributes defined at the class level are shared across instances and can lead to unintended side effects:

```python
# content of test_class_demo.py
class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1
```

Running this:

```bash
$ pytest -k TestClassDemoInstance -q
.F                                                                   [100%]
================================= FAILURES =================================
______________________ TestClassDemoInstance.test_two ______________________

self = <test_class_demo.TestClassDemoInstance object at 0xdeadbeef0002>

    def test_two(self):
>       assert self.value == 1
E       assert 0 == 1
E        +  where 0 = <test_class_demo.TestClassDemoInstance object at 0xdeadbeef0002>.value

test_class_demo.py:9: AssertionError
========================= short test summary info ==========================
FAILED test_class_demo.py::TestClassDemoInstance::test_two - assert 0 == 1
1 failed, 1 passed in 0.12s
```

To avoid such pitfalls, use instance attributes (set in `setUp` methods or fixtures) rather than class attributes.

## 8. Floating-Point Comparisons

Comparing floating-point numbers directly can lead to failures due to precision errors. pytest provides `pytest.approx()` to handle this elegantly.

```python
# content of test_approx.py
import pytest


def test_sum():
    assert (0.1 + 0.2) == pytest.approx(0.3)
```

`approx` works with scalars, lists, dictionaries, and NumPy arrays. You can customize the relative and absolute tolerances:

```python
assert 1.000001 == pytest.approx(1.0, rel=1e-5)
assert 0.000001 == pytest.approx(0.0, abs=1e-6)
```

## 9. Using Temporary Directories

pytest provides built-in fixtures for temporary files and directories. The `tmp_path` fixture (available in pytest 7+) returns a `pathlib.Path` object pointing to a unique temporary directory that is automatically cleaned up after the test.

```python
# content of test_tmp_path.py
def test_needsfiles(tmp_path):
    print(tmp_path)
    assert 0
```

Running this test:

```bash
$ pytest -q test_tmp_path.py
F                                                                    [100%]
================================= FAILURES =================================
_____________________________ test_needsfiles ______________________________

tmp_path = PosixPath('PYTEST_TMPDIR/test_needsfiles0')

    def test_needsfiles(tmp_path):
        print(tmp_path)
>       assert 0
E       assert 0

test_tmp_path.py:3: AssertionError
--------------------------- Captured stdout call ---------------------------
PYTEST_TMPDIR/test_needsfiles0
========================= short test summary info ==========================
FAILED test_tmp_path.py::test_needsfiles - assert 0
1 failed in 0.12s
```

Other built-in temporary directory fixtures include `tmpdir` (returns a legacy `py.path.local` object) and `tmp_path_factory` for creating multiple temporary directories per test session.

## 10. Fixtures: Reusable Test Resources

Fixtures are functions that provide reusable test resources – such as database connections, API clients, or test data – and manage their setup and teardown. They are defined using the `@pytest.fixture` decorator and can be requested by name in test functions.

```python
import pytest

@pytest.fixture
def sample_data():
    return {"key": "value", "number": 42}

def test_with_fixture(sample_data):
    assert sample_data["number"] == 42
```

Fixtures can have different scopes: `function` (default), `class`, `module`, `package`, or `session`. They can also yield values to perform teardown after the test:

```python
@pytest.fixture
def db_connection():
    conn = create_connection()
    yield conn
    conn.close()
```

To list all available fixtures (including built-in ones), run:

```bash
pytest --fixtures
```

Add `-v` to include fixtures with leading underscores.

## 11. Markers: Categorizing Tests

Markers allow you to tag tests for selective execution or to modify test behavior. Use the `@pytest.mark.<name>` decorator.

```python
import pytest

@pytest.mark.slow
def test_heavy_computation():
    ...

@pytest.mark.smoke
def test_critical_feature():
    ...
```

Run only tests with a specific marker:

```bash
pytest -m slow
```

You can combine markers with logical operators:

```bash
pytest -m "smoke and not slow"
```

Custom markers must be registered in `pytest.ini` or `pyproject.toml` to avoid warnings:

```ini
# pytest.ini
[pytest]
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    smoke: sanity checks
```

## 12. Parametrization: Testing Multiple Inputs

The `@pytest.mark.parametrize` decorator enables running the same test function with different arguments. This reduces code duplication and clearly documents the test cases.

```python
import pytest

@pytest.mark.parametrize("input_val,expected", [
    (1, 2),
    (3, 4),
    (5, 6),
])
def test_increment(input_val, expected):
    assert input_val + 1 == expected
```

Parametrization can also be applied at class level, and multiple parameters can be combined using the `param` helper for more control (e.g., adding test IDs).

```python
@pytest.mark.parametrize(
    "a,b,expected",
    [
        pytest.param(1, 2, 3, id="positive"),
        pytest.param(-1, -2, -3, id="negative"),
    ],
)
def test_addition(a, b, expected):
    assert a + b == expected
```

## 13. Configuration and Plugins

pytest can be configured via `pytest.ini`, `pyproject.toml`, or `tox.ini`. Common settings include:

```ini
[pytest]
minversion = 7.0
addopts = -ra -q --strict-markers
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

Plugins extend pytest’s functionality. Popular plugins for automation testing include:

- `pytest-xdist`: parallel test execution
- `pytest-cov`: code coverage reporting
- `pytest-html`: HTML reports
- `pytest-mock`: mocking utilities
- `pytest-django` / `pytest-flask`: framework integration

Install plugins via pip and they are automatically discovered.

## 14. Best Practices for Automation Testing

- **Use descriptive test names**: Names should reflect the scenario (e.g., `test_user_can_login_with_valid_credentials`).
- **Keep tests isolated**: Each test should not depend on the outcome of another. Use fixtures to manage setup/teardown.
- **Follow the Arrange-Act-Assert pattern**: Organize each test into clear phases.
- **Leverage parametrization** to avoid copy‑paste test code.
- **Group related tests using classes or modules** but avoid complex inheritance.
- **Use markers** to categorize tests (smoke, regression, slow) and control execution.
- **Prefer `tmp_path`** over manual temporary directory management.
- **Handle floating-point comparisons** with `approx` to avoid brittle assertions.
- **Maintain a clean `conftest.py`** to share fixtures across multiple test files.
- **Integrate with CI/CD** pipelines to run tests automatically on each commit.

## 15. Conclusion

pytest provides a robust, scalable foundation for automation testing. Its simple syntax, powerful assertion introspection, and rich ecosystem of fixtures and plugins enable QA engineers to build maintainable test suites that integrate seamlessly with modern development workflows. 

---
---

# How to Invoke pytest: A Comprehensive Guide for Automation Testing Engineers

## Introduction

pytest is one of the most powerful and widely used testing frameworks in the Python ecosystem. Its flexibility in test discovery, execution, and reporting makes it an essential tool for automation testing engineers. Understanding how to invoke pytest correctly—and how to leverage its command‑line options—is fundamental to building efficient and maintainable test suites.


## 1. Invoking pytest

The most common way to run pytest is by using the `pytest` command from the terminal. By default, pytest discovers and runs all tests in the current directory and its subdirectories that follow the naming conventions: files named `test_*.py` or `*_test.py`, and functions or methods named `test_*` inside those files.

```bash
pytest
```

This command will:

- Recursively scan the current directory.
- Collect all test items (functions, methods, classes) that match the default patterns.
- Execute them and report the results.

### Basic Syntax

```bash
pytest [options] [file_or_dir] [file_or_dir] ...
```

If no arguments are provided, pytest uses the current directory as the root for test discovery. You can also specify one or more files or directories:

```bash
pytest tests/
pytest test_module.py tests/functional/
```

---

## 2. Specifying Which Tests to Run

pytest offers several powerful ways to select exactly the tests you want to execute, without modifying the test code.

### 2.1 Run Tests in a Module

To run all tests contained in a single module:

```bash
pytest test_mod.py
```

### 2.2 Run Tests in a Directory

To run all tests inside a specific directory (and its subdirectories):

```bash
pytest testing/
```

### 2.3 Run Tests by Keyword Expressions

The `-k` option allows you to filter tests by a keyword expression. The expression is matched against test names, class names, and file names (case‑insensitive). You can use Python operators such as `and`, `or`, `not`, and parentheses.

```bash
pytest -k 'MyClass and not method'
```

This runs tests that contain `MyClass` in their name but do **not** contain `method`.  
On Windows, use double quotes instead of single quotes:

```bash
pytest -k "MyClass and not method"
```

### 2.4 Run Tests by Collection Arguments

You can pinpoint a specific test, class, or method using the `::` syntax. The general form is:

```
pytest <module>::<class>::<method>
```

Examples:

- Run a specific test function:
  ```bash
  pytest tests/test_mod.py::test_func
  ```

- Run all tests in a class:
  ```bash
  pytest tests/test_mod.py::TestClass
  ```

- Run a specific test method inside a class:
  ```bash
  pytest tests/test_mod.py::TestClass::test_method
  ```

- Run a specific parameterized test (the parameter values appear in brackets):
  ```bash
  pytest tests/test_mod.py::test_func[x1,y2]
  ```

### 2.5 Run Tests by Marker Expressions

Markers are labels you can attach to tests using `@pytest.mark.name`. To run all tests with a given marker:

```bash
pytest -m slow
```

If a marker accepts keyword arguments (e.g., `@pytest.mark.slow(phase=1)`), you can filter on those as well:

```bash
pytest -m "slow(phase=1)"
```

For more advanced marker filtering, combine with keyword expressions.

### 2.6 Run Tests from Packages

If you have installed your package and want to run tests based on the package name (using its import path), use the `--pyargs` option:

```bash
pytest --pyargs pkg.testing
```

This imports `pkg.testing` and uses its filesystem location to discover tests.

### 2.7 Read Arguments from a File (since pytest 8.2)

You can store command‑line arguments in a text file and pass them using the `@` prefix. Each argument should be on its own line.

For example, create a file `tests_to_run.txt`:

```
tests/test_file.py
tests/test_mod.py::test_func[x1,y2]
tests/test_mod.py::TestClass
-m slow
```

Then invoke pytest as:

```bash
pytest @tests_to_run.txt
```

This is especially useful for managing large, repetitive test execution sets or for storing configurations that are reused across CI pipelines.

---

## 3. Profiling Test Execution Duration

Understanding which tests are slow is critical for optimizing test suites. pytest provides built‑in options to measure and report test durations.

To display the ten slowest tests that took longer than 1.0 second:

```bash
pytest --durations=10 --durations-min=1.0
```

- `--durations=N` shows the N slowest tests.
- `--durations-min=M` sets a minimum duration threshold (in seconds) for inclusion.
- By default, durations shorter than 0.005 seconds are not shown unless you pass `-vv` (very verbose).

You can also combine this with other selection criteria to profile a subset of tests.

---

## 4. Managing Loading of Plugins

pytest allows you to control which plugins are loaded at invocation time, either to add custom behavior or to disable built‑in or third‑party plugins.

### 4.1 Early Loading Plugins

Use the `-p` option to load a plugin before test collection begins. The argument can be:

- A full dotted module name (e.g., `myproject.plugins`).
- The entry‑point name of a plugin (e.g., `pytest_cov`).

Examples:

```bash
pytest -p mypluginmodule
pytest -p pytest_cov
```

### 4.2 Disabling Plugins

To prevent a plugin from loading, prefix its name with `no:`.

For instance, to disable the built‑in `doctest` plugin:

```bash
pytest -p no:doctest
```

This can be useful when you want to avoid running doctests in certain environments or when a plugin causes conflicts.

---

## 5. Other Ways of Calling pytest

While the `pytest` command is the primary interface, there are alternative invocation methods that provide additional flexibility.

### 5.1 Calling pytest through `python -m pytest`

You can invoke pytest using the Python interpreter’s module switch:

```bash
python -m pytest [...]
```

This is nearly equivalent to calling `pytest` directly, with one important difference: it adds the current directory to `sys.path`, which can help with import issues. It is often used in environments where the `pytest` executable is not directly available or to ensure the correct Python interpreter is used.

### 5.2 Calling pytest from Python Code

You can invoke pytest programmatically by calling `pytest.main()`. This is useful for embedding test execution inside a larger application or for custom test runners.

```python
import pytest

# Run with default arguments (reads from sys.argv)
retcode = pytest.main()

# Run with explicit arguments
retcode = pytest.main(["-x", "mytestdir"])

# Run with custom plugins
class MyPlugin:
    def pytest_sessionfinish(self):
        print("*** test run reporting finishing")

if __name__ == "__main__":
    retcode = pytest.main(["-qq"], plugins=[MyPlugin()])
    exit(retcode)
```

`pytest.main()` returns the exit code (0 for success, non‑zero for failures or errors) rather than raising `SystemExit`. This allows you to handle the outcome gracefully.

**Important Note:** Because Python’s import system caches modules, calling `pytest.main()` multiple times in the same process will not pick up changes to test files that have already been imported. For this reason, it is not recommended to run multiple test sessions within a single process.

---

## 6. Getting Help and Inspecting the Environment

pytest provides several help flags that are invaluable for debugging and learning:

- Show version and installation location:
  ```bash
  pytest --version
  ```

- List available built‑in fixtures:
  ```bash
  pytest --fixtures
  ```

- Display full help with all command‑line and configuration options:
  ```bash
  pytest -h
  pytest --help
  ```

These commands can help you understand what options are available and how pytest is configured in your environment.

---

## 7. Best Practices for Automation Testing Engineers

- **Use explicit test selection** in CI pipelines to avoid running the entire test suite unnecessarily. For example, run only tests affected by recent changes using `-k` or marker expressions.
- **Leverage `--durations`** to identify and refactor slow tests.
- **Store complex test selection patterns** in a file and use `@` to keep command lines manageable.
- **Avoid multiple `pytest.main()` calls** in the same process; instead, spawn a subprocess if you need to run tests repeatedly.
- **Use `-p` for custom plugins** that add logging, reporting, or environment setup without modifying test code.
- **Combine with `-x` (exit on first failure)** or `--maxfail=N` to fail fast during development.

---

## Conclusion

Mastering pytest invocation is a fundamental skill for any automation testing engineer. Whether you are running a single test during development, selecting a subset in a CI pipeline, or profiling performance, the flexibility of pytest’s command‑line interface empowers you to work efficiently. By understanding the various ways to specify tests, manage plugins, and call pytest from Python code, you can build robust, scalable test automation frameworks that integrate seamlessly with your development and deployment workflows.

---
---
# Professional Automation Testing with pytest: Invocation and Execution Strategies

## 1. Introduction

pytest is a mature, highly extensible testing framework for Python. It simplifies test writing through concise syntax, powerful assertion introspection, and a rich plugin ecosystem. For automation testing engineers, understanding how to invoke pytest efficiently is fundamental to building scalable, maintainable test suites. This document provides a comprehensive reference on pytest invocation – from basic test selection to advanced plugin management – designed for production-level QA engineering.

## 2. Basic Invocation

The primary method to run tests is the `pytest` command. By default, it executes all tests in files matching the patterns `test_*.py` or `*_test.py` located in the current directory and its subdirectories. Test discovery follows standard rules:

- Test files: `test_*.py`, `*_test.py`
- Test classes: `Test*` (no `__init__` method)
- Test functions/methods: prefixed with `test_`

Example:

```bash
pytest
```

This runs all discovered tests and reports results.

For a quick overview of command-line flags, refer to the [Complete pytest command-line flags reference](https://docs.pytest.org/en/stable/reference/reference.html#command-line-flags).

## 3. Specifying Which Tests to Run

pytest provides flexible mechanisms to select specific tests. These options can be combined to fine-tune execution.

### 3.1 Run Tests in a Module

Execute all tests inside a particular Python file:

```bash
pytest test_mod.py
```

### 3.2 Run Tests in a Directory

Run all tests within a directory (and its subdirectories):

```bash
pytest testing/
```

### 3.3 Run Tests by Keyword Expressions

Use `-k` to select tests whose names match a given expression. The expression is case‑insensitive and can include Python operators (`and`, `or`, `not`, parentheses) using filenames, class names, and function names as variables.

```bash
pytest -k 'MyClass and not method'
```

This runs tests that contain "MyClass" in their name but exclude those that also contain "method". On Windows, use double quotes instead of single quotes:

```bash
pytest -k "MyClass and not method"
```

### 3.4 Run Tests by Collection Arguments

Specify exact tests using the `::` notation, following the pattern `module_path::class_name::test_name`. Parameters from parametrization can be included using `[]`.

- **Specific test within a module:**

  ```bash
  pytest tests/test_mod.py::test_func
  ```

- **All tests in a class:**

  ```bash
  pytest tests/test_mod.py::TestClass
  ```

- **Specific test method:**

  ```bash
  pytest tests/test_mod.py::TestClass::test_method
  ```

- **Specific parametrization instance:**

  ```bash
  pytest tests/test_mod.py::test_func[x1,y2]
  ```

### 3.5 Run Tests by Marker Expressions

Markers (decorators like `@pytest.mark.slow`) allow categorizing tests. Use `-m` to run only tests with a given marker.

```bash
pytest -m slow
```

For markers with keyword arguments, the expression can include those values:

```bash
pytest -m "slow(phase=1)"
```

### 3.6 Run Tests from Packages

When tests are installed as part of a package, use `--pyargs`:

```bash
pytest --pyargs pkg.testing
```

This imports the specified module and uses its filesystem location to discover and run tests.

### 3.7 Read Arguments from a File

Starting with pytest 8.2, you can store command-line arguments in a file and pass them using the `@` prefix. Each line in the file represents an argument.

File `tests_to_run.txt`:

```
tests/test_file.py
tests/test_mod.py::test_func[x1,y2]
tests/test_mod.py::TestClass
-m slow
```

Invocation:

```bash
pytest @tests_to_run.txt
```

You can generate such a file with `pytest --collect-only -q` and then edit it as needed.

## 4. Getting Help and Inspecting the Environment

pytest provides several introspection commands:

- **Version and import location:**

  ```bash
  pytest --version
  ```

- **Available built-in fixtures:**

  ```bash
  pytest --fixtures
  ```

- **Complete help on command-line options and configuration:**

  ```bash
  pytest -h
  pytest --help
  ```

## 5. Profiling Test Execution Duration

To identify slow tests, use the `--durations` option. The following lists the 10 slowest tests that take longer than 1.0 second:

```bash
pytest --durations=10 --durations-min=1.0
```

By default, durations shorter than 0.005 seconds are suppressed. Use `-vv` to show all durations.

## 6. Managing Plugins

pytest’s functionality can be extended with plugins. You can control which plugins are loaded at runtime.

### 6.1 Early Loading Plugins

Use `-p` to load a plugin before test collection. The argument can be:

- A full dotted module name (e.g., `myproject.plugins`)
- An entry‑point name (e.g., `pytest_cov` for the `pytest-cov` plugin)

```bash
pytest -p pytest_cov
```

### 6.2 Disabling Plugins

To prevent a specific plugin from loading, prefix the name with `no:`:

```bash
pytest -p no:doctest
```

This disables the `doctest` plugin, which normally runs doctests from text files.

## 7. Alternative Ways to Invoke pytest

Beyond the command-line script, pytest can be invoked through the Python interpreter or programmatically.

### 7.1 Using `python -m pytest`

Execute pytest as a module:

```bash
python -m pytest [...]
```

This is almost identical to the `pytest` command, except that it adds the current directory to `sys.path`. This can be useful when dealing with import issues.

### 7.2 Calling pytest from Python Code

You can run pytest from within a Python script using `pytest.main()`. This returns the exit code without raising `SystemExit`.

```python
import pytest

# Run with default arguments (reads sys.argv)
retcode = pytest.main()

# Pass explicit arguments
retcode = pytest.main(["-x", "mytestdir"])
```

Plugins can be added dynamically:

```python
# myinvoke.py
import sys
import pytest

class MyPlugin:
    def pytest_sessionfinish(self):
        print("*** test run reporting finishing")

if __name__ == "__main__":
    sys.exit(pytest.main(["-qq"], plugins=[MyPlugin()]))
```

Running this script:

```bash
$ python myinvoke.py
*** test run reporting finishing
```

**Important Note:** Calling `pytest.main()` multiple times within the same process is not recommended. Because Python caches imported modules, subsequent calls will not reflect changes made to test files or modules between calls. For re‑running tests after code changes, start a new process.

## 8. Best Practices for Test Invocation in CI/CD and Local Development

- **Use configuration files** (`pytest.ini`, `pyproject.toml`) to define default options, avoiding repetitive command-line flags.
- **Leverage markers** to separate test suites (e.g., `smoke`, `regression`, `slow`) and run them selectively in different pipeline stages.
- **Combine selection methods** for fine‑grained control: `pytest -k "test_login" -m "not slow" tests/api/`.
- **Set `--durations-min`** to a reasonable threshold to catch performance regressions.
- **Always run tests in isolation** – avoid relying on order or shared state; use fixtures for setup/teardown.
- **Use `--strict-markers`** (often set in configuration) to prevent typos in marker names.
- **When invoking from code**, treat `pytest.main()` as a one‑time call per process; prefer subprocess invocation for repeated runs.

## 9. Conclusion

Mastering pytest invocation is essential for building efficient, maintainable test automation. Whether selecting tests by module, keyword, marker, or collection path, controlling plugin loading, or integrating pytest into CI/CD pipelines, the flexibility of the command line empowers QA engineers to tailor execution to any scenario. C