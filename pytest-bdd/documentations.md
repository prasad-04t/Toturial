# pytest-bdd: Professional Guide for Automation Testing Engineers

## 1. Introduction

Behavior-Driven Development (BDD) bridges the gap between business requirements and technical implementation by using a common language—Gherkin—to describe software behavior. `pytest-bdd` is a plugin for the pytest framework that brings BDD capabilities to Python. It allows you to write executable specifications in plain-text `.feature` files, then implement them as Python functions, leveraging the full power of pytest’s fixtures, markers, and plugins.

Unlike many BDD tools, `pytest-bdd` does not require a separate runner. It integrates seamlessly with pytest, enabling you to reuse unit test fixtures, run tests in parallel, and produce rich reports. This guide provides a comprehensive, production‑ready reference for automation testing engineers, covering everything from basic setup to advanced patterns and best practices.

---

## 2. Core Concepts

| Concept          | Description |
|------------------|-------------|
| **Gherkin**      | A plain‑text language with keywords (`Feature`, `Scenario`, `Given`, `When`, `Then`, `And`, `But`, `Background`, `Scenario Outline`, `Examples`). |
| **Feature File** | A `.feature` file containing one or more scenarios that describe a specific feature of the application. |
| **Scenario**     | A concrete example of a business rule, composed of steps following the `Given-When-Then` structure. |
| **Step Definition** | A Python function decorated with `@given`, `@when`, or `@then` that matches a Gherkin step and contains the automation logic. |
| **Fixtures**     | pytest’s dependency injection mechanism used to manage test setup, teardown, and shared resources. |
| **Step Matchers** | Decorators that link a step definition to one or more Gherkin steps using regular expressions or parse expressions. |

---

## 3. Installation and Project Setup

### 3.1 Prerequisites

- Python 3.7 or higher
- `pip` package manager

### 3.2 Install pytest and pytest-bdd

```bash
pip install pytest pytest-bdd
```

### 3.3 Recommended Project Structure

A well‑organized project improves maintainability and scalability.

```
project_root/
├── features/
│   ├── login.feature
│   ├── registration.feature
│   └── steps/
│       ├── conftest.py          # Shared fixtures and hooks
│       ├── login_steps.py
│       └── registration_steps.py
├── pages/                        # Page Object Model (if UI testing)
│   ├── base_page.py
│   └── login_page.py
├── utils/
│   └── helpers.py
├── reports/                      # Test reports
├── pytest.ini
├── requirements.txt
└── conftest.py                   # Top‑level fixtures / plugins
```

---

## 4. Writing Feature Files with Gherkin

Feature files are written in Gherkin and stored with the `.feature` extension. Only one feature is allowed per file.

### 4.1 Basic Feature File Example

**`features/login.feature`**

```gherkin
Feature: User Login
  As a registered user
  I want to log in to the application
  So that I can access my dashboard

  Background:
    Given the application is running
    And the user "testuser" exists with password "secret"

  Scenario: Successful login with valid credentials
    When I navigate to the login page
    And I enter "testuser" in the username field
    And I enter "secret" in the password field
    And I click the login button
    Then I should be redirected to the dashboard
    And I should see a welcome message "Welcome, testuser"

  Scenario Outline: Login with invalid credentials
    When I navigate to the login page
    And I enter "<username>" in the username field
    And I enter "<password>" in the password field
    And I click the login button
    Then I should see an error message "<error>"

    Examples:
      | username | password | error               |
      | testuser | wrong    | Invalid credentials |
      |          | secret   | Username required   |
      | testuser |          | Password required   |
```

### 4.2 Key Gherkin Elements

- **Feature**: High‑level description of a feature.
- **Background**: Steps executed before each scenario (common setup).
- **Scenario**: A concrete example.
- **Scenario Outline**: Parametrizes a scenario with an `Examples` table.
- **Examples**: Data table for a scenario outline.
- **Tags**: Use `@tag` above features, rules, or scenarios to group and filter tests.

---

## 5. Implementing Step Definitions

Step definitions are Python functions decorated with `@given`, `@when`, or `@then`. They reside in the `steps/` directory or in `conftest.py` and are discovered automatically.

### 5.1 Basic Step Matching (Exact String)

```python
from pytest_bdd import given, when, then

@given("the application is running")
def app_running():
    pass

@when("I navigate to the login page")
def navigate_to_login(browser):
    browser.get("https://example.com/login")

@then("I should be redirected to the dashboard")
def verify_dashboard_url(browser):
    assert browser.current_url == "https://example.com/dashboard"
```

### 5.2 Step Aliases

Use multiple decorators to reuse the same step function under different names.

```python
@given("I have an article")
@given("there's an article")
def article(author, target_fixture="article"):
    return create_test_article(author=author)
```

### 5.3 Using Asterisks (`*`) in Place of Keywords

To reduce redundancy, you can use an asterisk `*` as a wildcard. It works the same as the step keyword it replaces.

```gherkin
Feature: Resource owner
  Scenario: I'm the author
    Given I'm an author
    * I have an article
    * I have a pen
```

```python
from pytest_bdd import given

@given("I'm an author")
def _():
    pass

@given("I have an article")
def _():
    pass

@given("I have a pen")
def _():
    pass
```

### 5.4 Step Arguments and Parsers

`pytest-bdd` provides several parsers to capture parameters from step text.

#### 5.4.1 String Parser (Default)

Matches the step text exactly; no parameters.

#### 5.4.2 Parse Parser

Uses named placeholders like `{name:type}`. Type conversion can be applied via `extra_types`.

```python
from pytest_bdd import parsers

@given(parsers.parse("there are {start:d} cucumbers"), target_fixture="cucumbers")
def given_cucumbers(start):
    return {"start": start, "eat": 0}
```

#### 5.4.3 Cfparse Parser

Extends the parse parser with cardinality fields (`*`, `+`, `?`). Automatically creates missing type converters.

```python
@given(parsers.cfparse("there are {start:Number} cucumbers", extra_types={"Number": int}))
def given_cucumbers(start):
    return {"start": start, "eat": 0}
```

#### 5.4.4 Re Parser

Uses full regular expressions with named groups `(?P<name>…)`. Converters can be passed to post‑process values.

```python
@given(parsers.re(r"there are (?P<start>\d+) cucumbers"), converters={"start": int})
def given_cucumbers(start):
    return {"start": start, "eat": 0}
```

### 5.5 Overriding Fixtures via Given Steps (`target_fixture`)

Sometimes a given step needs to replace an existing fixture for a specific scenario. Use `target_fixture` to inject the step’s return value into the named fixture.

```python
@pytest.fixture
def foo():
    return "foo"

@given("I have injecting given", target_fixture="foo")
def injecting_given():
    return "injected foo"

@then('foo should be "injected foo"')
def foo_is_foo(foo):
    assert foo == "injected foo"
```

Both `when` and `then` steps can also use `target_fixture` to provide a fixture.

---

## 6. Scenarios and Scenario Outlines

### 6.1 Manual Scenario Binding with `@scenario`

Decorate a test function with `@scenario` to bind it to a specific feature file and scenario.

```python
from pytest_bdd import scenario

@scenario("publish_article.feature", "Publishing the article")
def test_publish():
    pass
```

The function can contain additional assertions or logic after the scenario steps have executed.

### 6.2 Automatic Scenario Binding with `scenarios()`

For large test suites, use `scenarios()` to automatically bind all scenarios found in a feature file or folder.

```python
from pytest_bdd import scenarios

scenarios("features")          # all .feature files under 'features'
scenarios("features/login.feature")  # single file
scenarios("features", "other.feature")  # multiple paths
```

`scenarios()` respects manual bindings if placed after them.

### 6.3 Scenario Outlines

Scenario Outlines allow data‑driven testing using an `Examples` table. Variables in steps are enclosed in angle brackets (`<variable>`).

**Feature snippet:**

```gherkin
Scenario Outline: Outlined given, when, then
  Given there are <start> cucumbers
  When I eat <eat> cucumbers
  Then I should have <left> cucumbers

  Examples:
    | start | eat | left |
    |  12   |  5  |  7   |
```

**Step definitions with parsers:**

```python
from pytest_bdd import given, when, then, parsers

@given(parsers.parse("there are {start:d} cucumbers"), target_fixture="cucumbers")
def given_cucumbers(start):
    return {"start": start, "eat": 0}

@when(parsers.parse("I eat {eat:d} cucumbers"))
def eat_cucumbers(cucumbers, eat):
    cucumbers["eat"] += eat

@then(parsers.parse("I should have {left:d} cucumbers"))
def should_have_left_cucumbers(cucumbers, left):
    assert cucumbers["start"] - cucumbers["eat"] == left
```

#### 6.3.1 Multiple Example Tables

You can have multiple `Examples` blocks, each optionally tagged.

```gherkin
Scenario Outline: Outlined with multiple example tables
  Given there are <start> cucumbers
  When I eat <eat> cucumbers
  Then I should have <left> cucumbers

  @positive
  Examples: Positive results
    | start | eat | left |
    |  12   |  5  |  7   |
    |  5    |  4  |  1   |

  @negative
  Examples: Negative results
    | start | eat | left |
    |  3    |  9  |  -6  |
```

Filtering by tag (e.g., `pytest -m positive`) runs only the associated examples.

#### 6.3.2 Handling Empty Example Cells

By default, empty cells become empty strings. To treat them as `None`, use a converter with the `re` parser.

```python
def empty_to_none(value):
    return None if value.strip() == "" else value

@then(
    parsers.re("there are (?P<start>.*?) cucumbers"),
    converters={"start": empty_to_none}
)
def _(start):
    assert start is None
```

### 6.4 Docstrings and Datatables in Scenarios

#### 6.4.1 Datatables

A step that includes a Gherkin data table can accept a `datatable` argument, which is a list of lists (rows).

```gherkin
Given the following user details:
  | name  | email             | age |
  | John  | john@example.com  | 30  |
```

```python
@given("the following user details:", target_fixture="users")
def _(datatable):
    # datatable = [["name", "email", "age"], ["John", "john@example.com", "30"]]
    return [dict(zip(datatable[0], row)) for row in datatable[1:]]
```

#### 6.4.2 Docstrings

A step with a multiline docstring can accept a `docstring` argument, which is a string.

```gherkin
Then a step has a docstring
  """
  This is a docstring
  on two lines
  """
```

```python
@then("a step has a docstring")
def _(docstring):
    assert docstring == "This is a docstring\non two lines"
```

---

## 7. Organizing Tests and Reusability

### 7.1 Backgrounds

A `Background` section in a feature file runs steps before each scenario. Only `Given` steps should be used in a background.

```gherkin
Background:
  Given a global administrator named "Greg"
  And a blog named "Greg's anti-tax rants"
```

### 7.2 Reusing Fixtures and Steps Across Features

Fixtures defined in `conftest.py` are available to all steps. Steps defined in `conftest.py` or in any file under `steps/` are also globally discoverable.

```python
# conftest.py
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@given("the application is running")
def app_running():
    pass
```

### 7.3 Default Steps

`pytest-bdd` provides built‑in `trace` steps for debugging:

- `Given trace` – enters pdb debugger.
- `When trace` – enters pdb debugger.
- `Then trace` – enters pdb debugger.

### 7.4 Configuring Feature File Paths

Set a base path for feature files in `pytest.ini`:

```ini
[pytest]
bdd_features_base_dir = features/
```

Override per scenario with the `features_base_dir` parameter:

```python
@scenario("foo.feature", "Foo feature", features_base_dir="./local-features/")
def test_foo_local():
    pass
```

### 7.5 Avoid Retyping the Feature File Name

Use `functools.partial` to create a reusable `scenario` function.

```python
from functools import partial
import pytest_bdd

scenario = partial(pytest_bdd.scenario, "/path/to/publish_article.feature")

@scenario("Publishing the article")
def test_publish():
    pass
```

---

## 8. Advanced Features

### 8.1 Programmatic Step Generation

For complex models, you can generate step definitions dynamically. Pass `stacklevel` to step decorators to inject them into the correct module.

```python
def generate_wallet_steps(model_name="wallet", stacklevel=1):
    stacklevel += 1
    human_name = model_name.replace("_", " ")

    @given(f"I have a {human_name}", target_fixture=model_name, stacklevel=stacklevel)
    def _(request):
        return request.getfixturevalue(model_name)

    # ... generate additional steps

generate_wallet_steps("wallet")
```

### 8.2 Hooks

`pytest-bdd` exposes hooks for fine‑grained control over the test lifecycle. Define them in `conftest.py`.

- `pytest_bdd_before_scenario(request, feature, scenario)`
- `pytest_bdd_after_scenario(request, feature, scenario)`
- `pytest_bdd_before_step(request, feature, scenario, step, step_func)`
- `pytest_bdd_before_step_call(request, feature, scenario, step, step_func, step_func_args)`
- `pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args)`
- `pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception)`
- `pytest_bdd_step_func_lookup_error(request, feature, scenario, step, exception)`

Example:

```python
def pytest_bdd_before_scenario(request, feature, scenario):
    print(f"Starting scenario: {scenario.name}")
```

### 8.3 Custom Tag Handling

Implement `pytest_bdd_apply_tag` to control how tags are converted to pytest marks.

```python
def pytest_bdd_apply_tag(tag, function):
    if tag == 'todo':
        marker = pytest.mark.skip(reason="Not implemented yet")
        marker(function)
        return True
    return None   # fall back to default
```

---

## 9. Integration and Reporting

### 9.1 Browser Testing with pytest-splinter

For UI testing, `pytest-splinter` provides a `browser` fixture that works with Selenium WebDriver.

```bash
pip install pytest-splinter
```

```python
@when("I go to the article page")
def go_to_article(article, browser):
    browser.visit(f"/manage/articles/{article.id}/")
```

### 9.2 Reporting

#### 9.2.1 Cucumber JSON Report

```bash
pytest --cucumberjson=report.json
```

Produces a Cucumber‑compatible JSON report with expanded scenario outlines.

#### 9.2.2 Gherkin Terminal Reporter

```bash
pytest -v --gherkin-terminal-reporter
```

Displays steps with Gherkin syntax in the terminal.

#### 9.2.3 Other Reports

Combine with standard pytest reporting plugins: `pytest-html`, `pytest-xdist` for parallel execution, `pytest-allure` for Allure reports.

### 9.3 Tag‑Based Test Selection

Tags become pytest markers. Use `-m` to filter.

```bash
pytest -m "smoke and not wip"
```

Add tags to `pytest.ini` if using `--strict-markers`:

```ini
[pytest]
markers =
    smoke: Smoke tests
    regression: Full regression tests
```

---

## 10. Code Generation and Migration

### 10.1 Generating Test Code from Feature Files

The `pytest-bdd` command‑line tool can generate stub code for a feature file.

```bash
pytest-bdd generate features/some.feature > tests/functional/test_some.py
```

### 10.2 Smart Code Suggestion

Run pytest with `--generate-missing` to generate only missing steps and scenarios.

```bash
pytest --generate-missing --feature features tests/functional
```

The output includes the exact code that needs to be added to make the tests pass.

### 10.3 Migration Guides

#### 10.3.1 Migrating from Version 5.x.x

- Feature‑level `Examples` tables are no longer supported; move them to each scenario.
- Vertical example tables are removed; use horizontal orientation.
- Step arguments are no longer fixtures; use `target_fixture` to define a fixture from a step.
- Variable templates (`<...>`) are parsed only within scenario outlines.

#### 10.3.2 Migrating from Version 4.x.x

- Replace `<parameter>` in steps with parsed `{parameter}`.
- Use `converters` on the step level instead of `example_converters`.

#### 10.3.3 Migrating from Version 3.x.x

- Given steps are no longer fixtures; use `target_fixture` if a fixture is needed.
- Remove `strict_gherkin` parameters and `bdd_strict_gherkin` from ini.
- Remove step validation hooks.

---

## 11. Best Practices for Automation Engineers

1. **Write Executable Specifications**  
   Keep feature files readable by non‑technical stakeholders. Use domain language and avoid technical details.

2. **One Step, One Action**  
   Each step definition should perform a single logical action. This improves reusability and maintainability.

3. **Use Page Object Model (POM)**  
   For UI tests, encapsulate page interactions in page classes. Steps should call these classes, not Selenium directly.

4. **Leverage pytest Fixtures**  
   Use fixtures for browser management, test data, and teardown. This keeps step definitions clean and reduces boilerplate.

5. **Parameterize Test Data**  
   Use scenario outlines and data tables to cover multiple input combinations without duplicating steps.

6. **Adopt a Consistent Naming Convention**  
   Name step definition files after the feature they support (e.g., `login_steps.py`). Use meaningful step function names.

7. **Tag Strategically**  
   Use tags like `@smoke`, `@regression`, `@wip` to organize test runs. Avoid over‑tagging; keep tags focused.

8. **Version Control Feature Files**  
   Store `.feature` files alongside code. Use clear commit messages when updating scenarios.

9. **Run Tests in CI**  
   Integrate pytest‑bdd tests into continuous integration pipelines. Use parallel execution (`pytest-xdist`) for faster feedback.

10. **Regularly Review and Refactor**  
    As the codebase grows, review steps for duplication. Refactor common steps into reusable functions or fixtures.

---

## 12. Troubleshooting Common Issues

| Issue | Solution |
|-------|----------|
| **Step not found** | Ensure the step definition is in a discoverable location (e.g., `steps/` folder or `conftest.py`). Use `pytest --collect-only` to verify collected tests. |
| **Fixture not found** | Verify the fixture is defined in a `conftest.py` in the same or parent directory of the test. Check that the fixture name matches the step argument. |
| **Parser mismatch** | When using `parsers.parse`, ensure the placeholders `{name}` match the function argument names. For regex, named groups must match. |
| **Feature file not loaded** | Call `scenarios('path/to/feature.feature')` in your test file, or use `@scenario`. Ensure the path is correct relative to the test location. |
| **Empty cells not handled** | Use a custom converter with `parsers.re` to map empty strings to `None` or other values. |
| **Tags not applied** | If using `--strict-markers`, define all tags in `pytest.ini`. Customize tag handling with `pytest_bdd_apply_tag` if needed. |

---

## 13. Conclusion

`pytest-bdd` empowers automation testing engineers to build maintainable, scalable, and collaborative test suites. By combining the expressive power of Gherkin with pytest’s rich ecosystem, you can create executable specifications that serve as both living documentation and reliable automated tests.

This guide has covered the essential concepts, from writing feature files and step definitions to advanced topics like programmatic step generation and custom hooks. Apply these principles in your projects to improve test quality, foster collaboration, and accelerate delivery.

For further reference, consult the official documentation:

- [pytest-bdd Documentation](https://pytest-bdd.readthedocs.io/)
- [pytest Documentation](https://docs.pytest.org/)
- [Gherkin Reference](https://cucumber.io/docs/gherkin/)

---

*This document is intended as a living reference. Update it as your team’s practices evolve.*