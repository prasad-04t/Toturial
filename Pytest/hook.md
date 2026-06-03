# Professional Automation Testing with pytest: Writing Hook Functions

## 1. Introduction

pytest’s extensibility is built on a hook‑based architecture. Plugins can implement **hook functions** that are called by pytest at various stages of the test lifecycle. This allows you to modify behavior, add new functionality, or integrate with external systems without modifying pytest itself. This document explains how to write hook functions, covering their validation, execution order, wrapping, and advanced techniques like declaring new hooks and storing data across hooks.

---

## 2. Hook Function Validation and Execution

When you implement a hook function in a plugin, pytest validates that the argument names match the hook specification. If you omit an argument, it is simply not passed. This allows hooks to evolve without breaking existing plugins.

Example: The `pytest_collection_modifyitems` hook is called after test collection. Its signature is `(session, config, items)`. If your plugin only needs `config` and `items`, you can define it as:

```python
def pytest_collection_modifyitems(config, items):
    # modify items list here
    ...
```

pytest will call your function, passing only the arguments you listed. This “pruning” makes plugins future‑compatible.

**Important:** Hook functions other than `pytest_runtest_*` are **not allowed to raise exceptions**. Doing so will break the pytest run. If you must signal an error, use the appropriate mechanisms (e.g., `pytest.fail` inside tests, or raise an exception only if you are certain it’s safe).

---

## 3. The `firstresult` Option

Some hook specifications use `firstresult=True`. This means that pytest will call hook implementations until one returns a non‑`None` value, and then stop. The returned value becomes the result of the hook call.

This is useful when only one plugin should provide an answer, e.g., a default value. Example:

```python
# hook specification (in a plugin)
@hookspec(firstresult=True)
def pytest_config_file_default_value():
    """Return the default value for the config file."""
```

Implementations:

```python
# in a conftest.py
def pytest_config_file_default_value():
    return "config.yaml"
```

Now when `pluginmanager.hook.pytest_config_file_default_value()` is called, it returns `"config.yaml"` and stops.

---

## 4. Hook Wrappers: Executing Around Other Hooks

A hook wrapper is a generator function that wraps the execution of other hook implementations. It is declared with `wrapper=True` in the `@pytest.hookimpl` decorator. The wrapper yields exactly once; before the `yield`, it runs before other hooks; after the `yield`, it runs after them (or after an exception).

Example:

```python
import pytest

@pytest.hookimpl(wrapper=True)
def pytest_pyfunc_call(pyfuncitem):
    # before the test function runs
    do_something_before()

    # execute the next hooks (including the test itself)
    res = yield

    # after the test
    new_res = post_process_result(res)

    # return the (possibly modified) result
    return new_res
```

- If the underlying hook implementation raises an exception, that exception is raised at the `yield` point. You can catch it with a try‑except‑finally block.
- The wrapper must return a result (or raise an exception). A common pattern is to return `(yield)` if no modification is needed.

**Order:** Wrappers are executed **before** any non‑wrapper hooks, regardless of `tryfirst`/`trylast` settings (unless multiple wrappers are involved; their order among themselves can be influenced by `tryfirst`/`trylast`).

---

## 5. Hook Function Ordering

You can influence the order in which hook implementations are called using `tryfirst` and `trylast` in the `@pytest.hookimpl` decorator.

- `tryfirst=True`: execute this implementation as early as possible (but after wrappers).
- `trylast=True`: execute this implementation as late as possible.
- Neither: default ordering (after `tryfirst` ones, before `trylast` ones).

Example:

```python
# Plugin 1
@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(items):
    # runs early
    ...

# Plugin 2
@pytest.hookimpl(trylast=True)
def pytest_collection_modifyitems(items):
    # runs late
    ...
```

When a hook wrapper is used, it runs before all non‑wrapper implementations, regardless of `tryfirst`/`trylast`. The `tryfirst`/`trylast` settings for wrappers only affect ordering among multiple wrappers.

**Execution order summary** (for a given hook):
1. Hook wrappers (in order of their own `tryfirst`/`trylast`).
2. Non‑wrapper implementations in order: `tryfirst`, then normal, then `trylast`.

---

## 6. Declaring New Hooks

Plugins can define their own hooks that other plugins can implement. This is done by:

1. Defining the hook specification functions (usually in a separate module) with the `@hookspec` decorator.
2. Registering them in `pytest_addhooks`.

### 6.1 Define the Hook Specification

Create a module, e.g., `myplugin/hooks.py`:

```python
from pluggy import HookspecMarker

hookspec = HookspecMarker("pytest")

@hookspec
def pytest_my_hook(config):
    """My custom hook."""
```

The function must be named starting with `pytest_` (though not strictly required by pluggy, pytest’s conventions use it). The decorator can accept arguments like `firstresult=True`.

### 6.2 Register the Hooks in `pytest_addhooks`

In your plugin module, implement `pytest_addhooks`:

```python
def pytest_addhooks(pluginmanager):
    from myplugin import hooks
    pluginmanager.add_hookspecs(hooks)
```

`pytest_addhooks` is called when your plugin is loaded. After registration, other plugins can implement `pytest_my_hook`.

### 6.3 Calling Your Custom Hook

You can call your hook from a fixture or another hook using the `config.hook` object:

```python
@pytest.fixture
def my_fixture(pytestconfig):
    # Call the hook; returns a list of results (or single result if firstresult=True)
    results = pytestconfig.hook.pytest_my_hook(config=pytestconfig)
    # ... use results
```

**Note:** Hook calls must pass keyword arguments that match the hook specification.

---

## 7. Using Hooks from 3rd Party Plugins

Sometimes you want to conditionally use hooks from an external plugin (like pytest‑xdist) only if that plugin is installed. If you simply implement the hook in your plugin, pytest will validate it even when the external plugin is absent, leading to obscure errors.

A recommended pattern is to defer the hook implementation to a separate plugin class and register it only if the external plugin is present:

```python
# myplugin.py
class DeferPlugin:
    """Plugin that implements hooks for pytest-xdist."""

    def pytest_testnodedown(self, node, error):
        # handle the xdist hook
        ...

def pytest_configure(config):
    if config.pluginmanager.hasplugin("xdist"):
        config.pluginmanager.register(DeferPlugin())
```

Now the hook functions are only added when needed, avoiding validation issues.

---

## 8. Storing Data on Items Across Hook Functions

Plugins often need to associate data with a test item across different hook phases (e.g., during setup, call, teardown). Instead of assigning arbitrary attributes to the item (which may cause conflicts), pytest provides the **stash** mechanism.

A stash is a type‑safe dictionary available on `item.stash`. You create a **stash key** for each piece of data:

```python
import pytest

been_there_key = pytest.StashKey[bool]()
done_that_key = pytest.StashKey[str]()
```

Then in a hook, you can store values:

```python
def pytest_runtest_setup(item):
    item.stash[been_there_key] = True
    item.stash[done_that_key] = "no"
```

And retrieve them later:

```python
def pytest_runtest_teardown(item):
    if not item.stash[been_there_key]:
        print("Oh?")
    item.stash[done_that_key] = "yes!"
```

Stashes are available on `Config`, `Session`, `Module`, `Class`, `Function`, and other node objects.

**Benefits:**
- Type‑safe (using `StashKey[T]`).
- Avoids attribute name collisions.
- Easy to access from any hook that receives the node.

---

## 9. Best Practices

- **Use `tryfirst` and `trylast` sparingly** – they create ordering dependencies; rely on them only when necessary.
- **Document your hooks** – if you declare new hooks, provide clear documentation on when they are called and what parameters they receive.
- **Test your hooks** – use the `pytester` fixture to verify that your plugin behaves correctly in an isolated environment.
- **Use `StashKey` for cross‑hook data** – it’s safer and more explicit than ad‑hoc attributes.
- **Avoid raising exceptions in non‑runtest hooks** – unless you are certain it won’t disrupt pytest.
- **Register hooks conditionally** when depending on optional plugins.
- **Respect the hook signature** – even though you can omit arguments, keep the function signature consistent with the specification to avoid confusion.

---

## 10. Conclusion

Writing hook functions is the primary way to extend pytest. By understanding validation, ordering, wrappers, and advanced patterns like declaring new hooks and using the stash, you can build powerful plugins that integrate seamlessly with the pytest ecosystem. Following the best practices outlined here will help you create robust, maintainable, and future‑proof plugins that enhance your automation framework.