# Professional Automation Testing with pytest: Managing Logging

## 1. Introduction

Logging is a critical part of any application, and testing code that produces logs requires careful handling. pytest provides a powerful, integrated logging system that captures log messages during test execution, displays them alongside failures, and offers fine‑grained control via fixtures and configuration. This document covers everything from basic log capture to advanced features like live logs, file logging, and customizing log colors.

---

## 2. Default Log Capture Behavior

pytest automatically captures log messages of level **WARNING** or above and displays them in a dedicated section for each failed test, alongside captured stdout and stderr.

Example output for a failing test:

```
----------------------- Captured stdlog call ----------------------
test_reporting.py    26 WARNING  text going to logger
----------------------- Captured stdout call ----------------------
text going to stdout
----------------------- Captured stderr call ----------------------
text going to stderr
==================== 2 failed in 0.02 seconds =====================
```

By default, each captured log message shows the module name, line number, log level, and the message.

---

## 3. Configuring Log Format and Date Format

You can customize the log and date format using command‑line options or configuration files. The formatting options follow Python’s standard `logging` module conventions.

### 3.1 Command‑Line Options

```bash
pytest --log-format="%(asctime)s %(levelname)s %(message)s" \
       --log-date-format="%Y-%m-%d %H:%M:%S"
```

With these options, the captured log output appears as:

```
----------------------- Captured stdlog call ----------------------
2010-04-10 14:48:44 WARNING text going to logger
```

### 3.2 Configuration File

Add the following to your `pytest.ini`, `pyproject.toml`, or `tox.ini`:

```ini
[pytest]
log_format = %(asctime)s %(levelname)s %(message)s
log_date_format = %Y-%m-%d %H:%M:%S
```

---

## 4. Disabling Specific Loggers

To suppress logs from a particular logger, use the `--log-disable` option multiple times:

```bash
pytest --log-disable=main --log-disable=testing
```

This prevents messages from the named loggers from being captured and displayed.

---

## 5. Disabling All Captured Output on Failures

If you want to prevent the display of captured stdout, stderr, and logs for failing tests, use:

```bash
pytest --show-capture=no
```

Other values for `--show-capture` are `stdout`, `stderr`, `log`, and `all` (default).

---

## 6. The `caplog` Fixture

The `caplog` fixture provides programmatic access to log records captured during a test. It allows you to change log levels, inspect logs, and assert on log content.

### 6.1 Changing Log Levels

- **Set level globally for a test**:

  ```python
  def test_foo(caplog):
      caplog.set_level(logging.INFO)
  ```

- **Set level for a specific logger**:

  ```python
  def test_foo(caplog):
      caplog.set_level(logging.CRITICAL, logger="root.baz")
  ```

- **Temporarily change level inside a context**:

  ```python
  def test_bar(caplog):
      with caplog.at_level(logging.INFO):
          # code that logs at INFO
  ```

  For a specific logger:

  ```python
  with caplog.at_level(logging.CRITICAL, logger="root.baz"):
      ...
  ```

All level changes are automatically reverted after the test ends.

### 6.2 Inspecting Captured Logs

The `caplog` fixture exposes captured logs in several ways:

- `caplog.records`: list of `logging.LogRecord` objects captured during the test.
- `caplog.text`: concatenated log messages as a single string.
- `caplog.record_tuples`: list of `(logger_name, level, message)` tuples, convenient for assertions.

Examples:

```python
def test_baz(caplog):
    func_under_test()
    for record in caplog.records:
        assert record.levelname != "CRITICAL"
    assert "wally" not in caplog.text
```

```python
def test_foo(caplog):
    logging.getLogger().info("boo %s", "arg")
    assert caplog.record_tuples == [("root", logging.INFO, "boo arg")]
```

### 6.3 Clearing Captured Logs

Use `caplog.clear()` to reset the captured log records within a test.

```python
def test_something_with_clearing_records(caplog):
    some_method_that_creates_log_records()
    caplog.clear()
    your_test_method()
    assert ["Foo"] == [rec.message for rec in caplog.records]
```

### 6.4 Accessing Logs by Phase

The `caplog.records` attribute contains logs from the **current stage** only (setup, call, or teardown). To access logs from a different stage, use `caplog.get_records(when)`.

Example: a fixture that checks for warnings during setup and call phases:

```python
@pytest.fixture
def window(caplog):
    window = create_window()
    yield window
    for when in ("setup", "call"):
        messages = [
            x.message for x in caplog.get_records(when)
            if x.levelno == logging.WARNING
        ]
        if messages:
            pytest.fail(f"warning messages encountered during testing: {messages}")
```

### 6.5 Warning About Root Logger Modification

The `caplog` fixture adds a handler to the root logger. If your test modifies the root logger (e.g., with `logging.config.dictConfig`), this handler may be removed. Ensure that any such configuration **adds to** existing handlers rather than replacing them, or use `caplog` after the configuration is applied.

---

## 7. Live Logs (Console Output)

Live logs print logging records directly to the console as they are emitted, without waiting for test completion.

### 7.1 Enabling Live Logs

Add to your configuration file:

```ini
[pytest]
log_cli = true
```

Or use the command line:

```bash
pytest --log-cli-level=INFO
```

### 7.2 Controlling Live Log Output

- `--log-cli-level`: set the minimum level for console logs (e.g., `INFO`, `WARNING`).
- `--log-cli-format`: custom format for live logs.
- `--log-cli-date-format`: custom date format.

If not specified, live logs use the same format as captured logs (`--log-format` and `--log-date-format`).

### 7.3 Configuration File Options

```ini
[pytest]
log_cli = true
log_cli_level = INFO
log_cli_format = %(asctime)s %(levelname)s %(message)s
log_cli_date_format = %Y-%m-%d %H:%M:%S
```

---

## 8. Logging to a File

You can write all logging output to a file for later analysis.

### 8.1 Basic File Logging

```bash
pytest --log-file=/path/to/logfile.log
```

By default, the file is overwritten each test run. To append, use:

```bash
pytest --log-file=/path/to/logfile.log --log-file-mode=a
```

### 8.2 File Logging Options

- `--log-file-level`: minimum level for file logs (default: `NOTSET`).
- `--log-file-format`: custom format for file logs.
- `--log-file-date-format`: custom date format.

If not specified, file logs use the same format as captured logs.

### 8.3 Configuration File Options

```ini
[pytest]
log_file = /path/to/logfile.log
log_file_mode = w
log_file_level = DEBUG
log_file_format = %(asctime)s %(levelname)s %(message)s
log_file_date_format = %Y-%m-%d %H:%M:%S
```

### 8.4 Dynamic File Path

You can change the log file path programmatically using `set_log_path()`. This feature is experimental.

```python
def test_dynamic_log_path(caplog):
    caplog.set_log_path("/tmp/my_test.log")
    # logs will now go to /tmp/my_test.log
```

The method respects the `log_file_mode` configuration (append or write).

---

## 9. Customizing Log Colors

If colored terminal output is enabled, log levels are displayed with colors. You can change the colors or add colors for custom log levels using the `add_color_level()` method.

Example in `conftest.py`:

```python
import logging
import pytest

@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    logging_plugin = config.pluginmanager.get_plugin("logging-plugin")
    # Change color of INFO to cyan
    logging_plugin.log_cli_handler.formatter.add_color_level(logging.INFO, "cyan")
    # Add color for a custom level SPAM (assumed already defined)
    logging_plugin.log_cli_handler.formatter.add_color_level(logging.SPAM, "blue")
```

**Warning:** This API is experimental and may change without notice.

---

## 10. Compatibility and Release Notes

The logging feature was introduced as a drop‑in replacement for the third‑party `pytest-catchlog` plugin. They conflict with each other; if you need the old plugin, disable the built‑in logging with:

```ini
[pytest]
addopts = -p no:logging
```

### Incompatible Changes in pytest 3.4

- Log levels are no longer changed automatically unless explicitly requested via `log_level` config or `--log-level`. This allows users to configure loggers themselves. If a test needs a lower level than the global setting, use `caplog.set_level()`.
- Live logs are disabled by default; enable with `log_cli = true`.
- Live logs now go to `sys.stdout` and do not require `-s`.

To partially restore the 3.3 behavior, you can use:

```ini
[pytest]
log_cli = true
log_level = NOTSET
```

---

## 11. Best Practices

- **Use `caplog` for assertions**: Instead of relying on live logs or manual inspection, use `caplog.record_tuples` or `caplog.text` to verify that the correct log messages were emitted.
- **Set appropriate log levels**: For performance, capture only the levels you need (e.g., `WARNING` and above in CI, `DEBUG` when debugging locally).
- **Use file logging in CI**: Write logs to a file and archive it as an artifact for post‑run analysis.
- **Avoid interfering with root logger**: If you must reconfigure logging, use `caplog` after your configuration, or add handlers rather than replacing them.
- **Leverage stage‑specific logs**: Use `caplog.get_records(when)` to check logs from setup or teardown phases, especially in fixtures.

---

## 12. Conclusion

pytest’s logging capabilities give you complete control over how log messages are captured, displayed, and validated during test execution. From simple automatic capture to advanced fixtures like `caplog`, live console output, and file logging, you can integrate logging checks seamlessly into your test suite. By following the practices outlined here, you can ensure that your tests not only verify functional correctness but also confirm that your application logs appropriately.
---
---

# Professional Automation Testing with pytest: Capturing stdout/stderr Output

## 1. Introduction

Capturing standard output and standard error is essential for testing code that produces console output. pytest provides powerful, configurable capturing mechanisms that allow you to control what output is collected during test execution, how it is displayed on failures, and how to inspect it programmatically within tests. This document explains the various capturing options, the fixtures that give you fine‑grained access to captured output, and best practices for debugging and verifying console output in your test suite.

---

## 2. Default Capturing Behavior

By default, pytest intercepts any output sent to `stdout` and `stderr` during test execution. If a test fails (or a setup/teardown method fails), the captured output from that test is displayed alongside the failure traceback. This behavior ensures that you see relevant diagnostic output without being overwhelmed by output from passing tests.

Additionally, `stdin` is set to a “null” object that raises an error if read from, preventing tests from accidentally waiting for interactive input.

The default capturing mode is **file descriptor (fd) level** – pytest intercepts writes to the low‑level file descriptors 1 and 2 (stdout and stderr). This means that even output from subprocesses or C extensions that write directly to file descriptors will be captured.

---

## 3. Capturing Methods

pytest offers three distinct capturing methods, each with different trade‑offs:

| Method | Description |
|--------|-------------|
| **fd** (default) | Captures writes to operating system file descriptors 1 and 2. This includes output from `print()`, `sys.stdout.write()`, and also output from subprocesses and libraries that bypass Python’s `sys.stdout` (e.g., C extensions). |
| **sys** | Captures only writes to Python’s `sys.stdout` and `sys.stderr` objects. Output that goes directly to file descriptors (e.g., from a subprocess) will **not** be captured. |
| **tee-sys** | Captures writes to `sys.stdout` and `sys.stderr` (like `sys` mode) but also passes the output through to the actual console. This allows you to see live output while still having it captured for later inspection (e.g., for JUnitXML reports). |

---

## 4. Controlling Capturing from the Command Line

You can influence capturing using command‑line options:

```bash
pytest -s                    # disable all capturing (equivalent to --capture=no)
pytest --capture=sys         # use sys-level capturing
pytest --capture=fd          # use fd-level capturing (default)
pytest --capture=tee-sys     # use tee-sys capturing
pytest --capture=no          # disable capturing
```

The `-s` flag is a shortcut for `--capture=no` and is often used during debugging to see all output immediately.

You can also control which captured output is shown on failures with `--show-capture`. By default, captured `stdout`, `stderr`, and logs are shown. To change this:

```bash
pytest --show-capture=no      # show no captured output
pytest --show-capture=stdout  # show only stdout
pytest --show-capture=stderr  # show only stderr
pytest --show-capture=log     # show only logs
pytest --show-capture=all     # show all (default)
```

---

## 5. Using `print()` Statements for Debugging

One of the simplest debugging techniques is to insert `print()` statements. Because pytest captures output, these prints will appear only when a test fails, helping you pinpoint the problem without cluttering the output of passing tests.

Example:

```python
# test_module.py
def setup_function(function):
    print("setting up", function)

def test_func1():
    assert True

def test_func2():
    assert False
```

When run:

```bash
$ pytest
=========================== test session starts ============================
collected 2 items

test_module.py .F                                                    [100%]

================================= FAILURES =================================
________________________________ test_func2 ________________________________

    def test_func2():
>       assert False
E       assert False

test_module.py:12: AssertionError
-------------------------- Captured stdout setup ---------------------------
setting up <function test_func2 at 0xdeadbeef0001>
```

The print from the setup of the failing test is shown, while the print from the passing test is hidden.

---

## 6. Fixtures for Accessing Captured Output

pytest provides several fixtures that give you direct access to the captured output inside your tests. These fixtures are especially useful when you need to verify that the correct output was produced.

### 6.1 `capsys` and `capsysbinary`

- **`capsys`**: Captures output from `sys.stdout` and `sys.stderr` as text.
- **`capsysbinary`**: Captures output as bytes (useful for binary data).

Both fixtures have a `readouterr()` method that returns a `namedtuple` with `out` and `err` attributes.

```python
def test_myoutput(capsys):
    print("hello")
    sys.stderr.write("world\n")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == "world\n"
    
    print("next")
    captured = capsys.readouterr()
    assert captured.out == "next\n"
```

Calling `readouterr()` consumes the captured output so far – subsequent calls will only see output produced after that point.

### 6.2 `capfd` and `capfdbinary`

- **`capfd`**: Captures output at the file descriptor level (text).
- **`capfdbinary`**: Captures output at the file descriptor level as bytes.

These fixtures are useful when the code under test writes directly to file descriptors (e.g., using `os.write()` or spawning subprocesses). Their interface is identical to `capsys`.

```python
import os

def test_subprocess_output(capfd):
    os.write(1, b"hello\n")
    captured = capfd.readouterr()
    assert captured.out == "hello\n"
```

### 6.3 Temporarily Disabling Capture

Sometimes you want to let output go through to the console during a specific part of a test, for example when debugging interactively. The capture fixtures provide a `disabled()` context manager for this purpose.

```python
def test_disabling_capturing(capsys):
    print("this output is captured")
    with capsys.disabled():
        print("output not captured, going directly to sys.stdout")
    print("this output is also captured")
```

Outside the context, capturing resumes normally.

---

## 7. Advanced Usage

### 7.1 Capturing Subprocess Output

When using the **fd** capturing mode (the default), output from subprocesses launched by your tests is also captured. This is because the subprocess inherits the file descriptors, and pytest intercepts writes to them.

Example:

```python
import subprocess

def test_subprocess_capture(capsys):
    subprocess.run(["echo", "hello"], capture_output=False)  # output goes to stdout
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
```

If you need to capture output from subprocesses separately, you can use `subprocess.run(..., capture_output=True)` and inspect the returned `CompletedProcess` object – but that will bypass pytest’s capture.

### 7.2 Interaction with Logging

pytest also captures logging output (by default, level `WARNING` and above). Logging messages appear in a separate “Captured stdlog” section. If you want to verify log messages alongside stdout/stderr, you can use the `caplog` fixture in combination with `capsys`.

### 7.3 Combining with the `-r` Flag

The `-r` flag controls the summary report. For example, `-rP` shows all passing tests that have captured output. This can be useful to review `print()` statements from passing tests when you need to see them for verification.

---

## 8. Best Practices

- **Use `print()` statements liberally for debugging** – they will only appear when the test fails, making them safe to leave in the code.
- **Prefer `capsys` over `capfd`** unless you specifically need to capture subprocess output. `capsys` is simpler and sufficient for most Python code.
- **Consume captured output with `readouterr()`** when you need to verify intermediate output. Remember that it clears the captured buffer.
- **Use `disabled()` context manager sparingly** – it should be used only when you need to interactively debug or when you intentionally want to see output during a test.
- **When testing subprocesses**, consider whether you want to capture their output via pytest (using fd mode) or handle it explicitly with `subprocess.run(..., capture_output=True)`.
- **In CI environments**, you may want to use `--capture=tee-sys` to see live output while still having it captured for reports.

---

## 9. Conclusion

pytest’s capturing system gives you fine‑grained control over how output is collected and displayed. By understanding the different capture methods, using the provided fixtures, and following best practices, you can effectively debug failing tests, verify console output, and maintain clean, informative test runs. These capabilities are essential for building robust automation test suites that interact with code that produces output to the console.

---
---
# Professional Automation Testing with pytest: Managing Warnings

## 1. Introduction

Warnings are an important part of software quality – they indicate potential issues without stopping execution. pytest provides comprehensive support for capturing, controlling, and asserting on warnings during test runs. This document covers all aspects of warning handling, from basic capture to advanced filtering, marking, and custom assertions, ensuring your test suites can verify that your code emits the correct warnings and remains clean of unexpected ones.

---

## 2. Automatic Warning Capture

Starting with pytest 3.1, pytest automatically captures warnings emitted during test execution and displays them at the end of the session. This includes warnings from both your code and third‑party libraries.

Consider a simple example:

```python
# test_show_warnings.py
import warnings

def api_v1():
    warnings.warn(UserWarning("api v1, should use functions from v2"))
    return 1

def test_one():
    assert api_v1() == 1
```

Running pytest produces:

```
$ pytest test_show_warnings.py
=========================== test session starts ============================
collected 1 item

test_show_warnings.py .                                              [100%]

============================= warnings summary =============================
test_show_warnings.py::test_one
  /home/sweet/project/test_show_warnings.py:5: UserWarning: api v1, should use functions from v2
    warnings.warn(UserWarning("api v1, should use functions from v2"))

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================= 1 passed, 1 warning in 0.12s =======================
```

The captured warnings are shown in a separate `warnings summary` section. The test passes, but the warning is reported.

---

## 3. Controlling Warnings with `-W` and `filterwarnings`

pytest allows you to control how warnings are treated using Python’s warning filter syntax, either via the command‑line `-W` option or the `filterwarnings` configuration option.

### 3.1 Command‑Line `-W`

The `-W` flag works like the Python interpreter’s `-W` option. For example, to turn any `UserWarning` into an error:

```bash
pytest -q test_show_warnings.py -W error::UserWarning
```

Output:

```
F                                                                    [100%]
================================= FAILURES =================================
_________________________________ test_one _________________________________
    ...
E       UserWarning: api v1, should use functions from v2
...
1 failed in 0.12s
```

The test now fails because the warning is raised as an exception.

### 3.2 Configuration File `filterwarnings`

You can set warning filters permanently in your `pytest.ini`, `pyproject.toml`, or `tox.ini` using the `filterwarnings` option. The order of filters matters – the last matching filter determines the action.

Example in `pytest.ini`:

```ini
[pytest]
filterwarnings =
    error
    ignore::UserWarning
    ignore:function ham\(\) is deprecated:DeprecationWarning
```

- `error`: treat all warnings as errors (highest precedence in this list)
- `ignore::UserWarning`: ignore all `UserWarning`s
- `ignore:function ham\(\) is deprecated:DeprecationWarning`: ignore deprecation warnings whose message starts with the given regex (note the escaping of parentheses)

In TOML (e.g., `pyproject.toml`), use an array of strings:

```toml
[tool.pytest.ini_options]
filterwarnings = [
    "error",
    "ignore::UserWarning",
    'ignore:function ham\(\) is deprecated:DeprecationWarning',
]
```

**Important:** The format of filters in `filterwarnings` differs slightly from the command‑line `-W`. Here, `message` is a regular expression that must match the *start* of the warning message (case‑insensitive). For more details, see the [warning filter documentation](https://docs.pytest.org/en/stable/reference/reference.html#confval-filterwarnings).

---

## 4. Per‑Test Warning Filters with `@pytest.mark.filterwarnings`

For fine‑grained control, you can apply warning filters to individual tests, classes, or modules using the `@pytest.mark.filterwarnings` marker.

### 4.1 Basic Usage

```python
import warnings
import pytest

def api_v1():
    warnings.warn(UserWarning("api v1, should use functions from v2"))
    return 1

@pytest.mark.filterwarnings("ignore:api v1")
def test_one():
    assert api_v1() == 1
```

Now the `UserWarning` is ignored only for this test.

### 4.2 Multiple Filters and Precedence

Filters are applied in the order the decorators are listed, but due to the way decorators are evaluated, **filters from earlier decorators take precedence over later ones**. This is the reverse of the traditional `warnings.filterwarnings` order.

Example:

```python
# Ignore "api v1" warnings, but fail on all other warnings
@pytest.mark.filterwarnings("ignore:api v1")
@pytest.mark.filterwarnings("error")
def test_one():
    assert api_v1() == 1
```

Here, the `ignore` filter is applied first (due to the outermost decorator), then the `error` filter. Since `ignore` matches, the warning is ignored and the test passes.

### 4.3 Applying to Classes and Modules

- **Class level**: decorate the class.

```python
@pytest.mark.filterwarnings("error")
class TestWarnings:
    def test_one(self):
        ...
```

- **Module level**: set the `pytestmark` variable.

```python
pytestmark = pytest.mark.filterwarnings("error")
```

If you need multiple filters at module level, assign a list (using the traditional `filterwarnings` order, where later filters take precedence):

```python
pytestmark = [
    pytest.mark.filterwarnings("ignore:api v1"),
    pytest.mark.filterwarnings("error"),
]
```

In this case, `error` comes after `ignore`, so it will be applied last and therefore take precedence, making warnings errors (unless `ignore` already matched).

**Note:** Filters applied via marks take precedence over those from command line or configuration.

---

## 5. Disabling Warnings Summary

You can suppress the warnings summary entirely with the `--disable-warnings` flag:

```bash
pytest --disable-warnings
```

This hides the summary, but warnings are still captured and can be accessed via other means.

---

## 6. Disabling Warning Capture Entirely

If you prefer to handle warnings yourself or use an external system, you can disable pytest’s warning capture plugin entirely:

```bash
pytest -p no:warnings
```

Or in the configuration:

```ini
[pytest]
addopts = -p no:warnings
```

---

## 7. Handling Deprecation Warnings

pytest displays `DeprecationWarning` and `PendingDeprecationWarning` from user code and third‑party libraries by default, following [PEP 565](https://peps.python.org/pep-0565/). This helps keep your code modern.

However, when you explicitly capture warnings (e.g., with `pytest.warns()` or `recwarn`), the warnings are not displayed – they are consumed by your test.

If you need to suppress specific deprecation warnings (e.g., from a library you cannot change), use warning filters:

```ini
[pytest]
filterwarnings = ignore:.*U.*mode is deprecated:DeprecationWarning
```

### 7.1 Checking for Deprecation Warnings

Use `pytest.deprecated_call()` to assert that a block of code triggers a deprecation warning:

```python
import pytest

def test_myfunction_deprecated():
    with pytest.deprecated_call():
        myfunction(17)
```

This fails if `myfunction(17)` does not issue a `DeprecationWarning` or `PendingDeprecationWarning`.

---

## 8. Asserting Warnings with `pytest.warns`

The `pytest.warns()` context manager allows you to assert that a specific warning (or any warning) is raised.

### 8.1 Basic Usage

```python
import warnings
import pytest

def test_warning():
    with pytest.warns(UserWarning):
        warnings.warn("my warning", UserWarning)
```

If the expected warning is not raised, the test fails.

### 8.2 Matching the Message

Use the `match` parameter to check the warning message against a regex or a literal string (escaping is your responsibility):

```python
with pytest.warns(UserWarning, match="must be 0 or None"):
    warnings.warn("value must be 0 or None", UserWarning)

# Using regex
with pytest.warns(UserWarning, match=r"must be \d+$"):
    warnings.warn("value must be 42", UserWarning)

# Escape literal regex characters
import re
with pytest.warns(UserWarning, match=re.escape("issue with foo() func")):
    warnings.warn("issue with foo() func")
```

### 8.3 Accessing Raised Warnings

`pytest.warns()` returns a `WarningsRecorder` (list‑like) containing all warnings raised during the block:

```python
with pytest.warns(RuntimeWarning) as record:
    warnings.warn("another warning", RuntimeWarning)

assert len(record) == 1
assert record[0].message.args[0] == "another warning"
```

If you don’t care about the warning type, you can omit the argument to capture all warnings:

```python
with pytest.warns() as record:
    warnings.warn("user", UserWarning)
    warnings.warn("runtime", RuntimeWarning)

assert len(record) == 2
```

### 8.4 Using `pytest.warns` as a Function Call

You can also call `pytest.warns` with a function and its arguments:

```python
pytest.warns(UserWarning, my_function, arg1, arg2)
```

Or with a code string:

```python
pytest.warns(UserWarning, "my_function(arg1, arg2)")
```

---

## 9. Recording Warnings with the `recwarn` Fixture

The `recwarn` fixture records warnings emitted during the entire test function, providing a `WarningsRecorder` instance.

```python
import warnings
import pytest

def test_hello(recwarn):
    warnings.warn("hello", UserWarning)
    assert len(recwarn) == 1
    w = recwarn.pop(UserWarning)   # remove the first UserWarning from the list
    assert issubclass(w.category, UserWarning)
    assert str(w.message) == "hello"
```

The `recwarn` fixture automatically resets the warning filter after the test, preventing leakage.

**Note:** The `WarningsRecorder` returned by both `pytest.warns()` and `recwarn` offers the same interface.

---

## 10. Custom Failure Messages

When using `pytest.warns()`, you can produce custom failure messages if no warnings are issued:

```python
def test():
    with pytest.warns(Warning) as record:
        f()
        if not record:
            pytest.fail("Expected a warning!")
```

This can be useful when you need to provide more context than the default failure message.

---

## 11. Advanced: Ensuring Only Certain Warnings Are Issued

To ensure that exactly one warning of a specific type is raised and no others, combine `recwarn` with assertions:

```python
def test_warning(recwarn):
    # ... code that may produce warnings ...
    assert len(recwarn) == 1
    user_warning = recwarn.pop(UserWarning)
    assert issubclass(user_warning.category, UserWarning)
```

To verify that **no** warnings are emitted, you can temporarily turn warnings into errors:

```python
def test_no_warnings():
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        # ... code that should not warn ...
```

Alternatively, use `recwarn` and assert `len(recwarn) == 0`.

---

## 12. Internal pytest Warnings

pytest itself may emit warnings in certain situations, such as:

- A test class with an `__init__` method (prevents collection).
- Deprecated features used in your test code.

These warnings are captured and displayed just like user warnings. They can be filtered using the same mechanisms (e.g., `filterwarnings`). See the [Backwards Compatibility Policy](https://docs.pytest.org/en/stable/deprecations.html) for details on deprecations.

---

## 13. Resource Warnings

`ResourceWarning` (e.g., unclosed files) can be especially useful for detecting leaks. To get more information about where a resource was created, enable `tracemalloc`:

```bash
PYTHONTRACEMALLOC=20 pytest
```

This will include a traceback pointing to the allocation site in the warning output. Consult the [Python Development Mode](https://docs.python.org/3/library/devmode.html) documentation for more details.

---

## 14. Best Practices

- **Use `pytest.warns()`** to verify that your code emits the expected warnings. This ensures that deprecated or unusual conditions are properly signaled.
- **Apply warning filters at the module or class level** to avoid repeating the same filter on every test.
- **Prefer `pytest.mark.filterwarnings` over command‑line flags** for per‑test control.
- **Enable `tracemalloc`** in CI when debugging resource leaks.
- **Do not ignore all warnings** globally; it hides real problems. Instead, selectively ignore known false positives.
- **Use `--disable-warnings`** only when you are confident the warnings are irrelevant and you want a cleaner output.
- **Combine `recwarn` with assertions** to enforce strict warning policies (e.g., “no warnings allowed”).
- **Keep warning filters well‑documented** in your configuration to explain why they are present.

---

## 15. Conclusion

pytest’s warning handling features give you complete control over how warnings are captured, displayed, and asserted. Whether you need to check for expected deprecations, enforce a “no warnings” policy, or simply silence harmless third‑party messages, the tools described here allow you to integrate warning management seamlessly into your test suite. By mastering these capabilities, you can ensure your code stays clean, modern, and reliable.