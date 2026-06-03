# Cucumber & Behave

## What is Cucumber?
**Cucumber** is a **testing tool** used for **Behavior-Driven Development (BDD)**. It allows you to write test cases in **plain English (or simple language)** so that both technical and non-technical people can understand them.
###  Key Idea

Instead of writing complex code-based test cases, Cucumber lets you describe application behavior in a **human-readable format**.
### Example (Gherkin Language)
Cucumber uses a language called **Gherkin**:

```gherkin
Feature: Login functionality

  Scenario: Successful login
    Given user is on login page
    When user enters valid username and password
    Then user should be redirected to homepage
```

###  How It Works

* **Feature file** → Written in Gherkin (plain English steps)
* **Step Definitions** → Actual code (Java, Python, etc.) that executes those steps
* **Test Runner** → Runs the tests and shows results

### 🔹 Why Use Cucumber?

* ✔ Easy to understand (even for non-developers)
* ✔ Improves collaboration between developers, testers, and business teams
* ✔ Keeps requirements and test cases in sync
* ✔ Supports multiple languages (Java, Python, JavaScript, etc.)


### 🔹 Simple Definition

👉 Cucumber is a tool that helps you **write automated tests in simple English and link them to code**.

---
---
## What is Gherkin?

**Gherkin** is a **simple, human-readable language** used in **Behavior-Driven Development (BDD)** to write test scenarios. It is mainly used with tools like Cucumber.

### Key Idea

Gherkin allows you to describe application behavior in **plain English**, so **developers, testers, and business people** can all understand the requirements.

### Example of Gherkin

```gherkin
Feature: Login functionality

  Scenario: Successful login
    Given user is on login page
    When user enters valid username and password
    Then user should see homepage
```

### Important Keywords

Gherkin uses specific keywords:

* **Feature** → What feature you are testing
* **Scenario** → A test case
* **Given** → Pre-condition
* **When** → Action
* **Then** → Expected result
* **And / But** → Additional steps


## 🔹 How It Works

1. Write scenarios in Gherkin (plain text)
2. Map each step to code (Step Definitions)
3. Execute using Cucumber

## 🔹 Why Use Gherkin?

* ✔ Easy to read and write
* ✔ No programming knowledge needed
* ✔ Improves communication
* ✔ Acts as both **documentation + test cases**

## 🔹 Simple Definition

👉 Gherkin is a language used to **write test cases in plain English format** for BDD.

---
---

## Whaty is Behave?
**Behave** is a **Behavior-Driven Development (BDD) testing framework for Python**. It is similar to Cucumber, but specifically designed for Python projects.

### Key Idea

Behave allows you to write test cases in **plain English (Gherkin language)** and connect them to **Python code** that performs the actual test actions.

## Example (Feature File in Behave)

```gherkin id="behave1"
Feature: Login functionality

  Scenario: Successful login
    Given user is on login page
    When user enters username and password
    Then user should see homepage
```

### Step Definition (Python Code)

```python
from behave import given, when, then

@given('user is on login page')
def step_given(context):
    print("Open login page")

@when('user enters username and password')
def step_when(context):
    print("Enter credentials")

@then('user should see homepage')
def step_then(context):
    print("Verify homepage")
```


###  How It Works

1. Write scenarios using **Gherkin**
2. Create step definitions in Python
3. Run tests using Behave
4. It matches steps → executes Python code → shows results


### Why Use Behave?

* ✔ Designed for Python projects
* ✔ Easy to read (non-technical friendly)
* ✔ Supports automation tools like Selenium / Playwright
* ✔ Improves collaboration between teams

## 🔹 Simple Definition

👉 Behave is a **Python BDD framework that executes Gherkin-based test scenarios**.

---
---

## What do you meant by a feature file?
A **feature file** is a **text file where you write test scenarios in plain English using Gherkin**. It describes **what the application should do**, not how it is implemented.

### Key Idea

A feature file acts like a **bridge between business requirements and automation tests**.

* Business people → understand it
* Testers → write it
* Developers → automate it


### Example of a Feature File

```gherkin id="feat1"
Feature: Login functionality

  Scenario: Successful login
    Given user is on login page
    When user enters valid username and password
    Then user should be redirected to homepage
```

### Structure of a Feature File

* **Feature** → Describes the functionality
* **Scenario** → A specific test case
* **Steps (Given, When, Then)** → Define flow

### File Details

* Extension: `.feature`
* Used in tools like Cucumber and Behave
* Stored in project (usually inside `features/` folder)

### Why It Is Important

* ✔ Easy to read and write
* ✔ Acts as **documentation + test case**
* ✔ Keeps requirements clear
* ✔ Helps in team collaboration


### Simple Definition

👉 A feature file is a **BDD file written in plain English that describes application behavior using scenarios**.

---
---

## What is Step definition?
**Step Definition** is the **actual code implementation** for the steps written in a feature file.
It connects the plain-English steps (Gherkin) to executable code.

###  Key Idea
In a feature file, you write:
> Given / When / Then (in English)
In step definitions, you write:
> Python/Java code that performs those steps
### Example

### Feature File (Gherkin)

```gherkin
Scenario: Login
  Given user is on login page
  When user enters username and password
  Then user should see homepage
```

### Step Definition (Python – Behave)

```python
from behave import given, when, then

@given('user is on login page')
def step_given(context):
    print("Opening login page")

@when('user enters username and password')
def step_when(context):
    print("Entering credentials")

@then('user should see homepage')
def step_then(context):
    print("Verifying homepage")
```

### How It Works

* Cucumber / Behave reads the feature file
* Matches each step with a step definition
* Executes the corresponding code

### Important Points

* Written in programming language (Python, Java, etc.)
* Uses decorators like `@given`, `@when`, `@then`
* Each step in feature file must have a matching step definition
* Can include automation (Selenium, Playwright, API calls, etc.)

### Simple Definition

👉 Step definition is **code that executes the steps written in a feature file**.
---
---

## What do you mean by Scenario and Scenario Outline?
### Scenario

A **Scenario** is a **single test case** that describes one specific behavior of an application using steps written in Gherkin.

 It represents **one flow with one set of data**.

#### Example:

```gherkin id="sc1"
Scenario: Successful login
  Given user is on login page
  When user enters valid username and password
  Then user should see homepage
```

✔ Used when you want to test **one situation**
✔ Simple and straightforward

### Scenario Outline

A **Scenario Outline** is used when you want to run the **same scenario multiple times with different data sets**.

 It uses placeholders (`< >`) and an **Examples table**.

#### Example:

```gherkin id="sc2"
Scenario Outline: Login with multiple users
  Given user is on login page
  When user enters "<username>" and "<password>"
  Then user should see "<result>"

Examples:
  | username | password | result     |
  | user1    | pass1    | homepage   |
  | user2    | pass2    | error page |
```

✔ Used for **data-driven testing**
✔ Avoids repeating the same scenario


### Key Difference

| Scenario          | Scenario Outline    |
| ----------------- | ------------------- |
| Runs once         | Runs multiple times |
| Fixed data        | Multiple data sets  |
| No Examples table | Uses Examples table |


### Simple Definition

* 👉 **Scenario** = One test case with one set of data
* 👉 **Scenario Outline** = One test case executed with multiple data sets

---
---

## Different keywords used in Cucumber/Behave to write a scenario?
In **BDD tools like Cucumber and Behave**, scenarios are written using **Gherkin keywords**. These keywords define the structure and flow of your test cases.

### Main Keywords Used in Scenarios

#### 1. Feature

* Describes the **overall functionality**

```gherkin
Feature: Login functionality
```


#### 2. Scenario

* Represents a **single test case**

```gherkin
Scenario: Valid login
```


#### 3. Given

* Defines the **initial condition (pre-condition)**

```gherkin
Given user is on login page
```

#### 4. When

* Describes the **action performed**

```gherkin
When user enters username and password
```

#### 5. Then

* Describes the **expected result**

```gherkin
Then user should see homepage
```

#### 6. And / But

* Used to **add more steps** (avoid repetition)

```gherkin
And user clicks login button
But error message should not be displayed
```

#### 7. Scenario Outline

* Used for **data-driven testing**

```gherkin
Scenario Outline: Login with multiple users
```


#### 8. Examples

* Provides **test data for Scenario Outline**

```gherkin
Examples:
  | username | password |
```

---

#### 9. Background

* Runs **common steps before each scenario**

```gherkin
Background:
  Given user is on login page
```

#### 10. Tags

* Used to **group or filter tests**

```gherkin
@login @smoke
Scenario: Valid login
```

## 🔹 Simple Flow

👉 **Feature → Scenario → Given → When → Then → And/But**

## 🔹 Simple Definition

👉 These keywords help you **write structured, readable test cases in plain English**.

---
---

## What is the use of Background keyword in Cucumber?
The **`Background`** keyword in Cucumber (and Behave) is used to define **common steps that run before every scenario in a feature file**.

### Key Idea

👉 Instead of repeating the same steps in every scenario, you write them once in **Background**.


### Example

```gherkin id="bg1"
Feature: Login functionality

Background:
  Given user is on login page
  And user has valid account

Scenario: Successful login
  When user enters correct credentials
  Then user should see homepage

Scenario: Invalid login
  When user enters wrong credentials
  Then user should see error message
```
### How It Works

* **Background steps run before each Scenario**
* Execution flow:

👉 Background → Scenario 1
👉 Background → Scenario 2

### Why Use Background?

* ✔ Avoids duplication of common steps
* ✔ Makes feature files clean and readable
* ✔ Improves maintainability


### Important Points

* Defined **once per feature file**
* Should contain only **common preconditions**
* Runs before **every scenario automatically**


### Simple Definition

👉 Background is used to **execute common preconditions before each scenario in a feature file**.


### When NOT to Use

* If steps are different for each scenario
* If too many steps (makes it hard to read)

---
---
## What are cucumber/Behave tags and where we use them?
**Tags** in Cucumber and Behave are **labels (starting with `@`) used to organize, filter, and control execution of scenarios or features**.

### Key Idea
Tags help you **run only specific tests instead of running all tests**.

### Example

```gherkin id="tag1"
@smoke @login
Feature: Login functionality

  @positive
  Scenario: Successful login
    Given user is on login page
    When user enters valid credentials
    Then user should see homepage

  @negative
  Scenario: Invalid login
    Given user is on login page
    When user enters wrong credentials
    Then user should see error message
```

---

### Where We Use Tags

#### 1. At Feature Level

* Applies to all scenarios inside the feature

```gherkin id="tag2"
@smoke
Feature: Login functionality
```

#### 2. At Scenario Level

* Applies only to that specific scenario

```gherkin id="tag3"
@regression
Scenario: Successful login
```


### How to Run Using Tags

#### In Cucumber (Java)

```bash id="tag4"
mvn test -Dcucumber.filter.tags="@smoke"
```

#### In Behave (Python)

```bash id="tag5"
behave --tags=@smoke
```

### Common Tag Types (Real Projects)

* `@smoke` → Basic critical tests
* `@regression` → Full test suite
* `@sanity` → Quick checks
* `@positive` / `@negative` → Test type
* `@login`, `@payment` → Feature/module-based

### Why Tags Are Useful

* ✔ Run selective tests
* ✔ Save execution time
* ✔ Organize large test suites
* ✔ Integrate with CI/CD pipelines

### Simple Definition

👉 Tags are **labels used to group and execute specific test scenarios in Cucumber/Behave**.

---
---
## What are Hooks?
**Hooks** in Cucumber and Behave are **special blocks of code that run automatically before or after test scenarios**.



### Key Idea

 Hooks are used for **setup and teardown** (things you don’t want to repeat in every scenario).


### Types of Hooks

#### 1. Before Hook

* Runs **before each scenario**
* Used for setup

#### 2. After Hook

* Runs **after each scenario**
* Used for cleanup

### Example (Behave – Python)

```python id="hook1"
from behave import *

def before_scenario(context, scenario):
    print("Launch browser")

def after_scenario(context, scenario):
    print("Close browser")
```


### Example (Cucumber – Java)

```java id="hook2"
import io.cucumber.java.Before;
import io.cucumber.java.After;

@Before
public void setUp() {
    System.out.println("Launch browser");
}

@After
public void tearDown() {
    System.out.println("Close browser");
}
```


### Tagged Hooks (Important)

 Hooks can run only for specific tagged scenarios:

#### Example:

```java id="hook3"
@Before("@smoke")
public void beforeSmoke() {
    System.out.println("Run only for smoke tests");
}
```


### Why Use Hooks?

* ✔ Avoid code duplication
* ✔ Centralized setup/cleanup
* ✔ Manage browser, DB, API setup
* ✔ Capture screenshots on failure


### Hooks vs Background

| Hooks                       | Background              |
| --------------------------- | ----------------------- |
| Written in code             | Written in feature file |
| Used for setup/teardown     | Used for test steps     |
| Invisible to business users | Visible in feature file |


### Simple Definition

👉 Hooks are **special methods that run before or after scenarios to handle setup and cleanup tasks**.

---
---
## Different Hooks in Cucumber?
In Cucumber, **Hooks** are used to run code at different stages of test execution (before/after scenarios or steps).


### Different Types of Hooks in Cucumber

#### 1. Before

* Runs **before each scenario**

```java
@Before
public void setUp() {
    System.out.println("Launch browser");
}
```

#### 2. After

* Runs **after each scenario**

```java
@After
public void tearDown() {
    System.out.println("Close browser");
}
```


#### 3. BeforeStep

* Runs **before each step in a scenario**

```java
@BeforeStep
public void beforeStep() {
    System.out.println("Before step");
}
```
#### 4. AfterStep

* Runs **after each step**

```java
@AfterStep
public void afterStep() {
    System.out.println("After step");
}
```



#### 5. BeforeAll

* Runs **once before all scenarios**

```java
@BeforeAll
public static void beforeAll() {
    System.out.println("Start test execution");
}
```


#### 6. AfterAll

* Runs **once after all scenarios**

```java
@AfterAll
public static void afterAll() {
    System.out.println("End test execution");
}
```


#### Tagged Hooks (Very Important)

 Run hooks only for specific scenarios using tags:

```java
@Before("@smoke")
public void beforeSmoke() {
    System.out.println("Run only for smoke tests");
}
```


#### 🔹 Execution Order (Simple)

👉 BeforeAll → Before → BeforeStep → Scenario Steps → AfterStep → After → AfterAll


### Why These Hooks Are Useful

* ✔ Setup (browser, DB, test data)
* ✔ Cleanup (close browser, logout)
* ✔ Logging and reporting
* ✔ Screenshot on failure

---
---

## 🔹 Simple Definition

👉 Cucumber hooks are **methods that run at different stages of test execution (before/after scenarios or steps)**.

---
---

## Different Hooks in Behave?
In Behave, **Hooks** are predefined functions that run at different stages of test execution. They are written inside the `environment.py` file.

## 🔹 Different Types of Hooks in Behave

### 1. before_all

* Runs **once before all features**

```python
def before_all(context):
    print("Start test execution")
```

### 2. after_all

* Runs **once after all features**

```python
def after_all(context):
    print("End test execution")
```

### 3. before_feature

* Runs **before each feature**

```python
def before_feature(context, feature):
    print(f"Starting feature: {feature.name}")
```


### 4. after_feature

* Runs **after each feature**

```python
def after_feature(context, feature):
    print(f"Finished feature: {feature.name}")
```

### 5. before_scenario

* Runs **before each scenario**

```python
def before_scenario(context, scenario):
    print(f"Starting scenario: {scenario.name}")
```


### 6. after_scenario

* Runs **after each scenario**

```python
def after_scenario(context, scenario):
    print(f"Finished scenario: {scenario.name}")
```

### 7. before_step

* Runs **before each step**

```python
def before_step(context, step):
    print(f"Before step: {step.name}")
```

### 8. after_step

* Runs **after each step**

```python
def after_step(context, step):
    print(f"After step: {step.name}")
```

### 9. before_tag

* Runs **before a specific tag**

```python
def before_tag(context, tag):
    print(f"Before tag: {tag}")
```

### 10. after_tag

* Runs **after a specific tag**

```python
def after_tag(context, tag):
    print(f"After tag: {tag}")
```

#### Execution Flow

👉 before_all
→ before_feature
→ before_scenario
→ before_step
→ Scenario Steps
→ after_step
→ after_scenario
→ after_feature
→ after_all

#### Why Hooks Are Useful

* ✔ Setup (browser launch, DB connection)
* ✔ Cleanup (close browser, clear data)
* ✔ Logging and reporting
* ✔ Screenshot on failure


#### Simple Definition

👉 Behave hooks are **functions that execute automatically at different stages of test execution**.

---
---

##  What are the advantages of using Cucumber/Behave?
Using Cucumber / Behave provides several practical advantages, especially in real-world automation projects.

### Key Advantages

### 1. Easy to Understand (Non-Technical Friendly)
* Test cases are written in plain English using Gherkin
* Business analysts, testers, and developers can all read and understand

### 2. Improves Collaboration

* Acts as a **common language** between:

  * Developers
  * Testers
  * Business stakeholders
 Everyone works on the same requirements.


### 3. Living Documentation

* Feature files serve as **documentation + test cases**
* Always up-to-date with the application behavior

### 4. Reusability of Steps

* Step definitions can be reused across multiple scenarios
* Reduces duplication of code


### 5. Supports Data-Driven Testing

* Using **Scenario Outline + Examples**, you can test multiple data sets easily

### 6. Better Test Coverage

* Encourages writing tests based on **user behavior and requirements**
* Helps identify missing scenarios early


### 7. Integration with Automation Tools

* Works with tools like:

  * Selenium
  * Playwright
  * APIs

👉 Makes it powerful for UI and API automation.


### 8. Tag-Based Execution

* Run specific tests using tags (`@smoke`, `@regression`)
* Saves execution time in CI/CD pipelines


### 9. Structured and Organized Tests

* Clear format:
  👉 Feature → Scenario → Steps


### Simple Summary

👉 Cucumber/Behave helps you **write readable, maintainable, and collaborative automated tests based on real user behavior**.

---
---

## What is strict option in Cucumber/Behave?
The **strict option** in Cucumber / Behave is used to **control how the test run behaves when there are undefined or pending steps**.

### Key Idea

👉 **Strict mode ensures that all steps must be properly implemented**.

If any step does not have a matching step definition → test execution will **fail**.

### Behavior

###  Strict = TRUE

* If any step is:

  * Undefined
  * Pending
    👉 Test is marked as **FAILED**


###  Strict = FALSE

* Undefined or pending steps are:
  👉 **Ignored or marked as skipped**
* Test may still pass


### Example (Cucumber – Java)

```java
@CucumberOptions(
    strict = true
)
```


### In Behave (Python)

Behave runs in **strict mode by default**
👉 If a step is missing → test fails immediately


### Why Use Strict Mode?

* ✔ Ensures all steps are implemented
* ✔ Avoids incomplete test cases
* ✔ Improves test reliability
* ✔ Catches missing automation early


### Simple Definition

👉 Strict option ensures that **tests fail if any step is not defined or implemented**.

### Real-Time Insight

In real projects:

* Always keep **strict = true**
* Otherwise, tests may give **false positive results** (looks passed but actually incomplete)

---
---
## What are the reports in Cucumber / Behave?

**Reporting** in Cucumber / Behave means **generating test execution results in a readable format** (HTML, JSON, etc.) so you can see which tests passed, failed, or were skipped.

### Key Idea

👉 Reports help you understand:

* Which scenarios passed/failed
* Execution time
* Error details
* Step-by-step results

### Types of Reports

### 1. Pretty / Console Report

* Simple output in terminal
* Shows steps and results

### 2. HTML Report (Most Used)

* User-friendly report in browser
* Includes:

  * Scenario status
  * Screenshots (if added)
  * Step details


### 3. JSON Report

* Used for integration with CI/CD tools
* Machine-readable format


### 4. JUnit/XML Report

* Used for Jenkins and other CI tools

###  Reporting in Cucumber (Java)

```java id="rep1"
@CucumberOptions(
  plugin = {
    "pretty",
    "html:target/cucumber-report.html",
    "json:target/cucumber.json",
    "junit:target/cucumber.xml"
  }
)
```

---

### Reporting in Behave (Python)

Run command:

```bash id="rep2"
behave -f pretty -f html -o report.html
```

👉 Or install third-party tools:

* **Allure Reports**
* Extent Reports

###  Advanced Reporting Tools

* Allure Report → Rich UI, graphs, history
* Extent Reports → Detailed HTML reports

###  Why Reporting is Important

* ✔ Track test results easily
* ✔ Identify failures quickly
* ✔ Share results with team
* ✔ Integrate with CI/CD (Jenkins, GitHub Actions)


### Real-Time Example

👉 After execution:

* Open HTML report
* Check failed scenarios
* View screenshots/logs
* Debug issues


### Simple Definition

👉 Reporting is the process of **generating detailed test execution results in readable formats like HTML or JSON**.

---
---

