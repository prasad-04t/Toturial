# Professional Automation Testing with pytest: Using Subtests

## 1. Introduction

pytest 9.0 introduced a new experimental feature called *subtests*, which allows grouping multiple assertions within a single test function while continuing execution after a failure. Subtests are an alternative to parametrization, especially useful when the exact set of test values is not known at test collection time (e.g., generated dynamically during test execution).

This document covers the usage, output interpretation, verbosity controls, typing, and a comparison with traditional parametrization.

**Note:** This feature is experimental; its behavior (particularly failure reporting) may evolve in future releases. However, the core functionality and usage are considered stable.

## 2. Basic Usage

To use subtests, your test function must accept a `subtests` argument. pytest automatically provides a `subtests` fixture of type `pytest.Subtests`. Inside the test, you create subtest contexts using the `subtests.test()` context manager.

Each subtest is an independent assertion block. If an assertion fails, the subtest is marked as failed, but the test continues to run subsequent subtests.

### 2.1 Example

```python
# content of test_subtest.py

def test(subtests):
    for i in range(5):
        with subtests.test(msg="custom message", i=i):
            assert i % 2 == 0
```

### 2.2 Output

Running this test with `pytest -q` produces:

```bash
$ pytest -q test_subtest.py
uuuuuF                                                               [100%]
================================= FAILURES =================================
_______________________ test [custom message] (i=1) ________________________

subtests = <_pytest.subtests.Subtests object at 0xdeadbeef0001>

    def test(subtests):
        for i in range(5):
            with subtests.test(msg="custom message", i=i):
>               assert i % 2 == 0
E               assert (1 % 2) == 0

test_subtest.py:6: AssertionError
_______________________ test [custom message] (i=3) ________________________

subtests = <_pytest.subtests.Subtests object at 0xdeadbeef0001>

    def test(subtests):
        for i in range(5):
            with subtests.test(msg="custom message", i=i):
>               assert i % 2 == 0
E               assert (3 % 2) == 0

test_subtest.py:6: AssertionError
___________________________________ test ___________________________________
contains 2 failed subtests
========================= short test summary info ==========================
SUBFAILED[custom message] (i=1) test_subtest.py::test - assert (1 % 2) == 0
SUBFAILED[custom message] (i=3) test_subtest.py::test - assert (3 % 2) == 0
FAILED test_subtest.py::test - contains 2 failed subtests
3 failed, 3 subtests passed in 0.12s
```

Key points:

- `uuuuuF` – each `u` indicates a passed subtest, `F` indicates a failed top‑level test.
- Each failing subtest is reported separately with its context (the `msg` and any keyword arguments passed to `subtests.test`).
- After all subtests, a final summary shows the total number of failed subtests.
- The top‑level test itself is marked as failed because it contains one or more failed subtests.

## 3. Advanced Usage

### 3.1 Multiple Subtest Blocks and Mixing with Normal Assertions

You can have multiple subtest sections inside a test, and also include ordinary assertions outside `subtests.test` blocks.

```python
def test(subtests):
    # First block
    for i in range(5):
        with subtests.test("stage 1", i=i):
            assert i % 2 == 0

    # Normal assertion
    assert func() == 10

    # Second block
    for i in range(10, 20):
        with subtests.test("stage 2", i=i):
            assert i % 2 == 0
```

If an ordinary assertion fails, the test stops immediately (like any normal test). Subtest failures do not stop the test.

### 3.2 Identifying Subtests

The `subtests.test()` context manager accepts any keyword arguments, which are used to identify the subtest in the output. The `msg` parameter is especially useful for providing a human‑readable label.

```python
with subtests.test(msg="check parity", value=value):
    assert value % 2 == 0
```

In failure output, the subtest will appear as:

```
test [check parity] (value=5)
```

## 4. Verbosity Control

By default, only subtest failures are shown. Passed subtests produce no output unless verbosity is increased.

- `pytest -v` shows progress for passed subtests as well (each subtest appears as a line).
- You can control subtest verbosity independently using the `verbosity_subtests` setting (if available). In the core implementation, the global verbosity level applies to subtests as well.

## 5. Typing

pytest exports the `Subtests` class for type annotations.

```python
def test(subtests: pytest.Subtests) -> None:
    with subtests.test():
        ...
```

This helps static type checkers (like mypy) and improves code readability.

## 6. Parametrization vs Subtests

Both parametrization and subtests allow running a test with multiple sets of values, but they differ fundamentally.

| Aspect                     | Parametrization                                  | Subtests                                          |
|----------------------------|--------------------------------------------------|---------------------------------------------------|
| **When evaluated**         | At collection time (static)                      | During test execution (dynamic)                   |
| **Test generation**        | Creates separate test nodes                      | Runs inside a single test                         |
| **Command‑line selection** | Individual parametrized tests can be selected via `-k` | Cannot select individual subtests from CLI        |
| **Plugin integration**     | Works with `--last-failed`, parallel execution   | Limited; plugins treat the whole test as a unit   |
| **Failure handling**       | First failure stops that test instance; other instances run normally | All subtests run regardless of failures; multiple failures reported together |
| **Best for**               | Known parameter sets, decision tables            | Dynamic data, generating many checks at runtime   |

### 6.1 When to Use Subtests

- You do not know the exact parameters until test execution (e.g., reading from a database, API, or generating on the fly).
- You want to see all failures in one run, not just the first one.
- You want to avoid the overhead of creating many separate test nodes (which can be heavy for thousands of cases).
- You are writing a test that would be cumbersome to parametrize (e.g., nested loops with dependencies).

### 6.2 When to Use Parametrization

- You know the parameter set in advance.
- You need to run each case in isolation (e.g., for parallel execution or precise failure tracking).
- You want to use pytest’s advanced selection features (`-k`, `-m`) on individual cases.
- You are using plugins that rely on per‑test metadata.

## 7. Best Practices

- **Use meaningful `msg` and keyword arguments** to make subtest identification clear in failure reports.
- **Avoid mixing ordinary assertions** with subtests if you need to see multiple failures; an ordinary assertion will halt the test.
- **Keep subtests independent** – do not rely on state changes from one subtest to affect another; order should not matter.
- **Consider performance** – creating thousands of subtests in a single test may be slower than parametrization due to the overhead of exception handling, but it can be more memory‑efficient for huge parameter spaces.
- **Document why you chose subtests** over parametrization, especially in code reviews.

## 8. Compatibility Note

The subtests feature was originally provided by the third‑party plugin `pytest-subtests`. Since pytest 9.0, it has been merged into the core. The core implementation is intended to be compatible with the plugin, except that it does not include the plugin’s custom command‑line options for subtest output control. If you were using the plugin, you can remove it after upgrading to pytest 9.0.

## 9. Conclusion

Subtests offer a flexible way to group multiple assertions within a single test, allowing all failures to be reported together. This is especially valuable when dealing with dynamic test data or when you want to avoid the explosion of test nodes that parametrization would create. By understanding the trade‑offs between subtests and parametrization, automation testing engineers can choose the right tool for each scenario, leading to more maintainable and informative test suites.

---
---
# Professional Automation Testing with pytest: Temporary Directories and Files

## 1. Introduction

Testing often requires creating temporary files or directories for isolated data, output verification, or resource management. pytest provides built‑in fixtures to handle temporary directories securely and cleanly. These fixtures automatically clean up after tests, ensuring that test runs are isolated and do not interfere with each other or leave behind residual data.

This document covers the primary fixtures for temporary directories—`tmp_path`, `tmp_path_factory`, and their legacy counterparts—as well as configuration options for directory location and retention.

## 2. The `tmp_path` Fixture

The `tmp_path` fixture provides a temporary directory unique to each test function. It returns a `pathlib.Path` object, making it compatible with modern Python path handling.

### 2.1 Basic Usage

```python
# content of test_tmp_path.py
CONTENT = "content"

def test_create_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT, encoding="utf-8")
    assert p.read_text(encoding="utf-8") == CONTENT
    assert len(list(tmp_path.iterdir())) == 1
    assert 0   # intentional failure to show output
```

Running the test (with a deliberate failure) reveals the temporary directory path:

```bash
$ pytest test_tmp_path.py
=========================== test session starts ============================
collected 1 item

test_tmp_path.py F                                                   [100%]

================================= FAILURES =================================
_____________________________ test_create_file _____________________________

tmp_path = PosixPath('PYTEST_TMPDIR/test_create_file0')

    def test_create_file(tmp_path):
        d = tmp_path / "sub"
        d.mkdir()
        p = d / "hello.txt"
        p.write_text(CONTENT, encoding="utf-8")
        assert p.read_text(encoding="utf-8") == CONTENT
        assert len(list(tmp_path.iterdir())) == 1
>       assert 0
E       assert 0

test_tmp_path.py:11: AssertionError
========================= short test summary info ==========================
FAILED test_tmp_path.py::test_create_file - assert 0
============================ 1 failed in 0.12s =============================
```

The fixture automatically creates a directory (e.g., `PYTEST_TMPDIR/test_create_file0`) and cleans it up after the test finishes.

### 2.2 Key Characteristics

- **Function scope**: Each test gets its own fresh directory.
- **`pathlib.Path` interface**: Use methods like `/`, `mkdir()`, `write_text()`, etc.
- **Automatic cleanup**: The directory is removed after the test, unless retention policies are configured (see Section 5).

## 3. The `tmp_path_factory` Fixture

The `tmp_path_factory` is a **session‑scoped** fixture that allows creating temporary directories outside the scope of a single test. It is useful for generating resources that can be shared across multiple tests, such as a large file that is expensive to create.

### 3.1 Basic Usage

```python
# contents of conftest.py
import pytest

@pytest.fixture(scope="session")
def image_file(tmp_path_factory):
    # Assume compute_expensive_image() is a slow function
    img = compute_expensive_image()
    fn = tmp_path_factory.mktemp("data") / "img.png"
    img.save(fn)
    return fn

# contents of test_image.py
def test_histogram(image_file):
    img = load_image(image_file)
    # compute and test histogram
```

Here, `tmp_path_factory.mktemp("data")` creates a temporary directory named with the prefix `data` (plus a unique suffix). The fixture returns the path to the saved image, and all tests using `image_file` share the same file.

### 3.2 Methods

- `mktemp(basename: str, numbered: bool = True) -> Path`: Creates a temporary directory. If `numbered` is `True`, a unique suffix is appended to `basename`. Returns a `Path` object.
- `getbasetemp() -> Path`: Returns the base temporary directory used by the factory.

### 3.3 When to Use `tmp_path_factory`

- You need to share a temporary resource across multiple tests.
- You want to create a directory outside the context of a single test (e.g., in a fixture with broader scope).

## 4. Legacy Fixtures: `tmpdir` and `tmpdir_factory`

pytest also provides `tmpdir` and `tmpdir_factory` fixtures for backward compatibility. These use `py.path.local` objects, which are not `pathlib.Path` objects.

- `tmpdir`: Function‑scoped, returns a `py.path.local` object.
- `tmpdir_factory`: Session‑scoped, returns a factory that creates `py.path.local` directories.

**Important:** The legacy fixtures are deprecated. New code should use `tmp_path` and `tmp_path_factory`. To help migrate existing codebases, you can disable the legacy plugin entirely:

```bash
pytest -p no:legacypath
```

This will raise errors when legacy fixtures are used. You can also set this permanently in your configuration:

```ini
# pytest.ini
[pytest]
addopts = -p no:legacypath
```

## 5. Temporary Directory Location and Retention

The location and retention of temporary directories can be configured through command‑line options and environment variables.

### 5.1 Default Behavior

When `--basetemp` is **not** specified, temporary directories are created under a structure like:

```
{temproot}/pytest-of-{user}/pytest-{num}/{testname}/
```

- `{temproot}`: System temporary directory (`tempfile.gettempdir()`). Override with `PYTEST_DEBUG_TEMPROOT` environment variable.
- `{user}`: The current user name.
- `{num}`: An auto‑incremented number that increases with each test suite run.
- `{testname}`: A sanitized version of the test function name.

This structure provides retention: by default, the last **3** temporary directories are kept. The number of retained runs can be configured with the `tmp_path_retention_count` option (see below). The retention policy ensures that old directories are not removed prematurely while limiting disk usage.

### 5.2 Using `--basetemp`

If you specify a base directory with `--basetemp` (e.g., `pytest --basetemp=/path/to/basetemp`), pytest will use that directory directly:

```
{basetemp}/{testname}/
```

**Warning:** When using `--basetemp`, the directory is **cleared blindly** before each test run. Ensure you use a dedicated directory not used for other purposes. Retention does not apply in this mode.

### 5.3 Configuration Options

- `tmp_path_retention_count`: Set the number of temporary directories to keep. Example:
  ```ini
  [pytest]
  tmp_path_retention_count = 5
  ```
- `tmp_path_retention_policy`: Determines which runs are kept. The default is `"all"`, meaning all runs up to the retention count are kept. Other values may be used by plugins.

These settings can be placed in `pytest.ini`, `pyproject.toml`, or `tox.ini`.

### 5.4 Environment Variables

- `PYTEST_DEBUG_TEMPROOT`: Override the system temporary directory root (useful for debugging or forcing a specific location).

## 6. Interaction with pytest‑xdist

When using `pytest-xdist` to run tests in parallel on the local machine, pytest automatically configures a base temporary directory for each worker. This ensures that all temporary data from the entire test run lands under a single per‑run temporary directory, preventing collisions between workers.

## 7. Best Practices

- **Prefer `tmp_path` and `tmp_path_factory`** over the legacy fixtures to benefit from `pathlib` and future compatibility.
- **Do not rely on specific paths** inside the temporary directory; always use the provided fixture object to construct paths.
- **Use `tmp_path_factory` sparingly** – only when sharing resources across tests is necessary. Overuse can lead to side effects between tests.
- **Configure retention** appropriately for your CI environment. Too low retention may cause unnecessary re‑creation of expensive resources; too high may waste disk space.
- **Clean up after yourself** even though pytest removes directories; if you create files outside the fixture (e.g., using `tempfile`), ensure manual cleanup.
- **When debugging a failing test**, you can inspect the temporary directory by printing `tmp_path` and then manually examining it before pytest cleans it up. Use `--basetemp` to preserve directories beyond the retention period.

## 8. Conclusion

pytest’s temporary directory fixtures provide a robust, secure way to manage test‑generated files. The modern `tmp_path` and `tmp_path_factory` fixtures integrate seamlessly with `pathlib`, while configuration options give you fine control over where and how long temporary data is kept. Mastering these fixtures is essential for writing isolated, repeatable, and maintainable test suites in any automation project.