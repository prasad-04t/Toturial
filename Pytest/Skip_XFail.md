# Professional Automation Testing with pytest: Handling Tests That Cannot Succeed

## 1. Introduction

In real‑world test suites, certain tests may not be able to pass under specific conditions – they may depend on unavailable resources, target platforms they don’t support, or they may be documenting known bugs. pytest provides two powerful mechanisms to handle such situations: **skip** and **xfail**. Skip means the test is not executed because it cannot succeed under the current environment; xfail means the test is expected to fail, and we want to record that outcome without failing the test suite.

This document explains how to use skip and xfail effectively, covering decorators, imperative methods, parametrization, reporting, and best practices.

---

## 2. Understanding Skip and XFail

- **Skip**: A test is skipped when it cannot be run at all – for example, because a required library is missing, the operating system is wrong, or a feature is not yet implemented. The test is not executed, and the result is marked as `SKIPPED` in the report.

- **XFail** (expected failure): A test is run, but even if it fails, it is reported as `XFAIL` (expected failure). If it unexpectedly passes, it becomes `XPASS` and by default does not cause the suite to fail (though it can be configured to do so). This is useful for marking known bugs or incomplete features.

pytest counts skip and xfail tests separately in the summary. By default, detailed information about them is not shown to avoid clutter. You can use the `-r` option to display extra information, e.g., `pytest -rxXs` shows details for xfailed, xpassed, and skipped tests.

---

## 3. Skipping Test Functions

### 3.1 Using the `@pytest.mark.skip` Decorator

The simplest way to skip a test is to apply the `skip` decorator, optionally with a `reason`.

```python
import pytest

@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    ...
```

When collected, this test will be skipped with the given reason.

### 3.2 Imperative Skip with `pytest.skip()`

Sometimes the skip condition cannot be evaluated at import time. In such cases, call `pytest.skip(reason)` inside the test or its setup.

```python
def test_function():
    if not valid_config():
        pytest.skip("unsupported configuration")
```

The function stops executing immediately after `pytest.skip()`.

### 3.3 Module‑Level Skip

You can skip an entire module by calling `pytest.skip()` with `allow_module_level=True` at the module top‑level.

```python
import sys
import pytest

if not sys.platform.startswith("win"):
    pytest.skip("skipping windows-only tests", allow_module_level=True)
```

All tests in the module will be skipped.

---

## 4. Conditional Skipping with `skipif`

The `@pytest.mark.skipif` decorator skips a test if a condition evaluates to `True`.

### 4.1 Basic Usage

```python
import sys
import pytest

@pytest.mark.skipif(sys.version_info < (3, 13), reason="requires python3.13 or higher")
def test_function():
    ...
```

If the condition is `True`, the test is skipped with the given reason.

### 4.2 Sharing Markers Between Modules

You can define a marker once and reuse it across multiple test modules.

```python
# test_mymodule.py
import mymodule
import pytest

minversion = pytest.mark.skipif(
    mymodule.__versioninfo__ < (1, 1),
    reason="at least mymodule-1.1 required"
)

@minversion
def test_function():
    ...
```

Then import the marker in another module:

```python
# test_myothermodule.py
from test_mymodule import minversion

@minversion
def test_anotherfunction():
    ...
```

### 4.3 Using Condition Strings (Legacy)

For backward compatibility, you can also pass a string condition, which is evaluated as a Python expression at collection time.

```python
@pytest.mark.skipif("hasattr(os, 'sep')")
def test_function():
    ...
```

However, this form is less flexible and not recommended for new code.

---

## 5. Skipping All Tests in a Class or Module

### 5.1 Class‑Level Skip

Apply `skipif` (or `skip`) to a class to skip all its test methods.

```python
@pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")
class TestPosixCalls:
    def test_function(self):
        # will not run on windows
```

### 5.2 Module‑Level Skip with `pytestmark`

Set the global variable `pytestmark` to a marker (or list of markers) to affect all tests in the module.

```python
# test_module.py
pytestmark = pytest.mark.skipif(sys.platform == "win32", reason="linux only")
```

Now every test in the module is skipped on Windows.

If multiple `skipif` conditions apply to a test, it will be skipped if **any** condition is true.

---

## 6. Skipping Entire Files or Directories

Sometimes you need to skip a whole file or directory (e.g., because it contains code that is incompatible with the current Python version). In that case, you should exclude them from test collection. This can be done by modifying the test discovery patterns in `pytest.ini` or by using `--ignore` on the command line. Refer to the [Customizing test collection](https://docs.pytest.org/en/stable/example/pythoncollection.html) documentation for details.

---

## 7. Skipping on Missing Import Dependency

Use `pytest.importorskip` to skip a test if a required module is not installed. This function can be used at module level, inside a test, or in a fixture.

```python
docutils = pytest.importorskip("docutils")
```

If the import fails, the test (or the whole module) is skipped. You can also enforce a minimum version:

```python
docutils = pytest.importorskip("docutils", minversion="0.3")
```

The version is read from the module’s `__version__` attribute.

---

## 8. Marking Expected Failures with XFail

### 8.1 Using the `@pytest.mark.xfail` Decorator

Apply the `xfail` marker to indicate that a test is expected to fail.

```python
@pytest.mark.xfail
def test_function():
    ...
```

When the test runs and fails, it is reported as `XFAIL` (expected failure). If it passes, it is reported as `XPASS` (unexpected pass).

### 8.2 The `condition` Parameter

You can conditionally xfail a test:

```python
@pytest.mark.xfail(sys.platform == "win32", reason="bug in a 3rd party library")
def test_function():
    ...
```

If the condition is `False`, the test runs normally (it may pass or fail like any other test).

### 8.3 The `reason` Parameter

Always provide a reason to document why the test is expected to fail.

```python
@pytest.mark.xfail(reason="known parser issue")
def test_function():
    ...
```

### 8.4 The `raises` Parameter

Specify an exception (or tuple of exceptions) that the test is expected to raise. If the test fails with a different exception, it will be reported as a regular failure.

```python
@pytest.mark.xfail(raises=RuntimeError)
def test_function():
    raise RuntimeError("expected")
```

### 8.5 The `run` Parameter

Set `run=False` to skip executing the test entirely (but still mark it as xfail). This is useful for tests that would crash the interpreter or are known to be broken beyond recovery.

```python
@pytest.mark.xfail(run=False)
def test_function():
    ...  # will not be executed
```

### 8.6 The `strict` Parameter

By default, XPASS (unexpected pass) does **not** fail the test suite. To change that, set `strict=True` on the marker.

```python
@pytest.mark.xfail(strict=True)
def test_function():
    ...  # will fail the suite if it unexpectedly passes
```

You can also set the default behavior for all xfail tests using the `strict_xfail` configuration option.

```ini
[pytest]
strict_xfail = true
```

### 8.7 Imperative XFail with `pytest.xfail()`

You can mark a test as xfail from inside the test or a fixture by calling `pytest.xfail(reason)`. This immediately stops the test and marks it as xfailed.

```python
def test_function():
    if not valid_config():
        pytest.xfail("failing configuration (but should work)")
    # other code will not be executed after xfail
```

---

## 9. Combining Skip/XFail with Parametrization

When using `@pytest.mark.parametrize`, you can apply skip or xfail markers to individual parameter sets using `pytest.param`.

```python
import sys
import pytest

@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (1, 2),
        pytest.param(1, 0, marks=pytest.mark.xfail),            # xfail this case
        pytest.param(1, 3, marks=pytest.mark.xfail(reason="some bug")),
        (2, 3),
        (3, 4),
        (4, 5),
        pytest.param(
            10, 11,
            marks=pytest.mark.skipif(sys.version_info >= (3, 0), reason="py2k")
        ),
    ],
)
def test_increment(n, expected):
    assert n + 1 == expected
```

This gives you fine‑grained control over which parameterized test instances are skipped or expected to fail.

---

## 10. Controlling Skip/XFail Reporting

Use the `-r` option to show detailed information about skipped, xfailed, and xpassed tests.

- `-r s` : show skipped tests
- `-r x` : show xfailed tests
- `-r X` : show xpassed tests
- `-r a` : show all except passes (a shortcut)
- Combine: `-r xsX`

Example:

```bash
pytest -rxXs
```

See `pytest -h` for the full list of `-r` options.

---

## 11. Command‑Line Options

- `--runxfail`: Force xfail‑marked tests to run as normal (no special handling). This also disables the effect of `pytest.xfail()`.
- `--disable-warnings`: Suppress the warning summary (not directly related to skip/xfail).

---

## 12. Configuration

The `strict_xfail` option in `pytest.ini` or `pyproject.toml` sets the default `strict` behavior for all xfail markers.

Example in `pytest.ini`:

```ini
[pytest]
strict_xfail = true
```

When `true`, any XPASS will cause the test suite to fail.

---

## 13. Examples

Below is a demonstration module showing various skip and xfail usages.

```python
from __future__ import annotations
import pytest

xfail = pytest.mark.xfail

@xfail
def test_hello():
    assert 0

@xfail(run=False)
def test_hello2():
    assert 0

@xfail("hasattr(os, 'sep')")
def test_hello3():
    assert 0

@xfail(reason="bug 110")
def test_hello4():
    assert 0

@xfail('pytest.__version__[0] != "17"')
def test_hello5():
    assert 0

def test_hello6():
    pytest.xfail("reason")

@xfail(raises=IndexError)
def test_hello7():
    x = []
    x[1] = 1
```

Running with `-rx` yields:

```
=========================== test session starts ============================
collected 7 items

xfail_demo.py xxxxxxx                                                [100%]

========================= short test summary info ==========================
XFAIL xfail_demo.py::test_hello
XFAIL xfail_demo.py::test_hello2
  reason: [NOTRUN]
XFAIL xfail_demo.py::test_hello3
  condition: hasattr(os, 'sep')
XFAIL xfail_demo.py::test_hello4
  bug 110
XFAIL xfail_demo.py::test_hello5
  condition: pytest.__version__[0] != "17"
XFAIL xfail_demo.py::test_hello6
  reason: reason
XFAIL xfail_demo.py::test_hello7
============================ 7 xfailed in 0.12s ============================
```

---

## 14. Best Practices

- **Use skip for environmental conditions**: If a test cannot run at all (wrong OS, missing dependency), skip it.
- **Use xfail for known bugs**: Mark tests that document a bug or an incomplete feature with `xfail`. This keeps the suite green while tracking progress.
- **Provide clear reasons**: Always include a `reason` string to explain why a test is skipped or expected to fail. This aids future maintainers.
- **Prefer decorators over imperative calls** when the condition can be evaluated at collection time – it makes the intent clearer.
- **Use `pytest.importorskip` at module level** to skip entire modules if a dependency is missing.
- **Combine skip/xfail with parametrization** to treat individual parameter sets differently.
- **Set `strict_xfail` in CI** to catch regressions where a previously xfailed test starts passing unexpectedly.
- **Review skip/xfail reports regularly** to ensure that stale markers are removed once bugs are fixed.

---

## 15. Conclusion

pytest’s skip and xfail mechanisms give you fine‑grained control over how tests that cannot succeed are handled. By using them appropriately, you can maintain a green test suite even while documenting known issues, handling platform‑specific constraints, and managing dependencies. This leads to more reliable and informative test outcomes, making it easier to focus on real problems.