# Professional Automation Testing with pytest: Doctest Support

## 1. Introduction

Doctests are a form of documentation testing where examples embedded in docstrings or text files are executed and verified against expected output. pytest integrates with Python’s standard `doctest` module, extending it with additional features like fixture injection, custom option flags, and seamless integration with the rest of the test suite.

This document provides a comprehensive guide to using doctests with pytest, covering discovery, configuration, advanced options, and pytest‑specific enhancements.

## 2. Running Doctests in Text Files

By default, pytest collects and runs doctests from any file matching the pattern `test*.txt`. You can customize this pattern using the `--doctest-glob` option, which may be specified multiple times.

Example text file `test_example.txt`:

```
hello this is a doctest
>>> x = 3
>>> x
3
```

Run pytest:

```bash
$ pytest
=========================== test session starts ============================
collected 1 item

test_example.txt .                                                   [100%]

============================ 1 passed in 0.12s =============================
```

To change the glob pattern:

```bash
pytest --doctest-glob="*.rst"
```

You can also combine multiple patterns:

```bash
pytest --doctest-glob="*.rst" --doctest-glob="*.txt"
```

## 3. Running Doctests in Docstrings

Doctests can also be embedded in docstrings of modules, classes, and functions. To enable collection of doctests from docstrings, use the `--doctest-modules` flag.

Example module `mymodule.py`:

```python
def something():
    """a doctest in a docstring
    >>> something()
    42
    """
    return 42
```

Run:

```bash
pytest --doctest-modules
=========================== test session starts ============================
collected 2 items

mymodule.py .                                                        [ 50%]
test_example.txt .                                                   [100%]

============================ 2 passed in 0.12s =============================
```

You can make this permanent by adding to your configuration file, e.g., `pytest.ini`:

```ini
[pytest]
addopts = --doctest-modules
```

## 4. Configuration Options

### 4.1 Encoding

The default encoding for doctest files is UTF‑8. You can change it with the `doctest_encoding` option in your configuration file:

```ini
[pytest]
doctest_encoding = latin1
```

### 4.2 Standard Doctest Options

pytest supports the standard `doctest` option flags, which can be enabled in the configuration file using `doctest_optionflags`. Multiple flags are separated by spaces.

Example enabling `NORMALIZE_WHITESPACE` and `IGNORE_EXCEPTION_DETAIL`:

```ini
[pytest]
doctest_optionflags = NORMALIZE_WHITESPACE IGNORE_EXCEPTION_DETAIL
```

You can also set options inline within a doctest using a special comment:

```python
>>> something_that_raises()  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
ValueError: ...
```

### 4.3 pytest‑Specific Doctest Options

pytest introduces additional option flags to make doctests more portable and robust:

- **`ALLOW_UNICODE`**: Strips the `u` prefix from Unicode strings in expected output, allowing doctests to run unchanged in Python 2 and Python 3.
- **`ALLOW_BYTES`**: Strips the `b` prefix from byte strings in expected output.
- **`NUMBER`**: Enables approximate comparison for floating‑point numbers. Numbers are compared using `pytest.approx()` with a relative tolerance derived from the precision shown in the expected output. For example:
  ```python
  math.pi
  3.14   # matches 3.14159... to two decimal places
  ```
  This works for lists and anywhere a number appears in the output (including inside strings). Because `NUMBER` can match numbers embedded in strings, it may not be suitable for global use in `doctest_optionflags`; use it selectively inline when needed.

These options can be enabled globally in the config file or inline via `# doctest: +ALLOW_UNICODE` etc.

## 5. Controlling Failure Behavior

### 5.1 Continue on Failure

By default, a doctest stops after the first failure. To see all failures in a doctest, use the `--doctest-continue-on-failure` flag:

```bash
pytest --doctest-modules --doctest-continue-on-failure
```

### 5.2 Output Format

You can change the diff output style for doctest failures using the `--doctest-report` option. Available values:

- `none` – no diff output
- `udiff` – unified diff (default)
- `cdiff` – context diff
- `ndiff` – ndiff (line‑by‑line)
- `only_first_failure` – show only the first failure

Example:

```bash
pytest --doctest-modules --doctest-report ndiff
```

## 6. pytest‑Specific Features

### 6.1 Using Fixtures in Doctests

You can use pytest fixtures inside doctests via the `getfixture` helper. This function is injected into the doctest namespace and returns the requested fixture.

Example text file `example.rst`:

```
>>> tmp = getfixture('tmp_path')
>>> (tmp / 'file.txt').write_text('content')
>>> ...
```

The fixture must be defined in a location where pytest can find it (e.g., `conftest.py` or a plugin). Note that `getfixture` is not available in standard `doctest`; it is a pytest extension.

Additionally, fixtures marked with `autouse=True` are automatically active during doctest runs, and you can apply the `@pytest.mark.usefixtures` marker to a doctest text file to use fixtures without `getfixture`.

### 6.2 The `doctest_namespace` Fixture

The `doctest_namespace` fixture provides a dictionary that can be used to inject objects into the doctest namespace. It is intended for use in your own fixtures.

Example `conftest.py`:

```python
import pytest
import numpy

@pytest.fixture(autouse=True)
def add_np(doctest_namespace):
    doctest_namespace["np"] = numpy
```

Now in your doctests (in docstrings or text files), you can use `np` directly:

```python
def arange():
    """
    >>> a = np.arange(10)
    >>> len(a)
    10
    """
```

This fixture is discovered in the same directory tree as the test files, so place `conftest.py` appropriately.

### 6.3 Skipping Doctests

You can skip individual doctest examples using the standard `doctest.SKIP` directive:

```python
def test_random():
    """
    >>> random.random()  # doctest: +SKIP
    0.156231223

    >>> 1 + 1
    2
    """
```

pytest also allows you to use `pytest.skip()` and `pytest.xfail()` inside doctests, though this reduces readability and should be used sparingly.

- In **Python modules** (docstrings), these functions affect only the current docstring.
- In **text files**, they skip/xfail the entire remaining file after the call.

Example:

```python
>>> import sys, pytest
>>> if sys.platform.startswith('win'):
...     pytest.skip('this doctest does not work on Windows')
...
>>> import fcntl
>>> ...
```

**Note:** Using `pytest.skip()` or `pytest.xfail()` inside doctests is discouraged because it mixes testing logic with documentation and can be confusing for readers.

## 7. Alternatives and External Packages

While pytest’s built‑in doctest support covers many needs, you may also consider these external packages for advanced use cases:

- **pytest-doctestplus**: Adds extra features like `+FLOAT_CMP` (which uses `pytest.approx` for floats) and supports testing reStructuredText files. It is widely used in the scientific Python community.
- **Sybil**: Parses examples from documentation files (including reStructuredText, Markdown, etc.) and executes them as part of your test suite. It provides fine‑grained control over which examples to run and how to prepare the execution environment.

These packages integrate with pytest and can be installed via `pip`.

## 8. Best Practices

- **Keep doctests simple**: They work best for illustrating basic usage and verifying examples. For complex test scenarios, use regular pytest test functions.
- **Use `ALLOW_UNICODE` and `ALLOW_BYTES`** to maintain compatibility across Python versions.
- **Prefer `NUMBER` for floating‑point comparisons** to avoid brittle tests.
- **Use fixtures sparingly** inside doctests. If you need complex setup, consider moving to a regular test.
- **Separate doctests from production code** when possible to avoid clutter, but doctests in docstrings serve as both documentation and tests.
- **Configure doctest options globally** in your `pytest.ini` or `pyproject.toml` to keep command‑line simple.
- **Use `--doctest-continue-on-failure`** to see all failing examples in one run, which is helpful when writing or refactoring documentation.

## 9. Conclusion

pytest’s doctest support bridges the gap between documentation and testing, allowing you to verify examples while keeping them in sync with your code. By leveraging the configuration options, pytest‑specific features like fixtures, and external packages for advanced needs, you can build comprehensive test suites that include doctests as a valuable component. Following the best practices outlined here will help you maintain clean, portable, and reliable doctests that integrate seamlessly with your overall testing strategy.