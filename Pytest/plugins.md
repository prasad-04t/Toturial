# Professional Automation Testing with pytest: Installing and Using Plugins

## 1. Introduction

pytest’s functionality can be extended through a rich ecosystem of third‑party plugins. These plugins add capabilities such as code coverage reporting, parallel test execution, Django integration, BDD support, and many others. This document explains how to install, manage, and configure plugins, as well as how to control their loading and unloading. Mastering plugin usage is essential for building a test automation framework that leverages the full power of the pytest ecosystem.

---

## 2. Installing a Third‑Party Plugin

Plugins are Python packages distributed via PyPI. They can be installed using `pip`:

```bash
pip install pytest-NAME
```

To uninstall a plugin:

```bash
pip uninstall pytest-NAME
```

Once installed, pytest automatically discovers and integrates the plugin – no additional activation is required. The plugin becomes available in your test runs.

---

## 3. Popular Plugins

Here is a selection of widely used pytest plugins:

| Plugin | Description |
|--------|-------------|
| **pytest-django** | Write tests for Django applications with pytest integration. |
| **pytest-twisted** | Test Twisted applications; starts a reactor and processes deferreds. |
| **pytest-cov** | Code coverage reporting (compatible with distributed testing). |
| **pytest-xdist** | Distribute tests to CPUs and remote hosts; supports `boxed` mode (survive segmentation faults) and `looponfailing` mode (auto‑rerun failing tests on file changes). |
| **pytest-instafail** | Report test failures immediately as they occur, not only at the end. |
| **pytest-bdd** | Write tests using behavior‑driven development (BDD) with Gherkin syntax. |
| **pytest-timeout** | Timeout tests based on function markers or global settings. |
| **pytest-pep8** | Add a `--pep8` option to check PEP8 compliance. |
| **pytest-flakes** | Check source code with pyflakes. |
| **allure-pytest** | Generate test reports compatible with the Allure Framework. |

For a complete, up‑to‑date list of plugins with testing status against various pytest and Python versions, visit the [Pytest Plugin List](https://docs.pytest.org/en/stable/reference/plugin_list.html) or search on [PyPI](https://pypi.org/search/?q=pytest-).

---

## 4. Requiring Plugins in a Test Module or conftest File

You can force the loading of specific plugins within a test module or a `conftest.py` file by declaring a `pytest_plugins` variable:

```python
pytest_plugins = ("myapp.testsupport.myplugin",)
```

When the module or `conftest` is loaded, the listed plugins will be loaded as well. This is useful when a test suite depends on a custom plugin that must always be present.

**Important:** Using `pytest_plugins` in non‑root `conftest.py` files is deprecated. It is recommended to place such declarations only in the **root** `conftest.py` or in a plugin module.

**Reserved name:** `pytest_plugins` is a reserved name and should not be used for anything else.

---

## 5. Finding Out Which Plugins Are Active

To see a list of active plugins and their names, run:

```bash
pytest --trace-config
```

This outputs an extended test header that shows all activated plugins, including local plugins (i.e., `conftest.py` files) and their load status.

---

## 6. Deactivating / Unregistering a Plugin by Name

Sometimes you may need to prevent a plugin from being loaded. Use the `-p no:NAME` option:

```bash
pytest -p no:NAME
```

This prevents the plugin with the given name from being activated. To disable a plugin permanently for a project, add this option to the `addopts` line in your configuration file (e.g., `pytest.ini`):

```ini
[pytest]
addopts = -p no:NAME
```

Alternatively, you can set the `PYTEST_ADDOPTS` environment variable to include `-p no:NAME`, which allows conditional disabling in CI environments.

To find the exact name of a plugin (e.g., for `pytest-xdist`, the name might be `xdist`), use `pytest --trace-config` and look for the plugin name in the output.

---

## 7. Disabling Plugin Autoloading

Normally, pytest automatically loads all installed plugins. Starting with pytest 8.4, you can disable this automatic loading and instead manually specify which plugins to load.

- Use the `--disable-plugin-autoload` command‑line flag, or
- Set the environment variable `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1`.

When autoload is disabled, only plugins listed in `PYTEST_PLUGINS` (or passed via `-p` on the command line) are loaded.

Examples:

```bash
export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
export PYTEST_PLUGINS=NAME,NAME2
pytest
```

Or with command‑line:

```bash
pytest --disable-plugin-autoload -p NAME -p NAME2
```

You can also specify this in your configuration file:

```ini
[pytest]
addopts =
    --disable-plugin-autoload
    -p NAME
    -p NAME2
```

This is useful when you want to ensure that only a specific set of plugins is active, reducing the chance of interference from other installed plugins.

---

## 8. Plugin Lifecycle and Compatibility

- **Version compatibility**: Always check a plugin’s documentation for supported pytest versions. Some plugins may lag behind new pytest releases.
- **Upgrading plugins**: Regularly update plugins with `pip install -U pytest-NAME` to benefit from bug fixes and new features.
- **Uninstalling**: If you no longer need a plugin, uninstall it to avoid any unintended side effects.

---

## 9. Best Practices

- **Document plugin dependencies**: In your project’s documentation, list the plugins required and their versions (e.g., in a `requirements.txt` or `pyproject.toml`).
- **Use `pytest --trace-config`** to verify which plugins are loaded, especially in CI environments.
- **Prefer `addopts`** in `pytest.ini` for disabling plugins that should never be used in your project.
- **When writing reusable test harnesses**, consider using `pytest_plugins` in the root `conftest.py` to enforce the presence of necessary plugins.
- **Be cautious with plugin autoload** in large teams: if many plugins are installed globally, consider disabling autoload and explicitly listing only the required ones to avoid conflicts.
- **Test plugin interactions**: When using multiple plugins, verify that they work together (e.g., `pytest-xdist` and `pytest-cov`).

---

## 10. Conclusion

Plugins are a key reason for pytest’s success. They allow you to extend the framework to meet almost any testing need. By understanding how to install, manage, and control plugins, you can build a powerful, tailored test automation environment. Following the practices outlined in this document will help you maintain a clean, predictable test suite that leverages the best of the pytest ecosystem.

---
---

# Professional Automation Testing with pytest: Writing Plugins

## 1. Introduction

pytest’s extensibility is one of its greatest strengths. Plugins allow you to add custom functionality, modify test behavior, integrate with external systems, and share reusable components across projects. Plugins can be as simple as a local `conftest.py` file in your project or as complex as a distributable Python package. This document provides a comprehensive guide to writing pytest plugins, covering plugin discovery, implementation, packaging, assertion rewriting, and testing with the `pytester` fixture.

---

## 2. Plugin Overview

A pytest plugin is essentially a Python module that implements one or more **hook functions**. Hooks are the points where pytest allows plugins to intervene in the testing process – from configuration and collection to execution and reporting. All hooks follow the naming convention `pytest_*`, making them easy to identify.

pytest loads plugins from three sources:

- **Builtin plugins**: Internal plugins located in pytest’s `_pytest` directory.
- **External plugins**: Third‑party packages installed via `pip` that expose themselves through entry points.
- **`conftest.py` plugins**: Modules discovered in test directories (local per‑directory plugins).

---

## 3. Plugin Discovery Order at Tool Startup

The order in which plugins are loaded is important because later hooks can override earlier ones. pytest loads plugins in the following sequence:

1. **Command‑line blocking** – Scans for `-p no:name` options and blocks those plugins (including builtins).
2. **Builtin plugins** – All internal plugins are loaded.
3. **Explicit loading** – Scans for `-p name` options and loads those plugins (before normal parsing).
4. **Entry point plugins** – Loads all plugins registered via the `pytest11` entry point (unless `PYTEST_DISABLE_PLUGIN_AUTOLOAD` is set).
5. **Environment variable plugins** – Loads plugins listed in the `PYTEST_PLUGINS` environment variable.
6. **`conftest.py` files** – Loads initial `conftest.py` files:
   - Determine test paths (from command line, `testpaths` config, or current directory).
   - For each test path, load `conftest.py` in that directory and all parent directories.
   - Before loading a `conftest.py`, load its parent `conftest.py`s.
   - After loading a `conftest.py`, recursively load any plugins specified in its `pytest_plugins` variable.

This order ensures that local `conftest.py` hooks can override or extend global plugin behavior.

---

## 4. Local Plugins with `conftest.py`

A `conftest.py` file placed in a test directory acts as a local plugin. It can contain fixtures, hooks, and markers that apply only to tests in that directory and its subdirectories. Hooks defined in a `conftest.py` closer to the test file take precedence over those in higher‑level directories.

Example:

```
a/
├── conftest.py          # defines pytest_runtest_setup
└── test_sub.py          # test in a/
test_flat.py             # test in root
```

```python
# a/conftest.py
def pytest_runtest_setup(item):
    print("setting up", item)
```

Running:

```bash
pytest test_flat.py --capture=no      # no output from hook
pytest a/test_sub.py --capture=no     # prints "setting up ..."
```

**Important:** Avoid placing `conftest.py` outside a package if you plan to import from it; otherwise, import ambiguity may occur. It is good practice to either keep `conftest.py` inside a package or never import from it directly.

---

## 5. Writing Your Own Plugin

### 5.1 Basic Structure

A plugin can be a single Python file or a package. At minimum, it contains one or more hook implementations. For example:

```python
# myplugin.py
def pytest_configure(config):
    """Called after command line options have been parsed."""
    config.addinivalue_line("markers", "custom: my custom marker")
```

To use this plugin locally, place it in your project and load it via `-p myplugin` or by including it in `pytest_plugins`.

### 5.2 Using Hooks

The full list of hooks is documented in the [pytest API reference](https://docs.pytest.org/en/stable/reference/reference.html#hooks). Common hooks include:

- `pytest_addoption` – Add command‑line options.
- `pytest_configure` – Perform configuration after options are parsed.
- `pytest_collection_modifyitems` – Modify collected tests (e.g., add markers).
- `pytest_runtest_protocol` – Control test execution.
- `pytest_runtest_call` – Wrap the test call.
- `pytest_runtest_makereport` – Modify test reports.

### 5.3 Making Your Plugin Installable

To distribute your plugin, you need to define a **package** with a proper `pyproject.toml` (or `setup.py`) that includes an entry point under `pytest11`. This tells pytest where to find your plugin.

Example `pyproject.toml`:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "myproject"
classifiers = [
    "Framework :: Pytest",
]

[project.entry-points.pytest11]
myplugin = "myproject.pluginmodule"
```

After installation (e.g., `pip install -e .`), pytest will automatically load `myproject.pluginmodule` as a plugin. Verify with `pytest --trace-config`.

**Note:** Include `Framework :: Pytest` in your PyPI classifiers to help users discover your plugin.

---

## 6. Assertion Rewriting

One of pytest’s core features is the rewriting of `assert` statements to provide detailed failure reports. This rewriting is performed via an import hook that modifies the AST of modules before they are compiled. The hook is applied only to:

- Test modules (as defined by `python_files`).
- Modules that are part of plugins (i.e., modules listed in `pytest11` entry points or loaded via `pytest_plugins`).
- Any module explicitly registered with `pytest.register_assert_rewrite()`.

If your plugin contains helper modules that contain `assert` statements and you want them rewritten, you must register them before they are imported. This is typically done in the plugin’s `__init__.py`:

```python
# myplugin/__init__.py
import pytest
pytest.register_assert_rewrite("myplugin.helper")
```

Now when `myplugin.helper` is imported, its `assert` statements will be rewritten.

---

## 7. Requiring/Loading Plugins in a Test Module or conftest

You can specify that a plugin should be loaded when a test module or `conftest.py` is loaded by using the `pytest_plugins` variable:

```python
pytest_plugins = ["name1", "name2"]
```

This can be placed in a test module, `conftest.py`, or even a plugin module. The plugins are loaded recursively (if they themselves declare `pytest_plugins`).

**Deprecation:** Using `pytest_plugins` in a **non‑root** `conftest.py` is deprecated. To avoid confusion, only use it in the root `conftest.py` (located at the top of your test directory) or in plugin modules.

Plugins loaded via `pytest_plugins` are automatically marked for assertion rewriting, but only if they haven’t been imported earlier. To ensure rewriting works, call `pytest.register_assert_rewrite()` before importing the module, or structure your code to delay the import.

---

## 8. Accessing Another Plugin by Name

Sometimes a plugin needs to interact with another plugin. You can obtain a reference to a loaded plugin using the plugin manager:

```python
def pytest_configure(config):
    other = config.pluginmanager.get_plugin("name_of_plugin")
    if other:
        # use other plugin's features
```

Use `pytest --trace-config` to see the names of loaded plugins.

---

## 9. Registering Custom Markers

If your plugin introduces custom markers, you should register them in `pytest_configure` to avoid warnings and to make them appear in `pytest --markers` output.

```python
def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "cool_marker: this one is for cool tests."
    )
    config.addinivalue_line(
        "markers",
        "mark_with(arg, arg2): this marker takes arguments."
    )
```

---

## 10. Testing Plugins with `pytester`

pytest includes the `pytester` plugin specifically for testing other plugins. It provides fixtures and utilities to create temporary test files, run pytest in an isolated environment, and inspect results.

### 10.1 Enabling `pytester`

Add to your test suite’s `conftest.py`:

```python
pytest_plugins = ["pytester"]
```

Or invoke pytest with `-p pytester` when testing your plugin.

### 10.2 Using the `pytester` Fixture

The `pytester` fixture provides methods to create temporary `conftest.py` and test files, and to run pytest on them.

Example test for a plugin that adds a `hello` fixture:

```python
def test_hello(pytester):
    # Create a temporary conftest.py with a parametrized fixture
    pytester.makeconftest(
        """
        import pytest

        @pytest.fixture(params=["Brianna", "Andreas", "Floris"])
        def name(request):
            return request.param
        """
    )

    # Create a test file that uses the hello fixture (provided by our plugin)
    pytester.makepyfile(
        """
        def test_hello_default(hello):
            assert hello() == "Hello World!"

        def test_hello_name(hello, name):
            assert hello(name) == "Hello {0}!".format(name)
        """
    )

    # Run pytest on the temporary directory
    result = pytester.runpytest()

    # Assert that all 4 tests passed
    result.assert_outcomes(passed=4)
```

### 10.3 Using `copy_example` for Reusable Examples

For longer test files, you can store them as examples in your source tree and copy them into the temporary environment using `pytester.copy_example`. To enable this, set the `pytester_example_dir` option in your configuration file (e.g., `pytest.toml`):

```toml
[tool.pytest.ini_options]
pytester_example_dir = "."
```

Then in your test:

```python
def test_plugin(pytester):
    pytester.copy_example("test_example.py")
    result = pytester.runpytest("-k", "test_example")
    result.assert_outcomes(passed=1)
```

### 10.4 `RunResult` API

The `result` object returned by `pytester.runpytest()` is an instance of `RunResult` with useful methods:

- `result.assert_outcomes(passed=..., failed=..., skipped=..., xfailed=..., xpassed=..., errors=...)`
- `result.ret` – exit code of the pytest run.
- `result.parseoutcomes()` – returns a dictionary of outcome counts.
- `result.stdout`, `result.stderr` – captured output.

For a full reference, see the [pytester documentation](https://docs.pytest.org/en/stable/reference/reference.html#pytester).

---

## 11. Best Practices for Plugin Development

- **Start with a cookiecutter**: Use [cookiecutter-pytest-plugin](https://github.com/pytest-dev/cookiecutter-pytest-plugin) to generate a well‑structured plugin project.
- **Keep it focused**: A plugin should do one thing well. If you need multiple features, consider splitting them into separate plugins or modules.
- **Provide comprehensive documentation**: Include a README with installation instructions, usage examples, and a list of hooks/markers.
- **Write tests**: Use `pytester` to test your plugin’s behavior in isolation.
- **Register markers**: Always register custom markers to avoid warnings and improve discoverability.
- **Be mindful of import side effects**: Use `pytest.register_assert_rewrite` before importing modules that need assertion rewriting.
- **Use `--trace-config`** during development to verify your plugin is loaded correctly.
- **Consider compatibility**: Test your plugin against multiple pytest versions and Python versions (use `tox` or GitHub Actions).
- **Release to PyPI** with the `Framework :: Pytest` classifier to help users find it.

---

## 12. Conclusion

Writing pytest plugins is a powerful way to extend the testing framework to suit your project’s unique needs. Whether you create a simple local `conftest.py` or a full‑fledged installable package, understanding the plugin architecture, hook system, and testing tools will enable you to build robust, reusable automation components. By following the guidelines and best practices outlined here, you can contribute to the rich ecosystem of pytest plugins and enhance the testing capabilities of your organization.
---
---
# Professional Automation Testing with pytest: Writing Plugins

## 1. Introduction

pytest’s extensibility is one of its greatest strengths. Plugins allow you to add custom functionality, modify test behavior, integrate with external systems, and share reusable components across projects. Plugins can be as simple as a local `conftest.py` file in your project or as complex as a distributable Python package. This document provides a comprehensive guide to writing pytest plugins, covering plugin discovery, implementation, packaging, assertion rewriting, and testing with the `pytester` fixture.

---

## 2. Plugin Overview

A pytest plugin is essentially a Python module that implements one or more **hook functions**. Hooks are the points where pytest allows plugins to intervene in the testing process – from configuration and collection to execution and reporting. All hooks follow the naming convention `pytest_*`, making them easy to identify.

pytest loads plugins from three sources:

- **Builtin plugins**: Internal plugins located in pytest’s `_pytest` directory.
- **External plugins**: Third‑party packages installed via `pip` that expose themselves through entry points.
- **`conftest.py` plugins**: Modules discovered in test directories (local per‑directory plugins).

---

## 3. Plugin Discovery Order at Tool Startup

The order in which plugins are loaded is important because later hooks can override earlier ones. pytest loads plugins in the following sequence:

1. **Command‑line blocking** – Scans for `-p no:name` options and blocks those plugins (including builtins).
2. **Builtin plugins** – All internal plugins are loaded.
3. **Explicit loading** – Scans for `-p name` options and loads those plugins (before normal parsing).
4. **Entry point plugins** – Loads all plugins registered via the `pytest11` entry point (unless `PYTEST_DISABLE_PLUGIN_AUTOLOAD` is set).
5. **Environment variable plugins** – Loads plugins listed in the `PYTEST_PLUGINS` environment variable.
6. **`conftest.py` files** – Loads initial `conftest.py` files:
   - Determine test paths (from command line, `testpaths` config, or current directory).
   - For each test path, load `conftest.py` in that directory and all parent directories.
   - Before loading a `conftest.py`, load its parent `conftest.py`s.
   - After loading a `conftest.py`, recursively load any plugins specified in its `pytest_plugins` variable.

This order ensures that local `conftest.py` hooks can override or extend global plugin behavior.

---

## 4. Local Plugins with `conftest.py`

A `conftest.py` file placed in a test directory acts as a local plugin. It can contain fixtures, hooks, and markers that apply only to tests in that directory and its subdirectories. Hooks defined in a `conftest.py` closer to the test file take precedence over those in higher‑level directories.

Example:

```
a/
├── conftest.py          # defines pytest_runtest_setup
└── test_sub.py          # test in a/
test_flat.py             # test in root
```

```python
# a/conftest.py
def pytest_runtest_setup(item):
    print("setting up", item)
```

Running:

```bash
pytest test_flat.py --capture=no      # no output from hook
pytest a/test_sub.py --capture=no     # prints "setting up ..."
```

**Important:** Avoid placing `conftest.py` outside a package if you plan to import from it; otherwise, import ambiguity may occur. It is good practice to either keep `conftest.py` inside a package or never import from it directly.

---

## 5. Writing Your Own Plugin

### 5.1 Basic Structure

A plugin can be a single Python file or a package. At minimum, it contains one or more hook implementations. For example:

```python
# myplugin.py
def pytest_configure(config):
    """Called after command line options have been parsed."""
    config.addinivalue_line("markers", "custom: my custom marker")
```

To use this plugin locally, place it in your project and load it via `-p myplugin` or by including it in `pytest_plugins`.

### 5.2 Using Hooks

The full list of hooks is documented in the [pytest API reference](https://docs.pytest.org/en/stable/reference/reference.html#hooks). Common hooks include:

- `pytest_addoption` – Add command‑line options.
- `pytest_configure` – Perform configuration after options are parsed.
- `pytest_collection_modifyitems` – Modify collected tests (e.g., add markers).
- `pytest_runtest_protocol` – Control test execution.
- `pytest_runtest_call` – Wrap the test call.
- `pytest_runtest_makereport` – Modify test reports.

### 5.3 Making Your Plugin Installable

To distribute your plugin, you need to define a **package** with a proper `pyproject.toml` (or `setup.py`) that includes an entry point under `pytest11`. This tells pytest where to find your plugin.

Example `pyproject.toml`:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "myproject"
classifiers = [
    "Framework :: Pytest",
]

[project.entry-points.pytest11]
myplugin = "myproject.pluginmodule"
```

After installation (e.g., `pip install -e .`), pytest will automatically load `myproject.pluginmodule` as a plugin. Verify with `pytest --trace-config`.

**Note:** Include `Framework :: Pytest` in your PyPI classifiers to help users discover your plugin.

---

## 6. Assertion Rewriting

One of pytest’s core features is the rewriting of `assert` statements to provide detailed failure reports. This rewriting is performed via an import hook that modifies the AST of modules before they are compiled. The hook is applied only to:

- Test modules (as defined by `python_files`).
- Modules that are part of plugins (i.e., modules listed in `pytest11` entry points or loaded via `pytest_plugins`).
- Any module explicitly registered with `pytest.register_assert_rewrite()`.

If your plugin contains helper modules that contain `assert` statements and you want them rewritten, you must register them before they are imported. This is typically done in the plugin’s `__init__.py`:

```python
# myplugin/__init__.py
import pytest
pytest.register_assert_rewrite("myplugin.helper")
```

Now when `myplugin.helper` is imported, its `assert` statements will be rewritten.

---

## 7. Requiring/Loading Plugins in a Test Module or conftest

You can specify that a plugin should be loaded when a test module or `conftest.py` is loaded by using the `pytest_plugins` variable:

```python
pytest_plugins = ["name1", "name2"]
```

This can be placed in a test module, `conftest.py`, or even a plugin module. The plugins are loaded recursively (if they themselves declare `pytest_plugins`).

**Deprecation:** Using `pytest_plugins` in a **non‑root** `conftest.py` is deprecated. To avoid confusion, only use it in the root `conftest.py` (located at the top of your test directory) or in plugin modules.

Plugins loaded via `pytest_plugins` are automatically marked for assertion rewriting, but only if they haven’t been imported earlier. To ensure rewriting works, call `pytest.register_assert_rewrite()` before importing the module, or structure your code to delay the import.

---

## 8. Accessing Another Plugin by Name

Sometimes a plugin needs to interact with another plugin. You can obtain a reference to a loaded plugin using the plugin manager:

```python
def pytest_configure(config):
    other = config.pluginmanager.get_plugin("name_of_plugin")
    if other:
        # use other plugin's features
```

Use `pytest --trace-config` to see the names of loaded plugins.

---

## 9. Registering Custom Markers

If your plugin introduces custom markers, you should register them in `pytest_configure` to avoid warnings and to make them appear in `pytest --markers` output.

```python
def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "cool_marker: this one is for cool tests."
    )
    config.addinivalue_line(
        "markers",
        "mark_with(arg, arg2): this marker takes arguments."
    )
```

---

## 10. Testing Plugins with `pytester`

pytest includes the `pytester` plugin specifically for testing other plugins. It provides fixtures and utilities to create temporary test files, run pytest in an isolated environment, and inspect results.

### 10.1 Enabling `pytester`

Add to your test suite’s `conftest.py`:

```python
pytest_plugins = ["pytester"]
```

Or invoke pytest with `-p pytester` when testing your plugin.

### 10.2 Using the `pytester` Fixture

The `pytester` fixture provides methods to create temporary `conftest.py` and test files, and to run pytest on them.

Example test for a plugin that adds a `hello` fixture:

```python
def test_hello(pytester):
    # Create a temporary conftest.py with a parametrized fixture
    pytester.makeconftest(
        """
        import pytest

        @pytest.fixture(params=["Brianna", "Andreas", "Floris"])
        def name(request):
            return request.param
        """
    )

    # Create a test file that uses the hello fixture (provided by our plugin)
    pytester.makepyfile(
        """
        def test_hello_default(hello):
            assert hello() == "Hello World!"

        def test_hello_name(hello, name):
            assert hello(name) == "Hello {0}!".format(name)
        """
    )

    # Run pytest on the temporary directory
    result = pytester.runpytest()

    # Assert that all 4 tests passed
    result.assert_outcomes(passed=4)
```

### 10.3 Using `copy_example` for Reusable Examples

For longer test files, you can store them as examples in your source tree and copy them into the temporary environment using `pytester.copy_example`. To enable this, set the `pytester_example_dir` option in your configuration file (e.g., `pytest.toml`):

```toml
[tool.pytest.ini_options]
pytester_example_dir = "."
```

Then in your test:

```python
def test_plugin(pytester):
    pytester.copy_example("test_example.py")
    result = pytester.runpytest("-k", "test_example")
    result.assert_outcomes(passed=1)
```

### 10.4 `RunResult` API

The `result` object returned by `pytester.runpytest()` is an instance of `RunResult` with useful methods:

- `result.assert_outcomes(passed=..., failed=..., skipped=..., xfailed=..., xpassed=..., errors=...)`
- `result.ret` – exit code of the pytest run.
- `result.parseoutcomes()` – returns a dictionary of outcome counts.
- `result.stdout`, `result.stderr` – captured output.

For a full reference, see the [pytester documentation](https://docs.pytest.org/en/stable/reference/reference.html#pytester).

---

## 11. Best Practices for Plugin Development

- **Start with a cookiecutter**: Use [cookiecutter-pytest-plugin](https://github.com/pytest-dev/cookiecutter-pytest-plugin) to generate a well‑structured plugin project.
- **Keep it focused**: A plugin should do one thing well. If you need multiple features, consider splitting them into separate plugins or modules.
- **Provide comprehensive documentation**: Include a README with installation instructions, usage examples, and a list of hooks/markers.
- **Write tests**: Use `pytester` to test your plugin’s behavior in isolation.
- **Register markers**: Always register custom markers to avoid warnings and improve discoverability.
- **Be mindful of import side effects**: Use `pytest.register_assert_rewrite` before importing modules that need assertion rewriting.
- **Use `--trace-config`** during development to verify your plugin is loaded correctly.
- **Consider compatibility**: Test your plugin against multiple pytest versions and Python versions (use `tox` or GitHub Actions).
- **Release to PyPI** with the `Framework :: Pytest` classifier to help users find it.

---

## 12. Conclusion

Writing pytest plugins is a powerful way to extend the testing framework to suit your project’s unique needs. Whether you create a simple local `conftest.py` or a full‑fledged installable package, understanding the plugin architecture, hook system, and testing tools will enable you to build robust, reusable automation components. By following the guidelines and best practices outlined here, you can contribute to the rich ecosystem of pytest plugins and enhance the testing capabilities of your organization.