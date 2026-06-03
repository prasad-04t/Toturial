# Professional Automation Testing with pytest: Managing Output

## 1. Introduction

pytest provides extensive control over how test results are displayed, from fine‑tuning traceback details to generating machine‑readable reports and even sharing failure information via pastebin. This document covers all output‑related features, enabling automation engineers to tailor pytest’s reporting for both interactive debugging and CI/CD integration.

## 2. Modifying Python Traceback Printing

pytest offers several command‑line options to adjust the amount of information shown when a test fails.

### 2.1 Local Variables in Tracebacks

- `--showlocals` (or `-l`): Show local variables in tracebacks.
- `--no-showlocals`: Hide local variables (useful if enabled by default in `addopts`).

```bash
pytest --showlocals      # or pytest -l
pytest --no-showlocals
```

### 2.2 Capturing Output

pytest captures stdout and stderr by default. You can control this with the `--capture` option:

- `--capture=fd`: Capture at the file descriptor level (default).
- `--capture=sys`: Capture at the sys level (stdout/stderr).
- `--capture=no`: Disable capturing entirely (shortcut: `-s`).
- `--capture=tee-sys`: Capture to logs but also output to sys level streams.

```bash
pytest --capture=no       # equivalent to pytest -s
pytest --capture=tee-sys  # see output while also capturing
```

### 2.3 Traceback Format

The `--tb` option controls traceback style:

- `--tb=auto`: Default. ‘long’ tracebacks for the first and last failure, ‘short’ for others.
- `--tb=long`: Exhaustive, informative traceback formatting.
- `--tb=short`: Shorter traceback format.
- `--tb=line`: Only one line per failure.
- `--tb=native`: Use Python’s standard library formatting (no pytest introspection).
- `--tb=no`: No traceback at all.

```bash
pytest --tb=short
pytest --tb=line
```

### 2.4 Full Traceback

The `--full-trace` option prints extremely long traces on error (even longer than `--tb=long`). It also ensures a stack trace is printed on `KeyboardInterrupt` (Ctrl+C), which is useful for debugging hung tests.

```bash
pytest --full-trace
```

## 3. Verbosity

The `-v` (verbose) flag increases the level of detail in the output. Multiple `v`s increase verbosity further.

- `-q` or `--quiet`: Reduce verbosity.
- `-v`: Increase verbosity; display individual test names.
- `-vv`: More verbose; show more details from test output (e.g., full diffs).
- `-vvv`: Even higher verbosity (may be used by plugins).

### 3.1 Effect of Verbosity on Failure Reports

Consider a test file with various failures. The following examples illustrate how verbosity changes the output.

**Normal (`pytest --no-header`):**

```
test_verbosity_example.py .FFF                                       [100%]
================================= FAILURES =================================
_____________________________ test_words_fail ______________________________
    ...
E         At index 2 diff: 'grapes' != 'orange'
E         Use -v to get more diff
____________________________ test_numbers_fail _____________________________
    ...
E         Omitting 1 identical items, use -vv to show
E         Left contains 4 more items: ...
___________________________ test_long_text_fail ____________________________
    ...
E       AssertionError: assert 'hello world' in 'Lorem ipsum...'
```

**Verbose (`-v`):**

Each test gets its own line, and diffs are more detailed (but still truncated).

```
test_verbosity_example.py::test_ok PASSED                            [ 25%]
test_verbosity_example.py::test_words_fail FAILED                    [ 50%]
...
E         At index 2 diff: 'grapes' != 'orange'
E
E         Full diff:
E           [
E               'banana',
E               'apple',...
E
E         ...Full output truncated (7 lines hidden), use '-vv' to show
```

**Very verbose (`-vv`):**

Diffs are shown in full, without truncation.

```
E         Full diff:
E           [
E               'banana',
E               'apple',
E         -     'orange',
E         ?      ^  ^^
E         +     'grapes',
E         ?      ^  ^ +
E               'melon',
E               'kiwi',
E           ]
```

The verbosity level also affects other outputs, such as `--fixtures` (where `-v` shows fixtures with leading underscores).

## 4. Fine‑Grained Verbosity

Instead of setting a global verbosity level, you can control specific aspects via configuration options:

- `verbosity_assertions`: Controls how verbose assertion output is.
- `verbosity_test_cases`: Controls how verbose test execution output is.

For example, to get the detailed diffs of `-vv` without showing each test name individually, you could set:

```ini
[pytest]
verbosity_assertions = 2
verbosity_test_cases = 0
```

Values are integers, where higher numbers mean more detail.

## 5. Producing a Detailed Summary Report

The `-r` option displays a “short test summary info” at the end of the session. It accepts a string of characters indicating which test outcomes to include.

Available characters:

- `f` – failed
- `E` – error
- `s` – skipped
- `x` – xfailed
- `X` – xpassed
- `p` – passed
- `P` – passed with output
- `a` – all except `pP`
- `A` – all
- `N` – none (overrides default `fE`)

Multiple characters can be combined, e.g., `-rfs` to show failed and skipped.

Example:

```bash
pytest -ra          # show all except passes
pytest -rfs         # show failures and skips
pytest -rpP         # show passes (p) and passes with output (P)
```

**Note:** By default, parametrized variants of skipped tests are grouped together if they share the same skip reason. Use `--no-fold-skipped` to print each skipped test separately.

## 6. Modifying Truncation Limits

When displaying long diffs, pytest truncates output to avoid flooding the terminal. The default limits are 8 lines or 640 characters, whichever comes first.

You can adjust these limits in the configuration file:

```ini
[pytest]
truncation_limit_lines = 10
truncation_limit_chars = 90
```

Setting both values to `0` disables truncation entirely. Setting only one disables that truncation mode while leaving the other active.

## 7. Creating JUnitXML Format Files

To generate XML reports compatible with CI servers like Jenkins, use:

```bash
pytest --junit-xml=path/to/report.xml
```

### 7.1 Customizing the Test Suite Name

Set the root test suite name with `junit_suite_name`:

```ini
[pytest]
junit_suite_name = my_suite
```

### 7.2 Reporting Test Duration

By default, the `time` attribute in the XML includes setup and teardown times. To report only the call duration, configure:

```ini
[pytest]
junit_duration_report = call
```

### 7.3 Adding Custom Properties to Test Cases

Use the `record_property` fixture to add `<property>` elements inside a test case’s `<properties>` section.

```python
def test_function(record_property):
    record_property("example_key", 1)
    assert True
```

This yields:

```xml
<testcase ...>
  <properties>
    <property name="example_key" value="1"/>
  </properties>
</testcase>
```

You can also integrate with markers:

```python
# conftest.py
def pytest_collection_modifyitems(session, config, items):
    for item in items:
        for marker in item.iter_markers(name="test_id"):
            test_id = marker.args[0]
            item.user_properties.append(("test_id", test_id))
```

```python
# test_function.py
import pytest

@pytest.mark.test_id(1501)
def test_function():
    assert True
```

**Warning:** Adding custom properties may break JUnitXML schema validation in some CI tools.

### 7.4 Adding Custom Attributes to the Test Case Element

Use the `record_xml_attribute` fixture to add (or override) attributes on the `<testcase>` element.

```python
def test_function(record_xml_attribute):
    record_xml_attribute("assertions", "REQ-1234")
    record_xml_attribute("classname", "custom_classname")
    assert True
```

Result:

```xml
<testcase assertions="REQ-1234" classname="custom_classname" ... />
```

**Warning:** This may also break schema validation; use with caution.

### 7.5 Adding Properties at the Test Suite Level

The session‑scoped `record_testsuite_property` fixture allows adding `<property>` tags under the `<testsuite>` element.

```python
import pytest

@pytest.fixture(scope="session", autouse=True)
def log_global_env_facts(record_testsuite_property):
    record_testsuite_property("ARCH", "PPC")
    record_testsuite_property("STORAGE_TYPE", "CEPH")
```

Generated XML:

```xml
<testsuite ...>
  <properties>
    <property name="ARCH" value="PPC"/>
    <property name="STORAGE_TYPE" value="CEPH"/>
  </properties>
  ...
</testsuite>
```

This is compatible with the latest xunit standard.

## 8. Sending Test Reports to an Online Pastebin Service

pytest can upload test run information to `https://bpaste.net/` and provide a URL.

- `--pastebin=failed`: Create a paste for each failed test.
- `--pastebin=all`: Create a paste for the entire session log.

```bash
pytest --pastebin=failed
pytest --pastebin=all
```

If the paste creation fails, a warning is emitted instead of failing the test suite.

## 9. Best Practices

- **Use `-v` in local development** to see which tests are running.
- **Use `-x` or `--maxfail` with `--tb=short`** to quickly iterate on failures.
- **Set `--full-trace` when debugging hanging tests** to capture a traceback on Ctrl+C.
- **Generate JUnit XML in CI pipelines** for integration with reporting tools.
- **Leverage `-r` to get a concise summary** of non‑passing tests.
- **Disable truncation only when needed** (e.g., in CI logs) by setting limits to 0.
- **Use `record_testsuite_property`** to provide environment metadata in the XML report.

## 10. Conclusion

Mastering pytest’s output control is essential for effective test automation. Whether you need detailed failure introspection, machine‑readable reports, or quick summaries, the options described above give you the flexibility to adapt pytest’s output to your workflow and infrastructure. By integrating these features into your test suites, you can improve debugging efficiency and ensure seamless integration with CI/CD systems.