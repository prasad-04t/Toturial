# 1. What is Playwright?

**Playwright** is a modern **web automation and testing framework** developed by Microsoft that allows you to automate browsers programmatically.

It is mainly used for:

* ✅ **UI Automation Testing**
* ✅ **End-to-End (E2E) Testing**
* ✅ **Cross-browser Testing**
* ✅ **Web Scraping**

 

## 🔍 Simple Definition

👉 **Playwright is a tool that controls web browsers (like Chrome, Firefox, Safari) using code to test web applications automatically.**

 

## 🌐 Supported Browsers

Playwright works with:

* **Chromium** (Chrome, Edge)
* **Firefox**
* **WebKit** (Safari engine)

 

## ⚙️ What Playwright Can Do

With Playwright, you can:

* Open websites
* Click buttons
* Enter text in forms
* Validate UI elements
* Take screenshots
* Record videos
* Intercept network requests
* Run tests in parallel

 

## 💻 Example (Python)

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://example.com")
    print(page.title())

    browser.close()

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        yield page

        browser.close()
```

 

## 🚀 Key Features

* ⚡ **Fast execution**
* 🔄 **Auto-wait (no need for explicit waits like Selenium)**
* 🌍 **Cross-browser support**
* 🧪 **Built-in testing capabilities**
* 📊 **Parallel execution support**
* 📡 **Network interception**

 

## 🆚 Why Playwright is Popular

Compared to traditional tools like Selenium:

* Less flaky tests
* Faster execution
* Handles modern web apps better
* No need for complex wait logic

## 📌 One-Line Interview Answer

👉 *“Playwright is a browser automation framework by Microsoft used for end-to-end testing and UI automation across multiple browsers with built-in auto-wait and parallel execution support.”* 

---
---

# 2. What is the difference between Selenium and Playwright?

Both **Selenium** and **Playwright** are popular tools for web automation, but they differ significantly in architecture, speed, and features.

 

## 📊 Key Differences (Easy Comparison)

| Feature                  | Selenium                           | Playwright                |
| ------------------------ | ---------------------------------- | ------------------------- |
| **Developer**            | Open-source (community-driven)     | Microsoft                 |
| **Architecture**         | WebDriver (external communication) | Direct browser control    |
| **Speed**                | Slower                             | ⚡ Faster                  |
| **Auto-wait**            | ❌ Manual waits required            | ✅ Built-in auto-wait      |
| **Parallel Execution**   | Needs Selenium Grid                | ✅ Built-in                |
| **Browser Support**      | Chrome, Firefox, Edge, Safari      | Chromium, Firefox, WebKit |
| **Handling Modern Apps** | Sometimes flaky                    | ✅ Very reliable           |
| **Network Interception** | Limited                            | ✅ Strong support          |
| **Setup Complexity**     | Requires drivers                   | ✅ Simple (no drivers)     |

 

## 🧠 Architecture Difference (Very Important)

### 🔹 Selenium Flow


* Test Script → WebDriver → Browser Driver → Browser
* Requires **ChromeDriver, GeckoDriver, etc.**
* Communication happens via **JSON Wire Protocol / W3C**

👉 More layers = slower + more chances of failure

### 🔹 Playwright Flow


* Test Script → Playwright → Browser
* No separate driver needed
* Direct communication with browsers

👉 Fewer layers = faster + more stable

 

## ⚡ Example: Waiting for Element

### Selenium

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "login"))
)
```

### Playwright

```python
page.click("#login")  # auto-waits internally
```

👉 Playwright automatically waits → less code, fewer failures

 

## 🚀 Key Advantages of Playwright

* Built-in **auto-waiting**
* Faster execution
* Supports **multiple tabs, iframes easily**
* Powerful **network mocking**
* Better handling of **dynamic UI (React, Angular apps)**

 

## ⚠️ When Selenium is Still Used

* Legacy frameworks
* Large existing projects
* Wide community support
* Integration with older tools

 

## 🎯 Interview Answer (Best)

👉 *“Selenium uses WebDriver and requires browser drivers, making it slower and more complex, while Playwright directly controls browsers with built-in auto-waiting, faster execution, and better support for modern web applications.”*

 

## 💡 Simple Way to Remember

* **Selenium = Old, stable, more setup**
* **Playwright = Modern, fast, less code**

---
---

# 3.What are the advantages of a Playwright?

Playwright has become very popular in modern automation because it solves many problems that tools like Selenium struggle with.


## ⚡ 1. Auto-Wait (No Manual Waits)

* Playwright **automatically waits** for elements to be ready
* No need for `sleep()` or explicit waits

👉 Result: **Less flaky tests + cleaner code**

## 🚄 2. Faster Execution

* Direct communication with browsers (no WebDriver layer)
* Optimized for speed

👉 Tests run **much faster than Selenium**

## 🌐 3. Cross-Browser Support

Supports multiple browsers with one API:

* Chromium (Chrome, Edge)
* Firefox
* WebKit (Safari engine)

👉 Write once → run everywhere

## 🔁 4. Built-in Parallel Execution

* Run multiple tests at the same time
* No need for Selenium Grid

👉 Saves **execution time in CI/CD**

## 🧠 5. Handles Modern Web Apps Easily

* Works smoothly with:

  * React
  * Angular
  * Vue

👉 Handles **dynamic elements, AJAX, SPAs** better

 

## 📡 6. Network Interception & Mocking

* Capture and modify API calls
* Mock backend responses

```python
page.route("**/api/*", lambda route: route.continue_())
```

👉 Very useful for **API + UI testing**

## 📸 7. Built-in Screenshots & Video Recording

* Capture screenshots automatically
* Record test execution videos

👉 Helps in **debugging failures**

## 🧪 8. Headless & Headed Mode

* Run tests in background (headless)
* Or visually (headed)

👉 Flexible for both **CI and debugging**

## 🔄 9. Multi-Tab & Multi-Context Support

* Easily handle:

  * Multiple tabs
  * Multiple users (contexts)

👉 Useful for **real-world scenarios**

 
## 🔐 10. Isolation with Browser Contexts

* Each test runs in a **separate clean environment**
* No shared cookies/session

👉 Improves **test reliability**

## 🧩 11. Easy Integration with Testing Tools

Works well with:

* pytest
* Allure
* Jenkins, GitHub Actions

## 🛠️ 12. No Driver Management

* No need for ChromeDriver/GeckoDriver
* Playwright manages browsers internally

👉 Easier setup

 

## 🎯 Best Interview Answer

👉 *“Playwright provides faster execution, built-in auto-waiting, parallel execution, cross-browser support, and better handling of modern web applications, making tests more reliable and easier to maintain compared to traditional tools.”*


## 💡 Simple Summary

* ✅ Fast
* ✅ Reliable
* ✅ Less code
* ✅ Modern

---
---

# 4. Name some disadvantages of Playwright.

Even though Playwright is powerful and modern, it still has some limitations you should know—especially for interviews.

 

## 🚧 1. Smaller Community Compared to Selenium

* Selenium has been around longer
* More tutorials, StackOverflow answers, and plugins

👉 Playwright community is growing, but still **not as large**

 

## 📚 2. Fewer Learning Resources (Relatively)

* Less documentation compared to Selenium (especially older legacy cases)
* Fewer real-world examples in some edge scenarios

👉 Beginners may sometimes struggle to find solutions

 

## 🧪 3. Limited Support for Legacy Systems

* Works best with **modern web applications**
* May not work well with:

  * Older browsers (like IE)
  * Legacy enterprise apps

👉 Selenium is better for **legacy compatibility**

 

## 🧰 4. Newer Tool (Less Mature Ecosystem)

* Still evolving
* Some integrations/tools are not as mature

👉 Enterprise adoption is still growing

 

## 🖥️ 5. Higher Resource Usage

* Playwright launches full browser instances
* Can consume more memory in large test suites

👉 Needs better system resources for large-scale runs

 

## 🔄 6. Frequent Updates

* Playwright updates often
* Sometimes requires updating code or dependencies

👉 Maintenance effort can increase

 

## 🧑‍💻 7. Requires Programming Knowledge

* Not very beginner-friendly for non-coders
* No strong record/playback ecosystem like some tools

👉 Requires **good coding skills (Python/JS/TS)**

 

## 🔌 8. Limited Third-Party Integrations (Compared to Selenium)

* Fewer plugins/tools compared to Selenium ecosystem

👉 Especially in older enterprise setups

 

## 📱 9. Mobile Testing Limitations

* Supports **mobile emulation**
* But not full real-device testing like Appium

👉 For real mobile testing → need other tools

 

## 🎯 Best Interview Answer

👉 *“Playwright’s disadvantages include a smaller community, limited support for legacy systems, higher resource usage, and a less mature ecosystem compared to Selenium, although it is rapidly evolving.”*

 

## 💡 Simple Way to Remember

* ❌ Smaller ecosystem
* ❌ Not for legacy apps
* ❌ More resource usage
* ❌ Still growing

---
---
# 5. What are the different testing types the Playwright supports?

Playwright is very versatile—it supports multiple types of testing used in real-world QA projects.

 

##  1. End-to-End (E2E) Testing

* Tests complete user workflows from start to finish
* Example: Login → Add to cart → Checkout

👉 Ensures the **entire application works correctly**

 

##  2. UI (User Interface) Testing

* Validates UI elements like:

  * Buttons
  * Forms
  * Labels
  * Layout

👉 Ensures the **frontend behaves correctly**

 

## 🔹 3. Cross-Browser Testing

* Run tests on:

  * Chromium
  * Firefox
  * WebKit

👉 Ensures app works across **different browsers**

 

## 🔹 4. API Testing

* Interact with backend APIs using Playwright
* Validate responses, status codes, data

```python
response = request.get("https://api.example.com")
assert response.status == 200
```

👉 Useful for **API + UI combined testing**

 

## 🔹 5. Visual Testing

* Compare screenshots to detect UI changes

```python
page.screenshot(path="homepage.png")
```

👉 Helps catch **layout or design issues**

 

## 🔹 6. Regression Testing

* Re-run test cases after changes
* Ensure existing functionality is not broken

👉 Very common in CI/CD pipelines

 

## 🔹 7. Smoke Testing

* Run a small set of critical tests
* Example: App launch, login

👉 Quick check before deeper testing

 

## 🔹 8. Integration Testing

* Validate interaction between:

  * UI + API
  * Multiple modules

👉 Ensures components work together

 

## 🔹 9. Performance (Basic Level)

* Measure page load time
* Monitor network requests

👉 Not a full performance tool, but useful for **basic checks**

 

## 🔹 10. Mobile Emulation Testing

* Simulate mobile devices

```python
context = browser.new_context(viewport={"width": 375, "height": 667})
```

👉 Test responsive UI without real devices

 

## 🔹 11. Accessibility Testing (Basic)

* Check accessibility features (with integrations)

👉 Helps ensure app is usable for all users

 

## 🔹 12. Parallel Testing

* Run multiple tests simultaneously

👉 Reduces execution time significantly

 

## 🎯 Best Interview Answer

👉 *“Playwright supports end-to-end testing, UI testing, API testing, cross-browser testing, regression testing, smoke testing, visual testing, and mobile emulation testing, making it a comprehensive tool for modern automation needs.”*

 

## 💡 Simple Memory Trick

Think:

👉 **E2E + UI + API + Cross-browser + Regression**

---
---

# 6. What are the programming languages that the playwright supports?

Playwright supports multiple modern programming languages, making it flexible for different types of automation engineers.

 

## 🌟 1. JavaScript (JS)

* Most commonly used language with Playwright
* Native support since Playwright was originally built for Node.js

👉 Widely used in frontend and automation

 

## 🌟 2. TypeScript (TS)

* Superset of JavaScript
* Provides type safety and better code structure

👉 Preferred for **large automation frameworks**

 

## 🌟 3. Python

* Simple and easy to learn
* Very popular among QA engineers

👉 Best choice if you are already using **pytest**

 

## 🌟 4. Java

* Common in enterprise environments
* Used with frameworks like TestNG or JUnit

👉 Useful if your company uses Java-based automation

 

## 🌟 5. .NET (C#)

* Supported via Microsoft ecosystem
* Works well with Visual Studio

👉 Preferred in **.NET-based projects**

 

## 📊 Quick Summary

| Language   | Usage                      |
| ---------- | -------------------------- |
| JavaScript | Most popular               |
| TypeScript | Best for scalable projects |
| Python     | Easy & widely used in QA   |
| Java       | Enterprise projects        |
| C# (.NET)  | Microsoft ecosystem        |

 

## 🎯 Best Interview Answer

👉 *“Playwright supports JavaScript, TypeScript, Python, Java, and C#, allowing testers and developers to choose a language based on their project and ecosystem.”*

 

## 💡 Tip for You (QA Engineer)

Since you are already working with Python:

👉 Stick with **Python + PyTest + Playwright**
👉 This combo is highly in demand in automation jobs

---
---

# 7. Briefly describe the commands that are used for Playwright installation and Execution of tests

Here are the **important commands** you should know for installing and running tests with Playwright.

 

## 1. Installation Commands

###  Install Playwright

```bash
pip install playwright
```

👉 Installs Playwright library in your Python environment

 

###  Install Browsers

```bash
playwright install
```

👉 Downloads required browsers:

* Chromium
* Firefox
* WebKit

 

###  Install PyTest Integration

```bash
pip install pytest-playwright
```

👉 Installs Playwright plugin for pytest

 

###  (Optional) Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

 

## 2. Test Execution Commands

###  Run All Tests

```bash
pytest
```

👉 Executes all test files in the project

 

###  Run Specific Test File

```bash
pytest tests/test_login.py
```

 

###  Run Specific Test Function

```bash
pytest tests/test_login.py::test_valid_login
```

 

###  Run Tests in Headed Mode (UI visible)

```bash
pytest --headed
```

 

###  Run Tests in Headless Mode (default)

```bash
pytest --headless
```

 

###  Run Tests in Specific Browser

```bash
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

 

###  Run Tests in Parallel

```bash
pytest -n 4
```

👉 Requires:

```bash
pip install pytest-xdist
```

 

###  Generate HTML Report

```bash
pytest --html=report.html
```

 

###  Generate Allure Report

```bash
pytest --alluredir=reports/
allure serve reports/
```

 

## 3. Useful Utility Commands

###  Code Generator (Record & Play)

```bash
playwright codegen https://example.com
```

👉 Opens browser + generates automation code

 

###  Run Playwright Script Directly

```bash
python script.py
```

 

## Best Interview Answer

👉 *“Playwright installation involves installing the library using pip, downloading browser binaries using `playwright install`, and optionally installing pytest-playwright for testing. Tests are executed using pytest commands with options like browser selection, headless/headed mode, and parallel execution.”*

 

## 💡 Quick Shortcut (Most Important Commands)

```bash
pip install pytest-playwright
playwright install
pytest
```

---
---

# 8. What is a Configuration File in Playwright explain?


A **configuration file** in Playwright is used to **store global settings and test configurations** so that you don’t need to repeat them in every test.

👉 It helps you **control how tests run** from one central place.

 

## 🔍 Simple Definition

👉 *A configuration file is a central file where we define settings like browser type, base URL, timeouts, reporting, and execution options for Playwright tests.*

 

## 📁 Common Config Files in Playwright + Python

In Python projects (with pytest), configuration is usually managed using:

###  1. `pytest.ini`

Used to define:

* Test paths
* Logging
* Default options
* Reporting

Example:

```ini
[pytest]
addopts = --browser chromium --headed --html=report.html
testpaths = tests

log_cli = true
log_cli_level = INFO
```

 

###  2. `conftest.py`

This is the **most important config file** in Playwright + PyTest.

Used for:

* Fixtures (setup/teardown)
* Browser setup
* Reusable configurations

Example:

```python
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        yield page

        browser.close()

```

👉 This setup will be reused across all tests

 

###  3. Custom Config File (Optional)

You can create your own config file like:

```python
# config.py
BASE_URL = "https://example.com"
TIMEOUT = 30000
BROWSER = "chromium"
```

Use in tests:

```python
from utils.config import BASE_URL
page.goto(BASE_URL)
```

 

##  Why Configuration File is Important

* ✅ Avoid code duplication
* ✅ Centralized control
* ✅ Easy to maintain
* ✅ Environment-based execution (QA, Dev, Prod)
* ✅ Improves framework design

 

##  Real Framework Usage

Typical structure:

```
project/
│
├── tests/
├── pages/
├── utils/
│   └── config.py
│
├── conftest.py
├── pytest.ini
```

 

## 🎯 Best Interview Answer

👉 *“In Playwright with Python, configuration files like pytest.ini and conftest.py are used to define global test settings such as browser configuration, base URL, fixtures, logging, and execution options, enabling centralized and reusable test setup.”*

 

## 💡 Simple Way to Remember

👉 **Config file = Central control of your framework**

---
---
# 📄 What is the **Page Class** in Playwright?

The **Page class** is one of the most important concepts in Playwright.

👉 It represents a **single browser tab (or window)** where you interact with a web application.

 

## 🔍 Simple Definition

👉 *A Page is an object that allows you to perform actions like navigating, clicking, typing, and validating elements on a web page.*

 

## 🌐 Real-Time Understanding

* When you open a browser → you create a **Browser**
* Inside it → you create a **Context**
* Inside context → you create a **Page**

👉 Flow:

```
Browser → Context → Page
```

 

## 💻 Example (Python)

```python
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        yield page

        browser.close()
```

 

## ⚙️ What You Can Do with Page

### 🔹 1. Navigate to URL

```python
page.goto("https://example.com")
```

 

### 🔹 2. Interact with Elements

```python
page.fill("#username", "admin")
page.click("#login")
```

 

### 🔹 3. Get Page Information

```python
page.title()
page.url
```

 

### 🔹 4. Assertions

```python
assert "Dashboard" in page.title()
```

 

### 🔹 5. Screenshots

```python
page.screenshot(path="page.png")
```

 

### 🔹 6. Handle Multiple Tabs

```python
new_page = context.new_page()
```

 

## 🧠 Why Page Class is Important

* Central object for all UI interactions
* Used in every test case
* Represents real user behavior

👉 Without Page → you cannot automate anything

 

## 🧩 In Framework (POM Usage)

Example:

```python
class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, locator):
        locator.click()

    def fill(self, locator, text):
        locator.fill(text)


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_btn = page.locator("#login")

    def login(self, username, password):
        self.fill(self.username, username)
        self.fill(self.password, password)
        self.click(self.login_btn)
```

👉 `page` is passed to all page objects

 

## 🎯 Best Interview Answer

👉 *“The Page class in Playwright represents a single browser tab or window and provides methods to interact with web elements, navigate pages, and perform validations, making it the core object for UI automation.”*

 

## 💡 Simple Way to Remember

👉 **Page = Browser Tab you automate**

---
---
# 11. How to navigate to specific URLs in Playwright explain with sample tests?

Navigation in Playwright means opening a web page using the **`page.goto()`** method.

## 🔍 Simple Definition

👉 *Navigation is the process of directing the browser to a specific URL using `page.goto()`.*

 

## ⚙️ Basic Syntax

```python
page.goto("https://example.com")
```

👉 This command opens the given URL in the browser.


## 💻 Example 1: Basic Navigation (Python)

```python
from playwright.sync_api import sync_playwright

def test_open_website():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://example.com")

        assert "Example" in page.title()

        browser.close()
```

 

## 🧪 Example 2: Using PyTest (Recommended)

```python
def test_google(page):
    page.goto("https://www.google.com")
    assert "Google" in page.title()
```

👉 Here, `page` is a fixture provided by pytest

 

## ⚡ Example 3: Navigation with Wait Options

Playwright allows you to control when navigation is considered complete.

```python
page.goto("https://example.com", wait_until="load")
page.goto("https://www.google.com", wait_until="commit")
page.goto("https://www.google.com", wait_until="domcontentloaded")
page.goto("https://www.google.com", wait_until="networkidle")
```

### Available options:

* `"load"` → Wait until full page load
* `"domcontentloaded"` → Wait until DOM is ready
* `"networkidle"` → Wait until no network activity

 

## 🔄 Example 4: Navigate + Perform Actions

```python
def test_login(page):
    page.goto("https://example.com/login")

    assert "Dashboard" in page.title()
```

 

## 🔙 Example 5: Navigation Controls

```python
page.go_back()      # Go to previous page
page.go_forward()   # Go to next page
page.reload()       # Refresh page
```

 

## ⏱️ Example 6: Timeout Handling

```python
page.goto("https://example.com", timeout=60000)
```

👉 Timeout is in milliseconds (60 sec)

 

## 🧠 Best Practices

* Use valid URLs (http/https)
* Prefer `base_url` in config for reusable navigation
* Avoid unnecessary waits (Playwright auto-waits)

 

## 🎯 Best Interview Answer

👉 *“In Playwright, navigation to a specific URL is done using the `page.goto()` method, which opens the desired web page and supports options like wait conditions and timeouts. It is commonly used in test cases to start user workflows.”*

 

## 💡 Simple Way to Remember

👉 **page.goto() = Open website**

---
---

## 📊 Reporters Supported by Playwright

Reporters in Playwright are used to **generate test execution results** in different formats (console, HTML, JSON, etc.).

👉 They help you **analyze test results, failures, logs, and execution details**.

 

## 🔍 Simple Definition

👉 *A reporter is a tool that collects and displays test results in a readable format.*

 

## 🧾 Built-in Reporters in Playwright (JS/TS – `@playwright/test`)

### 🔹 1. List Reporter (Default)

* Displays test results in a simple list format in console

Example output:

```
✓ test_login passed
✗ test_checkout failed
```

👉 Best for **quick debugging**

 

### 🔹 2. Line Reporter

* Shows one line per test (updates dynamically)

👉 Useful for **CI logs**

 

### 🔹 3. Dot Reporter

* Displays dots for each test

Example:

```
....F..
```

👉 Good for **large test suites**

 

### 🔹 4. HTML Reporter

* Generates a detailed HTML report with:

  * Pass/Fail status
  * Screenshots
  * Logs
  * Timeline

👉 Best for **report sharing**

 

### 🔹 5. JSON Reporter

* Outputs results in JSON format

👉 Useful for **custom integrations**

 

### 🔹 6. JUnit Reporter

* Generates XML reports

👉 Used in CI tools like Jenkins

 

### 🔹 7. GitHub Reporter

* Integrates with GitHub Actions

👉 Shows results directly in pipeline

 

### 🔹 8. Allure Reporter (External)

* Advanced reporting with:

  * Steps
  * Attachments
  * Graphs

👉 Requires integration with Allure

 

## 🧩 Configuration Example (JS/TS)

```javascript
// playwright.config.ts
export default {
  reporter: [
    ['list'],
    ['html'],
    ['junit', { outputFile: 'results.xml' }]
  ]
};
```

 

## 🐍 In Python (Your Case)

Playwright uses pytest reporters:

### Common ones:

* HTML Report → `pytest-html`
* Allure Report → `allure-pytest`
* JUnit XML → built-in pytest
* Console → default pytest output

Example:

```bash
pytest --html=report.html
pytest --alluredir=reports/
```

 

## 🎯 Best Interview Answer

👉 *“Playwright supports multiple reporters such as List, Line, Dot, HTML, JSON, and JUnit reporters for different reporting needs. It also supports advanced reporting using Allure. In Python, reporting is typically handled using pytest plugins like pytest-html and Allure.”*

 

## 💡 Simple Way to Remember

👉 **Console → HTML → JSON → CI (JUnit) → Advanced (Allure)**

---
---
## 🎯 What are Locators in Playwright?

**Locators** in Playwright are used to **find and interact with elements** on a web page.

👉 They help you identify elements like:

* Buttons
* Input fields
* Links
* Text

 

## 🔍 Simple Definition

👉 *A locator is a way to uniquely identify and interact with an element on a webpage.*

 

## 💡 Why Locators are Important

* Required for every UI action
* Helps avoid flaky tests
* Playwright locators are **auto-waiting & reliable**

 

## 🧩 Types of Locators in Playwright

 

## 🔹 1. get_by_role() (Recommended)

Uses **ARIA roles** (best practice)

```python
page.get_by_role("button", name="Login").click()
```

👉 Most reliable and readable

 

## 🔹 2. get_by_text()

Locate element using visible text

```python
page.get_by_text("Submit").click()
```

 

## 🔹 3. get_by_label()

Used for form fields

```python
page.get_by_label("Username").fill("admin")
```

 

## 🔹 4. get_by_placeholder()

```python
page.get_by_placeholder("Enter email").fill("test@mail.com")
```

 

## 🔹 5. get_by_test_id()

Used with test attributes

```python
page.get_by_test_id("login-btn").click()
```

👉 Requires `data-testid` attribute in HTML

 

## 🔹 6. CSS Selectors

```python
page.locator("#username").fill("admin")
page.locator(".login-btn").click()
```

 

## 🔹 7. XPath Locators

```python
page.locator("//input[@name='username']").fill("admin")
```

👉 Less recommended compared to Playwright locators

 

## 🔹 8. Chained Locators

```python
page.locator("form").locator("#username").fill("admin")
```

 

## 🔹 9. nth Element Locator

```python
page.locator(".item").nth(0).click()
```

 

## 🔹 10. Filtered Locators

```python
page.locator("button").filter(has_text="Submit").click()
```

 

## 💻 Example Test

```python
def test_login(page):
    page.goto("https://example.com/login")

    page.get_by_label("Username").fill("admin")
    page.get_by_label("Password").fill("password")
    page.get_by_role("button", name="Login").click()

    assert "Dashboard" in page.title()
```

 

## 🧠 Locator Priority (Best Practice)

1. ✅ `get_by_role()`
2. ✅ `get_by_label()`
3. ✅ `get_by_text()`
4. ✅ `get_by_test_id()`
5. ⚠️ CSS
6. ❌ XPath (last option)

 

## 🎯 Best Interview Answer

👉 *“Locators in Playwright are used to identify and interact with web elements. Playwright provides built-in locators like get_by_role, get_by_text, get_by_label, and CSS/XPath selectors, with auto-waiting and improved reliability.”*

 

## 💡 Simple Way to Remember

👉 **Locator = Find element on webpage**

---
---

## 🔤 Text Selectors in Playwright

Text selectors are used to **locate elements based on visible text** on the webpage. Playwright provides multiple powerful ways to handle text-based element selection.

 

## 🔍 Simple Definition

👉 *Text selectors allow you to find elements using the text they display to the user.*

 

## 🧩 Different Types of Text Selectors

 

## 🔹 1. `get_by_text()` (Recommended)

* Finds elements by visible text
* Most commonly used

```python
page.get_by_text("Login").click()
```

👉 Supports **partial & exact match**

 

## 🔹 2. Exact Text Match

```python
page.get_by_text("Login", exact=True).click()
```

👉 Matches only exact text

 

## 🔹 3. Partial Text Match

```python
page.get_by_text("Log").click()
```

👉 Matches elements containing the text

 

## 🔹 4. Text Selector using `locator()`

```python
page.locator("text=Login").click()
```

👉 Legacy but still supported

 

## 🔹 5. Using `has_text` Filter

```python
page.locator("button").filter(has_text="Submit").click()
```

👉 Finds element containing specific text inside it

 

## 🔹 6. Using `has` with Text

```python
page.locator("div", has=page.get_by_text("Welcome"))
```

👉 Select parent elements containing text

 

## 🔹 7. Regular Expression (Regex) Text

```python
import re
page.get_by_text(re.compile("Log.*")).click()
```

👉 Matches dynamic text patterns

 

## 🔹 8. Case-Insensitive Matching

```python
import re
page.get_by_text(re.compile("login", re.IGNORECASE)).click()
```

👉 Ignores uppercase/lowercase differences

 

## 🔹 9. Chained Text Selector

```python
page.locator("form").get_by_text("Submit").click()
```

👉 Scoped search within a parent element

 

## 🔹 10. nth Match with Text

```python
page.get_by_text("Item").nth(0).click()
```

👉 Select specific occurrence

 

## 💻 Example Test

```python
def test_text_selector(page):
    page.goto("https://example.com")

    page.get_by_text("More information").click()
```

 

## 🧠 Best Practices

* ✅ Prefer `get_by_text()` over `text=`
* ✅ Use exact match when needed
* ✅ Combine with filters for precision
* ⚠️ Avoid very generic text (like "Click")

 

## 🎯 Best Interview Answer

👉 *“Playwright provides multiple text selectors such as get_by_text, exact and partial matching, regex-based matching, and text filters like has_text. These help locate elements based on visible text in a reliable and flexible way.”*

 

## 💡 Simple Way to Remember

👉 **Text selector = Find element using visible text**

---
---

## ✅ Assertions in Playwright

Assertions are used to **verify that the application behaves as expected** during test execution.

👉 They help you **validate results** like:

* Page title
* Element visibility
* Text content
* URL
* Attributes

 

## 🔍 Simple Definition

👉 *Assertions are checks that compare expected results with actual results in a test.*

 

## 🧪 Types of Assertions in Playwright

 

## 🔹 1. Using `expect()` (Auto-Wait Assertions)

In JavaScript/TypeScript (`@playwright/test`):

```javascript
import { expect } from '@playwright/test';

await expect(page).toHaveTitle('Example Domain');
```

👉 Automatically waits until condition is met

 

## 🐍 In Python (Your Case)

Playwright uses pytest assertions.

 

## 🔹 2. Basic Assertion (Python)

```python
def test_title(page):
    page.goto("https://example.com")
    assert "Example" in page.title()
```

 

## 🔹 3. Assert Element Visibility

```python
def test_visibility(page):
    page.goto("https://example.com")

    element = page.locator("h1")
    assert element.is_visible()
```

 

## 🔹 4. Assert Text Content

```python
def test_text(page):
    page.goto("https://example.com")

    text = page.locator("h1").text_content()
    assert text == "Example Domain"
```

 

## 🔹 5. Assert URL

```python
def test_url(page):
    page.goto("https://example.com")

    assert "example.com" in page.url
```

 

## 🔹 6. Assert Element Count

```python
def test_count(page):
    page.goto("https://example.com")

    elements = page.locator("a")
    assert elements.count() > 0
```

 

## 🔹 7. Assert Attribute

```python
def test_attribute(page):
    page.goto("https://example.com")

    element = page.locator("a")
    assert element.get_attribute("href") is not None
```

 

## ⚡ Recommended (Playwright Assertions in Python)

Playwright also provides **auto-wait assertions**:

```python
from playwright.sync_api import expect

def test_expect(page):
    page.goto("https://example.com")

    expect(page).to_have_title("Example Domain")
```

👉 Better than normal assert because:

* Auto-waits
* More stable

 

## 🧠 Best Practices

* ✅ Use `expect()` for better stability
* ✅ Avoid hard waits
* ✅ Validate critical UI elements
* ✅ Keep assertions clear and simple

 

## 🎯 Best Interview Answer

👉 *“Assertions in Playwright are used to validate expected outcomes. In Python, we can use pytest assertions or Playwright’s built-in expect API for auto-waiting assertions like checking title, visibility, text, and URL.”*

 

## 💡 Simple Way to Remember

👉 **Assertion = Verify result**

---
---

## 🚫 Negating Assertions in Playwright

Negating an assertion means verifying that something **does NOT happen / is NOT true**.

👉 In simple terms:
**Positive assertion → check something exists**
**Negative assertion → check something does NOT exist**

 

## 🔍 Simple Definition

👉 *Negation in Playwright is used to verify “not conditions” like an element is not visible, text is not present, or URL is not matched.*

 

# 🧪 1. In JavaScript / TypeScript (`@playwright/test`)

Playwright provides `.not` keyword for negation.

 

## 🔹 Example: Title Should NOT Match

```javascript id="x5k6yq"
await expect(page).not.toHaveTitle('Google');
```

 

## 🔹 Element Should NOT Be Visible

```javascript id="tv3k1u"
await expect(page.locator('#error')).not.toBeVisible();
```

 

## 🔹 Text Should NOT Be Present

```javascript id="m9azl9"
await expect(page.locator('h1')).not.toHaveText('Error');
```

 

## 🔹 URL Should NOT Contain Value

```javascript id="7klj9x"
await expect(page).not.toHaveURL(/login/);
```

 

# 🐍 2. In Python (Your Case)

Using pytest and Playwright:

 

## 🔹 Basic Negation with `assert`

```python id="vljx9h"
def test_negative_title(page):
    page.goto("https://example.com")

    assert "Google" not in page.title()
```

 

## 🔹 Element Should NOT Be Visible

```python id="7n5m2q"
def test_not_visible(page):
    page.goto("https://example.com")

    element = page.locator("#error")
    assert not element.is_visible()
```

 

## 🔹 Text Should NOT Match

```python id="e3y6vt"
def test_text_not_match(page):
    page.goto("https://example.com")

    text = page.locator("h1").text_content()
    assert text != "Error"
```

 

# ⚡ 3. Recommended: Playwright `expect()` with Negation

```python id="2u9b1r"
from playwright.sync_api import expect

def test_negation(page):
    page.goto("https://example.com")

    expect(page).not_to_have_title("Google")
```

 

## 🔹 Element NOT Visible (Auto-wait)

```python id="d9c4n2"
expect(page.locator("#error")).not_to_be_visible()
```

 

## 🔹 Text NOT Present

```python id="4kp2vz"
expect(page.locator("h1")).not_to_have_text("Error")
```

 

## 🧠 Why Use Negation?

* Validate **error messages are NOT shown**
* Ensure **wrong pages are NOT opened**
* Verify **elements are hidden/removed**

 

## 🎯 Best Interview Answer

👉 *“In Playwright, negation of assertions is done using `.not` in JavaScript or `not_` prefixed methods in Python expect API, such as `not_to_have_title()` or `not_to_be_visible()`, to verify negative conditions.”*

 

## 💡 Simple Way to Remember

* JS → `.not`
* Python → `not_`
* pytest → `not`

👉 **Negation = Verify something should NOT happen**

---
---

## 🔎 Does Playwright Support XPath?

👉 **Yes, Playwright supports XPath**, but it is **not recommended as the first choice**.

Playwright encourages using:

* `get_by_role()`
* `get_by_text()`
* `get_by_label()`

👉 XPath is mainly used when other locators are not sufficient.

 

## 🔍 Simple Definition

👉 *XPath is a language used to locate elements in an HTML/XML document using path expressions.*

 

## ⚙️ How to Use XPath in Playwright (Python)

You can use XPath with `locator()`.

 

## 🔹 1. Basic XPath Example

```python
page.locator("//input[@name='username']").fill("admin")
```

 

## 🔹 2. Click Using XPath

```python
page.locator("//button[text()='Login']").click()
```

 

## 🔹 3. Using `xpath=` Prefix (Optional)

```python
page.locator("xpath=//input[@id='password']").fill("12345")
```

👉 Both ways work the same

 

## 🔹 4. XPath with Contains

```python
page.locator("//button[contains(text(),'Log')]").click()
```

 

## 🔹 5. XPath with Multiple Conditions

```python
page.locator("//input[@type='text' and @name='username']").fill("admin")
```

 

## 🔹 6. XPath Using Parent/Child

```python
page.locator("//div[@class='form']//input[@name='username']").fill("admin")
```

 

## 💻 Example Test

```python
def test_login_xpath(page):
    page.goto("https://example.com/login")

    page.locator("//input[@name='username']").fill("admin")
    page.locator("//input[@name='password']").fill("password")
    page.locator("//button[text()='Login']").click()

    assert "Dashboard" in page.title()
```

 

## ⚠️ Why XPath is NOT Preferred

* ❌ Slower compared to Playwright locators
* ❌ More brittle (breaks easily with UI changes)
* ❌ Less readable

 

## ✅ Best Practice Order

1. ✅ `get_by_role()`
2. ✅ `get_by_label()`
3. ✅ `get_by_text()`
4. ✅ `get_by_test_id()`
5. ⚠️ CSS
6. ❌ XPath (last option)

 

## 🎯 Best Interview Answer

👉 *“Yes, Playwright supports XPath, and it can be used with the locator() method. However, it is generally recommended to use Playwright’s built-in locators like get_by_role or get_by_text for better reliability and readability.”*

 

## 💡 Simple Way to Remember

👉 **XPath = Supported but avoid if better locators exist**

---
---

## ⚙️ Command Line Options in Playwright

Command line options are **arguments you pass while running tests** to control how Playwright executes them.

👉 They help you:

* Choose browser
* Control execution mode
* Generate reports
* Debug tests

 

## 🔍 Simple Definition

👉 *Command line options are parameters passed during test execution to customize behavior without changing code.*

 

## 🐍 In Python (Using pytest)

Playwright uses **pytest command-line options**.

 

# 🚀 Most Useful Command Line Options

 

## 🔹 1. Run All Tests

```bash
pytest
```

👉 Executes all test cases

 

## 🔹 2. Run Specific File

```bash
pytest tests/test_login.py
```

 

## 🔹 3. Run Specific Test

```bash
pytest tests/test_login.py::test_valid_login
```

 

## 🔹 4. Run in Headed Mode (UI visible)

```bash
pytest --headed
```

👉 Useful for debugging

 

## 🔹 5. Run in Headless Mode

```bash
pytest --headless
```

👉 Faster execution (default in CI)

 

## 🔹 6. Choose Browser

```bash
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

 

## 🔹 7. Run Tests in Parallel

```bash
pytest -n 4
```

👉 Requires:

```bash
pip install pytest-xdist
```

 

## 🔹 8. Generate HTML Report

```bash
pytest --html=report.html
```

👉 Requires:

```bash
pip install pytest-html
```

 

## 🔹 9. Generate Allure Report

```bash
pytest --alluredir=reports/
allure serve reports/
```

👉 Uses Allure

 

## 🔹 10. Run with Verbose Output

```bash
pytest -v
```

👉 Shows detailed test results

 

## 🔹 11. Stop on First Failure

```bash
pytest -x
```

👉 Useful for quick debugging

 

## 🔹 12. Re-run Failed Tests

```bash
pytest --lf
```

👉 Runs last failed tests only

 

## 🔹 13. Run Tests by Marker

```bash
pytest -m smoke
```

👉 Run only specific tagged tests

 

## 🔹 14. Capture Screenshots on Failure

```bash
pytest --screenshot=only-on-failure
```

 

## 🔹 15. Record Video

```bash
pytest --video=on
```

 

## 🔹 16. Slow Motion (Debugging)

```bash
pytest --slowmo 1000
```

👉 Adds delay (in ms) between actions

 

## 🧠 Why Command Line Options Are Important

* No need to modify code
* Easy control in CI/CD pipelines
* Flexible test execution
* Helps debugging

 

## 🎯 Best Interview Answer

👉 *“Command line options in Playwright allow testers to control test execution dynamically using parameters such as browser selection, headless mode, parallel execution, reporting, and debugging options, typically through pytest in Python.”*

 

## 💡 Simple Way to Remember

👉 **CLI options = Control tests without changing code**

---
---

## ⚙️ Important Command Line Options in Playwright (Python)

In Playwright (Python), we mainly use **pytest CLI options** to control test execution.

Here are the **most important options** you should remember (especially for interviews 👇):

 

# 🚀 Most Important CLI Options

 

## 🔹 1. Run All Tests

```bash
pytest
```

👉 Runs all test cases in the project

 

## 🔹 2. Run Specific Test File

```bash
pytest tests/test_login.py
```

 

## 🔹 3. Run Specific Test Method

```bash
pytest tests/test_login.py::test_valid_login
```

 

## 🔹 4. Run in Headed Mode

```bash
pytest --headed
```

👉 Opens browser UI (useful for debugging)

 

## 🔹 5. Run in Headless Mode

```bash
pytest --headless
```

👉 Runs in background (faster, used in CI)

 

## 🔹 6. Run on Specific Browser

```bash
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

 

## 🔹 7. Parallel Execution

```bash
pytest -n 4
```

👉 Run tests in parallel (requires `pytest-xdist`)

 

## 🔹 8. Verbose Output

```bash
pytest -v
```

👉 Shows detailed test results

 

## 🔹 9. Stop on First Failure

```bash
pytest -x
```

👉 Stops execution after first failure

 

## 🔹 10. Run Failed Tests Only

```bash
pytest --lf
```

👉 Runs last failed tests

 

## 🔹 11. Generate HTML Report

```bash
pytest --html=report.html
```

 

## 🔹 12. Generate Allure Report

```bash
pytest --alluredir=reports/
allure serve reports/
```

👉 Uses Allure

 

## 🔹 13. Run Tests by Marker

```bash
pytest -m smoke
```

👉 Execute only tagged tests

 

## 🔹 14. Take Screenshot on Failure

```bash
pytest --screenshot=only-on-failure
```

 

## 🔹 15. Record Video

```bash
pytest --video=on
```

 

## 🔹 16. Slow Motion Execution

```bash
pytest --slowmo 1000
```

👉 Adds delay for debugging

 

# 🧠 Quick Summary (Top 5 Must-Know)

👉 If interviewer asks **“important options”**, say:

* `pytest` → run tests
* `--browser` → choose browser
* `--headed` → UI mode
* `-n` → parallel execution
* `--html` / `--alluredir` → reporting

 

## 🎯 Best Interview Answer

👉 *“Important Playwright command line options include running tests using pytest, selecting browsers with --browser, running in headed mode using --headed, executing tests in parallel using -n, and generating reports using options like --html and --alluredir.”*

 

## 💡 Simple Trick to Remember

👉 **Run → Browser → Mode → Parallel → Report**

---
---
## 🖥️ Headed vs Headless Mode in Playwright

Playwright allows you to run browser tests in two modes:

* **Headed Mode** → Browser UI is visible
* **Headless Mode** → Browser runs in background (no UI)

 

## 🔍 Simple Definition

👉 *Headed mode shows the browser during execution, while headless mode runs tests without opening the browser window.*

 

## 🖥️ 1. Headed Mode (UI Visible)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2Ah40B8Agqk5RzDqtYFSgT0g.png)

![Image](https://user-images.githubusercontent.com/13063165/212738654-b573b7c9-05be-476f-ab4c-201bf4265bc0.png)

![Image](https://www.bannerbear.com/images/ghost/2022-11-30-top-5-automated-ui-testing-tools-to-make-testing-faster-in-2022/7.png)

![Image](https://assets.testmuai.com/resources/images/main/automated-browser-testing-hero-image.png)

### ✅ Features:

* Browser window is visible
* You can see actions happening
* Useful for debugging

### 💻 Example (Python):

```python
browser = p.chromium.launch(headless=False)
```

### 🔧 CLI:

```bash
pytest --headed
```

 

## ⚡ 2. Headless Mode (No UI)

![Image](https://www.twilio.com/content/dam/twilio-com/global/en/blog/legacy/2020/automated-headless-browser-scripting-in-node-js-with-playwright/Copy_of_Language_template_-_GENERIC3_3.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/0%2ACwAehmRrGdDUTph1.png)

![Image](https://user-images.githubusercontent.com/13063165/212738654-b573b7c9-05be-476f-ab4c-201bf4265bc0.png)

![Image](https://playwright.dev/assets/images/ui-mode-1958baf0398aef5e9c9b5c68c5d56f2d.png)

### ✅ Features:

* No browser window
* Faster execution
* Used in CI/CD pipelines

### 💻 Example (Python):

```python
browser = p.chromium.launch(headless=True)
```

### 🔧 CLI:

```bash
pytest --headless
```

 

## ⚖️ Key Differences

| Feature     | Headed Mode | Headless Mode |
| ----------- | ----------- | ------------- |
| Browser UI  | ✅ Visible   | ❌ Not visible |
| Speed       | Slower      | ⚡ Faster      |
| Debugging   | Easy        | Difficult     |
| CI/CD Usage | Rare        | ✅ Common      |

 

## 🧠 When to Use What?

* 👉 Use **Headed Mode** → While debugging tests
* 👉 Use **Headless Mode** → For automation pipelines & faster runs

 

## 🎯 Best Interview Answer

👉 *“Headed mode in Playwright runs tests with a visible browser UI, useful for debugging, while headless mode runs tests in the background without UI, providing faster execution and is commonly used in CI/CD pipelines.”*

 

## 💡 Simple Way to Remember

* 👀 Headed = See browser
* ⚡ Headless = Fast & invisible

---
---
## 📊 Does Playwright Support HTML Reports?

👉 **Yes, Playwright supports HTML reports**, but how you generate them depends on the language:

* **JavaScript/TypeScript** → Built-in HTML reporter (`@playwright/test`)
* **Python** → Use pytest plugins like **pytest-html**

 

# 🧩 1. HTML Reports in Playwright (Python)

Since you're using Python, the most common way is:

 

## 🔹 Install HTML Reporter

```bash
pip install pytest-html
```

 

## 🔹 Generate HTML Report

```bash
pytest --html=report.html
```

👉 After execution, a file like **`report.html`** is created

 

## 🔹 Open Report

* Open `report.html` in browser
* Shows:

  * Test status (Pass/Fail)
  * Execution time
  * Logs

 

## 🔹 Example with More Options

```bash
pytest --html=reports/report.html --self-contained-html
```

👉 `--self-contained-html` → embeds CSS/images (better for sharing)

 

# 🧪 Example Test

```python
def test_example(page):
    page.goto("https://example.com")
    assert "Example" in page.title()
```

Run:

```bash
pytest --html=report.html
```

 

# ⚡ 2. Add HTML Reporting in pytest.ini

You can configure it once:

```ini
[pytest]
addopts = --html=reports/report.html --self-contained-html
```

👉 Now just run:

```bash
pytest
```

 

# 🚀 3. HTML Reports in JavaScript (For Knowledge)

Playwright provides built-in HTML reporting:

```bash
npx playwright test --reporter=html
npx playwright show-report
```

 

# 📊 What HTML Report Contains

* ✅ Test results (Pass/Fail/Skipped)
* ⏱ Execution time
* 🧾 Logs
* 📸 Screenshots (if configured)
* 📍 Test details

 

# 🧠 Why HTML Reports Are Important

* Easy to share with team
* Clear visualization of results
* Helps debugging failures
* Used in CI/CD pipelines

 

# 🎯 Best Interview Answer

👉 *“Yes, Playwright supports HTML reports. In Python, HTML reports can be generated using pytest-html plugin with commands like `pytest --html=report.html`, while in JavaScript Playwright provides a built-in HTML reporter.”*

 

## 💡 Simple Way to Remember

👉 **Python → pytest-html**
👉 **JS → built-in HTML reporter**

---
---

## ⏱️ Timeouts in Playwright

Timeouts define **how long Playwright waits** for an action or condition before failing the test.

👉 They prevent tests from waiting forever when something goes wrong.

 

## 🔍 Simple Definition

👉 *A timeout is the maximum time Playwright waits for an operation (like element, navigation, or assertion) to complete.*

 

## 🧠 Why Timeouts Are Important

* Avoid infinite waiting
* Handle slow-loading pages
* Improve test reliability
* Control execution time

 

# 🧩 Types of Timeouts in Playwright

 

## 🔹 1. Default Timeout

* Applies to most Playwright actions (click, fill, locator, etc.)

```python
page.set_default_timeout(30000)  # 30 seconds
```

👉 Default is usually **30 seconds**

 

## 🔹 2. Navigation Timeout

* Used for page navigation (`goto`, `reload`, etc.)

```python
page.set_default_navigation_timeout(60000)  # 60 seconds
```

👉 Applies to:

* `page.goto()`
* `page.reload()`
* `page.go_back()`

 

## 🔹 3. Action Timeout (Per Action)

* Set timeout for a specific action

```python
page.click("#login", timeout=10000)
```

👉 Only applies to that single action

 

## 🔹 4. Assertion Timeout

Used with Playwright’s `expect()`

```python
from playwright.sync_api import expect

expect(page).to_have_title("Example", timeout=5000)
```

👉 Waits until condition is met or timeout occurs

 

## 🔹 5. Fixture / Test Timeout (PyTest)

Using pytest:

```python
import pytest

@pytest.mark.timeout(60)
def test_example(page):
    page.goto("https://example.com")
```

👉 Entire test must complete within 60 seconds

 

## 🔹 6. Global Timeout (Configuration Level)

You can define in config:

```python
# conftest.py or config
context.set_default_timeout(30000)
```

👉 Applies across all tests

 

## 🔹 7. Wait-for Timeout

Used with explicit waits:

```python
page.wait_for_selector("#login", timeout=5000)
```

👉 Waits for element to appear

 

## 🔹 8. Expect Polling Timeout

Used when Playwright keeps checking condition

```python
expect(page.locator("#status")).to_have_text("Success", timeout=10000)
```

 

# ⚖️ Quick Summary

| Timeout Type       | Purpose              |
| ------------------ | -------------------- |
| Default Timeout    | General actions      |
| Navigation Timeout | Page loads           |
| Action Timeout     | Specific action      |
| Assertion Timeout  | expect() validations |
| Test Timeout       | Whole test           |
| Wait Timeout       | wait_for methods     |

 

## 💻 Example

```python
def test_timeout_example(page):
    page.set_default_timeout(10000)

    page.goto("https://example.com", timeout=20000)

    page.click("#login", timeout=5000)

    from playwright.sync_api import expect
    expect(page).to_have_title("Example Domain", timeout=3000)
```

 

## 🎯 Best Interview Answer

👉 *“Timeouts in Playwright define how long the framework waits for actions, navigation, or assertions to complete. Types include default timeout, navigation timeout, action timeout, assertion timeout, and test-level timeout.”*

 

## 💡 Simple Way to Remember

👉 **Timeout = Maximum wait time**

---
---
## 🔄 Navigation Forward & Backward in Playwright

Playwright provides simple methods to navigate through the browser history—just like clicking **Back** and **Forward** buttons in a real browser.

 

## 🔍 Simple Definition

👉 *Playwright allows navigation to previous and next pages using built-in methods on the Page object.*

 

# 🔙 1. Navigate Back (Previous Page)

Use:

```python
page.go_back()
```

👉 Takes the browser to the **previous page in history**

 

## 💻 Example

```python
def test_go_back(page):
    page.goto("https://example.com")
    page.goto("https://google.com")

    page.go_back()   # Goes back to example.com

    assert "Example" in page.title()
```

 

# 🔜 2. Navigate Forward (Next Page)

Use:

```python
page.go_forward()
```

👉 Moves to the **next page in history**

 

## 💻 Example

```python
def test_go_forward(page):
    page.goto("https://example.com")
    page.goto("https://google.com")

    page.go_back()
    page.go_forward()   # Goes forward to google.com

    assert "Google" in page.title()
```

 

# 🔄 3. Reload Page

```python
page.reload()
```

👉 Refreshes the current page

 

# ⏱️ 4. With Wait Options

You can control loading behavior:

```python
page.go_back(wait_until="load")
page.go_forward(wait_until="domcontentloaded")
```

 

# ⚠️ Important Notes

* Navigation works only if **history exists**
* If no previous/next page → returns `None`
* Playwright automatically waits for navigation to complete

 

# 🧠 Real-Time Scenario

Example flow:

1. Open homepage
2. Go to login page
3. Go back to homepage
4. Go forward to login page

👉 Useful for testing **browser navigation behavior**

 

# 🎯 Best Interview Answer

👉 *“In Playwright, we can navigate backward using `page.go_back()` and forward using `page.go_forward()`, which simulate browser navigation through history.”*

 

## 💡 Simple Way to Remember

* 🔙 `go_back()` → Previous page
* 🔜 `go_forward()` → Next page
* 🔄 `reload()` → Refresh

---
---

## ⚙️ Performing Actions in Playwright

In Playwright, **actions** are operations you perform on web elements—just like a real user interacting with a browser.

👉 Examples:

* Click a button
* Enter text
* Select dropdown
* Hover over element

 

## 🔍 Simple Definition

👉 *Actions in Playwright are methods used to interact with elements on a webpage.*

 

# 🧩 Common Actions in Playwright (Python)

 

## 🔹 1. Click Action

```python
page.click("#login")
```

👉 Clicks a button or link

 

## 🔹 2. Type / Fill Text

```python
page.fill("#username", "admin")
page.fill("#password", "12345")
```

👉 Clears and enters text

 

## 🔹 3. Press Keyboard Keys

```python
page.press("#username", "Enter")
```

👉 Simulates keyboard actions

 

## 🔹 4. Hover Over Element

```python
page.hover("#menu")
```

👉 Useful for dropdown menus

 

## 🔹 5. Double Click

```python
page.dblclick("#submit")
```

 

## 🔹 6. Right Click

```python
page.click("#item", button="right")
```

 

## 🔹 7. Drag and Drop

```python
page.drag_to("#source", "#target")
```

 

## 🔹 8. Select Dropdown Value

```python
page.select_option("#country", "India")
```

 

## 🔹 9. Check / Uncheck Checkbox

```python
page.check("#agree")
page.uncheck("#agree")
```

 

## 🔹 10. Upload File

```python
page.set_input_files("#file-upload", "test.pdf")
```

 

## 🔹 11. Scroll Page

```python
page.mouse.wheel(0, 500)
```

 

## 🔹 12. Get Text

```python
text = page.text_content("h1")
```

 

## 🔹 13. Wait for Element

```python
page.wait_for_selector("#login")
```

 

# 💻 Example: Real Test Scenario

```python
def test_login(page):
    page.goto("https://example.com/login")

    page.fill("#username", "admin")
    page.fill("#password", "password")
    page.click("#login")

    assert "Dashboard" in page.title()
```

 

# 🧠 Best Practices

* ✅ Prefer `locator()` or `get_by_*()` methods
* ✅ Avoid hard waits (`time.sleep`)
* ✅ Use Playwright auto-waiting
* ✅ Keep actions readable

 

# 🎯 Best Interview Answer

👉 *“In Playwright, actions are performed using methods like click(), fill(), hover(), select_option(), and drag_to() on the Page or Locator objects to simulate user interactions with web elements.”*

 

## 💡 Simple Way to Remember

👉 **Actions = User interactions (click, type, select, etc.)**

---
---

## 🌐 Does Playwright Support Safari?

👉 **Yes, Playwright supports Safari**, but **not directly**.

Instead, it uses:

👉 **WebKit browser engine (Safari’s engine)**

 

## 🔍 Simple Explanation

* Safari is built on **WebKit**
* Playwright runs tests on **WebKit**
* So it **simulates Safari behavior**

👉 That means:

✔ You can test Safari-like behavior
❗ But not the exact Safari browser UI (in most cases)

 

## 🧩 How to Run Tests on Safari (WebKit)

 

## 🔹 1. Install WebKit Browser

```bash
playwright install
```

👉 This installs:

* Chromium
* Firefox
* WebKit (Safari engine)

 

## 🔹 2. Run Tests Using WebKit

### Using CLI:

```bash
pytest --browser webkit
```

 

## 🔹 3. Example Test

```python
def test_safari(page):
    page.goto("https://example.com")
    assert "Example" in page.title()
```

Run:

```bash
pytest --browser webkit
```

 

## ⚠️ Important Limitations

* ❌ Not real Safari browser UI
* ❌ Some Safari-specific features may differ
* ❌ Real Safari testing requires macOS

 

## 🍏 Real Safari Testing (Advanced)

👉 If you want **actual Safari browser testing**:

* Must run on **macOS**
* Use WebKit with system Safari (limited scenarios)

 

## ⚖️ Summary

| Feature                | Support            |
| ---------------------- | ------------------ |
| Safari engine (WebKit) | ✅ Yes              |
| Real Safari browser    | ⚠️ Limited         |
| Cross-platform         | ✅ Yes (via WebKit) |

 

## 🎯 Best Interview Answer

👉 *“Yes, Playwright supports Safari through the WebKit browser engine. Tests can be executed using the webkit option, which simulates Safari behavior, although it is not always the exact Safari browser.”*

 

## 💡 Simple Way to Remember

👉 **Playwright = WebKit = Safari engine**

---
---

## ⏳ Waiting for an Element in Playwright

Playwright is smart—it has **auto-waiting built in**, so in many cases you **don’t need explicit waits**.

👉 But when needed, you can explicitly wait for elements using different methods.

 

## 🔍 Simple Definition

👉 *Waiting means pausing test execution until an element appears, disappears, or reaches a specific state.*

 

# 🧠 1. Auto-Wait (Default Behavior)

Playwright automatically waits before actions:

```python
page.click("#login")  # waits until element is ready
```

👉 No need for manual wait in most cases ✅

 

# 🧩 2. Explicit Wait Methods

 

## 🔹 1. wait_for_selector()

Most commonly used method

```python
page.wait_for_selector("#login")
```

👉 Waits until element appears in DOM

 

### With State

```python
page.wait_for_selector("#login", state="visible")
```

States:

* `"attached"` → present in DOM
* `"visible"` → visible to user
* `"hidden"` → not visible
* `"detached"` → removed from DOM

 

## 🔹 2. Using Locator + wait_for()

```python
locator = page.locator("#login")
locator.wait_for(state="visible")
```

👉 Recommended modern approach

 

## 🔹 3. Using expect() (Best Practice ✅)

```python
from playwright.sync_api import expect

expect(page.locator("#login")).to_be_visible()
```

👉 Advantages:

* Auto-waits
* More stable
* Cleaner code

 

## 🔹 4. wait_for_timeout() (NOT Recommended ❌)

```python
page.wait_for_timeout(5000)
```

👉 Hard wait (5 seconds)

⚠️ Avoid unless absolutely necessary

 

## 🔹 5. wait_for_load_state()

```python
page.wait_for_load_state("load")
```

👉 Waits for page to fully load

Options:

* `"load"`
* `"domcontentloaded"`
* `"networkidle"`

 

# 💻 Example Test

```python
def test_wait_example(page):
    page.goto("https://example.com")

    # Wait for element
    page.wait_for_selector("h1")

    # Better way
    from playwright.sync_api import expect
    expect(page.locator("h1")).to_be_visible()
```

 

# ⚖️ Best Approach Priority

1. ✅ `expect()` (best)
2. ✅ `locator.wait_for()`
3. ✅ `wait_for_selector()`
4. ❌ `wait_for_timeout()`

 

## 🎯 Best Interview Answer

👉 *“Playwright provides auto-waiting by default, but explicit waits can be implemented using methods like wait_for_selector(), locator.wait_for(), and expect() for more reliable synchronization.”*

 

## 💡 Simple Way to Remember

👉 **Playwright = Auto-wait first, explicit wait if needed**

---
---
## 🌐 What is Browser Context in Playwright?

A **Browser Context** is an **isolated environment inside a browser**.

👉 Think of it like a **separate browser session** where data is not shared.

 

## 🔍 Simple Definition

👉 *A browser context is a clean, isolated session within a browser that has its own cookies, cache, and storage.*

 

## 🧠 Real-Time Understanding

Imagine:

* One browser (Chrome)
* Multiple users logged in at the same time

👉 Each user = separate **Browser Context**

 

## 🧩 Flow in Playwright

```
Browser → Context → Page
```

* **Browser** → Actual browser (Chromium, Firefox)
* **Context** → Isolated session
* **Page** → Tab inside that context

 

## 💻 Example (Python)

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()

    context = browser.new_context()   # New isolated session
    page = context.new_page()

    page.goto("https://example.com")

    browser.close()
```

 

## 🔐 Why Browser Context is Important

### ✅ 1. Test Isolation

* Each test runs independently
* No shared cookies or sessions

 

### ✅ 2. Multiple Users Simulation

```python
context1 = browser.new_context()
context2 = browser.new_context()
```

👉 Simulate:

* User 1 login
* User 2 login

 

### ✅ 3. Faster Than Opening New Browser

* Context is lightweight
* Faster than launching multiple browsers

 

### ✅ 4. Clean Environment

* No cache
* No local storage
* No session leakage

 

## ⚙️ Advanced Usage

### 🔹 Set Viewport / Device

```python
context = browser.new_context(
    viewport={"width": 1280, "height": 720}
)
```

 

### 🔹 Add Cookies

```python
context.add_cookies([{
    "name": "token",
    "value": "123",
    "domain": "example.com"
}])
```

 

### 🔹 Record Video

```python
context = browser.new_context(record_video_dir="videos/")
```

 

## 🎯 Best Interview Answer

👉 *“A browser context in Playwright is an isolated browser session that allows tests to run independently with separate cookies, cache, and storage, enabling parallel execution and multi-user testing.”*

 

## 💡 Simple Way to Remember

👉 **Context = Separate browser session**

---
---
## 🪟 Opening Multiple Windows (Tabs) in Playwright

In Playwright, multiple windows are handled as **multiple pages (tabs)** inside a **browser context**.

👉 Each new window/tab = a new **`Page` object**

 

## 🔍 Simple Definition

👉 *Multiple windows in Playwright are created and managed using multiple Page objects within the same browser context.*

 

# 🧩 Ways to Open Multiple Windows

 

## 🔹 1. Open a New Tab Manually

```python
new_page = context.new_page()
```

 

## 💻 Example

```python
from playwright.sync_api import sync_playwright

def test_multiple_tabs():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        page1 = context.new_page()
        page1.goto("https://example.com")

        page2 = context.new_page()
        page2.goto("https://google.com")

        browser.close()
```

👉 Two tabs opened:

* Tab 1 → example.com
* Tab 2 → google.com

 

## 🔹 2. Handle New Window (Popup)

When clicking a link opens a new window:

```python
with context.expect_page() as new_page_info:
    page.click("#open-window")

new_page = new_page_info.value
new_page.wait_for_load_state()
```

👉 Captures newly opened tab

 

## 🔹 3. Using `expect_popup()`

```python
with page.expect_popup() as popup_info:
    page.click("#open")

popup = popup_info.value
popup.wait_for_load_state()
```

👉 Specifically for popups

 

## 🔹 4. Switch Between Windows

```python
page1.bring_to_front()
page2.bring_to_front()
```

👉 Focus on a specific tab

 

## 🔹 5. Close a Specific Window

```python
page2.close()
```

 

# 💻 Real-Time Example

```python
def test_multi_window(page, context):
    page.goto("https://example.com")

    # Open new window
    with page.expect_popup() as popup_info:
        page.click("a[target='_blank']")

    new_page = popup_info.value

    new_page.wait_for_load_state()

    print(new_page.title())

    new_page.close()
```

 

# 🧠 Key Points

* Each tab = **Page object**
* All pages share same **context (session)**
* Use `expect_page()` or `expect_popup()` for new windows

 

# ⚖️ Summary

| Action        | Method               |
| ------------- | -------------------- |
| New tab       | `context.new_page()` |
| Capture popup | `expect_popup()`     |
| Switch tab    | `bring_to_front()`   |
| Close tab     | `page.close()`       |

 

## 🎯 Best Interview Answer

👉 *“In Playwright, multiple windows are handled using multiple Page objects within a browser context. New tabs can be opened using context.new_page() or captured using expect_popup() when triggered by user actions.”*

 

## 💡 Simple Way to Remember

👉 **Window = Page object**

---
---

## 🧩 Handling iFrames in Playwright

An **iFrame (inline frame)** is a webpage embedded inside another webpage.
👉 You **cannot directly interact** with elements inside an iframe using the main page—you must switch context.

 

## 🔍 Simple Definition

👉 *An iframe is a nested HTML document, and Playwright provides special methods to interact with elements inside it.*

 

# 🧠 Why Special Handling is Needed

* Elements inside iframe belong to a **different DOM**
* Normal locators won’t work directly

👉 You must use **frame-specific APIs**

 

# 🧩 Ways to Handle iFrames

 

## 🔹 1. Using `frame_locator()` (Recommended ✅)

Best and most modern approach

```python
page.frame_locator("#frame-id").locator("#username").fill("admin")
```

 

## 💻 Example

```python
def test_iframe(page):
    page.goto("https://example.com")

    frame = page.frame_locator("#login-frame")

    frame.locator("#username").fill("admin")
    frame.locator("#password").fill("12345")
    frame.locator("#login").click()
```

 

## 🔹 2. Using `frame()` Method

```python
frame = page.frame(name="frame-name")
frame.fill("#username", "admin")
```

👉 You can identify frame by:

* `name`
* `url`

 

## 🔹 3. Using `page.frames`

```python
for frame in page.frames:
    print(frame.url)
```

👉 Useful to debug multiple frames

 

## 🔹 4. Handling Nested iFrames

```python
page.frame_locator("#outer-frame") \
    .frame_locator("#inner-frame") \
    .locator("#button").click()
```

 

## 🔹 5. Using `expect()` with iFrame

```python
from playwright.sync_api import expect

frame = page.frame_locator("#frame-id")
expect(frame.locator("#login")).to_be_visible()
```

 

# ⚠️ Common Mistakes

* ❌ Trying `page.locator()` directly for iframe elements
* ❌ Not waiting for iframe to load
* ❌ Using wrong frame selector

 

# ⚖️ Best Approach Priority

1. ✅ `frame_locator()` (best & recommended)
2. ⚠️ `frame()`
3. ⚠️ `page.frames` (for debugging)

 

# 💡 Real-Time Scenario

* Login form inside iframe
* Payment gateway iframe
* Ads / embedded widgets

 

## 🎯 Best Interview Answer

👉 *“In Playwright, iframes are handled using frame_locator() or frame() methods. The recommended approach is frame_locator(), which allows direct interaction with elements inside an iframe.”*

 

## 💡 Simple Way to Remember

👉 **iFrame = Use frame_locator()**

---
---

## 🖱️ Click & Double Click Actions in Playwright

Playwright provides powerful methods to simulate **mouse interactions** like clicking and double-clicking with multiple options for control.

 

## 🔍 Simple Definition

👉 *Click actions simulate user mouse clicks on elements, while double-click performs two rapid clicks on an element.*

 

# 🧩 1. Click Action

 

## 🔹 Basic Click

```python
page.click("#login")
```

👉 Clicks on the element

 

## 🔹 Using Locator (Recommended)

```python
page.locator("#login").click()
```

👉 More stable and readable

 

## 🔹 Click with Options

 

### ✅ 1. Right Click

```python
page.click("#item", button="right")
```

👉 Opens context menu

 

### ✅ 2. Double Click via Option

```python
page.click("#btn", click_count=2)
```

👉 Performs double click using click()

 

### ✅ 3. Delay Between Click Actions

```python
page.click("#btn", delay=1000)
```

👉 Waits 1 second before clicking

 

### ✅ 4. Force Click

```python
page.click("#hidden-btn", force=True)
```

👉 Clicks even if element is not visible

 

### ✅ 5. Click with Modifiers (Keyboard Keys)

```python
page.click("#link", modifiers=["Control"])
```

👉 Simulates Ctrl + Click

 

### ✅ 6. Click at Specific Position

```python
page.click("#box", position={"x": 10, "y": 20})
```

👉 Clicks at given coordinates inside element

 

 

# 🧩 2. Double Click Action

 

## 🔹 Basic Double Click

```python
page.dblclick("#submit")
```

 

## 🔹 Using Locator

```python
page.locator("#submit").dblclick()
```

 

## 🔹 Double Click with Options

 

### ✅ 1. Double Click with Delay

```python
page.dblclick("#btn", delay=500)
```

 

### ✅ 2. Double Click with Modifiers

```python
page.dblclick("#item", modifiers=["Shift"])
```

 

### ✅ 3. Double Click at Position

```python
page.dblclick("#box", position={"x": 50, "y": 50})
```

 

# 💻 Example Test

```python
def test_click_actions(page):
    page.goto("https://example.com")

    # Normal click
    page.click("#login")

    # Right click
    page.click("#menu", button="right")

    # Double click
    page.dblclick("#submit")

    # Force click
    page.click("#hidden", force=True)
```

 

# 🧠 Best Practices

* ✅ Use `locator().click()` instead of `page.click()`
* ✅ Avoid `force=True` unless necessary
* ✅ Prefer `dblclick()` over `click_count=2` for clarity

 

# 🎯 Best Interview Answer

👉 *“Playwright provides click() and dblclick() methods to perform mouse interactions. These methods support options like button type, delay, force click, modifiers, and position to handle different user interaction scenarios.”*

 

## 💡 Simple Way to Remember

👉 **click() = single click**
👉 **dblclick() = double click**

---
---

## 🖱️ How to Perform Right-Click in Playwright

Right-click (also called **context click**) is used to open the **context menu** on an element.

 

## 🔍 Simple Definition

👉 *Right-click simulates clicking the right mouse button on an element.*

 

# 🧩 Ways to Perform Right-Click

 

## 🔹 1. Using `click()` with `button="right"` (Most Common ✅)

```python
page.click("#element", button="right")
```

 

## 🔹 2. Using Locator (Recommended)

```python
page.locator("#element").click(button="right")
```

👉 Best practice (more stable)

 

# 💻 Example Test

```python
def test_right_click(page):
    page.goto("https://example.com")

    page.locator("#menu").click(button="right")

    # Example validation (depends on app)
    assert page.locator(".context-menu").is_visible()
```

 

# 🧩 Additional Options

 

## 🔹 1. Right Click with Delay

```python
page.click("#element", button="right", delay=500)
```

 

## 🔹 2. Right Click with Modifiers (Keyboard)

```python
page.click("#element", button="right", modifiers=["Shift"])
```

👉 Simulates **Shift + Right Click**

 

## 🔹 3. Right Click at Specific Position

```python
page.click("#box", button="right", position={"x": 10, "y": 20})
```

 

# 🧠 Real-Time Use Cases

* Open context menu
* Copy / paste actions
* Right-click options in apps
* File management UI

 

# ⚠️ Common Mistakes

* ❌ Forgetting `button="right"`
* ❌ Not validating context menu
* ❌ Using unstable locators

 

## 🎯 Best Interview Answer

👉 *“In Playwright, right-click can be performed using the click() method with the option button='right', typically on a locator for better stability.”*

 

## 💡 Simple Way to Remember

👉 **Right-click = click(button="right")**

---
---
## 🧩 What are Fixtures in Playwright?

Fixtures are used to **set up and manage test dependencies** like browser, page, test data, etc.

👉 They help you **reuse code** and **avoid duplication** in tests.

 

## 🔍 Simple Definition

👉 *A fixture is a reusable setup function that prepares the environment before a test runs and cleans up after it.*

 

## 🐍 In Python (Using pytest)

Playwright uses **pytest fixtures**.

 

# 🧠 Why Fixtures are Important

* ✅ Reusable setup
* ✅ Cleaner test code
* ✅ Better maintainability
* ✅ Automatic setup & teardown

 

# 🧩 Built-in Playwright Fixtures

When using `pytest-playwright`, you get:

### 🔹 1. `browser`

* Launches browser instance

### 🔹 2. `context`

* Creates browser context (session)

### 🔹 3. `page`

* Opens a new tab

 

## 💻 Example Using Built-in Fixture

```python
def test_example(page):
    page.goto("https://example.com")
    assert "Example" in page.title()
```

👉 No setup needed — fixture handles everything

 

# 🧩 Custom Fixtures

You can create your own fixtures in `conftest.py`

 

## 🔹 Example: Custom Browser Fixture

```python
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def custom_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()
```

 

## 🔹 Use in Test

```python
def test_custom(custom_page):
    custom_page.goto("https://example.com")
    assert "Example" in custom_page.title()
```

 

# 🔄 Fixture Scope

You can control how often fixture runs:

```python
@pytest.fixture(scope="function")  # default
@pytest.fixture(scope="class")
@pytest.fixture(scope="module")
@pytest.fixture(scope="session")
```

 

## 📊 Scope Meaning

| Scope    | Runs               |
| -------- | ------------------ |
| function | Every test         |
| class    | Once per class     |
| module   | Once per file      |
| session  | Once per execution |

 

# ⚙️ Real Framework Usage

```python
@pytest.fixture(scope="session")
def browser():
    # launch once for all tests
```

 

# 🧠 Key Concept

👉 Fixtures use **`yield`**:

* Before `yield` → setup
* After `yield` → teardown

 

## 🎯 Best Interview Answer

👉 *“Fixtures in Playwright are reusable setup functions provided through pytest that manage test dependencies like browser, context, and page, enabling clean and maintainable test automation.”*

 

## 💡 Simple Way to Remember

👉 **Fixture = Setup + Reuse + Cleanup**

---
---

## 🤖 What is CodeGen in Playwright?

**CodeGen (Code Generator)** is a Playwright tool that helps you **automatically generate automation code** by recording your actions in the browser.

 

## 🔍 Simple Definition

👉 *CodeGen is a feature in Playwright that records user interactions in the browser and converts them into automation scripts.*

 

## 🧠 How It Works

1. You run CodeGen command
2. Browser opens
3. You perform actions (click, type, navigate)
4. Playwright generates code in real-time

👉 It acts like **record & play** feature

 

## ⚙️ Command to Start CodeGen

```bash
playwright codegen https://example.com
```

👉 This will:

* Open browser
* Open CodeGen panel
* Start recording actions

 

## 💻 Example Generated Code (Python)

If you click login and type:

```python
page.goto("https://example.com")
page.get_by_label("Username").fill("admin")
page.get_by_label("Password").fill("12345")
page.get_by_role("button", name="Login").click()
```

 

## 🧩 Features of CodeGen

* ✅ Auto-generates locators
* ✅ Supports multiple languages (Python, JS, Java, C#)
* ✅ Suggests best locators (`get_by_role`, etc.)
* ✅ Helps beginners quickly create tests

 

## 🎯 Use Cases

* Learning Playwright
* Creating initial test scripts
* Finding locators easily
* Debugging UI interactions

 

## ⚠️ Limitations

* ❌ Generated code may not follow framework structure
* ❌ Needs cleanup and optimization
* ❌ Not suitable for large-scale automation directly

 

## 🧠 Best Practice

👉 Use CodeGen for:

* Getting locators
* Creating basic scripts

👉 Then:

* Refactor into **Page Object Model (POM)**

 

## 🎯 Best Interview Answer

👉 *“CodeGen in Playwright is a tool that records user interactions in the browser and generates automation code automatically, helping testers quickly create scripts and identify locators.”*

 

## 💡 Simple Way to Remember

👉 **CodeGen = Record actions → Generate code**

---
---

## 🔁 Parameterizing Tests in Playwright

**Parameterization** means running the **same test with different sets of data**.

👉 Instead of writing multiple tests, you write **one test + multiple inputs**

 

## 🔍 Simple Definition

👉 *Parameterization allows executing a test multiple times with different input values.*

 

# 🐍 In Python (Using pytest)

Playwright uses **pytest parameterization**

 

# 🧩 1. Using `@pytest.mark.parametrize` (Most Important ✅)

 

## 🔹 Example: Multiple Login Data

```python
import pytest

@pytest.mark.parametrize("username,password", [
    ("admin", "admin123"),
    ("user", "user123"),
    ("test", "test123")
])
def test_login(page, username, password):
    page.goto("https://example.com/login")

    page.fill("#username", username)
    page.fill("#password", password)
    page.click("#login")

    assert "Dashboard" in page.title()
```

👉 Test runs **3 times with different data**

 

# 🧩 2. Single Parameter Example

```python
@pytest.mark.parametrize("search", ["apple", "banana", "mango"])
def test_search(page, search):
    page.goto("https://example.com")

    page.fill("#search", search)
    page.press("#search", "Enter")
```

 

# 🧩 3. Using Test Data from List/Dict

```python
test_data = [
    {"user": "admin", "pwd": "123"},
    {"user": "user", "pwd": "456"}
]

@pytest.mark.parametrize("data", test_data)
def test_login(page, data):
    page.goto("https://example.com")

    page.fill("#username", data["user"])
    page.fill("#password", data["pwd"])
```

 

# 🧩 4. Using Fixtures with Parameterization

```python
@pytest.fixture(params=["chromium", "firefox"])
def browser_name(request):
    return request.param
```

👉 Runs test with multiple browsers

 

# 🧩 5. External Data (Advanced)

You can read from:

* Excel
* JSON
* CSV

Example:

```python
import json

with open("data.json") as f:
    data = json.load(f)

@pytest.mark.parametrize("user", data)
def test_data(page, user):
    print(user)
```

 

# 🧠 Advantages

* ✅ Reduces duplicate code
* ✅ Improves test coverage
* ✅ Easy to maintain
* ✅ Supports data-driven testing

 

# ⚠️ Best Practices

* Keep test data separate
* Use meaningful parameter names
* Avoid too many parameters in one test

 

# 🎯 Best Interview Answer

👉 *“Parameterization in Playwright is achieved using pytest’s @pytest.mark.parametrize, which allows running the same test with multiple sets of data, enabling efficient data-driven testing.”*

 

## 💡 Simple Way to Remember

👉 **One test + multiple data = Parameterization**

---
---
## 📤 File Upload in Playwright (Python)

In Playwright, file upload is handled using **`set_input_files()`**.

 

## 🔍 Simple Definition

👉 *File upload in Playwright is done by sending a file path to an `<input type="file">` element.*

 

# 🧩 1. Basic File Upload Example

```python
def test_file_upload(page):
    page.goto("https://the-internet.herokuapp.com/upload")

    # Upload file
    page.set_input_files("#file-upload", "test_file.txt")

    # Click upload button
    page.click("#file-submit")

    # Assertion
    assert page.locator("#uploaded-files").text_content() == "test_file.txt"
```

 

# 🧩 2. Using Locator (Recommended)

```python
def test_file_upload_locator(page):
    page.goto("https://the-internet.herokuapp.com/upload")

    page.locator("#file-upload").set_input_files("test_file.txt")
    page.locator("#file-submit").click()

    assert "test_file.txt" in page.locator("#uploaded-files").text_content()
```

 

# 🧩 3. Upload Multiple Files

```python
page.set_input_files("#file-upload", ["file1.txt", "file2.txt"])
```

 

# 🧩 4. Upload File from Absolute Path

```python
import os

file_path = os.path.abspath("test_file.txt")
page.set_input_files("#file-upload", file_path)
```

 

# 🧩 5. Handle Hidden File Input

```python
page.locator("#file-upload").set_input_files("test_file.txt", force=True)
```

 

# 🧩 6. Remove Uploaded File

```python
page.set_input_files("#file-upload", [])
```

 

# 🧠 Important Points

* Works only with `<input type="file">`
* No need to handle OS popup (Playwright bypasses it)
* Supports single & multiple file upload

 

# 🎯 Best Interview Answer

👉 *“File upload in Playwright is performed using the set_input_files() method, which directly sets the file path to an input element without interacting with the OS file dialog.”*

 

## 💡 Simple Way to Remember

👉 **Upload = set_input_files()**

---
---

## 📥 File Download in Playwright (Python)

Playwright provides built-in support to **handle file downloads** without dealing with browser popups.

 

## 🔍 Simple Definition

👉 *File download in Playwright is handled using the `expect_download()` method, which captures the download event and allows saving the file.*

 

# 🧩 1. Basic File Download Example

```python
def test_file_download(page):
    page.goto("https://the-internet.herokuapp.com/download")

    # Start waiting for download before clicking
    with page.expect_download() as download_info:
        page.click("text=sample.txt")

    download = download_info.value

    # Save file to local path
    download.save_as("downloads/sample.txt")

    # Validation
    assert download.suggested_filename == "sample.txt"
```

 

# 🧩 2. Using Locator (Recommended)

```python
def test_download_locator(page):
    page.goto("https://the-internet.herokuapp.com/download")

    with page.expect_download() as download_info:
        page.locator("text=sample.txt").click()

    download = download_info.value
    download.save_as("downloads/sample.txt")
```

 

# 🧩 3. Save File with Dynamic Path

```python
import os

def test_download_dynamic(page):
    page.goto("https://the-internet.herokuapp.com/download")

    with page.expect_download() as download_info:
        page.click("text=sample.txt")

    download = download_info.value

    file_path = os.path.join(os.getcwd(), "downloads", download.suggested_filename)
    download.save_as(file_path)
```

 

# 🧩 4. Get Downloaded File Path

```python
path = download.path()
print(path)
```

👉 Returns temporary file path

 

# 🧩 5. Verify File Exists

```python
import os

assert os.path.exists(file_path)
```

 

# 🧠 Important Points

* Use `expect_download()` **before clicking download link**
* Playwright handles browser download dialog automatically
* You can save file anywhere using `save_as()`
* `suggested_filename` gives actual file name

 

# ⚠️ Common Mistakes

* ❌ Clicking before `expect_download()`
* ❌ Not saving file (`save_as`)
* ❌ Wrong locator for download link

 

# 🎯 Best Interview Answer

👉 *“In Playwright, file downloads are handled using the expect_download() method, which listens for the download event and allows saving the file using save_as().”*

 

## 💡 Simple Way to Remember

👉 **Download = expect_download() + save_as()**

---
---
## 🧲 Drag and Drop in Playwright

Drag and drop simulates a user **clicking an element, holding it, and dropping it onto another element**.

 

## 🔍 Simple Definition

👉 *Drag and drop is an action where an element is dragged from a source and dropped onto a target.*

 

# 🧩 1. Using `drag_to()` (Recommended ✅)

This is the **simplest and most reliable way**.

```python
page.drag_to("#source", "#target")
```

 

## 💻 Example

```python
def test_drag_and_drop(page):
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")

    page.drag_to("#column-a", "#column-b")
```

 

# 🧩 2. Using Locator (Best Practice)

```python
def test_drag_with_locator(page):
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")

    source = page.locator("#column-a")
    target = page.locator("#column-b")

    source.drag_to(target)
```

 

# 🧩 3. Using Mouse Actions (Advanced)

If `drag_to()` doesn’t work (rare cases):

```python
def test_drag_mouse(page):
    page.goto("https://example.com")

    source = page.locator("#source")
    target = page.locator("#target")

    source.hover()
    page.mouse.down()
    target.hover()
    page.mouse.up()
```

 

# 🧩 4. Drag with Position

```python
source.drag_to(target, source_position={"x": 10, "y": 10},
                         target_position={"x": 50, "y": 50})
```

👉 Useful for complex UI elements

 

# 🧠 Important Points

* Prefer `drag_to()` (built-in & stable)
* Works with both **page** and **locator**
* Use mouse actions only if needed

 

# ⚠️ Common Issues

* Element not visible
* Incorrect locator
* Drag-and-drop not supported by UI

 

# 💻 Validation Example

```python
def test_drag_validation(page):
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")

    source = page.locator("#column-a")
    target = page.locator("#column-b")

    source.drag_to(target)

    assert "A" in target.text_content()
```

 

# 🎯 Best Interview Answer

👉 *“Drag and drop in Playwright can be performed using the drag_to() method, which moves an element from a source to a target. Alternatively, mouse actions like hover, mouse.down(), and mouse.up() can be used for advanced scenarios.”*

 

## 💡 Simple Way to Remember

👉 **Drag = drag_to()**

---
---

## 🚨 Handling Browser Popups / Dialogs in Playwright

Browser dialogs are native popups like:

* Alert (`alert`)
* Confirmation (`confirm`)
* Prompt (`prompt`)

👉 Playwright provides a **`dialog` event handler** to manage them.

 

## 🔍 Simple Definition

👉 *Browser dialogs are handled in Playwright using event listeners like `page.on("dialog")`.*

 

# 🧩 Types of Dialogs

* **Alert** → OK button
* **Confirm** → OK / Cancel
* **Prompt** → Input + OK / Cancel

 

# 🧠 Key Concept

👉 You must handle dialog **before triggering it**

 

# 🧩 1. Handle Alert (Accept)

```python id="3o7dva"
def test_alert(page):
    page.goto("https://example.com")

    page.on("dialog", lambda dialog: dialog.accept())

    page.click("#alert-button")
```

 

# 🧩 2. Handle Confirm (Accept / Dismiss)

### Accept

```python id="s7n5va"
page.on("dialog", lambda dialog: dialog.accept())
```

### Dismiss (Cancel)

```python id="d8e3sh"
page.on("dialog", lambda dialog: dialog.dismiss())
```

 

# 🧩 3. Handle Prompt (Enter Value)

```python id="h8r1b2"
page.on("dialog", lambda dialog: dialog.accept("Hello World"))

page.click("#prompt-button")
```

👉 Sends input to prompt

 

# 🧩 4. Capture Dialog Message

```python id="g2yx8k"
def handle_dialog(dialog):
    print(dialog.message)
    dialog.accept()

page.on("dialog", handle_dialog)
```

 

# 🧩 5. Using `expect_event()` (Advanced)

```python id="lqpj7c"
with page.expect_event("dialog") as dialog_info:
    page.click("#alert-button")

dialog = dialog_info.value
print(dialog.message)
dialog.accept()
```

 

# ⚠️ Important Notes

* ❗ If not handled → test will fail
* ❗ Always register handler **before action**
* ❗ Only one dialog can be active at a time

 

# 💻 Real Example

```python id="yxrq8s"
def test_confirm(page):
    page.goto("https://example.com")

    page.on("dialog", lambda dialog: dialog.dismiss())

    page.click("#confirm-button")
```

 

# 🧠 Best Practices

* Use `page.on("dialog")` for simple cases
* Use `expect_event()` for controlled handling
* Always validate dialog message when needed

 

# 🎯 Best Interview Answer

👉 *“In Playwright, browser dialogs like alerts, confirms, and prompts are handled using the page.on('dialog') event, where we can accept, dismiss, or provide input to the dialog.”*

 

## 💡 Simple Way to Remember

👉 **Dialog = page.on("dialog")**

---
---
## 🧪 What is `testInfo` Object in Playwright?

The **`testInfo` object** provides **metadata and runtime information about the currently executing test**.

👉 It is mainly used in **Playwright Test (`@playwright/test`) – JavaScript/TypeScript**

 

## 🔍 Simple Definition

👉 *`testInfo` is an object that contains details about the test execution such as test name, status, duration, attachments, and more.*

 

## ⚠️ Important Note (Python vs JS)

* In **JavaScript/TypeScript** → `testInfo` is built-in
* In **Python** → similar functionality is handled using pytest features (fixtures, request object, etc.)

 

# 🧩 What Information `testInfo` Provides

 

## 🔹 1. Test Title

```javascript
test('login test', async ({ page }, testInfo) => {
  console.log(testInfo.title);
});
```

 

## 🔹 2. Test Status

```javascript
console.log(testInfo.status);  // passed / failed
```

 

## 🔹 3. Expected Status

```javascript
console.log(testInfo.expectedStatus);
```

 

## 🔹 4. Test Duration

```javascript
console.log(testInfo.duration);
```

 

## 🔹 5. Attachments (Screenshots, Logs)

```javascript
await testInfo.attach('screenshot', {
  path: 'screenshot.png',
  contentType: 'image/png',
});
```

 

## 🔹 6. Retry Information

```javascript
console.log(testInfo.retry);
```

 

## 🔹 7. Output Directory

```javascript
console.log(testInfo.outputDir);
```

 

## 🔹 8. File & Line Info

```javascript
console.log(testInfo.file);
console.log(testInfo.line);
```

 

# 💻 Example

```javascript
import { test, expect } from '@playwright/test';

test('example test', async ({ page }, testInfo) => {
  await page.goto('https://example.com');

  console.log(testInfo.title);
  console.log(testInfo.status);

  await expect(page).toHaveTitle(/Example/);
});
```

 

# 🐍 Equivalent in Python (Concept)

In Python, similar info can be accessed using:

```python
def test_example(request):
    print(request.node.name)   # test name
```

👉 Provided by pytest

 

# 🧠 Why `testInfo` is Useful

* ✅ Debugging failures
* ✅ Adding attachments (screenshots, logs)
* ✅ Accessing test metadata
* ✅ Custom reporting

 

# 🎯 Best Interview Answer

👉 *“The testInfo object in Playwright provides runtime information about the current test such as its name, status, duration, and attachments, and is mainly used in Playwright’s JavaScript test runner.”*

 

## 💡 Simple Way to Remember

👉 **testInfo = Test details object**

---
---

## ❌ What is `testError` Object in Playwright?

The **`testError` object** represents the **error information when a test fails**.

👉 It contains details like:

* Error message
* Stack trace
* Failure reason

 

## 🔍 Simple Definition

👉 *`testError` is an object that holds information about a failure that occurred during test execution.*

 

## ⚠️ Important Note (JS vs Python)

* In **JavaScript/TypeScript (`@playwright/test`)** → `testError` is available via `testInfo.errors`
* In **Python** → similar behavior is handled using pytest (exceptions, logs)

 

# 🧩 How `testError` is Used (JS/TS)

You usually access it through **`testInfo`**

 

## 🔹 Example

```javascript
import { test } from '@playwright/test';

test('failing test', async ({ page }, testInfo) => {
  await page.goto('https://example.com');

  try {
    throw new Error('Something went wrong');
  } catch (error) {
    console.log(error.message);   // error message
    console.log(error.stack);     // stack trace
  }
});
```

 

## 🔹 Access Errors via `testInfo`

```javascript
if (testInfo.errors.length > 0) {
  console.log(testInfo.errors[0].message);
}
```

 

# 🧩 What Information `testError` Contains

* ❌ Error message
* 📍 Stack trace
* 🧪 Failed step details
* ⏱ Time of failure

 

# 🐍 Equivalent in Python (Important)

In Python (Playwright + pytest), we use **exceptions**:

 

## 🔹 Example

```python
def test_error_example(page):
    page.goto("https://example.com")

    assert "Google" in page.title()   # This will fail
```

👉 pytest automatically captures:

* Assertion error
* Stack trace
* Failure details

 

## 🔹 Custom Error Handling

```python
try:
    assert False, "Test failed"
except AssertionError as e:
    print(e)
```

 

# 🧠 Why `testError` is Useful

* Debug test failures
* Capture failure details
* Add logs/screenshots on failure
* Improve reporting

 

# 🎯 Best Interview Answer

👉 *“The testError object in Playwright contains details about test failures such as error messages and stack traces, and is typically accessed through testInfo in JavaScript. In Python, similar behavior is handled using pytest exceptions.”*

 

## 💡 Simple Way to Remember

👉 **testError = Failure details**

---
---
## 🌍 Global Setup & Teardown in Playwright

**Global Setup and Teardown** are used to run code **once before all tests** and **once after all tests**.

👉 They are useful for preparing and cleaning up the test environment.

 

## 🔍 Simple Definition

👉 *Global setup runs before the entire test suite starts, and global teardown runs after all tests are completed.*

 

# 🧠 Why Use Global Setup & Teardown?

* ✅ Login once and reuse session
* ✅ Setup test data
* ✅ Initialize environment
* ✅ Clean up data after tests

 

# 🧩 1. Global Setup

👉 Runs **once before all tests**

### 🔹 Example Use Cases:

* Launch browser
* Login and save session
* Create test data

 

## 💻 Example (Concept – Python)

Using pytest:

```python
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session", autouse=True)
def global_setup():
    print("Starting test suite...")
    yield
    print("Test suite execution completed")
```

 

# 🧩 2. Global Teardown

👉 Runs **once after all tests**

### 🔹 Example Use Cases:

* Close browser
* Delete test data
* Clear logs

 

## 💻 Example

```python
@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    print("Setup before all tests")

    yield   # tests run here

    print("Teardown after all tests")
```

 

# 🧩 3. Playwright (JS) Global Setup (For Knowledge)

```javascript
// global-setup.js
module.exports = async () => {
  console.log("Global Setup");
};
```

```javascript
// playwright.config.js
export default {
  globalSetup: './global-setup.js',
};
```

 

# 🧩 Real-Time Example

👉 Login once and reuse session:

```python
@pytest.fixture(scope="session")
def login_session(page):
    page.goto("https://example.com/login")
    page.fill("#username", "admin")
    page.fill("#password", "123")
    page.click("#login")
```

 

# ⚖️ Summary

| Type            | When it Runs     |
| --------------- | ---------------- |
| Global Setup    | Before all tests |
| Global Teardown | After all tests  |

 

# 🧠 Key Points

* Runs only **once per execution**
* Uses **session scope** in pytest
* Improves performance
* Avoids repeated setup

 

## 🎯 Best Interview Answer

👉 *“Global setup and teardown in Playwright are used to execute code once before and after the entire test suite, typically for initializing and cleaning up the test environment, and in Python this is implemented using pytest session-scoped fixtures.”*

 

## 💡 Simple Way to Remember

👉 **Start → Global Setup**
👉 **End → Global Teardown**

 
 
## 🌐 Capturing Network Logs in Playwright

Playwright allows you to **monitor, capture, and inspect network requests and responses** during test execution.

👉 Very useful for:

* API validation
* Debugging
* Performance checks

 

## 🔍 Simple Definition

👉 *Network logging means tracking HTTP requests and responses made by the browser.*

 

# 🧩 Ways to Capture Network Logs

 

## 🔹 1. Capture All Requests

```python
def test_capture_requests(page):
    def log_request(request):
        print("Request URL:", request.url)

    page.on("request", log_request)

    page.goto("https://example.com")
```

👉 Logs all outgoing requests

 

## 🔹 2. Capture All Responses

```python
def test_capture_responses(page):
    def log_response(response):
        print("Response URL:", response.url, "Status:", response.status)

    page.on("response", log_response)

    page.goto("https://example.com")
```

👉 Logs all responses

 

## 🔹 3. Capture Specific API Call

```python
def test_specific_api(page):
    def log_api(response):
        if "api" in response.url:
            print("API:", response.url, response.status)

    page.on("response", log_api)

    page.goto("https://example.com")
```

 

## 🔹 4. Get Request & Response Data

```python
def test_request_data(page):
    def handle_response(response):
        if "api" in response.url:
            print(response.json())

    page.on("response", handle_response)

    page.goto("https://example.com")
```

 

## 🔹 5. Wait for Specific Network Call

```python
def test_wait_for_api(page):
    with page.expect_response("**/api/users") as response_info:
        page.click("#load-users")

    response = response_info.value
    print(response.status)
```

 

## 🔹 6. Intercept & Modify Requests (Advanced)

```python
def test_intercept(page):
    page.route("**/api/*", lambda route: route.continue_())

    page.goto("https://example.com")
```

 

## 🔹 7. Block Network Requests

```python
page.route("**/*.png", lambda route: route.abort())
```

👉 Blocks images

 

# 🧠 Real-Time Use Cases

* Validate API responses in UI tests
* Debug failed network calls
* Mock backend responses
* Monitor performance

 

# ⚠️ Best Practices

* Filter specific APIs instead of logging all
* Avoid heavy logging in large tests
* Use `expect_response()` for validation

 

# 🎯 Best Interview Answer

👉 *“In Playwright, network logs can be captured using page.on('request') and page.on('response') events, and specific API calls can be handled using expect_response() or route interception.”*

 

## 💡 Simple Way to Remember

👉 **request = outgoing**
👉 **response = incoming**

---
---
## 📸 Capturing Screenshots in Playwright

Playwright provides built-in methods to take **screenshots of the page or specific elements** during test execution.

👉 Useful for:

* Debugging failures
* Reporting
* Visual validation

 

## 🔍 Simple Definition

👉 *Screenshots capture the current state of the webpage or element as an image.*

 

# 🧩 1. Capture Full Page Screenshot

```python
page.screenshot(path="page.png")
```

👉 Captures visible viewport

 

## 🔹 Full Page (Entire Scrollable Page)

```python
page.screenshot(path="full_page.png", full_page=True)
```

 

# 🧩 2. Capture Element Screenshot

```python
page.locator("#logo").screenshot(path="logo.png")
```

👉 Captures only that element

 

# 🧩 3. Screenshot with Options

 

## 🔹 Change Image Type

```python
page.screenshot(path="page.jpeg", type="jpeg")
```

 

## 🔹 Set Quality (JPEG only)

```python
page.screenshot(path="page.jpeg", quality=80)
```

 

## 🔹 Clip Specific Area

```python
page.screenshot(
    path="clip.png",
    clip={"x": 0, "y": 0, "width": 300, "height": 200}
)
```

 

# 🧩 4. Screenshot on Failure (PyTest)

```python
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")
```

👉 Automatically captures screenshot on failure

 

# 🧩 5. Screenshot as Bytes

```python
image = page.screenshot()
```

👉 Useful for attaching in reports

 

# 🧠 Best Practices

* ✅ Capture screenshots on failure
* ✅ Use meaningful file names
* ✅ Store in reports folder
* ✅ Avoid unnecessary screenshots

 

# 💻 Example Test

```python
def test_screenshot(page):
    page.goto("https://example.com")

    page.screenshot(path="homepage.png")

    assert "Example" in page.title()
```

 

# 🎯 Best Interview Answer

👉 *“In Playwright, screenshots can be captured using the screenshot() method on the page or locator, with options like full_page, clip, and image type, and can also be integrated into test reports.”*

 

## 💡 Simple Way to Remember

👉 **Screenshot = screenshot()**

---
---
## 🌐 Does Playwright Support API Testing?

👉 **Yes, Playwright supports API testing** using its built-in **APIRequestContext**.

You can:

* Send HTTP requests (GET, POST, PUT, DELETE)
* Validate responses
* Combine **API + UI testing** in one framework

 

## 🔍 Simple Definition

👉 *Playwright API testing allows sending and validating HTTP requests directly without using a browser.*

 

# 🧩 1. How to Perform API Testing in Playwright (Python)

Playwright provides a **`request` fixture** when using pytest.

 

## 🔹 1. GET Request Example

```python
def test_get_api(request):
    response = request.get("https://reqres.in/api/users/2")

    assert response.status == 200

    data = response.json()
    assert data["data"]["id"] == 2
```

 

## 🔹 2. POST Request Example

```python
def test_post_api(request):
    payload = {
        "name": "John",
        "job": "QA"
    }

    response = request.post("https://reqres.in/api/users", data=payload)

    assert response.status == 201
```

 

## 🔹 3. PUT Request Example

```python
def test_put_api(request):
    response = request.put(
        "https://reqres.in/api/users/2",
        data={"name": "Updated"}
    )

    assert response.status == 200
```

 

## 🔹 4. DELETE Request Example

```python
def test_delete_api(request):
    response = request.delete("https://reqres.in/api/users/2")

    assert response.status == 204
```

 

# 🧩 2. Send Headers & Auth

```python
def test_api_with_headers(request):
    response = request.get(
        "https://api.example.com/data",
        headers={"Authorization": "Bearer token"}
    )

    assert response.status == 200
```

 

# 🧩 3. Validate Response Body

```python
def test_response_validation(request):
    response = request.get("https://reqres.in/api/users/2")

    json_data = response.json()

    assert "data" in json_data
    assert json_data["data"]["email"] is not None
```

 

# 🧩 4. Combine API + UI Testing

```python
def test_api_ui(page, request):
    # Create user via API
    response = request.post(
        "https://reqres.in/api/users",
        data={"name": "test"}
    )

    assert response.status == 201

    # Validate in UI
    page.goto("https://example.com/users")
```

 

# 🧠 Advantages of API Testing in Playwright

* ✅ No need for separate tool (like Postman/Requests)
* ✅ Faster execution
* ✅ Easy integration with UI tests
* ✅ Built-in request handling

 

# ⚠️ Best Practices

* Validate status code + response body
* Use test data dynamically
* Avoid hardcoding values
* Combine API + UI for end-to-end testing

 

# 🎯 Best Interview Answer

👉 *“Yes, Playwright supports API testing using its built-in request context, allowing us to send HTTP requests like GET, POST, PUT, and DELETE and validate responses, making it possible to combine API and UI testing in a single framework.”*

 

## 💡 Simple Way to Remember

👉 **Playwright = UI + API testing in one tool**

---
---

## 👀 What is Visual Testing in Playwright?

**Visual Testing** is the process of verifying the **UI appearance of an application** by comparing screenshots.

👉 It checks:

* Layout
* Colors
* Fonts
* Alignment
* UI changes

 

## 🔍 Simple Definition

👉 *Visual testing ensures that the user interface looks correct by comparing current UI with expected UI (baseline images).*

 

## 🧩 How It Works

1. Capture a **baseline screenshot**
2. Run test → capture new screenshot
3. Compare both images
4. Highlight differences

 

## 💻 Example (Playwright)

```python
def test_visual(page):
    page.goto("https://example.com")

    page.screenshot(path="current.png")

    # Compare manually or using tools
```

👉 In advanced usage, tools compare images automatically

 

## 🎯 Types of Visual Testing

 

### 🔹 1. Full Page Comparison

* Entire page is compared

 

### 🔹 2. Element-Level Comparison

```python
page.locator("#logo").screenshot(path="logo.png")
```

👉 Compare only specific element

 

### 🔹 3. Responsive Testing

* Validate UI across devices

 

## 🧠 Why Do We Need Visual Testing?

 

## ✅ 1. Detect UI Bugs

* Broken layout
* Missing elements
* Overlapping text

 

## ✅ 2. Catch CSS Issues

* Alignment problems
* Font changes
* Color issues

 

## ✅ 3. Prevent Regression Issues

👉 After code changes:

* UI should not break

 

## ✅ 4. Improve User Experience

👉 Ensures UI looks correct for users

 

## ✅ 5. Cross-Browser UI Validation

👉 UI may look different in:

* Chrome
* Firefox
* Safari

 

## ⚠️ Without Visual Testing

* UI bugs go unnoticed
* Functional tests pass but UI is broken
* Poor user experience

 

## 🧠 Real-Time Example

👉 Login button:

* Functionally works ✅
* But not visible ❌

👉 Only visual testing catches this

 

## 🔧 Tools Used with Playwright

* Built-in screenshots
* Allure (for attachments)
* Third-party tools:

  * Applitools
  * Percy

 

## 🎯 Best Interview Answer

👉 *“Visual testing is the process of validating the UI appearance of an application by comparing screenshots to detect layout and design changes. It is important to catch UI regressions and ensure a consistent user experience.”*

 

## 💡 Simple Way to Remember

👉 **Functional testing = Works?**
👉 **Visual testing = Looks correct?**

---
---
## 👀 Simple Visual Test in Playwright (Python)

Here’s a **basic visual testing example** using screenshots.

 

## 🧩 1. Capture Baseline Screenshot (First Run)

```python
def test_visual_baseline(page):
    page.goto("https://example.com")

    # Capture baseline image
    page.screenshot(path="baseline.png", full_page=True)
```

👉 Run this once → saves **baseline image**

 

## 🧩 2. Compare with New Screenshot

```python
from playwright.sync_api import expect

def test_visual_compare(page):
    page.goto("https://example.com")

    # Take current screenshot
    page.screenshot(path="current.png", full_page=True)

    # Basic validation (title check)
    assert "Example" in page.title()
```

 

## 🧩 3. Better Visual Testing (Using Playwright Expect)

👉 Playwright provides built-in visual comparison:

```python
from playwright.sync_api import expect

def test_visual(page):
    page.goto("https://example.com")

    # Compare screenshot with baseline
    expect(page).to_have_screenshot()
```

👉 First run:

* Creates baseline image

👉 Next runs:

* Compares with baseline
* Fails if UI changes

 

## 🧩 4. Element-Level Visual Test

```python
from playwright.sync_api import expect

def test_element_visual(page):
    page.goto("https://example.com")

    element = page.locator("h1")

    expect(element).to_have_screenshot()
```

 

## 🧠 Important Notes

* First run → creates **baseline snapshot**
* Next runs → performs **comparison**
* Differences → test fails

 

## ⚠️ Best Practices

* Use stable UI pages
* Avoid dynamic content (ads, timestamps)
* Use element-level comparison for precision

 

## 🎯 Best Interview Answer

👉 *“Visual testing in Playwright can be implemented using screenshots or built-in expect().to_have_screenshot() method, which compares the current UI with a baseline image to detect visual changes.”*

 

## 💡 Simple Way to Remember

👉 **Visual Test = Screenshot + Compare**

---
---
## 📊 Configure Multiple Reporters in Playwright

You can configure **multiple reporters** to generate different types of reports (HTML, Allure, JUnit, etc.) in a single test run.

 

## 🔍 Simple Definition

👉 *Multiple reporters allow generating different report formats simultaneously for better analysis and CI/CD integration.*

 

# 🐍 In Python (Using pytest)

Playwright (Python) uses **pytest plugins** for reporting.

 

# 🧩 1. Install Required Reporters

```bash
pip install pytest-html allure-pytest
```

 

# 🧩 2. Run with Multiple Reporters (CLI)

```bash
pytest --html=reports/report.html --self-contained-html --alluredir=reports/allure-results
```

👉 This generates:

* ✅ HTML Report
* ✅ Allure Report

 

# 🧩 3. Configure in `pytest.ini` (Recommended)

```ini
[pytest]
addopts = --html=reports/report.html --self-contained-html --alluredir=reports/allure-results
```

👉 Now just run:

```bash
pytest
```

 

# 🧩 4. Generate Allure Report

```bash
allure serve reports/allure-results
```

👉 Uses Allure

 

# 🧩 5. Example Project Structure

```
project/
│
├── reports/
│   ├── report.html
│   └── allure-results/
│
├── tests/
├── pytest.ini
```

 

# 🧠 Why Use Multiple Reporters?

* ✅ HTML → Easy to read
* ✅ Allure → Detailed & visual
* ✅ JUnit → CI/CD integration
* ✅ JSON → Custom processing

 

# 🧩 6. (Optional) Add JUnit Report

```bash
pytest --junitxml=reports/results.xml
```

 

# ⚡ Combined Example

```bash
pytest \
--html=reports/report.html \
--self-contained-html \
--alluredir=reports/allure-results \
--junitxml=reports/results.xml
```

 

# 🧠 Best Practices

* Use **HTML + Allure** together
* Store reports in `/reports` folder
* Configure once in `pytest.ini`
* Integrate with CI tools like Jenkins

 

# 🎯 Best Interview Answer

👉 *“In Playwright Python, multiple reporters can be configured using pytest plugins like pytest-html and Allure by passing multiple command-line options or defining them in pytest.ini, allowing generation of different report formats in a single execution.”*

 

## 💡 Simple Way to Remember

👉 **Multiple reporters = Multiple report formats**

---
---
## 🔁 Serial Mode in Playwright

**Serial mode** means running tests **one after another in a specific order**, instead of running them in parallel.

 

## 🔍 Simple Definition

👉 *Serial mode executes tests sequentially, where each test waits for the previous one to finish.*

 

## 🧠 Why Serial Mode is Used

* Tests are **dependent on each other**
* Need to maintain **execution order**
* Shared state between tests

 

# 🧩 Example (JavaScript – `@playwright/test`)

```javascript
import { test } from '@playwright/test';

test.describe.serial('My Test Suite', () => {

  test('Step 1: Login', async ({ page }) => {
    await page.goto('https://example.com/login');
  });

  test('Step 2: Dashboard', async ({ page }) => {
    await page.goto('https://example.com/dashboard');
  });

});
```

👉 Tests run in order:

1. Login
2. Dashboard

 

## ⚠️ Default Behavior

👉 Playwright runs tests in **parallel by default**

👉 Serial mode overrides this behavior

 

# 🐍 In Python (Your Case)

Playwright + pytest:

👉 Tests run **sequentially by default**

BUT:

👉 Parallel execution can be enabled using:

```bash
pytest -n 4
```

👉 If you want serial behavior:

* Avoid parallel execution
* Or control using markers / fixtures

 

## ⚠️ Important Note

* Serial mode is mainly a **JS concept**
* In Python → execution is already sequential unless parallelized

 

# 🧠 When to Use Serial Mode

* Multi-step workflows (login → checkout)
* Data dependency between tests
* Stateful scenarios

 

# ⚠️ When NOT to Use

* Independent tests
* Large test suites (slows execution)

 

# ⚖️ Serial vs Parallel

| Feature    | Serial     | Parallel     |
| ---------- | ---------- | ------------ |
| Execution  | One by one | Simultaneous |
| Speed      | Slower     | Faster       |
| Dependency | Allowed    | Not allowed  |

 

## 🎯 Best Interview Answer

👉 *“Serial mode in Playwright ensures that tests run sequentially in a defined order, which is useful when tests are dependent on each other, whereas by default Playwright executes tests in parallel.”*

 

## 💡 Simple Way to Remember

👉 **Serial = One by one**
👉 **Parallel = All together**

 
 
## ⚡ Parallel Execution in Playwright

Parallel execution means running **multiple tests at the same time** to reduce total execution time.

 

## 🔍 Simple Definition

👉 *Parallel execution runs tests simultaneously across multiple workers or browsers.*

 

# 🐍 In Python (Using pytest)

Playwright (Python) uses **pytest-xdist** for parallel execution.

 

# 🧩 1. Install Required Package

```bash
pip install pytest-xdist
```

 

# 🧩 2. Run Tests in Parallel

```bash
pytest -n 4
```

👉 Runs tests on **4 workers (threads/processes)**

 

# 🧩 3. Auto Detect CPU Cores

```bash
pytest -n auto
```

👉 Uses system CPU cores automatically

 

# 🧩 4. Run Parallel with Browser Option

```bash
pytest -n 3 --browser chromium
```

 

# 🧩 5. Example Test

```python
def test_example(page):
    page.goto("https://example.com")
    assert "Example" in page.title()
```

👉 Multiple tests run simultaneously

 

# 🧩 6. Configure in `pytest.ini`

```ini
[pytest]
addopts = -n auto
```

👉 No need to pass `-n` every time

 

# 🧠 How It Works

* Each test runs in **separate worker process**
* Each worker gets its own:

  * Browser
  * Context
  * Page

👉 Ensures isolation

 

# ⚠️ Important Considerations

* ❗ Tests must be **independent**
* ❗ Avoid shared data
* ❗ Avoid static variables
* ❗ Use unique test data

 

# 🧠 Benefits

* ⚡ Faster execution
* 📉 Reduced CI time
* 🚀 Better scalability

 

# ⚖️ Parallel vs Serial

| Feature    | Parallel     | Serial     |
| ---------- | ------------ | ---------- |
| Speed      | Fast         | Slow       |
| Execution  | Simultaneous | One-by-one |
| Dependency | Not allowed  | Allowed    |

 

# 🎯 Best Interview Answer

👉 *“Parallel execution in Playwright Python is achieved using pytest-xdist by running tests with the -n option, allowing multiple tests to execute simultaneously across workers, improving execution speed.”*

 

## 💡 Simple Way to Remember

👉 **-n = number of parallel workers**

---
---
## 🐞 Helpful Ways to Debug Playwright Tests

Debugging helps you **identify why a test is failing** and fix issues faster. Playwright provides several powerful debugging techniques.

 

## 🔍 Simple Definition

👉 *Debugging is the process of analyzing and fixing errors in test execution.*

 

# 🧩 Top Debugging Methods

 

## 🔹 1. Run in Headed Mode

```bash
pytest --headed
```

👉 Opens browser so you can **see what’s happening**

 

## 🔹 2. Use Slow Motion

```bash
pytest --slowmo 1000
```

👉 Adds delay (1 second) between actions

 

## 🔹 3. Use `page.pause()` (Playwright Inspector)

```python
page.pause()
```

👉 Opens **Playwright Inspector**

* Step through actions
* Inspect elements
* Run commands live

 

## 🔹 4. Enable Debug Mode

```bash
PWDEBUG=1 pytest
```

👉 Launches:

* Inspector
* Debug tools

 

## 🔹 5. Take Screenshots

```python
page.screenshot(path="debug.png")
```

👉 Capture UI at failure point

 

## 🔹 6. Record Video

```bash
pytest --video=on
```

👉 Replay test execution

 

## 🔹 7. Capture Traces (Best 🔥)

```bash
pytest --tracing=on
```

👉 View detailed trace:

```bash
playwright show-trace trace.zip
```

👉 Includes:

* Steps
* Network logs
* Screenshots

 

## 🔹 8. Use Logs (Print Statements)

```python
print("Step executed")
```

👉 Simple but effective

 

## 🔹 9. Use Assertions with Messages

```python
assert "Login" in page.title(), "Login page not loaded"
```

👉 Better error understanding

 

## 🔹 10. Check Network Logs

```python
page.on("request", lambda req: print(req.url))
```

👉 Debug API failures

 

## 🔹 11. Use Breakpoints (Python Debugger)

```python
import pdb; pdb.set_trace()
```

👉 Pause execution and inspect variables

 

## 🧠 Best Practices

* Use **headed + slowmo** for UI issues
* Use **trace viewer** for deep debugging
* Capture **screenshots on failure**
* Avoid random waits

 

## 🎯 Best Interview Answer

👉 *“Playwright tests can be debugged using headed mode, slow motion, Playwright Inspector with page.pause(), trace viewer, screenshots, videos, and logs to analyze failures effectively.”*

 

## 💡 Simple Way to Remember

👉 **See → Slow → Pause → Trace → Fix**

---
---
## ⚙️ Actionability in Playwright

**Actionability** refers to the set of **conditions Playwright automatically checks** before performing any action (like click, fill, etc.).

👉 This is part of Playwright’s **auto-waiting mechanism**, which ensures actions happen only when elements are ready.

 

## 🔍 Simple Definition

👉 *Actionability means Playwright ensures an element is ready and safe to interact with before performing an action.*

 

## 🧠 Why Actionability is Important

* Prevents flaky tests
* Avoids manual waits
* Ensures stable execution
* Mimics real user behavior

 

# 🧩 Actionability Checks in Playwright

Before performing an action like `click()`, Playwright checks:

 

## 🔹 1. Element is Attached to DOM

👉 Element must exist in the page

 

## 🔹 2. Element is Visible

👉 Not hidden (`display:none`, `visibility:hidden`)

 

## 🔹 3. Element is Stable

👉 Not moving or animating

 

## 🔹 4. Element is Enabled

👉 Not disabled (`disabled` attribute)

 

## 🔹 5. Element is Receivable (Not Covered)

👉 Not blocked by another element (like popup or overlay)

 

## 🔹 6. Element is Editable (for input)

👉 Only for `fill()` and typing actions

 

# 💻 Example

```python
page.click("#login")
```

👉 Playwright automatically:

* Waits for element
* Checks visibility
* Ensures clickable
* Then performs click

 

# ⚠️ What Happens If Check Fails?

👉 Playwright will:

* Keep retrying until timeout
* Throw error if condition not met

Example error:

```
Element is not visible
```

 

# 🧩 Override Actionability (Force Action)

```python
page.click("#hidden-button", force=True)
```

👉 Skips actionability checks

⚠️ Use only when necessary

 

# 🧩 Example Scenario

### Without Playwright:

* Click fails if element not ready

### With Playwright:

```python
page.click("#submit")
```

👉 Automatically waits until:

* Button visible
* Enabled
* Clickable

 

# 🧠 Actionability vs Wait

| Feature   | Actionability | Manual Wait |
| --------- | ------------- | ----------- |
| Automatic | ✅ Yes         | ❌ No        |
| Reliable  | ✅ High        | ❌ Low       |
| Code      | Clean         | More code   |

 

# 🧠 Real-Time Example

👉 Login button appears after 2 seconds:

* Selenium → need explicit wait
* Playwright → auto-handled

 

# 🎯 Best Interview Answer

👉 *“Actionability in Playwright refers to built-in checks like visibility, stability, and enabled state that ensure an element is ready before performing actions, reducing the need for explicit waits and improving test reliability.”*

 

## 💡 Simple Way to Remember

👉 **Actionability = Ready to interact**

---
---


If you want next, I can help you with:

* 🔥 **Auto-wait vs Explicit wait deep comparison**
* 🔥 **Common actionability errors & fixes**
* 🔥 **Real-time flaky test debugging scenarios**


If you want, I can help you with:

* 🔥 **Real-time debugging scenario walkthrough**
* 🔥 **Fixing flaky tests (very important)**
* 🔥 **Common Playwright errors & solutions**


If you want next, I can help you with:

* 🔥 **Parallel execution issues & solutions**
* 🔥 **Data handling in parallel tests**
* 🔥 **Real-time CI/CD parallel setup**


If you want next, I can help you with:

* 🔥 **Parallel execution deep dive (important)**
* 🔥 **Test dependency design (best practices)**
* 🔥 **Real-time interview scenarios**


If you want next, I can help you with:

* 🔥 **Allure advanced setup with screenshots**
* 🔥 **CI/CD integration (Jenkins/GitHub Actions)**
* 🔥 **Your framework reporting optimization**


If you want, I can help you with:

* 🔥 **Handling dynamic UI in visual testing**
* 🔥 **Ignore regions in screenshots**
* 🔥 **Real-time visual testing strategy (industry level)**


If you want next, I can help you with:

* 🔥 **Visual testing tools comparison (Applitools vs Percy)**
* 🔥 **How to implement screenshot comparison in Playwright**
* 🔥 **Real-time visual testing strategy for projects**


If you want next, I can help you with:

* 🔥 **Playwright vs Requests library (important)**
* 🔥 **Real-time API + UI integration project**
* 🔥 **Advanced API validation techniques**


If you want next, I can help you with:

* 🔥 **Video recording in Playwright**
* 🔥 **Attach screenshots in Allure report**
* 🔥 **Visual testing (compare screenshots)**


If you want next, I can help you with:

* 🔥 **API + UI combined testing (very important)**
* 🔥 **Mock API responses in Playwright**
* 🔥 **Real-time debugging scenarios**


If you want next, I can help you with:

* 🔥 **Hooks vs Fixtures vs Setup (important interview question)**
* 🔥 **Login reuse using storage state (very important)**
* 🔥 **Real-time framework implementation**


If you want next, I can help you with:

* 🔥 **Hooks + error handling (very important)**
* 🔥 **Capture screenshots on failure automatically**
* 🔥 **Advanced debugging techniques in Playwright**


If you want next, I can help you with:

* 🔥 **Hooks in Playwright (beforeEach, afterEach)**
* 🔥 **How to attach screenshots on failure**
* 🔥 **Advanced reporting using testInfo**


If you want next, I can help you with:

* 🔥 **Handling file upload popups vs browser dialogs (important)**
* 🔥 **Real-time popup scenarios (ads, modals, windows)**
* 🔥 **Advanced event handling in Playwright**


If you want next, I can help you with:

* 🔥 **Mouse actions deep dive (hover, scroll, drag)**
* 🔥 **Real-time tricky drag-drop scenarios**
* 🔥 **Handling sliders and canvas elements**


If you want next, I can help you with:

* 🔥 **Upload vs Download difference (important)**
* 🔥 **Handling PDFs and images download validation**
* 🔥 **Real-time file validation scenarios in projects**


If you want, I can next show:

* 🔥 **File download handling (very important)**
* 🔥 **Upload without input tag (advanced scenario)**
* 🔥 **Real-time project example with validations**


If you want next, I can help you with:

* 🔥 **Data-driven framework using Excel/JSON (important)**
* 🔥 **Real-time login test with parameterization + POM**
* 🔥 **Advanced pytest features used in companies**


If you want next, I can help you with:

* 🔥 **Convert CodeGen script into framework (important)**
* 🔥 **Best locator strategies from CodeGen output**
* 🔥 **Real-time demo example explanation**


If you want next, I can explain:

* 🔥 **conftest.py deep dive (very important)**
* 🔥 **Fixture vs Hooks (important interview question)**
* 🔥 **Real-time framework design using fixtures**



If you want next, I can help you with:

* 🔥 **Keyboard + Mouse combination actions**
* 🔥 **Drag and drop advanced scenarios**
* 🔥 **Real-time UI interaction questions for interviews**


If you want next, I can help you with:

* 🔥 **Mouse actions (drag & drop, hover) deep dive**
* 🔥 **Keyboard actions in Playwright**
* 🔥 **Real-time tricky UI interaction scenarios**


If you want next, I can help you with:

* 🔥 **Shadow DOM vs iFrame (very important interview question)**
* 🔥 **Handling alerts, popups, and modals**
* 🔥 **Real-time tricky iframe scenarios**


If you want next, I can help you with:

* 🔥 **Handling multiple tabs interview scenarios**
* 🔥 **Switching between tabs (tricky questions)**
* 🔥 **Real-time multi-window test cases**


If you want next, I can explain:

* 🔥 **Browser vs Context vs Page (very important interview question)**
* 🔥 **Real-time multi-user test scenarios**
* 🔥 **Context vs Incognito mode comparison**


If you want next, I can help you with:

* 🔥 **Auto-wait vs explicit wait (very important interview question)**
* 🔥 **Common synchronization issues & solutions**
* 🔥 **Real-time debugging wait problems**


If you want next, I can help you with:

* 🔥 **Cross-browser testing strategy (very important)**
* 🔥 **Differences between Chromium, Firefox, WebKit**
* 🔥 **Real-world browser compatibility issues**


If you want next, I can help you with:

* 🔥 **Locator vs Action difference (important)**
* 🔥 **Real-time complex user scenarios**
* 🔥 **Action chaining & advanced usage**


If you want next, I can help you with:

* 🔥 **Handling navigation failures (very important)**
* 🔥 **Auto-wait vs navigation wait concepts**
* 🔥 **Real-time navigation test scenarios**


If you want next, I can help you with:

* 🔥 **Auto-wait vs explicit wait (very important question)**
* 🔥 **Common timeout issues & how to fix them**
* 🔥 **Real-time debugging scenarios with timeouts**


If you want next, I can help you with:

* 🔥 **Allure report setup (very important for interviews)**
* 🔥 **Attach screenshots to HTML report**
* 🔥 **Your framework reporting setup improvement**


If you want, I can next help you with:

* 🔥 **Real-time debugging techniques in Playwright**
* 🔥 **SlowMo, tracing, and video recording (important)**
* 🔥 **Common issues in headless mode & solutions**


If you want next, I can help you with:

* 🔥 **Real-time commands used in your framework (based on your pytest.ini)**
* 🔥 **CI/CD pipeline commands (Jenkins/GitHub Actions)**
* 🔥 **Advanced debugging commands used by senior QA engineers**


If you want next, I can help you with:

* 🔥 **Real-time CI/CD setup using these commands**
* 🔥 **Advanced pytest options used in companies**
* 🔥 **Your current framework optimization (based on your code)**


If you want next, I can help you with:

* 🔥 **Advanced XPath tricks for interviews**
* 🔥 **CSS vs XPath vs Playwright locators (deep comparison)**
* 🔥 **Real-time tricky locator scenarios**


If you want next, I can help you with:

* 🔥 **All Playwright matchers list (important for interviews)**
* 🔥 **Real-time negative test cases examples**
* 🔥 **Common mistakes in assertions & how to fix them**


If you want next, I can help you with:

* 🔥 **Hard vs Soft assertions (important interview question)**
* 🔥 **Common assertion mistakes in Playwright**
* 🔥 **Real-time test case examples with assertions**


If you want next, I can help you with:

* 🔥 **Advanced locator interview questions**
* 🔥 **Real-time tricky locator scenarios**
* 🔥 **XPath vs Playwright locators comparison**


If you want next, I can explain:

* 🔥 **Difference between locator vs selector (very important)**
* 🔥 **Advanced locator strategies with real examples**
* 🔥 **Tricky interview questions on locators**


If you want next, I can help you with:

* 🔥 **Allure reporting setup step-by-step**
* 🔥 **How to add screenshots in reports (important)**
* 🔥 **Real-time reporting in your framework**

If you want next, I can show:

* 🔥 **Real-time login test using navigation (important for interviews)**
* 🔥 **How navigation works with base URL in framework**
* 🔥 **Common navigation issues & solutions**


If you want next, I can explain:

* 🔥 **Browser vs Context vs Page (very important interview question)**
* 🔥 **Playwright locators deep dive**
* 🔥 **Fixtures and Page usage in PyTest**


If you want next, I can help you with:

* 🔥 **conftest.py deep explanation (very important for interviews)**
* 🔥 Real-time **framework setup with config, pages, tests**
* 🔥 Environment handling (QA/Stage/Prod) in Playwright


If you want, I can next show:

* 🔥 Complete **Playwright framework (real-time project)**
* 🔥 **Advanced pytest commands (used in companies)**
* 🔥 How to explain this confidently in interviews

If you want next, I can help you with:

* 🔥 **Playwright framework setup (step-by-step real project)**
* 🔥 **Top Playwright interview questions with answers**
* 🔥 **Hands-on coding questions for practice**


If you want next, I can help you with:

* 🔥 Real-time **Playwright framework explanation (important for interviews)**
* 🔥 **Advanced Playwright concepts (locators, fixtures, hooks)**
* 🔥 Mock interview questions for QA roles


If you want next, I can help you with:

* 🔥 **Top Playwright interview Q&A (very important for jobs)**
* 🔥 **Real-time project explanation (to explain in interviews)**
* 🔥 **Selenium → Playwright migration strategy**



If you want, I can next explain:

* Playwright **architecture (very important for interviews)**
* Playwright vs Selenium **deep comparison**
* Or build a **complete framework step-by-step**

If you want, I can next help you with:

* 🔥 **Top 20 Playwright interview questions (with answers)**
* 🔥 **Real-time framework setup (important for jobs)**
* 🔥 **How to explain Playwright in interviews confidently**

If you want next, I can show:

* 🔹 **Real-time code comparison (login test Selenium vs Playwright)**
* 🔹 **Migration from Selenium → Playwright (very useful for your profile)**
* 🔹 **Top interview questions with answers**
