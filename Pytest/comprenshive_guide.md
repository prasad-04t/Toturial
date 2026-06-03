# Professional Automation Testing with pytest: A Comprehensive Guide

## Table of Contents

1. Introduction
2. Installation and Setup
3. Writing Your First Test
4. Running Tests and Invocation Strategies
5. Writing and Reporting Assertions
6. Using Fixtures
7. Marking Test Functions with Attributes
8. Parametrization of Fixtures and Test Functions
9. Using Subtests
10. Temporary Directories and Files
11. Monkeypatching and Mocking
12. Doctest Support
13. Rerunning Failed Tests and Maintaining State
14. Handling Test Failures
15. Managing Output
16. Managing Logging
17. Conclusion

---

## 1. Introduction

pytest is a mature, feature‑rich testing framework for Python that empowers automation testing engineers to write simple, scalable, and maintainable tests. Its philosophy emphasizes readability, minimal boilerplate, and powerful introspection. This document provides a comprehensive reference covering installation, test discovery, assertions, fixtures, parametrization, mocking, logging, output management, and more – everything needed to build production‑grade test automation.

---

## 2. Installation and Setup

Install pytest using pip:

```bash
pip install -U pytest
```

Verify the installation:

```bash
$ pytest --version
pytest 9.0.2
```

For project isolation, use a virtual environment.

---

## 3. Writing Your First Test

Create a file named `test_sample.py`. pytest discovers tests in files matching `test_*.py` or `*_test.py`. A test function must be prefixed with `test_`.

```python
# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
```

Run the test:

```bash
$ pytest
=========================== test session starts ============================
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

The `assert` statement is sufficient – pytest’s advanced introspection shows intermediate values, eliminating the need for JUnit‑style assertion methods.

---

## 4. Running Tests and Invocation Strategies

### 4.1 Basic Invocation

```bash
pytest                     # run all tests in current directory
pytest test_mod.py         # run tests in a specific module
pytest testing/            # run tests in a directory
```

### 4.2 Selecting Tests

- **By keyword**: `pytest -k 'MyClass and not method'`
- **By collection arguments**: `pytest tests/test_mod.py::test_func` (also works for classes, methods, and parametrized instances)
- **By marker**: `pytest -m slow`
- **By package**: `pytest --pyargs pkg.testing`
- **From file**: `pytest @tests_to_run.txt` (one argument per line)

### 4.3 Help and Profiling

```bash
pytest --version          # show version and import location
pytest --fixtures         # list available built-in fixtures
pytest -h                 # full command-line help
pytest --durations=10 --durations-min=1.0  # show slowest 10 tests >1s
```

### 4.4 Plugin Management

- Early‑load plugins: `pytest -p mypluginmodule`
- Disable plugins: `pytest -p no:doctest`

### 4.5 Alternative Invocations

- `python -m pytest [...]` – adds current directory to `sys.path`
- `pytest.main()` from Python code (returns exit code)

---

## 5. Writing and Reporting Assertions

### 5.1 Using `assert`

pytest rewrites `assert` statements to provide detailed failure reports:

```python
def test_function():
    assert f() == 4
```

Failure output shows the actual values.

### 5.2 Approximate Equality

Use `pytest.approx` for floating‑point comparisons:

```python
assert (0.1 + 0.2) == pytest.approx(0.3)
```

### 5.3 Exception Assertions

Use `pytest.raises`:

```python
with pytest.raises(ZeroDivisionError):
    1 / 0
```

Capture exception info: `with pytest.raises(ValueError) as excinfo:` then inspect `excinfo.value`.

For exception groups, use `pytest.RaisesGroup`.

### 5.4 Warning Assertions

Use `pytest.warns` to check for warnings.

### 5.5 Context‑Sensitive Comparisons

pytest provides enhanced diffs for strings, sequences, and dictionaries.

### 5.6 Custom Assertion Explanations

Implement `pytest_assertrepr_compare` in `conftest.py`.

### 5.7 Returning Values in Tests

Test functions should not return a value; use `assert` instead.

---

## 6. Using Fixtures

### 6.1 Basic Usage

Fixtures are functions decorated with `@pytest.fixture`. Tests request them by name as arguments:

```python
import pytest

@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]

def test_fruit_salad(fruit_bowl):
    fruit_salad = FruitSalad(*fruit_bowl)
    assert all(fruit.cubed for fruit in fruit_salad.fruit)
```

### 6.2 Fixtures Requesting Other Fixtures

Fixtures can depend on other fixtures, promoting modularity.

### 6.3 Reusability and Caching

Each test gets its own fixture instance. Fixtures are cached per test; multiple requests return the same instance.

### 6.4 Autouse Fixtures

Use `autouse=True` to apply a fixture to every test automatically.

### 6.5 Scopes

- `function` (default)
- `class`
- `module`
- `package`
- `session`

### 6.6 Teardown

- **Yield fixtures**: `yield` the resource, then teardown after.
- **Finalizers**: `request.addfinalizer(callable)`.

### 6.7 Factory as Fixture

Return a function that creates the resource on demand.

### 6.8 Parametrizing Fixtures

Use `params` argument to run the fixture multiple times.

### 6.9 Overriding Fixtures

Fixtures can be overridden in deeper `conftest.py` files or test modules.

---

## 7. Marking Test Functions with Attributes

Markers are used to add metadata to tests, control execution, and select tests with `-m`.

### 7.1 Built‑in Markers

- `@pytest.mark.usefixtures`
- `@pytest.mark.filterwarnings`
- `@pytest.mark.skip`
- `@pytest.mark.skipif`
- `@pytest.mark.xfail`
- `@pytest.mark.parametrize`

### 7.2 Custom Markers

Create custom markers by using any name after `@pytest.mark`. Register them in `pytest.ini` or `pyproject.toml` to avoid warnings.

### 7.3 Applying Markers to Classes and Modules

- On a class: `@pytest.mark.smoke class TestSmoke: ...`
- On a module: `pytestmark = [pytest.mark.smoke, pytest.mark.regression]`

### 7.4 Strict Markers

Set `strict_markers = true` to error on unknown markers.

---

## 8. Parametrization of Fixtures and Test Functions

### 8.1 Test Function Parametrization

```python
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 42),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```

### 8.2 Stacking Parametrization

Multiple decorators generate the Cartesian product.

### 8.3 Parametrizing Classes and Modules

Apply the decorator to a class, or assign `pytestmark` for a module.

### 8.4 Using `pytest.param` to Mark Individual Sets

```python
pytest.param("6*9", 42, marks=pytest.mark.xfail)
```

### 8.5 Fixture Parametrization

```python
@pytest.fixture(params=["smtp.gmail.com", "mail.python.org"])
def smtp_connection(request):
    return smtplib.SMTP(request.param, 587, timeout=5)
```

### 8.6 Custom Parametrization with `pytest_generate_tests`

Implement the hook to generate parameters dynamically.

---

## 9. Using Subtests

Subtests allow grouping assertions within a single test, continuing execution after failures.

```python
def test(subtests):
    for i in range(5):
        with subtests.test(msg="custom message", i=i):
            assert i % 2 == 0
```

Each failure is reported individually. Subtests are evaluated at runtime, unlike parametrization which is static.

---

## 10. Temporary Directories and Files

### 10.1 `tmp_path` Fixture

Provides a `pathlib.Path` object unique to each test.

```python
def test_create_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text("content")
    assert p.read_text() == "content"
```

### 10.2 `tmp_path_factory` Fixture

Session‑scoped; creates temporary directories for shared resources.

### 10.3 Legacy `tmpdir` and `tmpdir_factory`

Use `py.path.local` objects; deprecated. Disable with `-p no:legacypath`.

### 10.4 Location and Retention

By default, directories are kept under a structure like `/tmp/pytest-of-{user}/pytest-{num}/testname/`. Retention count defaults to 3. Use `--basetemp` to specify a custom base.

---

## 11. Monkeypatching and Mocking

The `monkeypatch` fixture allows safe temporary modifications.

### 11.1 Core Methods

- `setattr(obj, name, value)`
- `delattr(obj, name)`
- `setitem(mapping, name, value)`
- `delitem(mapping, name)`
- `setenv(name, value)`
- `delenv(name)`
- `syspath_prepend(path)`
- `chdir(path)`
- `context()` – context manager for isolated patches

### 11.2 Examples

- Patching a function: `monkeypatch.setattr(Path, "home", mockreturn)`
- Mocking a class: define a mock class and replace `requests.get`
- Modifying environment: `monkeypatch.setenv("USER", "TestingUser")`
- Changing dict values: `monkeypatch.setitem(app.DEFAULT_CONFIG, "user", "test_user")`

### 11.3 Autouse Fixtures for Global Patches

```python
@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")
```

---

## 12. Doctest Support

### 12.1 Running Doctests

- Text files: `pytest --doctest-glob="*.rst"`
- Docstrings: `pytest --doctest-modules`

### 12.2 Configuration

- `doctest_encoding` – file encoding
- `doctest_optionflags` – standard doctest flags (e.g., `NORMALIZE_WHITESPACE`)
- pytest‑specific flags: `ALLOW_UNICODE`, `ALLOW_BYTES`, `NUMBER`

### 12.3 Using Fixtures in Doctests

The `getfixture` helper allows requesting fixtures inside doctests.

### 12.4 `doctest_namespace` Fixture

Inject objects into the doctest namespace (e.g., `np` for NumPy).

### 12.5 Skipping Doctests

Use `# doctest: +SKIP` or `pytest.skip()` / `pytest.xfail()` (with caveats).

---

## 13. Rerunning Failed Tests and Maintaining State

### 13.1 Rerunning Failures

- `--lf` (`--last-failed`) – run only failures from last run
- `--ff` (`--failed-first`) – run failures first, then others
- `--nf` (`--new-first`) – run new tests first (sorted by file mtime)

### 13.2 Stepwise Mode

`--stepwise` stops after first failure; next run continues from there. `--stepwise-skip` skips the current failing test.

### 13.3 Persistent Cache

The `config.cache` object allows storing JSON‑serializable values across sessions.

```python
val = pytestconfig.cache.get("example/value", None)
pytestconfig.cache.set("example/value", 42)
```

### 13.4 Inspecting and Clearing Cache

- `pytest --cache-show` – view cache contents
- `pytest --cache-clear` – delete all cache data

---

## 14. Handling Test Failures

### 14.1 Stopping After Failures

- `-x` – stop after first failure
- `--maxfail=N` – stop after N failures

### 14.2 Using pdb

- `--pdb` – drop into debugger on failure
- `--trace` – drop into debugger at start of each test
- `--pdbcls` – specify custom debugger class

### 14.3 Fault Handler

Enabled by default; dump tracebacks on segfault or timeout. Configure `faulthandler_timeout`.

### 14.4 Unraisable and Thread Exceptions

pytest warns about exceptions in `__del__` or unhandled thread exceptions. Can be disabled with `-p no:unraisableexception` / `-p no:threadexception`.

---

## 15. Managing Output

### 15.1 Traceback Styles

- `--tb=short`, `--tb=long`, `--tb=line`, `--tb=native`, `--tb=no`
- `--full-trace` – extremely long traces, shows on Ctrl+C

### 15.2 Capturing Output

- `--capture=fd` (default), `--capture=sys`, `--capture=no` (`-s`)
- `--capture=tee-sys` – output to both capture and sys streams

### 15.3 Verbosity

- `-q` / `--quiet` – reduce
- `-v` – increase, `-vv` – more, `-vvv` – even more
- Fine‑grained: `verbosity_assertions`, `verbosity_test_cases` in config

### 15.4 Summary Report with `-r`

Characters: `f` (failed), `E` (error), `s` (skipped), `x` (xfailed), `X` (xpassed), `p` (passed), `P` (passed with output), `a` (all except pP), `A` (all), `N` (none).

### 15.5 Truncation Limits

Set `truncation_limit_lines` and `truncation_limit_chars` in config.

### 15.6 JUnitXML Reports

- `--junit-xml=path` – generate XML
- `junit_suite_name` – root suite name
- `junit_duration_report` – `total` or `call`
- `record_property`, `record_xml_attribute`, `record_testsuite_property` fixtures for custom data

### 15.7 Pastebin Integration

`--pastebin=failed` or `--pastebin=all` uploads results to `bpaste.net`.

---

## 16. Managing Logging

### 16.1 Capturing Logs

pytest captures log messages of level `WARNING` and above by default and displays them in a separate section for failed tests.

### 16.2 Formatting Logs

Customize with command‑line options:

```bash
pytest --log-format="%(asctime)s %(levelname)s %(message)s" \
       --log-date-format="%Y-%m-%d %H:%M:%S"
```

Or in configuration file:

```ini
[pytest]
log_format = %(asctime)s %(levelname)s %(message)s
log_date_format = %Y-%m-%d %H:%M:%S
```

### 16.3 Disabling Specific Loggers

Use `--log-disable=logger_name` multiple times.

### 16.4 Disabling Captured Content

`--show-capture=no` disables reporting of stdout, stderr, and logs on failures.

### 16.5 The `caplog` Fixture

- `caplog.set_level(level, logger=None)` – change log level for a logger (default root)
- `caplog.at_level(level, logger=None)` – context manager for temporary level change
- `caplog.records` – list of `LogRecord` objects captured during the test
- `caplog.text` – concatenated log messages as string
- `caplog.record_tuples` – list of `(logger_name, level, message)` tuples
- `caplog.clear()` – reset captured records
- `caplog.get_records(when)` – retrieve records from a specific phase (`setup`, `call`, `teardown`)

### 16.6 Live Logs

Enable with `log_cli = true` in configuration. Control level with `--log-cli-level`, format with `--log-cli-format`, date format with `--log-cli-date-format`.

### 16.7 File Logging

Use `--log-file=path` to write logs to a file. Options:

- `--log-file-mode` – `w` (default) or `a`
- `--log-file-level`
- `--log-file-format`
- `--log-file-date-format`

Dynamic path can be set with `set_log_path()`.

### 16.8 Customizing Colors

Log levels can be colored using the `add_color_level` method in a `pytest_configure` hook.

### 16.9 Compatibility Notes

The internal logging plugin can be disabled with `-p no:logging`. Some behavior changed in pytest 3.4; see release notes for details.

---

## 17. Conclusion

pytest provides a complete ecosystem for automation testing, from simple unit tests to complex integration scenarios. Its features—flexible invocation, powerful fixtures, advanced assertions, parametrization, mocking, logging, and reporting—make it the framework of choice for Python testing. By mastering the concepts covered in this guide, automation engineers can build robust, maintainable test suites that integrate seamlessly into any development workflow.

This document is intended as a living reference; as pytest evolves, consult the official documentation for the latest updates and best practices.