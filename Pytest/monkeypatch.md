# Professional Automation Testing with pytest: Monkeypatching and Mocking

## 1. Introduction

In automated testing, you often need to simulate external dependencies, modify global settings, or control the environment to ensure repeatable and isolated test behavior. The `monkeypatch` fixture in pytest provides a safe and convenient way to temporarily alter attributes, dictionary items, environment variables, and system paths during test execution. All modifications are automatically undone after the test finishes, preventing side effects between tests.


## 2. The `monkeypatch` Fixture

The `monkeypatch` fixture is a built‑in fixture available in any test function or fixture that requests it. It offers a set of helper methods to patch various aspects of the Python runtime.

### 2.1 Core Methods

| Method | Description |
|--------|-------------|
| `monkeypatch.setattr(obj, name, value, raising=True)` | Set an attribute on an object. If `raising` is `True` (default), raises an `AttributeError` if the attribute does not exist. |
| `monkeypatch.delattr(obj, name, raising=True)` | Delete an attribute. |
| `monkeypatch.setitem(mapping, name, value)` | Set an item in a dictionary‑like object. |
| `monkeypatch.delitem(mapping, name, raising=True)` | Delete an item from a dictionary‑like object. |
| `monkeypatch.setenv(name, value, prepend=None)` | Set an environment variable. If `prepend` is a string (e.g., `os.pathsep`), the value will be prepended to the existing variable. |
| `monkeypatch.delenv(name, raising=True)` | Delete an environment variable. |
| `monkeypatch.syspath_prepend(path)` | Prepend `path` to `sys.path`. This also calls `pkg_resources.fixup_namespace_packages()` and `importlib.invalidate_caches()`. |
| `monkeypatch.chdir(path)` | Change the current working directory. |
| `monkeypatch.context()` | Return a context manager that isolates changes to a specific block. |

All modifications are automatically reverted after the test function or fixture that requested `monkeypatch` finishes.

## 3. Common Usage Scenarios

### 3.1 Monkeypatching Functions

Suppose you have a function that depends on the current user’s home directory. To make the test deterministic, you can patch `Path.home` to return a fixed path.

```python
# contents of test_module.py
from pathlib import Path

def getssh():
    return Path.home() / ".ssh"

def test_getssh(monkeypatch):
    def mockreturn():
        return Path("/abc")

    monkeypatch.setattr(Path, "home", mockreturn)

    x = getssh()
    assert x == Path("/abc/.ssh")
```

### 3.2 Monkeypatching Returned Objects: Building Mock Classes

When a function returns an object with methods you need to control, create a mock class that mimics the required interface.

```python
# app.py
import requests

def get_json(url):
    r = requests.get(url)
    return r.json()
```

```python
# test_app.py
import requests
import app

class MockResponse:
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}

def test_get_json(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    result = app.get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"
```

This approach avoids real network calls and provides full control over the response.

### 3.3 Using Fixtures to Share Mocks

For reusability, move the patch into a fixture.

```python
# test_app.py
import pytest
import requests
import app

class MockResponse:
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}

@pytest.fixture
def mock_response(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()
    monkeypatch.setattr(requests, "get", mock_get)

def test_get_json(mock_response):
    result = app.get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"
```

If you need the patch applied to all tests automatically, you can use `autouse=True` in the fixture, or place it in a `conftest.py`.

### 3.4 Global Patch: Preventing Network Access

To ensure no test accidentally performs HTTP requests, you can remove the `request` method from `requests.sessions.Session`.

```python
# conftest.py
import pytest

@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")
```

Now any attempt to use `requests.get()` or similar will raise an `AttributeError`.

**Warning:** Patching built‑in functions (like `open`, `compile`) may break pytest’s internals. If you must do so, consider using `monkeypatch.context()` to limit the scope, and use flags like `--tb=native`, `--assert=plain`, and `--capture=no` to reduce interference.

### 3.5 Monkeypatching Environment Variables

Test code that reads environment variables needs to simulate both present and absent values.

```python
# code.py
import os

def get_os_user_lower():
    username = os.getenv("USER")
    if username is None:
        raise OSError("USER environment is not set.")
    return username.lower()
```

```python
# test_code.py
import pytest

def test_upper_to_lower(monkeypatch):
    monkeypatch.setenv("USER", "TestingUser")
    assert get_os_user_lower() == "testinguser"

def test_raise_exception(monkeypatch):
    monkeypatch.delenv("USER", raising=False)
    with pytest.raises(OSError):
        _ = get_os_user_lower()
```

These tests can be combined with fixtures for clarity.

### 3.6 Monkeypatching Dictionaries

Global configuration dictionaries are common. Use `setitem` and `delitem` to alter them temporarily.

```python
# app.py
DEFAULT_CONFIG = {"user": "user1", "database": "db1"}

def create_connection_string(config=None):
    config = config or DEFAULT_CONFIG
    return f"User Id={config['user']}; Location={config['database']};"
```

```python
# test_app.py
import app

def test_connection(monkeypatch):
    monkeypatch.setitem(app.DEFAULT_CONFIG, "user", "test_user")
    monkeypatch.setitem(app.DEFAULT_CONFIG, "database", "test_db")

    expected = "User Id=test_user; Location=test_db;"
    assert app.create_connection_string() == expected

def test_missing_user(monkeypatch):
    monkeypatch.delitem(app.DEFAULT_CONFIG, "user", raising=False)
    with pytest.raises(KeyError):
        _ = app.create_connection_string()
```

Again, you can factor the patches into fixtures.

## 4. Scoped Patches with `monkeypatch.context()`

The `monkeypatch.context()` method returns a context manager that isolates patches to a specific block. This is useful when you need to apply patches only for a limited part of a test, or when patching standard library functions that pytest itself uses.

```python
import functools

def test_partial(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(functools, "partial", 3)
        assert functools.partial == 3
    # Outside the context, functools.partial is restored
```

This ensures that the patch does not affect the rest of the test, reducing the risk of breaking pytest internals.

## 5. Best Practices

- **Keep patches narrow** – patch only what is necessary for the test, and restore immediately (pytest does this automatically).
- **Use fixtures** to encapsulate patches, making tests more readable and reusable.
- **Prefer patching objects in your own code** rather than built‑ins or pytest internals. If you must patch standard library modules, use `monkeypatch.context()` to limit the scope.
- **Name mock functions clearly** – use descriptive names like `mock_return` or `fake_requests_get` to convey intent.
- **When patching functions, ensure the signature matches** – otherwise, the test may fail with a `TypeError`.
- **For mocking complex objects, define a dedicated mock class** rather than using lambda functions; it improves readability and allows you to add necessary attributes/methods easily.
- **Use `autouse` fixtures sparingly** – they affect all tests and can cause unexpected side effects if not carefully documented.
- **Verify that the patch was applied** – you can assert that the patched attribute has the expected value before using it.

## 6. Limitations and Warnings

- **Patching built‑in functions** (e.g., `open`, `compile`) may interfere with pytest’s own operation. Use `monkeypatch.context()` to limit the patch to a small block, and consider using `--tb=native`, `--assert=plain`, and `--capture=no` if you encounter issues.
- **Patching third‑party libraries** that pytest itself depends on (like `pluggy`) can also cause failures. Be cautious.
- **The `monkeypatch` fixture is not thread‑safe** – it is intended for single‑threaded test runs. If you use parallel testing (e.g., `pytest-xdist`), each worker process gets its own `monkeypatch` instance, so no conflicts occur across processes.
- **When patching a method that is called from another thread**, ensure the patch is in place before the thread starts.

## 7. Conclusion

The `monkeypatch` fixture is an indispensable tool for writing isolated, deterministic tests. It allows you to safely modify the runtime environment, mock dependencies, and simulate error conditions without leaving traces behind. By following the patterns and best practices outlined in this document, you can build robust test suites that are both maintainable and reliable.

For a complete reference, consult the [pytest API documentation for MonkeyPatch](https://docs.pytest.org/en/stable/reference/reference.html#monkeypatch).