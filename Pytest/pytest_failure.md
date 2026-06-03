# Professional Automation Testing with pytest: Rerunning Failed Tests and Maintaining State

## 1. Introduction

When running large test suites, it is common to encounter intermittent failures or to want to focus on fixing failing tests without re‑executing the entire suite. pytest provides built‑in support for remembering which tests failed in the last run and selectively re‑running them. Additionally, it offers a persistent cache that allows plugins and fixtures to store and retrieve data across test sessions.

These features are provided by the `cacheprovider` plugin, which is enabled by default. This document explains how to use these capabilities to improve test efficiency and debugging workflows.

## 2. Rerunning Failed Tests

pytest offers two command‑line options to control rerunning of previously failed tests.

### 2.1 `--lf` / `--last-failed`

The `--lf` (or `--last-failed`) option runs only the tests that failed in the last test run. All other tests are deselected.

Example: Suppose you have a test file `test_50.py` that contains 50 parametrized tests, with two failures.

```python
# test_50.py
import pytest

@pytest.mark.parametrize("i", range(50))
def test_num(i):
    if i in (17, 25):
        pytest.fail("bad luck")
```

First run (all tests):

```bash
$ pytest -q
.................F.......F........................                   [100%]
2 failed, 48 passed in 0.12s
```

Now run only the failures:

```bash
$ pytest --lf
=========================== test session starts ============================
collected 2 items
run-last-failure: rerun previous 2 failures

test_50.py FF                                                        [100%]

============================ 2 failed in 0.12s =============================
```

Only the two failing tests were executed.

### 2.2 `--ff` / `--failed-first`

The `--ff` (or `--failed-first`) option runs all tests, but the previously failed tests are executed first. This can be useful when you want to see if the failures persist while still validating the rest of the suite.

Using the same test file:

```bash
$ pytest --ff
=========================== test session starts ============================
collected 50 items
run-last-failure: rerun previous 2 failures first

test_50.py FF................................................        [100%]

2 failed, 48 passed in 0.12s
```

The output shows `FF` for the two failing tests, then dots for the passing ones.

### 2.3 Behavior When No Tests Failed

The `--lfnf` (or `--last-failed-no-failures`) option controls what happens when there are no previously recorded failures. Two values are available:

- `all`: (default) Run all tests.
- `none`: Do not run any tests; exit successfully with a message.

Example:

```bash
pytest --last-failed --last-failed-no-failures none
```

This will skip all tests and exit.

### 2.4 Running New Tests First (`--nf` / `--new-first`)

The `--nf` (or `--new-first`) option runs new tests (those that have not been executed before) first, followed by the rest of the tests. Additionally, tests are sorted by file modification time, with more recently modified files appearing first. This is helpful when you have added new tests and want to verify them quickly.

## 3. Stepwise Mode: Fixing Failures Incrementally

When a large number of tests fail, it can be overwhelming to fix them all at once. The `--stepwise` (or `--sw`) option helps you work through failures one by one.

- The test suite runs until the first failure, then stops.
- On the next invocation, pytest resumes from the last failing test and continues until the next failure.
- This repeats until all failures are fixed.

To skip a particular failing test and move to the next, use `--stepwise-skip`. This will ignore the current failing test and stop on the following failure. It implies `--stepwise` automatically.

Example usage:

```bash
# First run: stops at first failure
pytest --stepwise

# After fixing that failure, run again; will start from the next failing test
pytest --stepwise

# To skip the current failing test and move to the next
pytest --stepwise --stepwise-skip
```

## 4. The Persistent Cache

pytest stores cross‑session state in a cache directory (default `.pytest_cache`). This cache is used to remember which tests failed (`cache/lastfailed`), the order of tests (`cache/nodeids`), and any custom data stored by plugins or fixtures.

### 4.1 Accessing the Cache in Fixtures

The `config.cache` object is available in fixtures via the `pytestconfig` fixture. It provides two methods:

- `get(key, default)`: Retrieve a value from the cache.
- `set(key, value)`: Store a JSON‑serializable value in the cache.

Example: a fixture that caches the result of an expensive computation across test runs.

```python
# test_caching.py
import pytest

def expensive_computation():
    print("running expensive computation...")
    return 42

@pytest.fixture
def mydata(pytestconfig):
    val = pytestconfig.cache.get("example/value", None)
    if val is None:
        val = expensive_computation()
        pytestconfig.cache.set("example/value", val)
    return val

def test_function(mydata):
    assert mydata == 23
```

First run:

```bash
$ pytest -q
F                                                                    [100%]
-------------------------- Captured stdout setup ---------------------------
running expensive computation...
1 failed in 0.12s
```

Second run (the computation is not repeated because the value is retrieved from cache):

```bash
$ pytest -q
F                                                                    [100%]
1 failed in 0.12s
```

### 4.2 Inspecting Cache Content

You can view the contents of the cache using the `--cache-show` command‑line option. Optionally, you can provide a glob pattern to filter keys.

```bash
$ pytest --cache-show
=========================== test session starts ============================
cachedir: /home/sweet/project/.pytest_cache
--------------------------- cache values for '*' ---------------------------
cache/lastfailed contains:
  {'test_caching.py::test_function': True}
cache/nodeids contains:
  ['test_caching.py::test_function']
example/value contains:
  42
========================== no tests ran in 0.12s ===========================
```

Filtering example:

```bash
$ pytest --cache-show example/*
----------------------- cache values for 'example/*' -----------------------
example/value contains:
  42
```

### 4.3 Clearing the Cache

To clear all cache files and values, use the `--cache-clear` option. This is recommended for CI environments where isolation is critical.

```bash
pytest --cache-clear
```

## 5. Disabling the Cache Plugin

If you need to disable the cache plugin (e.g., because it interferes with your workflow), you can do so by deactivating it by name:

```bash
pytest -p no:cacheprovider
```

## 6. Best Practices

- **Use `--lf` during development** to quickly re‑run only the tests that failed, speeding up the feedback loop.
- **Combine `--lf` with `--stepwise`** when working through a large batch of failures.
- **Leverage `config.cache`** to store expensive setup results (e.g., downloading data, creating containers) across test runs, but ensure correctness by clearing the cache when the external state changes.
- **Include `--cache-clear` in CI pipelines** to guarantee a clean environment for each run.
- **Inspect cache with `--cache-show`** when debugging unexpected test behavior.

## 7. Conclusion

pytest’s built‑in cache and failure‑rerunning capabilities make it easier to manage test suites efficiently. By using `--lf`, `--ff`, `--stepwise`, and the persistent cache, automation engineers can focus on fixing failures without wasting time re‑executing passing tests. The cache also provides a flexible mechanism for storing cross‑session data, enabling performance optimizations and stateful fixtures. Incorporating these features into your daily testing workflow will lead to faster turnaround and more reliable results.

---
---
# Professional Automation Testing with pytest: Handling Test Failures

## 1. Introduction

Test failures are an inevitable part of software development. Efficiently handling failures—whether by stopping early, debugging interactively, or capturing diagnostic information—is crucial for maintaining productivity. pytest provides several built‑in mechanisms to control test execution upon failure, drop into debuggers, and report otherwise hidden exceptions. This document covers these features in detail.

## 2. Stopping After the First (or N) Failures

When running a large test suite, you may want to halt execution as soon as a failure occurs to get immediate feedback, especially during development. pytest offers two command‑line options for this:

- `-x` or `--exitfirst`: Stop after the first failure.
- `--maxfail=N`: Stop after N failures.

Example:

```bash
pytest -x                # stop after first failure
pytest --maxfail=2       # stop after two failures
```

These options are useful for fast‑feedback loops and for preventing long test runs when the initial failures are already significant.

## 3. Using pdb – The Python Debugger

pytest integrates seamlessly with Python’s built‑in debugger (`pdb`), allowing you to drop into an interactive debugging session when a test fails or even at the start of each test.

### 3.1 Dropping to pdb on Failures

Use the `--pdb` command‑line option to enter the debugger at the point of failure:

```bash
pytest --pdb
```

When a test fails, pytest will stop execution and present a `pdb` prompt. You can inspect variables, evaluate expressions, and continue execution. To drop into `pdb` only on the first failure and then exit, combine with `-x`:

```bash
pytest -x --pdb
```

Or for the first three failures:

```bash
pytest --pdb --maxfail=3
```

After a failure, the exception information is stored in `sys.last_value`, `sys.last_type`, and `sys.last_traceback`, allowing you to perform post‑mortem debugging even after the test session ends.

### 3.2 Dropping to pdb at the Start of a Test

To start every test with the debugger, use the `--trace` option:

```bash
pytest --trace
```

This will stop at the first line of each test function, giving you a chance to step through the test setup and execution.

### 3.3 Setting Breakpoints in Code

You can insert a breakpoint anywhere in your code using the standard Python `pdb.set_trace()` call. When pytest encounters it, it will automatically disable output capture for that test, allowing you to interact with the debugger. Output capture resumes after you continue.

```python
def test_example():
    import pdb; pdb.set_trace()
    assert 1 == 2
```

### 3.4 Using the `breakpoint()` Built‑in

Python 3.7 introduced the built‑in `breakpoint()` function, which invokes the configured debugger. pytest enhances this behavior:

- If `PYTHONBREAKPOINT` is set to its default value, pytest uses its custom PDB trace UI instead of the system’s default `Pdb`.
- When `--pdb` is used, the custom debugger is also used for failures.
- You can specify a custom debugger class with `--pdbcls`.

For example, to use the `IPython` debugger:

```bash
pytest --pdb --pdbcls=IPython.terminal.debugger:TerminalPdb
```

## 4. Fault Handler

pytest automatically enables the `faulthandler` module, which dumps Python tracebacks on segmentation faults or after a timeout. This is invaluable for diagnosing crashes in C extensions or stuck tests.

The fault handler is enabled by default. To disable it, use:

```bash
pytest -p no:faulthandler
```

You can also set a timeout to dump tracebacks if a test runs too long. In your configuration file (e.g., `pytest.ini`):

```ini
[pytest]
faulthandler_timeout = 5
```

This will dump the traceback of all threads if any test exceeds 5 seconds.

**Note:** This feature was originally provided by the `pytest-faulthandler` plugin. With the integration, the command‑line option `--faulthandler-timeout` has been replaced by the configuration option `faulthandler_timeout`. You can still set it from the command line using `-o faulthandler_timeout=5`.

## 5. Warnings for Unraisable Exceptions and Unhandled Thread Exceptions

Python sometimes raises exceptions in contexts where they cannot propagate, such as inside `__del__` methods or in threads that are not caught. These exceptions can go unnoticed but may indicate serious bugs. pytest automatically detects them and issues warnings.

### 5.1 Unraisable Exceptions

Unraisable exceptions occur when an exception is raised in a situation where there is no caller to handle it (e.g., in a `__del__` method). pytest reports these as `PytestUnraisableExceptionWarning`.

### 5.2 Unhandled Thread Exceptions

When a thread terminates due to an unhandled exception, the exception is normally lost. pytest captures these and issues a `PytestUnhandledThreadExceptionWarning`.

Both features are enabled by default. To disable them:

- For unraisable exceptions: `pytest -p no:unraisableexception`
- For unhandled thread exceptions: `pytest -p no:threadexception`

You can selectively silence these warnings using the `filterwarnings` marker:

```python
import pytest

@pytest.mark.filterwarnings("ignore::pytest.PytestUnraisableExceptionWarning")
def test_with_del():
    ...
```

The warning categories are `pytest.PytestUnraisableExceptionWarning` and `pytest.PytestUnhandledThreadExceptionWarning`.

## 6. Best Practices

- **Use `-x` or `--maxfail` during development** to get quick feedback on failures.
- **Combine `--pdb` with `-x`** to debug the first failure interactively.
- **Set `faulthandler_timeout` in CI** to identify hanging tests.
- **Enable warnings for unraisable exceptions** to catch subtle bugs in destructors or threading code.
- **Use `breakpoint()`** instead of `pdb.set_trace()` for cross‑platform debugging.
- **In CI pipelines**, avoid interactive debugger options; instead, rely on `--maxfail` and `--tb=short` to keep output manageable.

## 7. Conclusion

pytest’s failure handling features—from early test termination to integrated debugging and diagnostic warnings—give you fine‑grained control over how test failures are processed. By mastering these tools, you can speed up your development cycle, quickly isolate bugs, and ensure that even subtle errors are not overlooked. These capabilities are essential for building robust, maintainable test suites in any professional automation environment.