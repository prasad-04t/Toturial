# Professional Automation Testing with pytest: Writing and Reporting Assertions

## 1. Introduction

Assertions form the backbone of test automation. pytest enhances the standard Python `assert` statement with powerful introspection, providing detailed failure reports without requiring boilerplate code. This document covers all aspects of writing effective assertions, from basic comparisons to advanced exception and warning handling, ensuring your test suites are both expressive and maintainable.

## 2. Asserting with the `assert` Statement

pytest allows you to use the built-in `assert` statement to verify test expectations. When an assertion fails, pytest rewrites the statement to show intermediate values, making debugging straightforward.

Example:

```python
# content of test_assert1.py
def f():
    return 3

def test_function():
    assert f() == 4
```

Running this test:

```bash
$ pytest test_assert1.py
=========================== test session starts ============================
collected 1 item

test_assert1.py F                                                    [100%]

================================= FAILURES =================================
______________________________ test_function _______________________________

    def test_function():
>       assert f() == 4
E       assert 3 == 4
E        +  where 3 = f()

test_assert1.py:6: AssertionError
========================= short test summary info ==========================
FAILED test_assert1.py::test_function - assert 3 == 4
============================ 1 failed in 0.12s =============================
```

- The failure report shows the actual value returned by `f()` and the expected value.
- You can add an optional failure message: `assert a % 2 == 0, "value was odd, should be even"`. This message appears alongside the introspection output.

pytest’s assertion rewriting works for most subexpressions, including calls, attributes, comparisons, and operators. For details, see [Assertion introspection details](#assertion-introspection-details).

## 3. Assertions About Approximate Equality

Floating-point arithmetic often introduces small rounding errors. Instead of manual tolerance checks, use `pytest.approx`.

```python
import pytest
import numpy as np

def test_floats():
    assert (0.1 + 0.2) == pytest.approx(0.3)

def test_arrays():
    a = np.array([1.0, 2.0, 3.0])
    b = np.array([0.9999, 2.0001, 3.0])
    assert a == pytest.approx(b)
```

`pytest.approx` works with scalars, lists, dictionaries, and NumPy arrays. It also handles NaNs appropriately. You can customize relative and absolute tolerances:

```python
assert 1.000001 == pytest.approx(1.0, rel=1e-5)
assert 0.000001 == pytest.approx(0.0, abs=1e-6)
```

## 4. Assertions About Expected Exceptions

### 4.1 Using `pytest.raises` as a Context Manager

Use `pytest.raises` to verify that a block of code raises a specific exception.

```python
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

You can capture the exception object for further inspection:

```python
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    assert "maximum recursion" in str(excinfo.value)
```

`excinfo` is an `ExceptionInfo` instance with attributes `.type`, `.value`, and `.traceback`.

**Matching Exception Messages**

Pass the `match` parameter to check the exception’s string representation against a regular expression:

```python
def myfunc():
    raise ValueError("Exception 123 raised")

def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()
```

`match` uses `re.search`, so a simple substring like `"123"` also works. It also matches against PEP‑678 `__notes__`.

**Exact Exception Type Matching**

`pytest.raises` matches subclasses by default. To check for an exact type:

```python
def test_foo_not_implemented():
    def foo():
        raise NotImplementedError

    with pytest.raises(RuntimeError) as excinfo:
        foo()
    assert excinfo.type is RuntimeError   # fails because NotImplementedError is a subclass
```

### 4.2 Assertions About Expected Exception Groups

For `BaseExceptionGroup` or `ExceptionGroup`, use `pytest.RaisesGroup`.

```python
def test_exception_in_group():
    with pytest.RaisesGroup(ValueError):
        raise ExceptionGroup("group msg", [ValueError("value msg")])

    with pytest.RaisesGroup(ValueError, TypeError):
        raise ExceptionGroup("msg", [ValueError("foo"), TypeError("bar")])
```

Additional options:

- `match`: checks against the group’s message.
- `check`: accepts a callable that receives the group and must return `True` for success.
- `flatten_subgroups`: flattens nested groups for matching.
- `allow_unwrapped`: permits matching a single exception even if not wrapped in a group.

Example with `match` and `check`:

```python
def test_raisesgroup_match_and_check():
    with pytest.RaisesGroup(BaseException, match="my group msg"):
        raise BaseExceptionGroup("my group msg", [KeyboardInterrupt()])

    with pytest.RaisesGroup(
        Exception, check=lambda eg: isinstance(eg.__cause__, ValueError)
    ):
        raise ExceptionGroup("", [TypeError()]) from ValueError()
```

Use `pytest.RaisesExc` to specify details about a contained exception:

```python
def test_raises_exc():
    with pytest.RaisesGroup(pytest.RaisesExc(ValueError, match="foo")):
        raise ExceptionGroup("", (ValueError("foo")))
```

Both `pytest.RaisesGroup` and `pytest.RaisesExc` provide a `.matches()` method for testing outside a context manager, with a `.fail_reason` attribute for debugging.

### 4.3 `ExceptionInfo.group_contains()`

This helper checks if an `ExceptionGroup` contains a specific exception. However, it is **not** suitable for ensuring no other exceptions are present. Prefer `pytest.RaisesGroup` for strict structure validation.

```python
def test_exception_in_group():
    with pytest.raises(ExceptionGroup) as excinfo:
        raise ExceptionGroup(
            "Group message",
            [RuntimeError("Exception 123 raised")],
        )
    assert excinfo.group_contains(RuntimeError, match=r".* 123 .*")
    assert not excinfo.group_contains(TypeError)
```

- `depth` parameter: limit search to a specific nesting level (1 = top level).
- By default, it recursively searches all levels.

### 4.4 Alternate Legacy Form

Before the `with` statement was widely used, `pytest.raises` accepted a callable and its arguments:

```python
def func(x):
    if x <= 0:
        raise ValueError("x needs to be larger than zero")

pytest.raises(ValueError, func, x=-1)
```

This form is still fully supported but the context‑manager form is preferred for readability.

### 4.5 Using `xfail` with `raises`

The `@pytest.mark.xfail` decorator can be used to mark a test that is expected to fail with a specific exception:

```python
def f():
    raise IndexError()

@pytest.mark.xfail(raises=IndexError)
def test_f():
    f()
```

This marks the test as “xfail” only if it fails by raising `IndexError` (or a subclass). It is useful for documenting unfixed bugs or dependency issues.

For exception groups, use `RaisesGroup`:

```python
def f():
    raise ExceptionGroup("", [IndexError()])

@pytest.mark.xfail(raises=RaisesGroup(IndexError))
def test_f():
    f()
```

## 5. Assertions About Expected Warnings

Use `pytest.warns` to verify that code raises a specific warning:

```python
def test_warning():
    with pytest.warns(UserWarning):
        warnings.warn("my warning", UserWarning)
```

Like `pytest.raises`, it can capture the warning object for further inspection.

## 6. Context‑Sensitive Comparisons

pytest provides enhanced diff output for many data types:

- **Long strings**: context diff showing differences.
- **Long sequences**: first failing index.
- **Dictionaries**: differing entries.
- **Sets**: extra items on each side.

Example:

```python
# content of test_assert2.py
def test_set_comparison():
    set1 = set("1308")
    set2 = set("8035")
    assert set1 == set2
```

Output:

```
E       AssertionError: assert {'0', '1', '3', '8'} == {'0', '3', '5', '8'}
E
E         Extra items in the left set:
E         '1'
E         Extra items in the right set:
E         '5'
```

Use `-v` for more detailed diff.

## 7. Defining Custom Explanations for Failed Assertions

Implement the `pytest_assertrepr_compare` hook to provide custom failure explanations. The hook is called for failed `assert` comparisons.

**Placement:** In a `conftest.py` file at any level of your project.

Example:

```python
# content of conftest.py
from test_foocompare import Foo

def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return [
            "Comparing Foo instances:",
            f"   vals: {left.val} != {right.val}",
        ]
```

Now, given a test:

```python
# content of test_foocompare.py
class Foo:
    def __init__(self, val):
        self.val = val
    def __eq__(self, other):
        return self.val == other.val

def test_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2
```

The output becomes:

```
E       assert Comparing Foo instances:
E            vals: 1 != 2
```

- Return `None` to fall back to default introspection.
- The first line is treated as a summary, subsequent lines are indented.

## 8. Returning Non‑`None` Values in Test Functions

pytest issues a `PytestReturnNotNoneWarning` if a test function returns a value other than `None`. This catches a common beginner mistake of returning `True`/`False` instead of using `assert`.

Incorrect:

```python
@pytest.mark.parametrize(["a", "b", "result"], [[1, 2, 5], [2, 3, 8]])
def test_foo(a, b, result):
    return foo(a, b) == result   # This never fails based on the return value
```

Correct:

```python
def test_foo(a, b, result):
    assert foo(a, b) == result
```

## 9. Assertion Introspection Details

pytest rewrites `assert` statements in test modules at import time. This rewriting adds introspection information to the failure message without affecting non‑test modules.

- **Caching**: Rewritten modules are cached on disk as `.pyc` files. To disable caching (e.g., to avoid stale files in moving projects), add `sys.dont_write_bytecode = True` to the top of your `conftest.py`.
- **Read‑only filesystems**: If caching is not possible, rewriting still works (the rewritten code is kept in memory).
- **Manual rewriting**: To enable assertion rewriting for an imported module before import, call `pytest.register_assert_rewrite('module_name')` (e.g., in `conftest.py`).

### 9.1 Disabling Assert Rewriting

If the import hook interferes with custom import machinery, you have two options:

1. **Per‑module**: Add the string `PYTEST_DONT_REWRITE` to the module’s docstring.
2. **Global**: Use `--assert=plain` on the command line (disables rewriting for the whole test run).

## 10. Best Practices for Assertions in Automation Testing

- **Prefer simple, readable `assert` statements** – avoid complex expressions that obscure intent.
- **Use `pytest.approx` for all floating‑point comparisons** to avoid brittle tests.
- **Always capture exception objects** when additional validation is needed (e.g., checking the error message).
- **Use `pytest.RaisesGroup` instead of `group_contains`** when you need to ensure the exact structure of an `ExceptionGroup`.
- **Provide custom failure explanations** via `pytest_assertrepr_compare` for domain‑specific objects.
- **Never return values from test functions** – use `assert` to verify conditions.
- **Keep assertions focused** – one logical assertion per test is often ideal, but you can combine related checks with proper failure messages.

## 11. Conclusion

pytest’s assertion capabilities go far beyond a simple `assert` statement. By leveraging its rich introspection, specialized helpers like `approx`, `raises`, and `RaisesGroup`, as well as the ability to customize failure output, you can write clear, maintainable, and robust tests. Mastering these techniques is essential for any automation testing engineer aiming to build production‑grade test frameworks.