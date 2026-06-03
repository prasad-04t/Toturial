## 1. What Playwright?

**Playwright** is an open-source automation framework developed by Microsoft for testing of web applications. It allows you to programmatically control web browsers and simulate real user actions and verifying UI behavior.

### 1.1 What Playwright Actually Does
Playwright automatically controls the browser like a real user by opening websites, clicking buttons, entering data, and checking results. It helps test web applications quickly and reliably across different browsers.
 - Open Websites
```ts
await page.goto('https://example.com');
```
- Interact with Elements
 Click, type, select, etc.

```ts
await page.click('#login');
await page.fill('#username', 'admin');
```
- Navigate Between Pages

```ts
await page.goto('/dashboard');
await page.goBack();
```
- Validate UI Behavior

```ts
await expect(page).toHaveTitle('Home');
await expect(page.locator('h1')).toHaveText('Welcome');
```

- **Handle Real User Scenarios**
✔ Login flows
✔ Form submissions
✔ File upload/download
✔ Drag & drop
✔ Popups

-  **How It Works (Flow)**
```text
Test Script → Playwright → Browser → Application → Result
```

### 1.2 Why Playwright is Used?
Playwright is used for automating web application testing, including end-to-end and cross-browser testing. It helps reduce manual effort, improve test reliability with auto-waiting, and supports fast execution with parallel testing and CI/CD integration.

Playwright is mainly used for:
- Automated testing: ensuring web applications work correctly, reducing manual effort, and catching bugs early.
- Cross‑browser testing: allowing the same application to be tested on Chrome, Firefox, and Safari.
- UI testing: validating buttons, forms, layouts, and user interactions.
- API testing (basic support): testing backend APIs alongside the UI.


### 1.3 Key Features of Playwright
- **Multi‑Browser Support:** Run tests on multiple browsers using the same code.  
- **Auto‑Waiting:** Automatically waits for elements to appear, become clickable, and load fully — reducing flaky tests.  
- **Headless & Headed Mode:**  
  - *Headless* → runs without UI (faster, used in CI/CD).  
  - *Headed* → shows browser (useful for debugging).  
- **Powerful Selectors:** Supports CSS, XPath, text‑based, and role‑based selectors.  
- **Network Control:** Mock API responses, block network calls, and inspect requests.  
- **Parallel Execution:** Run multiple tests at the same time for faster execution.  
- **Built‑in Test Runner:** Provides its own framework with assertions (`expect`), fixtures, hooks (`beforeEach`, `afterEach`), and reports.  
- **Screenshots & Videos:** Automatically capture screenshots on failure and videos of test runs.  
- **CI/CD** Playwright can execute tests automatically in CI/CD pipelines, in parallel, and in headless mode.
  
### 1.4 How Playwright Works

Playwright works by executing test scripts that interact with a browser through its automation engine. It launches a browser, performs user-like actions such as clicking and typing, automatically waits for elements to be ready, and validates results using assertions.
```
Test Script → Playwright → Browser → Web Application → Result

Test Script (Your Code)
        ↓
Playwright Core
        ↓
Browser Engine (Chromium / Firefox / WebKit)
        ↓
Web Application
```
Playwright executes tests by interpreting scripts into browser actions, launching Chromium/Firefox/WebKit, performing user interactions with auto‑waiting, validating results through assertions, and finally generating reports with pass/fail status, screenshots, and videos.

### 1.5 Example (Simple Playwright Test)

```ts
// pages/SearchPage.ts
import { Page, Locator } from '@playwright/test';

export class SearchPage {
  readonly page: Page;
  readonly searchTermInput: Locator;

  constructor(page: Page) {
    this.page = page;
    this.searchTermInput = page.locator('[aria-label="Enter your search term"]');
  }

  async navigate(): Promise<void> {
    await this.page.goto('https://bing.com');
  }

  async search(text: string): Promise<void> {
    await this.searchTermInput.fill(text);
    await this.searchTermInput.press('Enter');
  }
}

// tests/search.spec.ts
import { test } from '@playwright/test';
import { SearchPage } from '../pages/SearchPage';

test('search test', async ({ page }) => {
  const searchPage = new SearchPage(page);

  await searchPage.navigate();
  await searchPage.search('search query');
});

```
```python
class SearchPage:
    def __init__(self, page):
        self.page = page
        self.search_term_input = page.locator('[aria-label="Enter your search term"]')

    def navigate(self):
        self.page.goto("https://bing.com")

    def search(self, text):
        self.search_term_input.fill(text)
        self.search_term_input.press("Enter")

# in the test

from models.search import SearchPage
page = browser.new_page()
search_page = SearchPage(page)
search_page.navigate()
search_page.search("search query")
```


### 1.6 Playwright vs Selenium 
Playwright is faster with built‑in auto‑waiting, easier setup, and modern APIs, while Selenium is slower, requires manual waits, has a more complex setup, and offers limited modern API support.

| Feature     | Playwright | Selenium |
| ----------- | ---------- | -------- |
| Speed       | Faster     | Slower   |
| Auto-wait   | Built-in   | Manual   |
| Setup       | Easy       | Complex  |
| Modern APIs | Yes        | Limited  |

### 1.7 Where Playwright is Used in Industry
Playwright is widely used in industry for automating and testing modern web applications, covering use cases such as web application testing, end‑to‑end user journey validation, regression testing, cross‑browser compatibility checks, CI/CD pipeline integration, UI and API testing, as well as performance monitoring and visual testing.
Example flow:
```
Developer → Code → CI Tool → Playwright Tests → Deployment
```


### 1.8 Why Playwright is Popular
Playwright is popular because it delivers fast, reliable, and modern web automation with less effort, built‑in auto‑waiting and retry mechanisms, direct browser communication for faster execution, multi‑browser support, an integrated test framework, powerful selectors, easy setup, strong debugging tools, CI/CD friendliness, and a modern architecture with TypeScript support

---
---

## 2. Playwright Architecture (How it Works Internally)

Playwright’s architecture is designed to be **fast, reliable, and cross-browser compatible**. Instead of using traditional drivers (like Selenium), it directly communicates with browsers using modern protocols.
 Playwright has **three main layers**:
- **Test Script Layer (Code)** :
The Test Script Layer is the top layer where we write automation scripts using Playwright APIs
   Written in TypeScript / JavaScript/other languages
   Uses Playwright APIs (`page`, `browser`, `context`)

- **Playwright Core (Client Library)** ;;
Playwright Core is the client library that acts as a bridge between test scripts and browser engines. It translates high-level commands into low-level instructions, manages communication with browsers, and handles features like auto-waiting, retries, and session management


- **Browser Engines** :
Browser engines are the actual browsers like Chromium, Firefox, and WebKit that Playwright interacts with. They are responsible for rendering web pages and executing user actions, while Playwright sends commands to them for automation.

### 2.1 Internal Flow (Step-by-Step)
Let’s understand what happens internally when you run a test:
- **Step 1: You Write Code**
```ts
await page.getByRole('button', { name: 'Login' }).click();
```
- **Step 2**: Playwright Converts Action into Protocol Command like a low-level instruction
✔  Example: “Find element → wait → click”

- **Step 3**: Communication via WebSocket / CDP
✔ Playwright communicates with browsers using:
✔ CDP (Chrome DevTools Protocol)** → for Chromium
✔ Custom protocols → for Firefox & WebKit

> Note: No external drivers like Selenium WebDriver

- **Step 4**: Browser Executes the Action
✔ Browser receives the command
✔ Finds the element
✔ Performs the click


- **Step 5**: Response Sent Back
✔ Browser sends success/failure
✔ Playwright continues next step

### 2.2 Key Components in Playwright Architecture
- **Browser** : Represents the actual browser instance.
```ts
const browser = await chromium.launch();
```
```python
browser = p.chromium.launch()
```
✔ Can launch multiple browsers
✔ Supports headless/headed mode

- **Browser Context** : Think of this as a separate user session.

```ts
const context = await browser.newContext();
```
```python
 context = browser.new_context()
```
Each context:
✔ Has its own cookies
✔ Has its own storage
✔ Is isolated from others
 Note : Like opening multiple incognito windows


- **Page**: Represents a single tab.

```ts
const page = await context.newPage();
```
```python
age = context.new_page()
```
 All interactions happen here:

✔ Click
✔ Fill
✔ Navigate


- **Playwright Test Runner** :Built-in test framework that handles:

✔ Test execution
✔ Parallel runs
✔ Assertions (`expect`)
✔ Reporting
Unlike TypeScript, Playwright Python does not have a built-in test runner.
Python commonly uses pytest with Playwright for:
✔ Test execution
✔ Parallel execution
✔ Assertions
✔ Fixtures
✔ Reporting


### 2.3 Real Execution Flow (Example)

```ts
import { chromium } from '@playwright/test';

(async () => {
  const browser = await chromium.launch({
    headless: false,
  });

  const context = await browser.newContext();

  const page = await context.newPage();

  await page.goto('https://example.com');

  await page.getByRole('button', { name: 'Login' }).click();

  await browser.close();
})();
```
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()
    page.goto("https://example.com")
    await page.getByRole('button', { name: 'Login' }).click();
    browser.close()
```
Internally:
```
 `goto()` → Browser loads URL
 `fill()` → Wait → Find input → Type text
 `click()` → Wait → Ensure visible → Click
```

> All waiting is **automatic**


### 2.4 Why Playwright Architecture is Powerful
- **No WebDriver Dependency** :Unlike Selenium
✔ No separate driver (like ChromeDriver)
✔  Direct browser communication

- **Auto-Wait Mechanism**: Playwright automatically waits for
✔ Elements to be visible
✔ Elements to be stable
✔ Network to be idle
> Note: This reduces flaky tests significantly

- **Isolation with Browser Contexts**
✔ Run tests in parallel safely
✔ No shared state issues

- **Fast Execution**
✔ Direct communication → less overhead
✔ Parallel execution → faster pipelines


### 2.5 Parallel Execution Architecture
Playwright uses a parallel execution where tests are distributed across multiple worker.
Each worker runs tests independently in an isolated browser context, ensuring no shared state and enabling faster and reliable test execution.
```
Test Runner
   ├── Worker 1 → Browser → Context → Page → Test A
   ├── Worker 2 → Browser → Context → Page → Test B
   └── Worker 3 → Browser → Context → Page → Test C
```


### 2.6 Comparison with Selenium Architecture
Playwright uses direct communication via CDP/WebSocket, making it faster, simpler to set up, and more stable, while Selenium relies on the WebDriver HTTP protocol, which is slower, requires drivers, and offers medium stability.
| Feature       | Playwright             | Selenium         |
| ------------- | ---------------------- | ---------------- |
| Communication | Direct (CDP/WebSocket) | WebDriver (HTTP) |
| Speed         | Faster                 | Slower           |
| Setup         | Simple                 | Needs drivers    |
| Stability     | High                   | Medium           |


---
---


## 3. Fixtures in Playwright
Fixtures in Playwright are reusable setup and teardown mechanisms used to provide resources like browser pages, contexts, test data ,or custom utilities. They help improve code reusability, maintainability, and test isolation.
### 3.1 What Exactly is a Fixture?
✔ Prepares the environment before a test runs
✔ Provides required objects/data to the test
✔ Cleans up after the test finishes

> In simple terms: **Fixtures = Setup + Usage + Teardown**

### 3.2 Why Fixtures are Important
- Without fixtures:
 ✔ You repeat the same setup in every test
 ✔ Code becomes messy and hard to maintain

- With fixtures:
  ✔ Code is reusable
  ✔ Tests are cleaner
  ✔ Setup is centralized


### 3.3 Built-in Fixtures in Playwright
Playwright already provides some default fixtures:
Common Built-in Fixtures:
```
 `browser` → launches browser
 `context` → new browser context
 `page` → new tab
```
In Playwright, browser represents the browser instance, context represents an isolated session like an incognito window, and page represents a single tab where actual test actions are performed.

**Example**

```ts
import { test, expect } from '@playwright/test';

test('example test', async ({ page }) => {
  await page.goto('https://example.com');
  await expect(page).toHaveTitle(/Example/);
});
```

Note:
```
`page` is a **fixture**
You didn’t create it — Playwright provided it
```

### 3.4 How Fixtures Work Internally
Internally, Playwright fixtures work using dependency injection and a lifecycle model. When a test requests a fixture like page, Playwright builds a dependency graph, initializes required fixtures such as browser and context, injects them into the test, and automatically performs clean up after execution.
✔ Fixture setup runs
✔ Fixture is passed to test
✔ Test executes
✔ Fixture teardown runs


### 3.5 Types of Fixtures

- **Test-Level Fixtures**
Test-level fixtures  are created fresh/separately for each test and destroyed after the test execution/finishes. They ensure test isolation by providing a clean environment, such as a new browser context and page, preventing data sharing between tests.

Step-by-step:
```
Setup → Create context + page
Inject → Provide page to test
Execute → Run test steps
Teardown → Close page + context
```

Example (Built-in Test-Level Fixture)

```ts
test('Test 1', async ({ page }) => {
  await page.goto('https://example.com');
});

test('Test 2', async ({ page }) => {
  await page.goto('https://google.com');
});
```
```python
def test_1(page):
    page.goto("https://example.com")


def test_2(page):
    page.goto("https://google.com")
```
Why Test-Level Fixtures are Important
✔ Test Isolation -No interference between tests
✔ No Flaky Tests- Clean state every time
✔ Parallel Execution- Multiple tests can run safely


- **Worker-Level Fixtures**
Worker-level fixtures are initialized/created once per worker process and shared across multiple tests running that worker. They are useful for expensive setup operations like browser launch or authentication, improving performance by avoiding repeated initialization.

How Playwright Runs Workers: 
Playwright runs tests in parallel workers (separate processes)
Each worker, Has its own environment, Runs multiple tests, Shares worker fixtures

Example of Worker-Level Fixture
```ts
import { test as base } from '@playwright/test';

const test = base.extend({
  sharedBrowser: [async ({ browser }, use) => {
    console.log('Setup once per worker');

    await use(browser);

    console.log('Teardown once per worker');
  }, { scope: 'worker' }]
});

test('Test 1', async ({ sharedBrowser }) => {
  console.log('Running Test 1');
});

test('Test 2', async ({ sharedBrowser }) => {
  console.log('Running Test 2');
});
```
```python
import pytest
@pytest.fixture(scope="session")
def shared_browser(playwright):
    print("Setup once per worker/session")
    browser = playwright.chromium.launch(headless=False)
    yield browser
    print("Teardown once per worker/session")
    browser.close()

def test_1(shared_browser):
    print("Running Test 1")
    page = shared_browser.new_page()
    page.goto("https://example.com")
    page.close()


def test_2(shared_browser):
    print("Running Test 2")
    page = shared_browser.new_page()
    page.goto("https://google.com")
    page.close()
```
What Happens Internally:
✔ Worker Starts -Playwright creates a worker process
✔ Fixture Setup (Once)- sharedBrowser is initialized only once
✔ Tests Run :Test 1 uses the fixture, Test 2 reuses the same fixture
✔ Teardown (Once) -After all tests → cleanup happens

When to Use Worker-Level Fixtures:
✔ Expensive Setup -Browser launch, Database connection, API authentication
✔ Shared Resources -Test data setup, Login session ,External services


- **Custom Fixtures**
Custom fixtures in Playwright are user-defined reusable components created using base.extend(). They allow us to encapsulate setup and teardown logic, inject dependencies into tests, and improve maintainability by avoiding code duplication. 

Example: Custom Fixture

```ts
import { test as base } from '@playwright/test';

const test = base.extend({
  loggedInPage: async ({ page }, use) => {
    await page.goto('https://example.com/login');
    await page.fill('#username', 'admin');
    await page.fill('#password', '1234');
    await page.click('#login');

    await use(page);
  }
});

test('Dashboard Test', async ({ loggedInPage }) => {
  await loggedInPage.click('#profile');
await expect(loggedInPage).toHaveURL(/dashboard/)
});
```
```python
import pytest
from playwright.sync_api import expect


class LoginPage:

    def __init__(self, page):
        self.page = page

        # Locators
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login")
        self.profile_button = page.locator("#profile")

    def navigate(self):
        self.page.goto("https://example.com/login")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def click_profile(self):
        self.profile_button.click()


# Custom Fixture
@pytest.fixture
def logged_in_page(page):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login("admin", "1234")

    yield login_page


# Test Case
def test_dashboard(logged_in_page):

    logged_in_page.click_profile()

    expect(logged_in_page.page).to_have_url(
        "https://example.com/dashboard"
    )
```

Types of Custom Fixtures You’ll Build
✔ Page Fixtures -Login page ,Dashboard page
✔ API Fixtures-Auth token, API client
✔ Data Fixtures- Test data setup, DB connection

* Why Custom Fixtures are Important
✔ Remove duplicate code
✔ Improve readability
✔ Centralize setup logic
✔ Make framework scalable



### 3.6 Key Concept: `use()` Function
In Playwright, the use() is a call back function is used inside fixtures to pass the prepared resource to the test. It controls the fixture lifecycle by pausing execution while the test runs and resuming afterward to perform teardown

```ts
import { test as base } from '@playwright/test';

const test = base.extend({
  myFixture: async ({ page }, use) => {
    console.log('Setup');

    await use(page);  // 👉 Pass to test

    console.log('Teardown');
  }
});

test('Example Test', async ({ myFixture }) => {
  console.log('Test Running');
});
```
```python
import pytest
from playwright.sync_api import expect


# Custom Fixture
@pytest.fixture
def logged_in_page(page):

    # -------------------
    # Setup
    # -------------------
    print("Setup Started")

    page.goto("https://example.com/login")

    username_input = page.locator("#username")
    password_input = page.locator("#password")
    login_button = page.locator("#login")

    username_input.fill("admin")
    password_input.fill("1234")

    login_button.click()

    print("Login Successful")

    # -------------------
    # Pass resource to test
    # Similar to: await use(page)
    # -------------------
    yield page

    # -------------------
    # Teardown
    # -------------------
    print("Teardown Started")

    page.close()

    print("Page Closed")


# Test Case
def test_dashboard(logged_in_page):

    print("Test Running")

    profile_button = logged_in_page.locator("#profile")

    profile_button.click()

    expect(logged_in_page).to_have_url(
        "https://example.com/dashboard"
    )

    print("Test Completed")
```
What it means:
✔ Everything before `use()`/`yield` → setup**
✔ Everything **after `use()`/`yield` → teardown**

Execution Flow 
✔ Setup starts
✔ use(value) is called
✔ Test executes
✔ After test finishes → control returns
✔ Teardown runs


### 3.7 Fixture Dependency (Advanced Concept)

Fixture dependency in Playwright refers to the relationship where one fixture depends on another fixture. Playwright automatically builds a dependency graph, initializes fixtures in the correct order, and tears them down in reverse order, ensuring proper setup and clean up.

```ts
import { test as base } from '@playwright/test';

const test = base.extend({
  loginPage: async ({ page }, use) => {
    await page.goto('https://example.com/login');
    await use(page);
  }
});

const test = base.extend({
  apiClient: async ({}, use) => {
    const client = await createClient();
    await use(client);
  },

  loggedInPage: async ({ page, apiClient }, use) => {
    await page.goto('https://example.com');
    // use apiClient if needed
    await use(page);
  }
});

test('Test', async ({ loggedInPage }) => {});

test('Test', async ({ loginPage }) => {
  await loginPage.fill('#username', 'admin');
});
```
```python
import pytest
from playwright.sync_api import expect


# ---------------------------------
# API Client Fixture
# ---------------------------------
@pytest.fixture
def api_client():

    print("Setup API Client")

    client = {
        "token": "sample_token"
    }

    yield client

    print("Teardown API Client")


# ---------------------------------
# Login Page Fixture
# ---------------------------------
@pytest.fixture
def login_page(page):

    print("Setup Login Page")

    page.goto("https://example.com/login")

    yield page

    print("Teardown Login Page")


# ---------------------------------
# Logged In Page Fixture
# Depends on:
#   ✔ page
#   ✔ api_client
# ---------------------------------
@pytest.fixture
def logged_in_page(page, api_client):

    print("Setup Logged In Page")

    page.goto("https://example.com/login")

    username = page.locator("#username")
    password = page.locator("#password")
    login_button = page.locator("#login")

    username.fill("admin")
    password.fill("1234")

    # Using api_client if needed
    print(api_client["token"])

    login_button.click()

    yield page

    print("Teardown Logged In Page")


# ---------------------------------
# Test Using logged_in_page
# ---------------------------------
def test_dashboard(logged_in_page):

    profile = logged_in_page.locator("#profile")

    profile.click()

    expect(logged_in_page).to_have_url(
        "https://example.com/dashboard"
    )


# ---------------------------------
# Test Using login_page
# ---------------------------------
def test_login(login_page):

    username = login_page.locator("#username")

    username.fill("admin")
```

### 3.8 Real-World Use Cases
Fixtures are commonly used for:
✔ Login once and reuse
✔ Test data setup
✔ API clients
✔ Database connections
✔ Page Object Model (POM) injection

### 10. Fixtures vs Hooks (Important Difference)
Both are used for setup and teardown, but they work very differently.
* Fixtures are reusable, dependency-based setup components, Injected into tests, Support dependency chaining ,Can be test-level or worker-level
* Hooks are lifecycle functions that run before/after tests
Example:
```ts
test.beforeEach(async ({ page }) => {
  await page.goto('https://example.com');
});
```

| Feature     | Fixtures    | Hooks (beforeEach) |
| ----------- | ----------- | ------------------ |
| Reusability | High        | Low                |
| Flexibility | Very high   | Limited            |
| Scope       | Test/Worker | Suite level        |
| Clean code  | Yes         | Can become messy   |



---
---

## 4. Selenium vs Playwright (Clear & Detailed Comparison)
Both Selenium WebDriver and **Playwright** are used for automating web applications, but they differ significantly in **architecture, speed, reliability, and modern capabilities**.

### 4.1 Basic Idea

> **Selenium** → Older, widely used automation tool based on WebDriver standard
> **Playwright** → Modern automation framework built for today’s web apps


### 4.2 Architecture Difference (Core Concept)
- **Selenium Architecture**
First, the test script sends commands to the WebDriver.
The WebDriver then forwards those commands to the browser driver (like ChromeDriver or GeckoDriver).
The browser driver communicates with the actual browser and performs the actions.

```
Test Script → WebDriver → Browser Driver → Browser
Note: drivers required
```

- **Playwright Architecture**
The test script sends commands to Playwright, and Playwright directly communicates with the browser to perform those actions.

```
Test Script → Playwright → Browser
Note:  No external drivers required

```

### 4.3 Key Differences Table
Selenium uses a WebDriver‑based HTTP architecture that requires drivers, runs slower, needs manual waits, is more flaky, and requires complex grid setups for parallel execution, while Playwright uses direct CDP/WebSocket communication with no drivers, faster execution, built‑in auto‑wait, less flakiness, simple parallel workers, modern browser support, strong network mocking, easy multi‑tab handling, and broad language support including JS, TS, Python, Java, and .NET.

| Feature            | Selenium                  | Playwright                 |
| ------------------ | ------------------------- | -------------------------- |
| Architecture       | WebDriver (HTTP-based)    | Direct (CDP/WebSocket)     |
| Setup              | Needs drivers             | No drivers needed          |
| Speed              | Slower                    | Faster                     |
| Auto-wait          | ❌ Manual waits            | ✅ Built-in auto-wait       |
| Flakiness          | More flaky                | Less flaky                 |
| Parallel execution | Complex (Grid setup)      | Simple (built-in workers)  |
| Browser support    | Wide                      | Modern browsers            |
| Language support   | Many (Java, Python, etc.) | JS, TS, Python, Java, .NET |
| Network mocking    | Limited                   | Strong support             |
| Multi-tab handling | Complex                   | Easy                       |



- **Waiting Mechanism**
In Selenium you must manually add waits like Thread.sleep or WebDriverWait, which slows tests and causes flaky failures, while Playwright automatically waits for elements to be visible and ready, ensuring faster and more stable execution.

```python
import time
from selenium.webdriver.support.ui import WebDriverWait
# Sleep for 5 seconds (like Thread.sleep in Java)
time.sleep(5)

# Explicit wait for up to 10 seconds
wait = WebDriverWait(driver, 10)

Problem: Slower tests, Flaky failures
```

```ts
await page.click('#login');

Automatically: Waits for element, Ensures visibility, Handles timing
```

- **Speed Comparison**
Selenium → slower due to multiple layers
Playwright → faster due to direct communication

Playwright removes: Driver overhead, Extra HTTP calls

 - **Browser Context**
Playwright’s unique browser context feature allows multiple isolated sessions within a single browser, enabling tests for different users without relaunching the browser.

```ts
const context1 = await browser.newContext();
const context2 = await browser.newContext();
```

- ** Parallel Execution**
In Selenium, parallel execution requires a complex Selenium Grid setup, whereas Playwright has built‑in support for parallel workers, allowing simple execution with a single command like npx playwright test --workers=4

- ** Network Control **
Selenium offers limited network control, while Playwright allows powerful request handling such as mocking APIs, blocking requests, and modifying responses with simple commands like page.route()


```ts
await page.route('**/api', route => route.abort());
```

- **Debugging & Reporting**
Selenium relies on third‑party tools for debugging and reporting, whereas Playwright provides built‑in support with a trace viewer, screenshots, and video recording for easier issue analysis.

---
---

## 5. Playwright Installation & Test Execution — Commands
### TypeScript

Here are the **essential commands** you need to install Playwright and run tests.

- ** Initialize a Project (Optional but Recommended)**

```bash
npm init -y
```

✔ Creates a `package.json` file
✔ Required for managing dependencies


- ** Install Playwright **
Recommended (with Test Runner)

```bash
npm init playwright@latest
```
✔ This command:
 Installs Playwright
 Installs browsers (Chromium, Firefox, WebKit)
 Creates sample tests
 Sets up config file

✔ Alternative (Manual Install)

```bash
npm install -D @playwright/test
```

✔ Then install browsers:

```bash
npx playwright install
```

- ** Run Tests **

✔ Run all tests

```bash
npx playwright test
```


✔ Run specific file

```bash
npx playwright test tests/example.spec.ts
```


✔ Run in headed mode (visible browser)

```bash
npx playwright test --headed
```

✔ Run in specific browser

```bash
npx playwright test --project=chromium
```

✔ Debug mode

```bash
npx playwright test --debug
```

✔ Run with UI mode (interactive)

```bash
npx playwright test --ui
```

- ** View Test Report **

```bash
npx playwright show-report
```
 Opens HTML report in browser


- ** Run Tests in Parallel **

```bash
npx playwright test --workers=4
```

### Python
Playwright + Python Installation & Test Execution Commands
Using pytest + Playwright. 

 -   **Create Virtual Environment**

```bash id="a1b2c3"
python -m venv venv
venv\Scripts\activate
```
- **Install Playwright**

```bash id="g7h8i9"
pip install playwright
```
- **Install Browsers**

```bash id="j1k2l3"
playwright install
```

Installs:

✔ Chromium
✔ Firefox
✔ WebKit

 - **Install PyTest Integration**

```bash id="m4n5o6"
pip install pytest-playwright
```

- **Verify Installation**

```bash id="p7q8r9"
playwright codegen google.com
```

Opens browser + generates automation code.

-  **Run All Tests**

```bash id="s1t2u3"
pytest
```

- **Run Specific Test File**

```bash id="v4w5x6"
pytest tests/test_login.py
```

- **Run Specific Test Method**

```bash id="y7z8a9"
pytest tests/test_login.py::test_valid_login
```
- **Run Tests in Headed Mode**

```bash id="b1c2d3"
pytest --headed
```

- **Run Tests in Specific Browser**


```bash id="e4f5g6"
pytest --browser chromium
```



```bash id="h7i8j9"
pytest --browser firefox
```


```bash id="k1l2m3"
pytest --browser webkit
```

- **Parallel Execution**

Install:

```bash id="n4o5p6"
pip install pytest-xdist
```

Run:

```bash id="q7r8s9"
pytest -n 4
```

Runs tests using 4 workers.

---

- **Generate HTML Report**

Install:

```bash id="t1u2v3"
pip install pytest-html
```

Run:

```bash id="w4x5y6"
pytest --html=report.html
```

-  **Run in Slow Motion**

```bash id="z7a8b9"
pytest --slowmo 1000
```

1000 = 1 second delay between actions.

- **Debug Mode**

```bash id="c1d2e3"
pytest --headed --slowmo 500
```

- **Record Trace**

```bash id="f4g5h6"
pytest --tracing on
```

- **Open Trace Viewer**

```bash id="i7j8k9"
playwright show-trace trace.zip
```


---
---

## 6. What is a Configuration File in Playwright?
### *TypeScript*
The Playwright configuration file is a central file where we define test execution settings such as browser configuration, timeouts, parallel execution, base URL, and reporting. It helps manage and control the behavior of tests in a scalable and maintainable way.
> In simple terms: **It controls the behavior of your entire test suite from one file.**

```ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests',

  timeout: 30000,

  use: {
    headless: true,
    baseURL: 'https://example.com',
    screenshot: 'only-on-failure',
  },
});
```

### 6.1 File Name & Location
 The config file is usually named:

```bash
playwright.config.ts
```
Located in the project root, Written in TypeScript (or JavaScript)


### 6.2 Why Configuration File is Important
The configuration file is important in Playwright because it centralizes test settings like browser configuration, timeouts, parallel execution, and reporting. It improves maintainability, avoids code duplication, ensures consistency, and makes the framework scalable.
- Without config:
✔ You would repeat settings in every test
✔ Hard to maintain
✔ Inconsistent behavior

- With config:
✔ Centralized control
✔ Cleaner test code
✔ Easy to update settings

### 6.3 Basic Example of Config File

```ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',

  timeout: 30000,

  expect: {
    timeout: 5000,
  },

  use: {
    browserName: 'chromium',
    headless: true,
    baseURL: 'https://example.com',
  },

  reporter: 'html',
});
```

### 6.4 Key Sections Explained
 - `testDir` - Defines where your test files are located
```ts
testDir: './tests'
```

- `timeout` -Maximum time for a test (30 seconds)

```ts
timeout: 30000
```

- `expect`-Timeout for assertions

```ts
expect: {
  timeout: 5000
}
```
- `use` (Very Important)
In Playwright, the use section in the configuration file defines default settings like browser type, headless mode, base URL, and debugging options. These settings are automatically applied to all tests, improving consistency and reducing code duplication.

```ts
use: {
  browserName: 'chromium',
  headless: true,
  baseURL: 'https://example.com',
}
```

- `reporter`-Generates HTML test reports

```ts
reporter: 'html'
```

- Multiple Browser Configuration
Multiple browser configuration in Playwright allows us to run the same test suite across different browsers like Chromium, Firefox, and WebKit using the projects section in the configuration file. It helps ensure cross-browser compatibility without writing separate test code.

```ts
projects: [
  { name: 'chromium', use: { browserName: 'chromium' } },
  { name: 'firefox', use: { browserName: 'firefox' } },
]
```


- Retry & Parallel Execution

```ts
export default defineConfig({
  retries: 2,
  workers: 4,
  fullyParallel: true, //All tests in a file to run in parallel
});

```

`retries` → Retries allow a failed test to run again automatically.
 `workers` → Running multiple tests at the same time

---

- ** Environment-Based Configuration**
Environment-based configuration in Playwright allows us to run the same test suite across different environments like QA, UAT, and production by using environment variables and dynamically setting values such as baseURL in the configuration file.
```ts
const config = {
  qa: { baseURL: 'https://qa.example.com' },
  uat: { baseURL: 'https://uat.example.com' },
  prod: { baseURL: 'https://example.com' },
};

export default defineConfig({
  use: config[process.env.ENV || 'qa'],
});

```

👉 Helps switch between:
✔ Dev
✔ QA
✔ Prod

### *Python*
A configuration file in Playwright is used to store global settings and test configurations so that you don’t need to repeat them in every test.
 It helps you control how tests run from one central place.

> A configuration file is a central file where we define settings like browser type, base URL, timeouts, reporting, and execution options for Playwright tests.

### 6.1 Common Config Files in Playwright + Python

In Python projects (with pytest), configuration is usually managed using:
 - **`pytest.ini`**
pytest.ini is a configuration file used by pytest to define test execution settings such as default options, test paths, markers, and logging. It helps centralize and simplify test configuration in Python automation projects.

Example:

```ini
[pytest]
# Default command-line options
addopts = -v --headed --browser chromium

# Test folder location
testpaths = tests

# Test file naming pattern
python_files = test_*.py

# Custom markers
markers =
    smoke: smoke tests
    regression: regression tests

# Logging configuration
log_cli = true
log_cli_level = INFO
```

 

###  2. `conftest.py`
conftest.py is a special pytest configuration file used to store reusable fixtures, setup, teardown logic, and shared test configurations. Fixtures defined in this file are automatically available to all test files without importing them

Example:

```python
import pytest

@pytest.fixture
def sample_data():
    return "Hello Playwright"
# test case

def test_example(sample_data):
    print(sample_data)

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
```
conftest.py → Provides Fixtures → Tests Use Fixtures
```
This setup will be reused across all tests

 - **.env**
A .env file is used to store environment variables such as URLs, usernames, passwords, and API keys separately from the code. It improves security, maintainability, and supports environment-based configuration.
Example .env File
```python
BASE_URL=https://example.com
USERNAME=admin
PASSWORD=1234
API_KEY=abc123
```
How to Read .env in Python
```
#Install package
pip install python-dotenv
# Python Example
from dotenv import load_dotenv
import os
load_dotenv()

url = os.getenv("BASE_URL")
username = os.getenv("USERNAME")
print(url)
print(username)
```
Why .env is Important in Automation
✔ Secure credentials
✔ Easy environment switching
✔ Cleaner code
✔ Better maintainability

- **config.ini**
  config.ini is a configuration file used to store reusable settings such as URLs, browser configurations, timeouts, and environment details separately from the code. It improves maintainability and supports environment-based execution
  
```python
  # Example config.ini
[QA]
base_url = https://www.redbus.in/

[UAT]
base_url = https://uat.makemytrip.com

[GRID]
grid_url = http://localhost:4444/wd/hub
```
How to Read config.ini in Python

```python
# Using configparser
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
url = config['QA']['base_url']
print(url)
```
Why We Use config.ini
✔ Store configuration separately from code
✔ Support multiple environments
✔ Avoid hardcoding values
✔ Easy maintenance

-  **Custom Config File (Optional)**
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

 - **Why Configuration File is Important**
✔ Avoid code duplication
✔ Centralized control
✔ Easy to maintain
✔ Environment-based execution (QA, Dev, Prod)
✔ Improves framework design


---
---

## 7. What is `@playwright/test` in Playwright?
@playwright/test is the official Playwright test runner that provides the testing framework, including test functions, fixtures, assertions, and execution capabilities like parallel runs and reporting.

> Simple Definition : `@playwright/test` = **Test runner + Assertions + Fixtures + Reporting + Execution engine**

It provides everything you need to:
Write tests
Run tests
Manage fixtures -setup/teardown
Perform assertions -Validate results


### 7.1 Why Do We Need It?
Without @playwright/test you can automate browser actions but lack structure, assertions, reporting, and parallel execution, whereas with @playwright/test everything is built‑in and ready to use.


### 7.2 What It Provides (Core Features)
- **Test Runner**
In Playwright, this functionality is provided by @playwright/test.
A Test Runner is a tool manages the entire test lifecycle
It manages setup and teardown,executes test cases, handles parallel execution and retries, and generates test reports. 

```ts
import { test } from '@playwright/test';

test('example test', async ({ page }) => {
  await page.goto('https://example.com');
});
```
What Does a Test Runner Do?
✔ Finds Test Files- Looks inside your project (e.g., tests/ folder)
✔ Executes Tests- Runs each test step-by-step
✔ Manages Setup & Teardown- Runs hooks (beforeEach, afterEach) ,Handles fixtures
✔ Runs Tests in Parallel -Executes multiple tests at the same time 
✔ Handles Retries- Re-runs failed tests
✔ Generates Reports- Shows pass/fail results, Provides logs and screenshots

- ** Assertions (`expect`) **
Assertions are verify that the actual result matches the expected result. 
In Playwright, assertions are implemented using the expect API and support auto-waiting(Auto-retries until condition is met) for reliable test execution.

```ts
import { expect } from '@playwright/test';
await expect(page).toHaveTitle(/Example/);
```

- **Built-in Fixtures**
Built-in fixtures in Playwright are predefined objects like page, browser, and context that are automatically provided to test functions. They help perform actions, manage browser sessions, and simplify test development without manual setup.

```ts
test('test with fixture', async ({ page }) => {
  await page.goto('https://example.com');
});
```
Common Built-in Fixtures
✔ page- Represents a browser tab Used for actions like:
goto()
click()
fill()
✔ context- Represents a browser session (like incognito) Handles: Cookies, Storage
✔  browser - Represents the full browser instance 
✔  request- Used for API testing
✔  testInfo- Provides test metadata: Test name, Status, Retry info


-  **Parallel Execution**
Parallel execution is the process of running multiple test cases simultaneously using multiple workers. In Playwright, it improves test execution speed and is configured using the workers setting.

✔ Sequential Execution (Slow)
```
Test 1 → Test 2 → Test 3 → Test 4
```

✔ Parallel Execution (Fast)
```
Test 1   Test 2   Test 3   Test 4
   \        |        |        /
     Running at the same time
```

```bash
npx playwright test --workers=4
```

✔ How It Works in Playwright
Playwright uses workers (separate processes)
Each worker Runs tests independently, Has its own browser instance

```
export default defineConfig({
  workers: 4,
});
```


 - **Hooks (Setup & Teardown)**
Hooks are special functions that run before or after your tests.
Hooks in Playwright are lifecycle methods like beforeAll, beforeEach, afterEach, and afterAll that run at specific stages of test execution. They are used for setup and teardown tasks to avoid code duplication.

```ts
test.beforeEach(async ({ page }) => {
  await page.goto('https://example.com');
});
```
 Types of Hooks
  ✔ beforeAll - Runs only once before all tests in a file
```ts
test.beforeAll(async () => {
  console.log('Runs once before all tests');
});

```

 ✔ beforeEach- Runs before every test
```ts
test.beforeEach(async ({ page }) => {
  await page.goto('https://example.com');
});
```


 ✔ afterEach- Runs after every test
```ts
test.afterEach(async () => {
  console.log('Runs after each test');
});
```


✔ afterAll- Runs once after all tests finish
```ts
test.afterAll(async () => {
  console.log('Runs once after all tests');
});
```
* Example
```ts
import { test } from '@playwright/test';

test.beforeAll(async () => {
  console.log('Start');
});

test.beforeEach(async ({ page }) => {
  await page.goto('https://example.com');
});

test('Test 1', async ({ page }) => {});
test('Test 2', async ({ page }) => {});

test.afterEach(async () => {
  console.log('After each test');
});

test.afterAll(async () => {
  console.log('End');
});

```
✔ Execution Order
```
beforeAll → beforeEach → Test → afterEach → beforeEach → Test → afterEach → afterAll
```

- ** Reporting **
Reporting in Playwright is the process of generating test execution results, including pass/fail status, logs, screenshots, and error details. Playwright provides built-in reporters like HTML, JSON, and list for better analysis and debugging.

```bash
npx playwright show-report
```
* Configure Reporting in playwright.config.ts
```ts
export default defineConfig({
  reporter: 'html',
});
```

- **Multiple Reporters (Advanced)**
```ts
export default defineConfig({
  reporter: [
    ['html'],
    ['list'],
    ['json', { outputFile: 'results.json' }]
  ],
});
```


- ** Useful Debug Options (with Reports 🔥)**
use: {
  screenshot: 'only-on-failure',
  video: 'retain-on-failure',
  trace: 'on-first-retry'
}



-  **Retries & Timeouts**
Retries in Playwright are used to rerun failed tests to handle flaky behavior, while timeouts define the maximum time allowed for test execution, actions, or assertions. Retries improve stability, and timeouts ensure tests do not run indefinitely.

```ts
export default defineConfig({
  retries: 2,
  retries: process.env.CI ? 2 : 0
});
```

 Types of Timeouts

✔ Test Timeout -Max time for entire test (30 seconds)
```ts
export default defineConfig({
  timeout: 30000,
});
```

✔ Assertion Timeout -Time to wait for assertion
```ts
expect: {
  timeout: 5000
}
```

✔ Action Timeout- Time for actions like:
```ts
use: {
  actionTimeout: 10000
}
click
fill
```
✔ Navigation Timeout- Time for page load/navigation
```
use: {
  navigationTimeout: 15000
}
 Example
await page.goto('https://example.com', { timeout: 15000 });

```
- **Test Functions**
Test functions in Playwright are defined using the test() method and represent individual test cases. Each function contains the test steps, actions, and assertions, and is executed by the Playwright test runner.
```ts
test('Test Name', async ({ page }) => {
  
  // 1. Setup (optional)
  
  // 2. Actions
  await page.goto('...');
  
  // 3. Assertions
  await expect(page).toBeVisible();
  
});
```

### 7.4 Example Using `@playwright/test`

```ts
import { test, expect } from '@playwright/test';

test('login test', async ({ page }) => {
  await page.goto('https://example.com');

  await page.fill('#username', 'admin');
  await page.fill('#password', 'password');

  await page.click('#login');

  await expect(page).toHaveURL(/dashboard/);
});
```

### 7.5 Difference: Playwright vs `@playwright/test`
Playwright is a browser automation library used to interact with web applications, 
whereas @playwright/test is the official test runner that provides test structure, assertions, fixtures, parallel execution, and reporting. 
In real projects, both are used together.

| Feature            | Playwright Core | `@playwright/test` |
| ------------------ | --------------- | ------------------ |
| Browser automation | ✅ Yes           | ✅ Yes              |
| Test runner        | ❌ No            | ✅ Yes              |
| Assertions         | ❌ No            | ✅ Yes              |
| Fixtures           | ❌ No            | ✅ Yes              |
| Reporting          | ❌ No            | ✅ Yes              |



### 7.6 Real-World Usage

In most projects:

* We always use `@playwright/test`
* It acts as the **foundation of the automation framework**

---
---

## 8. What is the Page Class in Playwright?

In Playwright, the Page class represents a single browser tab where all your test actions happen.

> In simple terms: **Page = Browser Tab = Where you interact with the web application**


### 8.1 Why Page Class is Important

Whenever you automate a web application, you need something to:
✔ Open a URL
✔ Click buttons
✔ Enter text
✔ Validate UI
 The **Page class provides all these capabilities**.

### 8.2 What Can You Do with Page?
page object you can open websites, click elements, enter text, retrieve data, and perform assertions to validate expected behavior.
- **Open Website**

```typescript id="rrjlwm"
await page.goto('https://example.com');
```
```python id="ewd4a6"
page.goto("https://example.com")
```

- **Click Elements**

```typescript id="8f0dzd"
const loginButton = page.locator('#login');

await loginButton.click();
```

```python id="tt0mgh"
login_button = page.locator("#login")

login_button.click()
```

- **Enter Text**

```typescript id="3z8m6p"
const usernameInput = page.locator('#username');

await usernameInput.fill('admin');
```

```python id="w38sjn"
username_input = page.locator("#username")

username_input.fill("admin")
```

- **Get Data**

```typescript id="ap6n5t"
const title = await page.title();

console.log(title);
```


```python id="azrk3d"
title = page.title()

print(title)
```

- **Assertions**

```typescript id="wjlwm0"
await expect(page).toHaveURL(
  'https://example.com'
);
```

```python id="j3jlwm"
from playwright.sync_api import expect

expect(page).to_have_url(
    "https://example.com"
)
```



### 8.3 Where Page Comes From

You don’t usually create it manually. It is provided by Playwright through **fixtures**.
Internally:
browser → context → page

```ts
import { test } from '@playwright/test';

test('example', async ({ page }) => {
  await page.goto('https://example.com');
});
```
```python
def test_example(page):

    page.goto("https://example.com")
```
✔ `page` is an instance of the **Page class**


### 8.4 How Page Fits in Architecture
In Playwright architecture, the Page class acts as an interface between the test script and the browser. The test interacts with the Page object, which sends commands to the Playwright core, and the core communicates with the browser to execute actions.
Hierarchy:

```text
Browser → Context → Page
```
✔ **Browser** → Entire browser instance
✔ **Context** → Separate session (like incognito)
✔ **Page** → Individual tab

### 8.5 Common Methods in Page Class
 - **Navigate to a URL**

```typescript id="mjlwm1"
await page.goto('https://example.com');
```
```python id="zjlwm1"
page.goto("https://example.com")
```

-  **Click an Element**
```typescript id="ajlwm2"
const loginButton = page.locator('#login');

await loginButton.click();
```
```python id="bjlwm2"
login_button = page.locator("#login")

login_button.click()
```
= **Enter Text**

```typescript id="cjlwm3"
const usernameInput = page.locator('#username');

await usernameInput.fill('admin');
```

```python id="djlwm3"
username_input = page.locator("#username")

username_input.fill("admin")
```

- **Get Page Title**
```typescript id="ejlwm4"
const title = await page.title();

console.log(title);
```
```python id="fjlwm4"
title = page.title()

print(title)
```

- **Take Screenshot**

```typescript id="gjlwm5"
await page.screenshot({
  path: 'image.png'
});
```

```python id="hjlwm5"
page.screenshot(
    path="image.png"
)
```

- **Handle Navigation**

```typescript id="ijlwm6"
await page.waitForURL('**/dashboard');
```
```python id="jjlwm6"
page.wait_for_url("**/dashboard")
```

✔ Example (Real Test)

```ts
import { test, expect } from '@playwright/test';

test('login test', async ({ page }) => {

  await page.goto('https://example.com');

  const usernameInput = page.locator('#username');
  const passwordInput = page.locator('#password');
  const loginButton = page.locator('#login');

  await usernameInput.fill('admin');

  await passwordInput.fill('password');

  await loginButton.click();

  await expect(page).toHaveURL(/dashboard/);

});
```
```python
from playwright.sync_api import expect 
def test_login(page):

    page.goto("https://example.com")

    username_input = page.locator("#username")

    password_input = page.locator("#password")

    login_button = page.locator("#login")

    username_input.fill("admin")

    password_input.fill("password")

    login_button.click()

    expect(page).to_have_url(
        r".*dashboard.*"
    )
```
All actions happen using the Page class

### 8.7 Multiple Pages (Tabs)

In Playwright, multiple pages represent multiple browser tabs within the same context. Each tab is controlled using a separate Page object, and new tabs can be handled using context.waitForEvent('page').
```
browser
   └── context
         ├── page (Tab 1)
         ├── page (Tab 2)
         └── page (Tab 3)
```
All tabs belong to the same context (session)

✔ Open Multiple Tabs Manually
```
const page1 = await context.newPage();
const page2 = await context.newPage();
await page1.goto('https://example.com');
await page2.goto('https://google.com');
```

✔ Handle New Tab (Popup)
When clicking opens a new tab:
```
const [newPage] = await Promise.all([
  context.waitForEvent('page'), // wait for new tab
  page.click('#open-tab'),      // action that opens tab
]);
```

✔ Get All Open Tabs
```
const pages = context.pages();
console.log(pages.length);
```
✔ Switch Between Tabs
```
await page1.bringToFront();
```
Makes that tab active

✔ Close a Tab
```
await page2.close();
```

✔ Real Example (Common Scenario)
login opens dashboard in new tab:

```
const [dashboard] = await Promise.all([
  context.waitForEvent('page'),
  page.click('text=Login'),
]);

await dashboard.waitForLoadState();
```

### 8.8 Key Features of Page Class

✔ Handles all user interactions
✔ Supports auto-waiting
✔ Works with locators and selectors
✔ Enables network interception
✔ Supports screenshots, videos, and tracing


### 8.* Page vs Browser vs Context
In Playwright, the browser represents the entire browser instance, the context represents an isolated session like an incognito window, and the page represents a single tab where test actions are performed. They follow a hierarchical relationship: browser → context → page.

- ** Browser**
 Browser = Entire browser application. Like Chrome, Firefox, Safari
```
const browser = await chromium.launch();
```
✔ Starts the browser
✔ Controls whole application
✔ Can have multiple contexts

- **Context**
Context = Isolated browser session (like Incognito mode)
```
const context = await browser.newContext();
```
✔ Separate cookies
✔ Separate storage
✔ Simulates different users
 
Multiple contexts = multiple users


| Component | Description                     |
| --------- | ------------------------------- |
| Browser   | Whole browser instance          |
| Context   | Isolated session                |
| Page      | Single tab (actual interaction) |

- ** Page **
Page = Single browser tab
```
const page = await context.newPage();
```

✔ Used for actions
✔ Interacts with UI
✔ Main object in tests


---
---
## 9. How to Navigate to Specific URLs in Playwright?
Navigation in Playwright is mainly done using the **`page.goto()`** method from the **Page class**. It tells the browser to open a specific URL and wait for the page to load.

- ** Basic Navigation **

Syntax

```ts
await page.goto('https://example.com');
```
This:
✔ Opens the given URL
✔ Waits for the page to load (auto-wait)


-  **Simple Sample Test**

```ts
import { test, expect } from '@playwright/test';

test('navigate to homepage', async ({ page }) => {
  await page.goto('https://example.com');

  await expect(page).toHaveTitle(/Example/);
});
```

- **Using Base URL (Recommended in Real Projects)**

Instead of writing full URLs every time, define a **baseURL** in config:

```ts
// playwright.config.ts
use: {
  baseURL: 'https://example.com',
}
```

Test Code :

```ts
test('navigate using baseURL', async ({ page }) => {
  await page.goto('/login');

  await expect(page).toHaveURL(/login/);
});
```

Playwright automatically combines:

```
baseURL + path → https://example.com/login
```


- **Navigation with Options**

You can control how Playwright waits for the page:

```ts
await page.goto('https://example.com', {
  waitUntil: 'load',
  timeout: 60000,
});
```
✔ `waitUntil` Options
✔ `'load'` → waits for full page load
✔ `'domcontentloaded'` → waits for HTML only
✔ `'networkidle'` → waits until network is quiet


- **Navigating Between Pages**

```ts
test('multiple navigation', async ({ page }) => {
  await page.goto('https://example.com');

  await page.click('text=More information');

  await page.waitForURL('**/more');

  await expect(page).toHaveURL(/more/);
});
```

- ** Handling Redirects**

```ts
test('redirect test', async ({ page }) => {
  await page.goto('http://example.com');

  await expect(page).toHaveURL('https://example.com/');
});
```

 Playwright automatically follows redirects


-- **Navigation with Query Parameters**

```ts
await page.goto('https://example.com/search?q=playwright');
```
 Useful for: Search testing, Dynamic URLs


- **Navigation in Multiple Tabs**

```ts
test('open new tab and navigate', async ({ context }) => {
  const newPage = await context.newPage();

  await newPage.goto('https://example.com');

  await expect(newPage).toHaveTitle(/Example/);
});
```

---
---

## 10. What are the different types of reporters that the playwright supports?

In Playwright, reporters are used to display and store test resultS after execution. They help you understand:
✔ Which tests passed/failed
✔ Execution time
✔ Error details
✔ Screenshots/videos (if configured)

Playwright supports multiple reporters such as HTML, List, Line, Dot, JSON, JUnit, and GitHub reporters. These reporters provide test results in different formats like visual dashboards, console logs, or structured files for CI/CD integration.

### 10.1 What is a Reporter?
 A reporter is a tool that formats test results into:
* Console output
* HTML reports
* JSON files
* CI-friendly formats


### 10.2 Built-in Reporters in Playwright

Playwright provides several built-in reporters:
- **List Reporter (Default)**
The List Reporter in Playwright displays test execution results in a detailed, line-by-line format in the console, showing the status of each test such as pass or fail, making it useful for local execution and debugging.

```ts
export default defineConfig({
  reporter: 'list',
});
```
```python
pytest -v
```
 Features:
✔ Shows each test step in console
✔ Displays pass/fail status
✔ Easy to read

Best for: Local development


- **Line Reporter**
The Line Reporter in Playwright displays test execution progress in a single updating line in the console, showing the current test status and progress. It is useful for reducing log clutter, especially in CI/CD environments.

```ts
export default defineConfig({
  reporter: 'line',
});
```
```python
pytest -v
```
Features:
✔ Compact output
✔ Updates in a single line

Best for: CI logs (less clutter)

- **Dot Reporter**
The Dot Reporter in Playwright displays test results as simple symbols, where each dot represents a passed test and a letter like ‘F’ represents a failed test. It is useful for minimal and fast output, especially in CI environments.

```ts
export default defineConfig({
  reporter: 'dot',
});
```
```python
pytest -q
```
Features:
✔ Each test = dot (`.`)
✔ Minimal output
 Best for: Very large test suites

4. HTML Reporter (Most Important)
The HTML Reporter in Playwright generates a detailed and interactive web-based report that shows test execution results, including pass/fail status, logs, screenshots, videos, and trace information. It is mainly used for debugging and analysing test failures.

```ts
export default defineConfig({
  reporter: 'html',
});

use: {
  screenshot: 'only-on-failure',
  video: 'retain-on-failure',
  trace: 'on-first-retry'
}
```
```bash
npx playwright show-report
```
```python
# Install:
pip install pytest-html

# Run:
pytest --html=report.html

# Generates:
report.html
```

Best for:
✔ Debugging
✔ Sharing reports


- **JSON Reporter** 
The JSON Reporter in Playwright generates test results in a structured JSON format, which is mainly used for integration with CI/CD tools, custom reporting systems, and automated analysis.

```ts
export default defineConfig({
  reporter: [['json', { outputFile: 'results.json' }]],
});

```
```pyhon
# Install:
pip install pytest-json-report
# Run:
pytest --json-report
# Generates:
.json report
Useful for integrations and dashboards.
```

 Features:
✔ Outputs results in JSON format
✔ Best for: Custom integrations, Data processing

- **JUnit Reporter**
The JUnit Reporter in Playwright generates test results in XML format, which is widely used by CI/CD tools like Jenkins to display and track test execution results. It helps integrate automated tests into continuous integration pipelines.

```ts
export default defineConfig({
  reporter: [
    ['junit', { outputFile: 'results.xml' }]
  ],
});
```
```python
# Run
pytest --junitxml=report.xml
# Generated File
report.xml
```
Features:

✔ XML format
✔ Best for: CI/CD tools (like Jenkins)

- **GitHub Reporter**
The GitHub Reporter in Playwright is used to display test results directly in GitHub Actions. It provides inline annotations, error messages, and links to the source code, making it easier to debug failures in CI pipelines.
```ts
export default defineConfig({
  reporter: 'github',
});

```
Features:
✔ Integrates with GitHub Actions
✔ Shows annotations in PRs
✔ Best for: GitHub pipelines

 - **Multiple Reporters (Very Useful)**

You can use more than one reporter:

```ts
reporter: [
  ['list'],
  ['html'],
  ['junit', { outputFile: 'results.xml' }]
]
```

✔ Configuration Example

```ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  reporter: [
    ['list'],
    ['html', { open: 'never' }],
  ],
});
```



### 10.3 Real-World Usage
  
In real‑world usage, Playwright reporters are chosen based on context—developers use list or HTML for local debugging, JUnit or line for CI/CD pipelines, GitHub reporters for GitHub Actions, and JSON for data processing.

| Scenario        | Reporter Used |
| --------------- | ------------- |
| Local debugging | list / html   |
| CI/CD pipelines | junit / line  |
| GitHub Actions  | github        |
| Data processing | json          |

---
---

## 11. What are Locators in Playwright?
Locators in Playwright are used to identify and interact with elements on a web page. They provide a reliable and flexible way to perform actions like clicking, typing, and validation, with built-in auto-waiting for better stability.

 > In simple terms:**Locator = a strategy to identify an element (button, input, link, etc.) on the page**

- Why Locators are Important:

To automate any UI action, you must first identify the element: Locators make this possible in a reliable and smart way.
✔ Identify elements reliably
✔ Perform actions (click, type, etc.)
✔ Avoid flaky tests
✔ Support auto-waiting

- Key Feature of Playwright Locators
Playwright locators provide features like auto-waiting, lazy evaluation, retry mechanisms, multiple locating strategies, strict mode, chaining, and built-in actionability checks, making tests more stable and reliable.
This reduces flaky tests significantly.

### 11.1 Common Types of Locators in Playwright
- **Role-based Locator (Recommended)**

```ts id="v7t3cl"
await page.getByRole('button', { name: 'Login' }).click();
```
```python
page.get_by_role('button', name='Login').click()
```
 ✔ Uses accessibility roles
✔ Most stable and readable

- **Text-based Locator** : Finds element by visible text

```ts id="0p9r6m"
await page.getByText('Submit').click();
```
```python
page.get_by_text('submit').click();
```
 

- **Label-based Locator** :Works with form labels

```ts id="g2g8pu"
await page.getByLabel('Username').fill('admin');
```
```python
page.get_by_label('Password').fill('admin)
```



- **Placeholder Locator**

```ts id="0sc9i1"
await page.getByPlaceholder('Enter email').fill('test@example.com');
```
```python
page.get_by_placeholder('Enter Name').fill('Pasad')
```

- **Alt Text Locator** : Used for images

```ts id="9y4o1n"
await page.getByAltText('logo').click();
```
```python
page.get_by_alt_text('logo').click()
```


- **Title Locator**

```ts id="7z2h6h"
await page.getByTitle('More info').click();
```
```python
page.get_by_title('Home Page').clcik()
```

- **Test ID Locator (Best for Automation)**

```ts id="1kz9di"
await page.getByTestId('login-btn').click();
```
```python
page.get_by_testid('login-btn').click()
```

✔ Requires `data-testid` attribute

- **CSS Selector Locator**

```ts id="t8n1vc"
await page.locator('#login').click();
```
```python
page.locator('#login').click();
```

- **XPath Locator**

```ts id="a1b2c3"
await page.locator('//button[text()="Login"]').click();
```
```python
page.locator('//button[text()="Login"]').click();
```

- **Chaining Locators**

```ts id="v8m2dw"
await page.locator('.form').getByRole('button', { name: 'Submit' }).click();
```
```python
page.locator('.form').get_by_role('button',name= 'submit').click();
```
Helps target elements more precisely


- **Filtering Locators**

```ts id="6a4o0x"
await page.getByRole('listitem').filter({ hasText: 'Product 1' }).click();
```
```python
 page.getByRole('listitem').filter(hasText ='Product 1').click();
```

#### Example Test Using Locators

```ts id="d9t2fx"
import { test, expect } from '@playwright/test';

test('login test', async ({ page }) => {
  await page.goto('https://example.com');

  await page.getByLabel('Username').fill('admin');
  await page.getByLabel('Password').fill('password');

  await page.getByRole('button', { name: 'Login' }).click();

  await expect(page.getByText('Welcome')).toBeVisible();
});
```
```python id="v8m2ql"
from playwright.sync_api import expect
def test_login(page):

    page.goto("https://example.com")

    page.get_by_label("Username").fill("admin")

    page.get_by_label("Password").fill("password")

    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Welcome")).to_be_visible()
```



### 11.2 Locator Priority (Best Practice Order)
  
The best practice order for Playwright locators is to prioritize getByRole(), then getByLabel(), getByText(), getByTestId(), and use CSS/XPath only as a last option.

✔ `getByRole()/get_by_role()` 
✔ `getByLabel()/get_by_label()`
✔ `getByText()/get_by_text()`
✔ `getByTestId()/get_by_testid()`
✔ CSS / XPath (last option)


### 11.3 Locator vs Selector (Important)
A selector is a string used to identify elements on a web page, whereas a locator is a Playwright object that uses selectors with additional features like auto-waiting, retries, and lazy evaluation, making it more reliable and recommended for test automation.
```ts
'#login'
'text=Submit'
'.btn-primary'
```

| Feature     | Locator | Selector (CSS/XPath) |
| ----------- | ------- | -------------------- |
| Auto-wait   | ✅ Yes   | ❌ No              |
| Retry       | ✅ Yes   | ❌ No              |
| Reliability | High    | Medium               |
| Readability | High    | Low                  |

---
---
## 12. What are the different types of text selectors available in Playwright?

In Playwright, text selectors are used to locate elements based on the visible text content shown on the UI. These are very useful because they mimic how a real user sees and interacts with the page.
Playwright supports different text selectors such as text= selector, getByText()/get_by_text(), partial and regex matching, getByRole()/get_by_role() with accessible name, and filtering using hasText. Among these, getByRole()/get_by_role() and getByText()/get_by_text() are recommended for stable and reliable tests.

- **`getByText()/get_by_text()` (Most Common)**

```ts
await page.getByText('Login').click();
```
```python
page.get_by_text('Login').click();

```
 Features:
✔ Matches visible text
✔ Works across elements (button, div, span, etc.)
✔ Supports partial match by default
✔ Exact Match- Matches only exact text

```ts
await page.getByText('Login', { exact: true }).click();
```
```python
page.get_by_text('Login', exact= true).click();

```


- **Text with Locator API (`locator('text=...')`)**

```ts
await page.locator('text=Login').click();
```
 Features:
✔ Legacy-style text selector
✔ Still supported
✔ Can be combined with other selectors

- **Partial Text Matching**
```ts
await page.getByText('Log').click();
```
```python
page.get_by_text'Log').click();
```
Matches:
✔ Login
✔ Logout
✔ Logging

- **Regex Text Matching**

```ts
await page.getByText(/login/i).click();
```
✔ Case-insensitive (`i`)
```python
page.get_by_text(re.compile("login", re.IGNORECASE)).click()
```

Features:
✔ Flexible matching

- **Exact Text Selector (Strict Match)**

```ts
await page.locator('text="Login"').click();
```
```python
page.locator('text="Login"').click();
```
✔ Matches only: "Login" (exact text)


- **Text Inside Specific Element**

```ts
await page.locator('button:has-text("Login")').click();
```
```python
page.locator('button:has-text("Login")').click();
```
Features:
✔ Restricts search to specific tag
✔ More precise


- **Filter with Text -Useful when multiple elements exist** 

```ts
await page.locator('.menu-item').filter({ hasText: 'Dashboard' }).click();
```
```python
await page.locator('.menu-item').filter(hasText = 'Dashboard' }).click();
```

- **Text in Nested Elements** 
Matches parent element containing text inside children

```ts
await page.locator('div:has-text("Welcome")').click();
```
```python
page.locator('div:has-text("Welcome")').click();
```


- **Combining Role + Text (Best Practice)**

```ts
await page.getByRole('button', { name: 'Login' }).click();
```
```pyhon
page.get_by_role('button', name=  'Login').click();
```
Preferred approach:
✔ More stable
✔ Accessibility-based

### 12.1 Example Test Using Text Selectors

```ts
import { test, expect } from '@playwright/test';

test('text selector example', async ({ page }) => {
  await page.goto('https://example.com');

  await page.getByText('More information').click();

  await expect(page.getByText('Example Domain')).toBeVisible();
});
```

```python
from playwright.sync_api import expect
def test_text_selector_example(page):

    page.goto("https://example.com")

    page.get_by_text("More information").click()

    expect(page.get_by_text("Example Domain")).to_be_visible()
```

### 12.2 Best Practices

* Prefer `getByRole()/get_by_role()` with text → most reliable
* Use `getByText()/get_by_text()` for simple cases
* Avoid overusing XPath for text
* Use regex for dynamic text

### 12.3 Quick Summary Table

| Selector Type | Example                      | Usage               |
| ------------- | ---------------------------- | ------------------- |
| `getByText()` | `'Login'`                    | Basic text matching |
| Exact match   | `{ exact: true }`            | Strict matching     |
| Regex         | `/login/i`                   | Flexible matching   |
| `text=`       | `'text=Login'`               | Legacy selector     |
| `has-text()`  | `'button:has-text("Login")'` | Scoped matching     |
| Filter        | `.filter({ hasText })`       | Refined search      |

---
---

## 13. what are the assertion ? How to use assertions in Playwright?
Assertions in Playwright are used to verify that the actual output matches the expected result. They are implemented using the `expect` API and support auto-waiting, ensuring reliable and stable test validation.

> In simple terms: Assertion = Check + Validation
✔ If the condition is true → test passes
✔ If the condition is false → test fails


- **Why Assertions are Important**
Assertions are important because they validate that the actual behavior of the application matches the expected outcome. They determine whether a test passes or fails, help catch bugs early, and ensure reliable and meaningful test execution.

Without assertions:
✔ Your test only performs actions
✔ No validation → no real testing

With assertions:
✔ You confirm results
✔ Ensure correctness of UI or behavior


- **Assertion Library in Playwright**
The assertion library in Playwright is provided by the expect API from @playwright/test. It includes built-in methods for validating web elements, page states, and general values, with features like auto-waiting and retry mechanisms to ensure reliable test execution.
Playwright provides built-in assertions using:

```ts
import { expect } from '@playwright/test';
```
```python
from playwright.sync_api import expect
```
 `expect()` is the main function used for assertions.


- **Key Feature: Auto-Retry (Very Important)**
Playwright assertions provide features like auto-waiting, retry mechanisms, built-in web assertions, smart timeouts, soft assertions, and clear error messages, making tests more reliable and less flaky.

Playwright assertions:
✔ Automatically retry until condition is met
✔ Wait until timeout
This makes tests:
✔ More reliable
✔ Less flaky



- **Basic Syntax**

```ts
await expect(actual).toBe(expected);
```
```pyhton
await expect(actual).to_be(expected);
```

### 13.1 Types of Assertions in Playwright
Playwright provides different types of assertions such as web assertions for page validation, locator assertions for element validation, generic assertions for values, soft and hard assertions for execution control, and negative assertions for validating absence. These assertions help ensure accurate and reliable test validation.

- ** Page Assertions**
Page assertions in Playwright are used to validate properties of the web page such as the URL and title. They ensure that the correct page is loaded and help verify navigation and application flow.

```ts
await expect(page).toHaveURL('https://example.com'); // Verifies current page URL
await expect(page).toHaveURL(/dashboard/); //Partial Match
await expect(page).toHaveTitle(/Example/); //Verifies the page title  With Regex Partial / flexible match
await expect(page).toHaveTitle(/Example/); //Verifies the page title
await expect(page.locator('h1')).toBeVisible(); // Validate important page element is visible -Confirms page is loaded correctly
await expect(page).toHaveScreenshot(); // Visual comparison // Detects UI changes
await page.waitForLoadState('load'); //Wait for page load - Often used with assertions
```
```python id="q8m2pl"
from playwright.sync_api import expect
import re
expect(page).to_have_url("https://example.com")  # Verifies current page URL
expect(page).to_have_url(re.compile("dashboard"))  # Partial Match
expect(page).to_have_title(re.compile("Example"))  # Verifies the page title with Regex Partial / flexible match
expect(page).to_have_title(re.compile("Example"))  # Verifies the page title
expect(page.locator("h1")).to_be_visible()  # Validate important page element is visible # Confirms page is loaded correctly
expect(page).to_have_screenshot()  # Visual comparison # Detects UI changes
page.wait_for_load_state("load")  # Wait for page load # Often used with assertions
```



- **Locator Assertions (Most Used)**
Locator assertions in Playwright are used to validate the state and properties of elements on a web page, such as visibility, text, value, and attributes. They work with locators and include auto-waiting and retry mechanisms for reliable test execution.

```ts
await expect(page.locator('#login')).toBeVisible(); // Check if element is visible
await expect(page.locator('#error')).toBeHidden(); // Check if element is not visible
await expect(page.locator('#username')).toHaveValue('admin');
await expect(page.locator('h1')).toHaveText('Welcome'); //Validate exact text
await expect(page.locator('h1')).toHaveText(/Welcome/); //  Partial / Regex
await expect(page.locator('h1')).toContainText('Wel'); // Check partial text
await expect(page.locator('#username')).toHaveValue('admin'); //Check input field value
await expect(page.locator('#submit')).toBeEnabled();
await expect(page.locator('#agree')).toBeChecked(); //For checkboxes / radio buttons
await expect(page.locator('#link')).toHaveAttribute('href', '/home'); 
await expect(page.locator('li')).toHaveCount(5); //Number of elements
await expect(page.locator('button')).toHaveCSS('color', 'rgb(0, 0, 0)'); //

```
```python id="m7q2pl"
from playwright.sync_api import expect
import re
expect(page.locator("#login")).to_be_visible() # Check if element is visible
expect(page.locator("#error")).to_be_hidden() # Check if element is not visible
expect(page.locator("#username")).to_have_value("admin") # Check input field value
expect(page.locator("h1")).to_have_text("Welcome") # Validate exact text
expect(page.locator("h1")).to_have_text(re.compile("Welcome")) # Partial / Regex
expect(page.locator("h1")).to_contain_text("Wel")b# Check partial text
expect(page.locator("#username")).to_have_value("admin") # Check input field value
expect(page.locator("#submit")).to_be_enabled() # Check button is enabled
expect(page.locator("#agree")).to_be_checked() # For checkboxes / radio buttons
expect(page.locator("#link")).to_have_attribute("href","/home") # Validate attribute value
expect(page.locator("li")).to_have_count(5) # Number of elements
expect(page.locator("button")).to_have_css("color","rgb(0, 0, 0)") # Validate CSS property
```



- **Text Assertions**

Text assertions in Playwright are used to verify the text content of elements using methods like toHaveText and toContainText. They support exact and partial matching, along with auto-waiting, ensuring reliable validation of UI content.

```ts
await expect(page.locator('.message')).toHaveText('Success'); //Checks exact text - Must match exactly
await expect(page.locator('h1')).toHaveText(/Welcome/); //Flexible matching-Partial / case-insensitive
await expect(page.locator('h1')).toContainText('Wel'); // Checks if text contains value -Useful for dynamic text
await expect(page.locator('li')).toHaveText(['Item 1','Item 2','Item 3']); // Multiple Elements Text -Checks list order + content
await expect(page.locator('h1')).toHaveText(/welcome/i); // Ignore Case / Whitespace - Case-insensitive

```
```python id="m7q2pl"
from playwright.sync_api import expect
import re

expect(page.locator(".message")).to_have_text("Success")  # Checks exact text

expect(page.locator("h1")).to_have_text(re.compile("Welcome"))  # Flexible matching

expect(page.locator("h1")).to_contain_text("Wel")  # Checks partial text

expect(page.locator("li")).to_have_text(["Item 1", "Item 2", "Item 3"])  # Multiple elements text

expect(page.locator("h1")).to_have_text(re.compile("welcome", re.IGNORECASE))  # Case-insensitive
```




- **State Assertions**
State assertions in Playwright are used to verify the current condition of elements, such as visibility, enablement, or selection state. Methods like toBeVisible, toBeEnabled, and toBeChecked ensure that elements behave correctly during test execution.

```ts
await expect(page.locator('#login')).toBeVisible();// heck if element is visible on screen
await expect(locator).toBeEnabled(); // Check if element is clickable
await expect(locator).toBeDisabled(); // Check if element is not clickable
await expect(locator).toBeChecked(); //For checkbox / radio button
await expect(page.locator('#error')).toBeHidden(); //Check if element is not visible
await expect(page.locator('#username')).toBeEditable(); // Check if input field is editable
await expect(page.locator('#input')).toBeEmpty(); //Check if input/element is empty

```
```python id="m7q2pl"
from playwright.sync_api import expect

expect(page.locator("#login")).to_be_visible()  # Check if element is visible on screen

expect(locator).to_be_enabled()  # Check if element is clickable

expect(locator).to_be_disabled()  # Check if element is not clickable

expect(locator).to_be_checked()  # For checkbox / radio button

expect(page.locator("#error")).to_be_hidden()  # Check if element is not visible

expect(page.locator("#username")).to_be_editable()  # Check if input field is editable

expect(page.locator("#input")).to_be_empty()  # Check if input/element is empty
```


- **Count Assertions** 
Count assertions in Playwright are used to verify the number of elements matched by a locator using the toHaveCount() method. They support auto-waiting and are useful for validating dynamic lists, tables, and search results.

```ts
await expect(page.locator('.item')).toHaveCount(3);
```
```python id="k7t1zx"
from playwright.sync_api import expect

expect(page.locator(".item")).to_have_count(3)
```



- **Attribute Assertions**
Attribute assertions in Playwright are used to verify the value of HTML attributes of elements using methods like toHaveAttribute(). They support exact and partial matching and include auto-waiting to ensure reliable validation.

```ts
await expect(locator).toHaveAttribute('type', 'text');
await expect(page.locator('a')).toHaveAttribute('href', 'https://example.com');
await expect(page.locator('#btn')).toHaveAttribute('class', 'btn-primary');
await expect(page.locator('#btn')).toHaveAttribute('class', /primary/);
await expect(page.locator('#status')).toHaveAttribute('data-state', 'active');

```
```python id="m7q2pl"
from playwright.sync_api import expect
import re

expect(locator).to_have_attribute("type", "text")

expect(page.locator("a")).to_have_attribute("href", "https://example.com")

expect(page.locator("#btn")).to_have_attribute("class", "btn-primary")

expect(page.locator("#btn")).to_have_attribute("class", re.compile("primary"))

expect(page.locator("#status")).to_have_attribute("data-state", "active")
```



- **Soft Assertions (Optional)**
Soft assertions in Playwright allow tests to continue execution even if an assertion fails, using expect.soft(). They help validate multiple conditions in a single test and report all failures at the end.
Test continues even if it fails

```ts
await expect.soft(page.locator('#msg')).toBeVisible();
import { test, expect } from '@playwright/test';

test('Soft Assertion Example', async ({ page }) => {
  await page.goto('https://example.com');

  await expect.soft(page).toHaveTitle('Wrong Title'); // ❌ fails but continues

  await expect.soft(page.locator('h1')).toHaveText('Example Domain'); // ✔ runs

  console.log('Test continues even after failure');
});
```
```python
import pytest_check as check
from playwright.sync_api import expect


def test_soft_assertion(page):

    page.goto("https://example.com")

    try:
        expect(page).to_have_title("Wrong Title")
    except AssertionError as e:
        check.fail(str(e))

    try:
        expect(page.locator("h1")).to_have_text("Example Domain")
    except AssertionError as e:
        check.fail(str(e))

    print("Test continues even after failure")
```


### 13.2 Timeout in Assertions
Assertion timeout in Playwright defines how long the framework will wait for a condition to be met before failing the assertion. Playwright automatically retries assertions within this timeout, improving test reliability and reducing flakiness.
- **How to Set Assertion Timeout**

✔ Global Timeout (Config) -Applies to all assertions
export default defineConfig({
  expect: {
    timeout: 5000
  }
});

✔ Per Assertion Timeout- Waits up to 10 seconds
```ts
await expect(page.locator('#message')).toHaveText('Success', {
  timeout: 10000
});
```

✔ How It Works Internally
```
Check condition → Not met → Retry → Retry → Retry → Timeout → Fail
```
---
---

## 14. How to Negate Assertions in Playwright?

In Playwright, we can negate assertions using the .not keyword with the expect API. It allows us to verify that a condition is not true, such as checking that an element is not visible or a value does not match.

In Playwright, you negate (reverse) any assertion using:

```ts
.not
```

> In Simple Words `.not` = “This condition should NOT be true”

### 14.1 Basic Syntax

```ts
await expect(locator).not.toMatchCondition();
```
- **Element Not Visible** - Verifies element is NOT visible

```ts
await expect(page.locator('#error')).not.toBeVisible();
```

 - **Text Should NOT Match**

```ts
await expect(page.locator('h1')).not.toHaveText('Error');
```

- **URL Should NOT Be**

```ts
await expect(page).not.toHaveURL('/login');
```

- **Title Should NOT Match**

```ts
await expect(page).not.toHaveTitle('Error Page');
```

- **Element Count Should NOT Be**

```ts
await expect(page.locator('li')).not.toHaveCount(0);
```

 - **Attribute Should NOT Match**

```ts
await expect(page.locator('#btn')).not.toHaveAttribute('disabled', '');
```

- **Checkbox NOT Checked**

```ts
await expect(page.locator('#agree')).not.toBeChecked();
```

- **Example (Real Scenario)**

```ts
test('Negative Validation', async ({ page }) => {
  await page.goto('https://example.com');

  await expect(page.locator('#error')).not.toBeVisible();
});
```

```python id="m7q2pl"
from playwright.sync_api import expect


# Basic Syntax
expect(locator).not_to_match_condition()
# Negative assertion syntax concept


# Element Not Visible
expect(page.locator("#error")).not_to_be_visible()
# Verifies element is NOT visible


# Text Should NOT Match
expect(page.locator("h1")).not_to_have_text("Error")


# URL Should NOT Be
expect(page).not_to_have_url("/login")


# Title Should NOT Match
expect(page).not_to_have_title("Error Page")


# Element Count Should NOT Be
expect(page.locator("li")).not_to_have_count(0)


# Attribute Should NOT Match
expect(page.locator("#btn")).not_to_have_attribute(
    "disabled",
    ""
)


# Checkbox NOT Checked
expect(page.locator("#agree")).not_to_be_checked()


# Example (Real Scenario)
def test_negative_validation(page):

    page.goto("https://example.com")

    expect(page.locator("#error")).not_to_be_visible()
```



✔ How It Works Internally
 Waits until condition becomes **false**
 Retries until timeout

✔ Important Behavior

```ts
await expect(locator).not.toBeVisible();
```

Playwright will:

✔ Wait for element to disappear
✔ Pass if it becomes hidden within timeout



### Why Negative Assertions Are Important

✔ Validate absence of errors
✔ Ensure element is removed
✔ Confirm state changes
✔ Improve test coverage

---
---
## 15. Does Playwright Support XPath?
Yes, Playwright supports XPath selectors using the locator() method or the xpath= prefix. However, it is generally recommended to use Playwright locators like getByRole or CSS selectors instead, as they are more stable and readable.

However: XPath is supported but not recommended as a first choice (Playwright prefers locators like `getByRole`, `getByText`, etc.).

- **How to Use XPath in Playwright**
You can use XPath with the `locator()` method.

Basic Syntax

```ts
await page.locator('//button[text()="Login"]').click();
```
```python id="m7q2pl"
page.locator('//button[text()="Login"]').click()
```



- **Using `xpath=` Prefix (Optional)**
```ts
await page.locator('xpath=//input[@id="username"]').fill('admin');
```
```python id="m7q2pl"
page.locator('xpath=//input[@id="username"]').fill("admin")
```




- **Sample Test Using XPath**

```ts
import { test, expect } from '@playwright/test';

test('login using xpath', async ({ page }) => {
  await page.goto('https://example.com');

  await page.locator('//input[@id="username"]').fill('admin');
  await page.locator('//input[@id="password"]').fill('password');

  await page.locator('//button[text()="Login"]').click();

  await expect(page).toHaveURL(/dashboard/);
});
```
```python id="m7q2pl"
from playwright.sync_api import expect
import re

def test_login_using_xpath(page):

    page.goto("https://example.com")

    page.locator('//input[@id="username"]').fill("admin")

    page.locator('//input[@id="password"]').fill("password")

    page.locator('//button[text()="Login"]').click()

    expect(page).to_have_url(
        re.compile("dashboard")
    )
```

### 15.1 Common XPath Examples

- **By Attribute**

```ts
await page.locator('//input[@name="email"]').fill('test@example.com');
```
- **By Text**

```ts
await page.locator('//a[text()="Home"]').click();
```

- **Contains Text**

```ts
await page.locator('//button[contains(text(),"Login")]').click();
```

- **Parent → Child**

```ts
await page.locator('//div[@class="form"]//input[@type="text"]').fill('data');
```

- **Using Index**

```ts
await page.locator('(//button)[1]').click();
```


- **Chaining with Locator**

```ts
const form = page.locator('//div[@class="form"]');
await form.locator('.//button[text()="Submit"]').click();
```

### 15.2 When Should You Use XPath?
 Use XPath when:
✔ Complex DOM relationships
✔ No good attributes available
✔ Dynamic elements

 Avoid XPath when:

✔ Simpler locators are available
✔ Elements have:
  ✔ Roles
  ✔ Labels
  ✔ Test IDs

### 15.3 Better Alternatives (Recommended)

Instead of XPath:
```ts
//  XPath
await page.locator('//button[text()="Login"]').click();
```

```ts
// Better
await page.getByRole('button', { name: 'Login' }).click();
```
Why better?

✔ More stable
✔ Less brittle
✔ Readable

### 15.4 XPath vs Playwright Locators
XPath is a DOM navigation-based selector that can be fragile and harder to maintain, whereas Playwright locators provide a more reliable and user-friendly way to interact with elements using features like auto-waiting and retry mechanisms. Playwright locators are recommended over XPath for stable test automation.

| Feature       | XPath           | Playwright Locators |
| ------------- | --------------- | ------------------- |
| Readability   | Low             | High                |
| Stability     | Medium          | High                |
| Auto-wait     | ✅ (via locator) | ✅                   |
| Best practice | ❌ Limited use   | ✅ Preferred         |

---
---

## 16 Command Line Options in Playwright
Command-line options in Playwright are arguments passed while running test commands to control execution behavior, such as selecting tests, browsers, parallel execution, retries, and reporting. They provide flexibility without modifying the test code.

> In simple terms: **CLI options = runtime controls for test execution**
### TypeScript
- **Basic Command** -Runs all tests using default configuration

```bash
npx playwright test
```

- **Commonly Used Command Line Options**

✔ Run Specific Test File -Executes only that file

```bash
npx playwright test tests/example.spec.ts
```

✔ Run Tests in Headed Mode -Opens browser UI (useful for debugging)

```bash
npx playwright test --headed
```

✔ Run in Specific Browser -Runs tests only in Chromium

```bash
npx playwright test --project=chromium
```

✔ Run Tests in Parallel -Executes tests using 4 parallel workers

```bash
npx playwright test --workers=4
```

✔ Run in Debug Mode
Enables:
 Step-by-step execution
Inspector tool

```bash
npx playwright test --debug
```

✔ UI Mode (Interactive Runner) -Opens visual interface to run/debug tests

```bash
npx playwright test --ui
```

✔ Run Tests by Name (grep)-Runs tests matching the keyword

```bash
npx playwright test --grep "login"
```


✔ Skip Tests by Name -Excludes matching tests

```bash
npx playwright test --grep-invert "login"
```

✔ Retry Failed Tests -Retries failed tests 2 times

```bash
npx playwright test --retries=2
```

✔ Set Timeout -Sets test timeout (60 seconds)

```bash
npx playwright test --timeout=60000
```

✔ Run Only Failed Tests -Executes previously failed tests

```bash
npx playwright test --last-failed
```

✔ Generate Trace (Debugging) -Captures trace for debugging

```bash
npx playwright test --trace=on
```

✔ Reporter Selection -Uses HTML reporter

```bash
npx playwright test --reporter=html
```

✔ Quiet Mode -Minimal console output

```bash
npx playwright test --quiet
```
✔ Grep Invert (Exclude Tests) -Exclude tests
```bash
npx playwright test --grep-invert "skip"
```


- **Combining Multiple Options **
Run Chromium tests in UI with 2 workers
```bash
npx playwright test --project=chromium --headed --workers=2
```


- ** Real-World Example**

```bash
npx playwright test tests/login.spec.ts --headed --debug --retries=1
```


This will:

✔ Run only login tests
✔ Open browser UI
✔ Enable debug mode
✔ Retry once if failed
### Python
* **Basic Command** - Runs all tests using default configuration

```bash id="a1b2c3"
pytest
```

* **Commonly Used Command Line Options**

✔ Run Specific Test File - Executes only that file

```bash id="d4e5f6"
pytest tests/test_example.py
```

✔ Run Tests in Headed Mode - Opens browser UI (useful for debugging)

```bash id="g7h8i9"
pytest --headed
```

✔ Run in Specific Browser - Runs tests only in Chromium

```bash id="j1k2l3"
pytest --browser chromium
```

✔ Run Tests in Parallel - Executes tests using 4 parallel workers

```bash id="m4n5o6"
pytest -n 4
```

✔ Run in Debug Mode
Enables:
Step-by-step execution

```bash id="p7q8r9"
pytest --headed --slowmo 500
```

✔ UI Mode (Interactive Runner) - Not available like Playwright TypeScript

```text id="s1t2u3"
No direct equivalent in Playwright Python
```

✔ Run Tests by Name (grep) - Runs tests matching the keyword

```bash id="v4w5x6"
pytest -k "login"
```

✔ Skip Tests by Name - Excludes matching tests

```bash id="y7z8a9"
pytest -k "not login"
```

✔ Retry Failed Tests - Retries failed tests 2 times

```bash id="b1c2d3"
pytest --reruns 2
```

✔ Set Timeout - Sets test timeout (60 seconds)

```bash id="e4f5g6"
pytest --timeout=60000
```

✔ Run Only Failed Tests - Executes previously failed tests

```bash id="h7i8j9"
pytest --last-failed
```

✔ Generate Trace (Debugging) - Captures trace for debugging

```bash id="k1l2m3"
pytest --tracing on
```

✔ Reporter Selection - Uses HTML reporter

```bash id="n4o5p6"
pytest --html=report.html
```

✔ Quiet Mode - Minimal console output

```bash id="q7r8s9"
pytest -q
```

✔ Grep Invert (Exclude Tests) - Exclude tests

```bash id="t1u2v3"
pytest -k "not skip"
```

* **Combining Multiple Options**
  Run Chromium tests in headed mode with 2 workers

```bash id="w4x5y6"
pytest --browser chromium --headed -n 2
```

* **Real-World Example**

```bash id="z7a8b9"
pytest tests/test_login.py --headed --slowmo 500 --reruns 1
```



- ** Why CLI Options are Useful**

✔ No need to modify code
✔ Quick control over execution
✔ Helpful in CI/CD pipelines
✔ Useful for debugging


---
---

## 17. What is headed and headless mode in Playwright?
Headless mode in Playwright runs the browser without a UI for faster execution and is commonly used in CI/CD, while headed mode runs the browser with a visible UI, which is useful for debugging and development

> In **Playwright**, tests can run in two modes:
✔ **Headed mode** → browser UI is visible
✔ **Headless mode** → browser runs in the background (no UI)

- **Headed Mode (Visible Browser)**
The browser opens like a normal user browser, and you can see all actions happening.
```bash
npx playwright test --headed
```
```python
pytest --headed
```

OR in config:

```ts
use: {
  headless: false
}
```
```pyhon
browser = playwright.chromium.launch(    headless=False)
```

 Advantages
✔ Easy debugging
✔ Visual confirmation
✔ Helps understand test flow

 Disadvantages

✔ Slower execution
✔ Uses more system resources

- **Headless Mode (No UI)**

The browser runs **in the background without opening a window**.

```bash
npx playwright test
```
```bash id="a1b2c3"
pytest
```

OR explicitly:

```ts
use: {
  headless: true
}
```
```python id="d4e5f6"
browser = playwright.chromium.launch(
    headless=True
)
```

Advantages
✔ Faster execution
✔ Ideal for CI/CD pipelines
✔ Less resource usage

 Disadvantages

✔ No visual feedback
✔ Harder to debug

---
---
## 18. What are Timeouts in Playwright?
Timeouts in Playwright define how long the framework waits for actions, assertions, or tests to complete before failing. They help control execution time, prevent indefinite waiting, and improve test reliability.
 
> In simple terms: **Timeout = Maximum waiting time before Playwright throws an error**

### 18.1  Why Timeouts are Important
Web apps are not always instant:
✔ Pages take time to load
✔ Elements appear after API calls
✔ Animations delay interactions
✔ Fail tests when something is wrong

Timeouts help:
✔ Prevent infinite waiting
✔ Handle slow applications
✔ Control test execution time
✔ Reduce flaky behavior

### 18.2 Types of Timeouts in Playwright
Playwright provides multiple timeouts such as test timeout, assertion timeout, action timeout, navigation timeout, fixture timeout, and global timeout. These control how long Playwright waits for different operations and help improve test reliability and performance.

- **Test Timeout**
Test timeout in Playwright defines the maximum time allowed for a test to complete. If the test exceeds this time, it fails automatically. It can be configured globally or per test to control execution time and ensure efficient test runs.

✔ Default Value
By default:  **30 seconds (30000 ms)** per test

How to Set Test Timeout:
✔ Global Timeout (Config) - Applies to all tests

```ts id="e8v2km"
export default defineConfig({
  timeout: 30000
});
```
```python id="m7q2pl"
# pytest.ini
[pytest]
timeout = 30000
```
OR
```python id="n4v7wp"
browser = playwright.chromium.launch(
    timeout=30000
)
```



 ✔ Per Test Timeout - This test can run up to 60 seconds
```ts id="g1p7zx"
test('Slow Test', async ({ page }) => {
  await page.goto('https://example.com');
}, 60000);
```
```python id="m7q2pl"
import pytest
@pytest.mark.timeout(60)
def test_slow_test(page):
    page.goto("https://example.com")
```
✔ Inside Test (Dynamic)

```ts id="q4r8yc"
test('Dynamic Timeout', async ({ page }, testInfo) => {
  testInfo.setTimeout(60000);
});
```
```python id="n4v7wp"
def test_dynamic_timeout(page):

    page.set_default_timeout(60000)
```



- **Expect (Assertion) Timeout**
Expect timeout in Playwright defines how long the framework waits for an assertion condition to be satisfied before failing. Playwright automatically retries assertions within this timeout, improving reliability and reducing flaky tests.

How to Set Expect Timeout
✔ Global Config -Applies to all assertions
```ts id="ex2b34"
export default defineConfig({
  expect: {
    timeout: 5000
  }
});
```
```python id="m7q2pl"
# pytest.ini

[pytest]
timeout = 5000
```
```python id="n4v7wp"
page.set_default_timeout(5000)
```

 ✔ Per Assertion -Waits up to 10 seconds

```ts id="ex3c45"
await expect(page.locator('#status')).toHaveText('Success', {
  timeout: 10000
});
```

```python id="k5t1zx"
from playwright.sync_api import expect

expect(page.locator("#status")).to_have_text(
    "Success",
    timeout=10000
)
```





- **Action Timeout **
Action timeout in Playwright defines the maximum time Playwright waits for an action like click or fill to complete. It ensures that elements are ready for interaction and prevents tests from failing prematurely or waiting indefinitely.
How to Set Action Timeout:
 
✔ Global Configuration -All actions will wait up to **10 seconds**

```ts
export default defineConfig({
  use: {
    actionTimeout: 10000
  }
});
```
```python id="m7q2pl"
page.set_default_timeout(10000)
# OR
context.set_default_timeout(10000)
```

✔ Per Action -This click waits max **5 seconds**

```ts
await page.locator('#login').click({
  timeout: 5000
});
```
```python id="k5t1zx"
page.locator("#login").click(
    timeout=5000
)
```





- ** Navigation Timeout**
Navigation timeout in Playwright defines how long the framework waits for a page navigation or load to complete before failing. It can be configured globally or per action and helps manage slow-loading pages effectively.
It is used in actions like:

 `page.goto()`
`page.click()` (when it triggers navigation)
`page.reload()`
`page.goBack()` / `goForward()`

Example : Waits up to **15 seconds** for page load

```ts 
await page.goto('https://example.com', {
  timeout: 15000
});
```
```python id="m7q2pl"
page.goto("https://example.com",timeout=15000)
```


✔ Set Navigation Timeout in Config -Applies to all navigation actions

```ts id="g7m2zx"
export default defineConfig({
  use: {
    navigationTimeout: 15000
  }
});
```
```python id="m7q2pl"
page.set_default_navigation_timeout(15000)
OR
context.set_default_navigation_timeout(15000)
```




✔ Load States (Important 🔥)
Navigation waits for a specific state:

```ts 
await page.goto('https://example.com', {
  waitUntil: 'load'
});
```
```python id="m7q2pl"
page.goto("https://example.com", wait_until="load")
```


Options:

| Option             | Meaning             |
| ------------------ | ------------------- |
| `load`             | Full page loaded    |
| `domcontentloaded` | HTML loaded         |
| `networkidle`      | No network activity |



- **Global Timeout (Config Level)**
Sets default timeout for all tests

```ts id="vpl1mj"
export default defineConfig({
  timeout: 30000,
});
```
```python id="m7q2pl"
# pytest.ini

[pytest]
timeout = 5000
```

- ** Hook Timeout**
Hook timeout in Playwright defines how long the framework waits for lifecycle hooks like beforeEach or beforeAll to complete. By default, it inherits the test timeout, and it can be customized using test.setTimeout().
 Where It Applies
Hooks like:

 `test.beforeAll()`
 `test.beforeEach()`
 `test.afterEach()`
 `test.afterAll()`
 
How to Set Hook Timeout

✔ Using `test.setTimeout()` (Inside Hook)

```ts 
test.beforeEach(async ({ page }) => {
  await page.goto('https://example.com');
}, { timeout: 20000 });

test.beforeEach(async ({ page }) => {
  test.setTimeout(60000); // 60 seconds
  await page.goto('https://example.com');
});
```
✔ Using Test-Level Timeout
 Hooks inherit the test timeout:

```ts
export default defineConfig({
  timeout: 30000
});
```


✔ Default Behavior
Hook timeout = **same as test timeout**

- **Fixture Timeout**
Fixture timeout in Playwright defines how long the framework waits for fixture setup and teardown before failing. It usually inherits the test timeout and can be customized when dealing with long-running setup processes.
Where It Applies
Fixtures like:
 `page`
 `context`
 `Custom fixtures`

✔ Default Behavior
 Fixture timeout = **same as test timeout**
 Usually **30 seconds**

 How to Set Fixture Timeout:

✔ Inside Custom Fixture

```ts 
import { test as base } from '@playwright/test';

const test = base.extend({
  myFixture: async ({}, use) => {
    // increase timeout
    test.setTimeout(60000);

    // setup
    await use('data');

    // teardown
  },
});
```
✔ Using Test Timeout (Inherited)

```ts id="f3m7zr"
export default defineConfig({
  timeout: 60000
});
```
Applies to:
```
Test
Hooks
Fixtures
```


### 18.3 How Timeouts Work Internally

* Playwright keeps checking condition
* If condition is met → proceeds
* If not → retries until timeout
* After timeout → throws error

### 18.4 Common Default Values
By default, Playwright sets a test timeout of 30 seconds, an expect timeout of 5 seconds, and an action timeout of 0 (inheriting from the test).

| Timeout Type   | Default Value |
| -------------- | ------------- |
| Test timeout   | 30 seconds    |
| Expect timeout | 5 seconds     |
| Action timeout | 0 (inherits)  |

---
---
## 19 How to navigate forward and backward in Playwright?
In Playwright, we can navigate backward using page.goBack() and forward using page.goForward(). These methods simulate browser navigation and support options like wait conditions and timeouts.

- **Navigate Back** :Moves to the previous page in browser history

```ts
await page.goBack();
```
Example

```ts
import { test, expect } from '@playwright/test';

test('navigate back example', async ({ page }) => {
  await page.goto('https://example.com');
  await page.goto('https://example.com/about');

  await page.goBack();

  await expect(page).toHaveURL('https://example.com/');
});
```
```python id="m7q2pl"
from playwright.sync_api import expect
page.go_back()
```
Example

```python id="n4v7wp"
from playwright.sync_api import expect

def test_navigate_back_example(page):

    page.goto("https://example.com")

    page.goto("https://example.com/about")

    page.go_back()

    expect(page).to_have_url(
        "https://example.com/"
    )
```



- **Navigate Forward** : Moves to the **next page** (after going back)

Syntax

```ts
await page.goForward();
```
 Example

```ts
import { test, expect } from '@playwright/test';

test('navigate forward example', async ({ page }) => {
  await page.goto('https://example.com');
  await page.goto('https://example.com/about');

  await page.goBack();
  await page.goForward();

  await expect(page).toHaveURL(/about/);
});
```

```python id="m7q2pl"
from playwright.sync_api import expect
page.go_forward()
```
Example
```python id="n4v7wp"
from playwright.sync_api import expect
import re


def test_navigate_forward_example(page):

    page.goto("https://example.com")

    page.goto("https://example.com/about")

    page.go_back()

    page.go_forward()

    expect(page).to_have_url(
        re.compile("about")
    )
```



- **Navigation with Options**

You can control waiting behavior:
```ts
await page.goBack({ waitUntil: 'load' });
await page.goForward({ waitUntil: 'domcontentloaded' });
```
`waitUntil` options:

 `'load'` → full page load
 `'domcontentloaded'` → HTML loaded
 `'networkidle'` → network idle
* **Navigation with Options**

```python id="m7q2pl"
page.go_back(wait_until="load")
page.go_forward(wait_until="domcontentloaded")
```

`wait_until` options:

```text id="n4v7wp"
"load" → full page load
"domcontentloaded" → HTML loaded
"networkidle" → network idle
```



### 19.1 Real-World Example

```ts
test('user navigation flow', async ({ page }) => {
  await page.goto('https://example.com');

  await page.click('text=More information');
  await expect(page).toHaveURL(/more/);

  await page.goBack();
  await expect(page).toHaveURL('https://example.com/');

  await page.goForward();
  await expect(page).toHaveURL(/more/);
});
```
```python id="m7q2pl"
from playwright.sync_api import expect
import re

def test_user_navigation_flow(page):

    page.goto("https://example.com")

    page.locator("text=More information").click()

    expect(page).to_have_url(
        re.compile("more")
    )

    page.go_back()

    expect(page).to_have_url(
        "https://example.com/"
    )

    page.go_forward()

    expect(page).to_have_url(
        re.compile("more")
    )
```



### 19.2 Important Notes

* Works only if there is **history available**
* Automatically waits for navigation
* Returns `null` if navigation is not possible

---
---
## 20 Performing Actions in Playwright
In Playwright, actions are performed using the page object and locators. Common actions include click, fill, type, select, hover, and drag-and-drop. Playwright automatically waits for elements to be ready before performing actions, making tests reliable.

- ** Basic Flow **

```ts 
await page.goto('https://example.com');     // open page
await page.getByRole('button', { name: 'Login' }).click(); // act
await expect(page).toHaveURL(/dashboard/);  // verify
```
```python id="m7q2pl"
from playwright.sync_api import expect
import re


page.goto("https://example.com")  # open page

page.get_by_role("button", name="Login").click()  # act

expect(page).to_have_url(
    re.compile("dashboard")
)  # verify
```


 **Locate → Act → Verify**


- **Core Interaction Methods**
 ✔ Click

```ts 
await page.getByRole('button', { name: 'Login' }).click();
```
✔ Type / Fill

```ts 
await page.getByLabel('Username').fill('admin');
```
✔ Clear + Type (via fill)

```ts 
await page.locator('#search').fill('');
```
✔ Press Keys

```ts 
await page.locator('#search').press('Enter');
```
- ** Form Actions**
✔ Select Dropdown

```ts 
await page.selectOption('#country', 'India');
```
✔ Check / Uncheck

```ts 
await page.locator('#agree').check();
await page.locator('#agree').uncheck();
```


- **Mouse & Keyboard Actions**
✔ Hover

```ts id="act_hover"
await page.locator('.menu').hover();
```

✔ Double Click

```ts id="act_double"
await page.locator('#item').dblclick();
```

✔ Right Click

```ts id="act_right"
await page.locator('#item').click({ button: 'right' });
```

- ** File Upload**

```ts id="act_upload"
await page.setInputFiles('#upload', 'file.pdf');
```

- **Drag and Drop**

```ts id="act_drag"
await page.dragAndDrop('#source', '#target');
```

- ** Handling Alerts**

```ts id="act_alert"
page.on('dialog', async dialog => {
  await dialog.accept();
});
```

- ** Taking Screenshot**

```ts id="act_ss"
await page.screenshot({ path: 'page.png' });
```

- **Working with Locators (Best Practice)**

```ts id="act_locator"
const loginBtn = page.getByRole('button', { name: 'Login' });
await loginBtn.click();
```


### 20.1 Example End-to-End Test

```ts id="act_full"
import { test, expect } from '@playwright/test';

test('login flow', async ({ page }) => {
  await page.goto('https://example.com');

  await page.getByLabel('Username').fill('admin');
  await page.getByLabel('Password').fill('password');

  await page.getByRole('button', { name: 'Login' }).click();

  await expect(page).toHaveURL(/dashboard/);
});
```
---
---

## 21 How to wait for a specific element in Playwright?
In Playwright, waiting for elements is handled automatically using locators and assertions. But when you need explicit control, Playwright provides several reliable ways to wait for a specific element.

- **Recommended Way: Use Assertions (Best Practice)**

```ts
await expect(page.locator('#login')).toBeVisible();
```
```python id="m7q2pl"
from playwright.sync_api import expect

expect(page.locator("#login")).to_be_visible()
```


What happens:
✔ Playwright keeps checking
✔ Waits until element becomes visible
✔ Fails after timeout if not found


- **Using `locator.waitFor()`**
```ts
await page.locator('#login').waitFor({ state: 'visible' });
```
```python id="m7q2pl"
page.locator("#login").wait_for(state="visible")
```
Possible states:
 `'attached'` → present in DOM
 `'detached'` → removed from DOM
 `'visible'` → visible on screen
 `'hidden'` → not visible

- **Using `page.waitForSelector()`**

```ts
await page.waitForSelector('#login', { state: 'visible' });
```
```python id="m7q2pl"
page.wait_for_selector("#login", state="visible")
```

Older style but still supported
Similar to `locator.waitFor()`


- ** Waiting for Element Before Action (Usually Not Needed)**

```ts
await page.click('#login');
```
 Playwright automatically:
✔ Waits for element
✔ Ensures it is clickable
✔ No manual wait required in most cases


- **Waiting for Element to Disappear**

```ts
await expect(page.locator('#loader')).toBeHidden();
```

OR

```ts
await page.locator('#loader').waitFor({ state: 'hidden' });
```

### 21.1 Example Test

```ts
import { test, expect } from '@playwright/test';

test('wait for element example', async ({ page }) => {
  await page.goto('https://example.com');

  // Wait for login button
  await expect(page.locator('#login')).toBeVisible();

  await page.click('#login');

  // Wait for success message
  await expect(page.locator('.success')).toHaveText('Welcome');
});
```


### 21.2 Timeout Control

```ts
await expect(page.locator('#login')).toBeVisible({ timeout: 10000 });
```
Waits up to 10 seconds

---
---

## 22. What is browser context?
A browser context in Playwright is an isolated browser session, similar to an incognito window, that has its own cookies, storage, and session data. It allows tests to run independently and supports multi-user and parallel testing.

> In simple terms: **Browser Context = Incognito Window / New User Session**


- ** Why Browser Context is Important**
When testing applications, you often need:

✔ Multiple users
✔ Clean sessions
✔ No shared cookies or data

> Browser contexts solve this by providing **isolation**.


- **How It Fits in Playwright Architecture**
Hierarchy:

```text
Browser → Context → Page
```

✔ **Browser** → Entire browser instance
✔ **Context** → Isolated session
✔ **Page** → Tab inside that session


- **Key Features of Browser Context**

✔ Isolated cookies
✔ Separate local/session storage
✔ Independent cache
✔ No data sharing between contexts

> Each context behaves like a **new user**


### 22.1 Creating a Browser Context

```ts 
const browser = await chromium.launch();

const context = await browser.newContext();
const page = await context.newPage();
```
```python id="m7q2pl"
browser = p.chromium.launch()

context = browser.new_context()

page = context.new_page()
```



- **Example: Multiple Users**

```ts id="4d8tv8"
const context1 = await browser.newContext();
const page1 = await context1.newPage();

const context2 = await browser.newContext();
const page2 = await context2.newPage();
```
```python id="m7q2pl"
context1 = browser.new_context()
page1 = context1.new_page()

context2 = browser.new_context()
page2 = context2.new_page()
```




### 22.2 Real-World Use Case
Example: Chat Application
✔ User A sends message
✔ User B receives message
Use two contexts to simulate both users


### 22.3 Context in Playwright Tests

You usually don’t create it manually:

```ts id="e3avxc"
test('example', async ({ context, page }) => {
  await page.goto('https://example.com');
});
```
```python id="m7q2pl"
def test_example(context, page):

    page.goto("https://example.com")
```



Playwright provides `context` as a **fixture**


### 22.4 Advanced: Context Options

```ts 
const context = await browser.newContext({
  viewport: { width: 1280, height: 720 },
  locale: 'en-US',
  geolocation: { latitude: 17.4, longitude: 78.5 },
});
```
```python id="m7q2pl"
context = browser.new_context(
    viewport={"width": 1280, "height": 720},
    locale="en-US",
    geolocation={"latitude": 17.4, "longitude": 78.5}
)
```


 Customize:
✔ Screen size
✔ Location
✔ Language

---
---
## 23 How to open multiple windows in Playwright?

In Playwright, multiple windows or tabs are handled using multiple Page objects within the same browser context. New windows can be captured using context.waitForEvent('page'), and each window is controlled independently.
 
> In simple terms: **Each new tab/window = a new `Page` object**

- **Open a New Tab (Most Common Way)**

```ts
const newPage = await context.newPage();
await newPage.goto('https://example.com');
```
```python id="m7q2pl"
new_page = context.new_page()

new_page.goto("https://example.com")
```



This creates a **new tab** in the same browser session.

Example: Multiple Tabs in One Test

```ts
import { test, expect } from '@playwright/test';

test('multiple tabs example', async ({ context }) => {
  const page1 = await context.newPage();
  await page1.goto('https://example.com');

  const page2 = await context.newPage();
  await page2.goto('https://example.com/about');

  await expect(page1).toHaveTitle(/Example/);
  await expect(page2).toHaveURL(/about/);
});
```
```python id="m7q2pl"
from playwright.sync_api import expect
import re


def test_multiple_tabs_example(context):

    page1 = context.new_page()

    page1.goto("https://example.com")

    page2 = context.new_page()

    page2.goto("https://example.com/about")

    expect(page1).to_have_title(
        re.compile("Example")
    )

    expect(page2).to_have_url(
        re.compile("about")
    )
```



✔ Here:

 `page1` → first tab
 `page2` → second tab


- **Handling Popup Windows (New Window from Click)**

Sometimes clicking a link opens a new window/tab.

 Use `waitForEvent('page')`

```ts
import { test, expect } from '@playwright/test';

test('handle new window popup', async ({ page }) => {
  await page.goto('https://example.com');

  const [newPage] = await Promise.all([
    page.context().waitForEvent('page'), // wait for new tab
    page.click('text=Open New Window'),  // action that opens it
  ]);

  await newPage.waitForLoadState();

  await expect(newPage).toHaveTitle(/Example/);
});
```
use `expect_page()`
```python id="m7q2pl"
from playwright.sync_api import expect
import re


def test_handle_new_window_popup(page):

    page.goto("https://example.com")

    with page.context.expect_page() as new_page_info:

        page.locator("text=Open New Window").click()

    new_page = new_page_info.value

    new_page.wait_for_load_state()

    expect(new_page).to_have_title(
        re.compile("Example")
    )
```




- **Switching Between Tabs**

```ts
await page1.bringToFront();
await page2.bringToFront();
```
```python id="m7q2pl"
page1.bring_to_front()

page2.bring_to_front()
```


 Helps when interacting with multiple tabs

- **Get All Open Pages**

```ts
const pages = context.pages();
console.log(pages.length);
```
```python id="m7q2pl"
pages = context.pages

print(len(pages))
```
Returns all open tabs

- **Close a Specific Tab**

```ts
await page2.close();
```
```python id="m7q2pl"
page2.close()
```

- **Multiple Windows with Separate Contexts (Advanced)**

```ts
const context1 = await browser.newContext();
const page1 = await context1.newPage();

const context2 = await browser.newContext();
const page2 = await context2.newPage();
```
```python id="m7q2pl"
context1 = browser.new_context()
page1 = context1.new_page()
context2 = browser.new_context()
page2 = context2.new_page()
```
Use when:
✔ Simulating multiple users
✔ Need full session isolation


### 23.2 Important Notes
Playwright treats windows and tabs the same way (Page)
Always wait for new page events when handling popups
Each page is independent

---
---
## 24 How to Handle iFrames in Playwright? 
In Playwright, iFrames can be handled using frameLocator() or page.frame(). The recommended approach is frameLocator(), which allows direct interaction with elements inside the frame with built-in auto-waiting.
In simple terms: iFrame = page inside a page → needs special access


- **Recommended Way: `frameLocator()\frame_locator()`**

```ts
await page.frameLocator('#frameId').locator('#login').click();
```
```python id="m7q2pl"
page.frame_locator("#frameId").locator("#login").click()
```


Why this is best:

✔ Auto-waiting
✔ Cleaner syntax
✔ Works well with nested elements

- **Example Test Using `frameLocator`**

```ts
import { test, expect } from '@playwright/test';

test('handle iframe using frameLocator', async ({ page }) => {
  await page.goto('https://example.com');

  const frame = page.frameLocator('#iframe');

  await frame.locator('#username').fill('admin');
  await frame.locator('#password').fill('password');

  await frame.locator('#login').click();
});
```
```python id="m7q2pl"
from playwright.sync_api import expect


def test_handle_iframe_using_frame_locator(page):

    page.goto("https://example.com")

    frame = page.frame_locator("#iframe")

    frame.locator("#username").fill("admin")

    frame.locator("#password").fill("password")

    frame.locator("#login").click()
```



- ** Using `frame()` Method**

```ts
const frame = page.frame({ name: 'frameName' });
await frame?.fill('#username', 'admin');
```
```python id="m7q2pl"
frame = page.frame(name="frameName")
frame.fill("#username", "admin")
```
Finds frame by:
✔ name
✔ URL
✔ other properties

- **Using `contentFrame()`**
Used when you first locate iframe element
```ts
const iframeElement = await page.locator('#iframe');
const frame = await iframeElement.contentFrame();
await frame.fill('#username', 'admin');
```
```python id="m7q2pl"
iframe_element = page.locator("#iframe")
frame = iframe_element.content_frame()
frame.fill("#username", "admin")
```


 
- ** Handling Nested iFrames**

```ts
const frame = page.frameLocator('#outer-frame')
                  .frameLocator('#inner-frame');

await frame.locator('#submit').click();
```
```python id="m7q2pl"
frame = page.frame_locator("#outer-frame").frame_locator("#inner-frame")
frame.locator("#submit").click()
```



- ** Waiting for iFrame**

Usually not required (auto-wait), but if needed:

```ts
await page.frameLocator('#iframe').locator('#login').waitFor();
```
```python id="m7q2pl"
page.frame_locator("#iframe").locator("#login").wait_for()
```



### 24.1 Example Real Scenario

```ts
test('iframe login', async ({ page }) => {
  await page.goto('https://example.com');

  const loginFrame = page.frameLocator('#login-frame');

  await loginFrame.getByLabel('Username').fill('admin');
  await loginFrame.getByLabel('Password').fill('password');

  await loginFrame.getByRole('button', { name: 'Login' }).click();
});
```


### 24.2 Important Points

✔ You cannot use `page.locator()` directly inside iframe
✔ Always use:
 `frameLocator()` (recommended)
  or `frame()`

---
---
## 25 How to Evaluate JavaScript in Playwright?

In Playwright, JavaScript can be executed inside the browser using methods like page.evaluate() and locator.evaluate(). These allow interaction with the DOM and retrieval of data directly from the page context.
Playwright lets you execute JavaScript in the browser using:

 `page.evaluate()`
 `locator.evaluate()`
 `evaluateHandle()` (advanced)

 > In Simple Words : You can run JavaScript inside the web page just like in browser DevTools

- **`page.evaluate()`** :Runs JS in the page context

```ts
const title = await page.evaluate(() => {
  return document.title;
});
```
 Gets page title

With Arguments

```ts
const result = await page.evaluate((num) => {
  return num * 2;
}, 5);

console.log(result); // 10
```


- **Access DOM Elements**

```ts
const text = await page.evaluate(() => {
  return document.querySelector('h1')?.innerText;
});
```


- **Using `locator.evaluate()`**
 Runs JS on a specific element

```ts
const text = await page.locator('h1').evaluate(el => el.textContent);
```

✔ Cleaner and safer


- **Modify Page Data**

```ts
await page.evaluate(() => {
  document.body.style.backgroundColor = 'red';
});
```
 Changes page UI


- **Return Complex Data**

```ts
const links = await page.evaluate(() => {
  return Array.from(document.querySelectorAll('a')).map(a => a.href);
});
```


- ** `evaluateHandle()` (Advanced)**
 Returns JS object handle

```ts
const handle = await page.evaluateHandle(() => document.body);
```

✔ Used for advanced scenarios


### 25.1 Important Points 

✔ Runs inside browser (not Node.js)
✔ Cannot directly access test variables
✔ Must pass arguments explicitly

### 25.2 Example (Real Scenario)

```ts
test('Evaluate Example', async ({ page }) => {
  await page.goto('https://example.com');

  const title = await page.evaluate(() => document.title);

  console.log(title);
});
```

---
---
## 26 What is CodeGen in Playwright?
CodeGen in Playwright is a tool that records user interactions in the browser and automatically generates Playwright test code. It is useful for quickly creating test scripts and identifying locators, but the generated code should be refined for production use.

> In simple terms: **CodeGen = Record user actions → Generate Playwright test script**

- ** What CodeGen Does?**
✔ Opens a browser
✔ Records clicks, typing, navigation
✔ Converts those actions into Playwright code

> Helps you quickly create test scripts without writing everything manually


- **How to Run CodeGen**

```bash
npx playwright codegen https://example.com
```
 This will:

✔ Open browser
✔ Start recording
✔ Show generated code in real-time


- **Features of CodeGen**
✔ Auto Locator Generation * Uses `getByRole`, `getByText`, etc.
✔ Live Code Generation -Updates code as you perform actions
✔ Multi-language Support
 TypeScript
 JavaScript
 Python
 Java

- **Useful Options**

✔ Save Script
```bash
npx playwright codegen --output=test.spec.ts
```
✔ Use Specific Browser

```bash
npx playwright codegen --browser=chromium
```
✔ Use Device Emulation

```bash
npx playwright codegen --device="iPhone 13"
```

### 26.1 When to Use CodeGen

✔ Learning Playwright
✔ Generating initial test scripts
✔ Finding correct locators
✔ Quick prototyping

---
---

## 27 How to Parameterize Tests in Playwright?
Parameterization in Playwright allows running the same test with multiple sets of data using loops, arrays, JSON files, or fixtures. It helps improve test coverage and reduces code duplication.

> In simple terms: **Write test once → run multiple times with different data**

Why Parameterization is Important

✔ Avoid duplicate tests
✔ Improve maintainability
✔ Easily test multiple scenarios (valid/invalid inputs, users, etc.)


- ** Method 1: Using Arrays (Most Common)**
 Example

```ts id="param_array"
import { test, expect } from '@playwright/test';

const users = [
  { username: 'user1', password: 'pass1' },
  { username: 'user2', password: 'pass2' },
];

users.forEach((user) => {
  test(`login test for ${user.username}`, async ({ page }) => {
    await page.goto('https://example.com');

    await page.fill('#username', user.username);
    await page.fill('#password', user.password);

    await page.click('#login');

    await expect(page).toHaveURL(/dashboard/);
  });
});
```
 Runs test multiple times with different users



- ** Method 2: Using `test.describe()` with Data**

```ts 
const testData = ['admin', 'guest'];

test.describe('role-based tests', () => {
  testData.forEach((role) => {
    test(`test for role ${role}`, async ({ page }) => {
      await page.goto(`https://example.com/${role}`);

      await expect(page).toHaveURL(new RegExp(role));
    });
  });
});
```

- ** Method 3: Using Fixtures (Advanced)**

```ts id="param_fixture"
import { test as base } from '@playwright/test';

type TestData = {
  user: string;
};

const test = base.extend<TestData>({
  user: ['admin', { option: true }],
});

test('fixture parameterized test', async ({ page, user }) => {
  await page.goto(`https://example.com/${user}`);
});
```
 Useful for scalable frameworks

- ** Method 4: Using External Data (JSON)**
 ✔ data.json

```json
[
  { "username": "user1", "password": "pass1" },
  { "username": "user2", "password": "pass2" }
]
```

 ✔ Test File

```ts id="param_json"
import { test, expect } from '@playwright/test';
import users from './data.json';

users.forEach((user) => {
  test(`login ${user.username}`, async ({ page }) => {
    await page.goto('https://example.com');

    await page.fill('#username', user.username);
    await page.fill('#password', user.password);

    await page.click('#login');

    await expect(page).toHaveURL(/dashboard/);
  });
});
```


- ** Method 5: Using Environment Variables**

```ts id="param_env"
const baseURL = process.env.BASE_URL || 'https://dev.example.com';

test('env test', async ({ page }) => {
  await page.goto(baseURL);
});
```


### 27.1 Best Practices
✔ Keep test data separate from test logic
✔ Use meaningful test names
✔ Avoid hardcoding values
✔ Use JSON/fixtures for large datasets

---
---

## 28 How to Handle File Upload in Playwright?
In Playwright, file upload is handled using the setInputFiles() method, which directly sets the file to an input element. It supports single and multiple file uploads and works without interacting with the OS file dialog.

- ** Upload Using `setInputFiles()` (Most Common)**
```ts
await page.setInputFiles(selector, filePath);
```

```ts
import { test, expect } from '@playwright/test';

test('file upload example', async ({ page }) => {
  await page.goto('https://example.com/upload');

  await page.locator('#fileUpload').setInputFiles('tests/sample.pdf');

  await expect(page.locator('#status')).toHaveText('Upload successful');
});
```

> Works when `<input type="file">` is available


- ** Upload Multiple Files**

```ts
import { test, expect } from '@playwright/test';

test('file upload example', async ({ page }) => {
  await page.goto('https://example.com/upload');

  await page.locator('#fileUpload').setInputFiles(['tests/sample.pdf', 'tests/file2.pdf']);

  await expect(page.locator('#status')).toHaveText('Upload successful');
});
```

- **Remove Uploaded Files** :Clears file input

```ts
await page.setInputFiles('#fileUpload', []);
```


-  **Upload via File Chooser (Advanced)**

When clicking a button opens file dialog:

```ts
test('upload using file chooser', async ({ page }) => {
  await page.goto('https://example.com');

  const [fileChooser] = await Promise.all([
    page.waitForEvent('filechooser'),
    page.click('#uploadBtn'), // button that opens file dialog
  ]);

  await fileChooser.setFiles('tests/sample.pdf');
});
```


- ** Important Points**
✔ File must exist in your project path
✔ Supports: PDF, Images, Any file type
✔ No OS-level interaction needed


---
---
## 29 How to Handle File Download in Playwright?
In Playwright, file downloads are handled using the page.waitForEvent('download') method. We capture the download event, then use methods like saveAs() or suggestedFilename() to store or verify the downloaded file.


### 29.1 Basic Approach (Recommended)

- ** Use `waitForEvent('download')`**

```ts 
import { test, expect } from '@playwright/test';

test('file download example', async ({ page }) => {
  await page.goto('https://example.com');

  const [download] = await Promise.all([
    page.waitForEvent('download'), // wait for download
    page.click('#downloadBtn'),    // action that triggers download
  ]);

  const path = await download.path();
  console.log(path);
});
```



- ** Save Downloaded File**

```ts 
await download.saveAs('downloads/report.pdf');
```

Saves file to a specific location

- ** Get File Name**

```ts 
const fileName = download.suggestedFilename();
console.log(fileName);
```

### 29.2 Example with Validation

```ts id="dl_validate"
test('download and verify', async ({ page }) => {
  await page.goto('https://example.com');

  const [download] = await Promise.all([
    page.waitForEvent('download'),
    page.click('text=Download Report'),
  ]);

  const fileName = download.suggestedFilename();

  expect(fileName).toContain('report');
});
```


### 29.3 Set Download Directory (Config)

```ts 
export default defineConfig({
  use: {
    acceptDownloads: true,
  },
});
```
Ensures downloads are allowed

###  29.4 Custom Download Path

```ts i
await download.saveAs(`downloads/${download.suggestedFilename()}`);
```


###  29.5 Handling Multiple Downloads

```ts id="dl_multi"
const download1 = page.waitForEvent('download');
await page.click('#download1');

const download2 = page.waitForEvent('download');
await page.click('#download2');
```

### 29.6 Important Notes

* Always use `Promise.all()` to avoid missing the event
* Download starts immediately after click
* File is temporary unless saved

---
---

## 30. How to perform drag and drop in Playwright?
In Playwright, drag and drop can be performed using dragAndDrop() or locator.dragTo(), which are the recommended methods. For complex scenarios, mouse events like mouse.down() and mouse.up() can be used.

- **Using `dragAndDrop()` (Recommended)**


```ts
await page.dragAndDrop(source, target);
```
 Example

```ts
import { test, expect } from '@playwright/test';

test('drag and drop example', async ({ page }) => {
  await page.goto('https://example.com/drag-drop');

  await page.dragAndDrop('#source', '#target');

  await expect(page.locator('#target')).toContainText('Dropped');
});
```

✔ Simple and clean
✔ Automatically handles waiting

- **Using Locator (Better Practice)**

```ts
await page.locator('#source').dragTo(page.locator('#target'));
```
 Preferred because:
✔ Uses locators
✔ More stable and readable

- **Using Mouse Actions (Advanced)**

When `dragAndDrop()` doesn’t work (custom UI):

```ts
const source = page.locator('#source');
const target = page.locator('#target');

await source.hover();
await page.mouse.down();

await target.hover();
await page.mouse.up();
```
 >Gives full control over drag behavior


- **Drag with Coordinates**

```ts
await page.mouse.move(100, 200);
await page.mouse.down();
await page.mouse.move(300, 400);
await page.mouse.up();
```
Useful for canvas or custom drag UIs



- **Example (Real Test)**

```ts
test('drag using locator', async ({ page }) => {
  await page.goto('https://example.com');

  const source = page.locator('#item1');
  const target = page.locator('#item2');

  await source.dragTo(target);

  await expect(target).toContainText('item1');
});
```

- ** Important Notes**

* Prefer `dragAndDrop()` or `dragTo()` first
* Use mouse actions only if needed
* Ensure elements are visible before dragging

---
---
## 31. How to handle browser popups or dialogs?
In Playwright, browser dialogs like alerts, confirms, and prompts are handled using the page.on('dialog') event. We can accept or dismiss dialogs using dialog.accept() or dialog.dismiss() and optionally pass input for prompt dialogs.
These include:
 `alert()`
 `confirm()`
 `prompt()`


 ### 31.1 Types of Browser Dialogs

| Type    | Description               |
| ------- | ------------------------- |
| alert   | Shows message + OK button |
| confirm | OK / Cancel options       |
| prompt  | Input field + OK / Cancel |


- **Basic Handling (Accept Dialog)**

```ts 
page.on('dialog', async dialog => {
  console.log(dialog.message());
  await dialog.accept();
});
```

 Accepts the popup automatically

- ** Dismiss Dialog (Cancel)**

```ts 
page.on('dialog', async dialog => {
  await dialog.dismiss();
});
```

- **Handle Prompt with Input**
Sends input value to prompt

```ts 
page.on('dialog', async dialog => {
  await dialog.accept('John Doe');
});
```
- **Example Test**

```ts id="dlg_example"
import { test, expect } from '@playwright/test';

test('handle alert popup', async ({ page }) => {
  await page.goto('https://example.com');

  page.on('dialog', async dialog => {
    console.log(dialog.type());    // alert / confirm / prompt
    console.log(dialog.message()); // popup message

    await dialog.accept();
  });

  await page.click('#showAlert');
});
```

- **Using `once()` (Better for Single Dialog)**

```ts id="dlg_once"
page.once('dialog', async dialog => {
  await dialog.accept();
});
```

 Handles only one dialog (cleaner approach)


### 31.2 Important Notes

✔ If you don’t handle dialog → test will **hang/fail**
✔ Must register handler **before triggering action**

---
---
## 33.What is testInfo Object?
The testInfo object provides information about the currently running test, such as its name, status, retry count, and output paths. It also allows attaching files and dynamically controlling test behavior.

> In simple terms:`testInfo` = details about the test + control over test execution/reporting**

 - **Why `testInfo` is Important**

✔ It helps you access test name, status, retries
✔ Attach logs, screenshots, files
✔ Dynamically control behavior
✔ Debug failures

- ** How to Use `testInfo`**
```ts 
import { test, expect } from '@playwright/test';

test('example test', async ({ page }, testInfo) => {
  console.log(testInfo.title);
});
```

> `testInfo` is passed as a **second argument** to the test function

- **Common Properties of `testInfo`**

| Property         | Description               |
| ---------------- | ------------------------- |
| `title`          | Test name                 |
| `status`         | pass / fail / skipped     |
| `expectedStatus` | Expected result           |
| `retry`          | Current retry count       |
| `project.name`   | Browser/project name      |
| `file`           | Test file path            |
| `outputDir`      | Folder for test artifacts |

- **Example**

```ts id="ti_props"
test('info example', async ({ page }, testInfo) => {
  console.log(testInfo.title);
  console.log(testInfo.file);
  console.log(testInfo.retry);
});
```

- **Attach Files (Very Important)**

```ts 
await testInfo.attach('screenshot', {
  path: 'screenshot.png',
  contentType: 'image/png',
});
```

> Adds attachments to report

 - **Capture Screenshot on Failure**

```ts
test.afterEach(async ({ page }, testInfo) => {
  if (testInfo.status !== testInfo.expectedStatus) {
    const screenshot = await page.screenshot();

    await testInfo.attach('failure-screenshot', {
      body: screenshot,
      contentType: 'image/png',
    });
  }
});
```

- **Output Directory Usage**

```ts id="ti_output"
const filePath = testInfo.outputPath('log.txt');
```
> Stores files safely per test

- **Skip or Modify Test Dynamically**

```ts 
test('conditional test', async ({}, testInfo) => {
  if (testInfo.project.name === 'firefox') {
    test.skip();
  }
});
```

- **Example (Real Usage)**

```ts id="ti_real"
test('login test', async ({ page }, testInfo) => {
  await page.goto('https://example.com');

  console.log(`Running: ${testInfo.title}`);

  await page.click('#login');
});
```


---
---
## 34.What is testError Object?
In Playwright, the test error object represents the details of a failure, including the error message and stack trace. It can be accessed using testInfo.error or through reporters to help debug failed tests.
> In simple terms: `testError` = details about why a test failed

- **Where You See `testError`**

Playwright does not pass `testError` directly as a parameter like `testInfo`, but it is available **inside `testInfo.errors`**.
```ts
testInfo.errors
```
This is an array of error objects (each one is a **testError**)

- **Structure of `testError`**
A typical `testError` contains:
`message` → error message
`stack` → stack trace
`value` → actual error object

- **Example:** Accessing `testError`

```ts
import { test } from '@playwright/test';

test.afterEach(async ({}, testInfo) => {
  if (testInfo.errors.length > 0) {
    const error = testInfo.errors[0];

    console.log('Error Message:', error.message);
    console.log('Stack Trace:', error.stack);
  }
});
```

- **Example Test with Failure**

```ts
import { test, expect } from '@playwright/test';

test('failure example', async ({ page }) => {
  await page.goto('https://example.com');

  // This will fail
  await expect(page).toHaveTitle('Wrong Title');
});
```
When this fails:

 `testError` is created internally
 Stored in `testInfo.errors`

- **Real Use Case: Debugging**

```ts
test.afterEach(async ({ page }, testInfo) => {
  if (testInfo.errors.length) {
    console.log('Test Failed:', testInfo.title);

    for (const err of testInfo.errors) {
      console.log(err.message);
    }
  }
});
```

- **Capture Screenshot on Error**

```ts
test.afterEach(async ({ page }, testInfo) => {
  if (testInfo.errors.length > 0) {
    const screenshot = await page.screenshot();

    await testInfo.attach('error-screenshot', {
      body: screenshot,
      contentType: 'image/png',
    });
  }
});
```

- **Difference: `testError` vs `testInfo`**
testError provides error details accessed via testInfo.errors for debugging failures, while testInfo is passed as a parameter to expose full test metadata and enable complete test control.

| Feature | `testError`        | `testInfo`          |
| ------- | ------------------ | ------------------- |
| Purpose | Error details      | Test metadata       |
| Access  | `testInfo.errors`  | Passed as parameter |
| Usage   | Debugging failures | Full test control   |

- **Important Notes**
✔ A test can have multiple errors
✔ Errors are stored in an **array**
✔ Useful in hooks like `afterEach`

---
---
35. What is global setup and tear down explain?
Global setup and teardown in Playwright are used to run initialization and cleanup code once before and after all tests. They help prepare the environment, reduce redundancy, and improve test execution efficiency.

> In simple terms:
* **Global Setup** → runs *before all tests start*
* **Global Teardown** → runs *after all tests finish*

- **Why Use Global Setup & Teardown?**

They are useful for tasks that should happen **only once**, such as:

✔ Logging in and saving session
✔ Seeding test data
✔ Starting/stopping servers
✔ Cleaning up databases

> Avoids repeating expensive setup in every test

- **Global Setup (Before All Tests)**
Example

```ts
// global-setup.ts
import { chromium } from '@playwright/test';

async function globalSetup() {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  await page.goto('https://example.com/login');
  await page.fill('#username', 'admin');
  await page.fill('#password', 'password');
  await page.click('#login');

  // Save login state
  await page.context().storageState({ path: 'storageState.json' });

  await browser.close();
}

export default globalSetup;
```

- **Global Teardown (After All Tests)**
Example

```ts
// global-teardown.ts
async function globalTeardown() {
  console.log('Cleaning up after tests...');
  // Example:
  // delete temp files
  // reset database
}

export default globalTeardown;
```

- **Configure in `playwright.config.ts`**

```ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  globalSetup: './global-setup.ts',
  globalTeardown: './global-teardown.ts',

  use: {
    storageState: 'storageState.json',
  },
});
```

---

- ** How It Works (Flow)**
✔ Global Setup runs once
✔ All tests execute
✔ Global Teardown runs once

- **Real-World Example**
✔ Login Once for All Tests
✔ Global setup logs in
✔ Saves session (`storageState`)
✔ All tests reuse session

> Faster and efficient

- **Key Differences from Hooks**

| Feature | Global Setup/Teardown | Hooks (`beforeEach`)   |
| ------- | --------------------- | ---------------------- |
| Runs    | Once for all tests    | Before/after each test |
| Scope   | Entire suite          | Per test or file       |
| Usage   | Expensive setup       | Test-specific setup    |

- ** Important Points**
✔ Runs **outside test context** (no `test` object)
✔ Should return a function (for teardown) or use separate file
✔ Good for performance optimization

---
---
## 36.How to capture Network logs in Playwright?
In Playwright, network logs can be captured using events like page.on('request') and page.on('response'). These allow tracking of API calls, request data, and responses, which helps in debugging and validation.

> In simple terms: Listen to network traffic → log or assert what happened

- **Capture All Requests**

```ts
page.on('request', request => {
  console.log('URL:', request.url());
  console.log('Method:', request.method());
});
```

> Fires for every outgoing request

- ** Capture All Responses**

```ts
page.on('response', response => {
  console.log('Status:', response.status());
  console.log('URL:', response.url());
});
```

> Fires when responses are received

- ** Capture Request + Response Together**

```ts
page.on('request', req => console.log('➡️', req.url()));
page.on('response', res => console.log('⬅️', res.url(), res.status()));
```

- **Example Test (Network Logging)**

```ts
import { test } from '@playwright/test';

test('capture network logs', async ({ page }) => {
  page.on('request', req => console.log('REQ:', req.url()));
  page.on('response', res => console.log('RES:', res.url(), res.status()));

  await page.goto('https://example.com');
});
```

- **Capture Specific API Call**

```ts
const response = await page.waitForResponse('**/api/users');
console.log(await response.json());
```

> Waits for a specific request pattern

- **Capture Request Payload **

```ts
page.on('request', request => {
  if (request.method() === 'POST') {
    console.log(request.postData());
  }
});
```

- **Capture Response Body**

```ts
page.on('response', async response => {
  if (response.url().includes('/api')) {
    const body = await response.text();
    console.log(body);
  }
});
```

- **Using `waitForRequest()`**

```ts
const request = await page.waitForRequest('**/login');
console.log(request.url());
```

- **Using Playwright Trace (Advanced Logging)**

```bash
npx playwright test --trace=on
```
Then open:

```bash
npx playwright show-trace trace.zip
```
Shows: Network calls, UI actions, Console logs

- **Real-World Example**

```ts
test('validate API response', async ({ page }) => {
  await page.goto('https://example.com');

  const response = await page.waitForResponse('**/api/login');

  const data = await response.json();

  console.log(data);
});
```

- **Important Notes**

✔ Register listeners **before navigation/action**
✔ Use filters to avoid too many logs
✔ Combine with assertions for validation

---
---
# 37. How to capture screenshots in Playwright?
In Playwright, screenshots can be captured using page.screenshot() for full page or viewport and locator.screenshot() for specific elements. Screenshots can also be configured to be captured automatically on test failures.
> In simple terms: Screenshot = capture current UI state for debugging or reporting

- **Capture Full Page Screenshot**

```ts
await page.screenshot({ path: 'screenshot.png' });
```
Captures visible viewport

- **Full Page (Entire Scroll)**

```ts
await page.screenshot({
  path: 'fullpage.png',
  fullPage: true,
});
```

 Captures entire page including scroll

-  **Capture Element Screenshot**

```ts
await page.locator('#login').screenshot({ path: 'element.png' });
```
Captures only specific element


Example Test

```ts
import { test } from '@playwright/test';

test('screenshot example', async ({ page }) => {
  await page.goto('https://example.com');

  await page.screenshot({ path: 'homepage.png' });
});
```

- **Capture Screenshot on Failure (Important)**

```ts
import { test } from '@playwright/test';

test.afterEach(async ({ page }, testInfo) => {
  if (testInfo.status !== testInfo.expectedStatus) {
    await page.screenshot({
      path: `screenshots/${testInfo.title}.png`,
    });
  }
});
```
 Very useful for debugging failed tests

- **Capture Screenshot as Buffer**

```ts
const screenshot = await page.screenshot();
```
 Can attach to reports

- ** Attach Screenshot to Report**

```ts
await testInfo.attach('screenshot', {
  body: await page.screenshot(),
  contentType: 'image/png',
});
```

- **Screenshot Options**

```ts
await page.screenshot({
  path: 'image.png',
  fullPage: true,
  type: 'png', // or 'jpeg'
  quality: 90, // for jpeg
});
```

- ** Auto Screenshot (Config)**

```ts
export default defineConfig({
  use: {
    screenshot: 'only-on-failure',
  },
});
```

Options:`'off'`, `'on'`,  `'only-on-failure'`

- **Best Practices**
✔ Use screenshots for debugging
✔ Capture on failure automatically
✔ Use meaningful file names
✔ Avoid excessive screenshots

---
---
## 38.Does Playwright support API testing? If so how can we perform API testing?
Yes, Playwright supports API testing using the built-in request fixture. It allows sending HTTP requests like GET and POST, validating responses, and integrating API testing with UI automation for end-to-end scenarios.

> In simple terms: Playwright can test backend APIs without opening a browser

### 38.1 What is API Testing in Playwright?
API testing  involves sending HTTP requests using the built-in request fixture and validating responses such as status codes, headers, and data. It allows faster and efficient backend testing and can be integrated with UI tests for end-to-end validation.

✔ Send HTTP requests (GET, POST, PUT, DELETE)
✔ Validate responses
✔ Test backend independently or along with UI

```ts
import { test, expect } from '@playwright/test';

test('API Test', async ({ request }) => {
  const response = await request.get('https://api.example.com/users');

  expect(response.status()).toBe(200);

  const body = await response.json();
  expect(body.length).toBeGreaterThan(0);
});
```

---

### 38.2 How to Perform API Testing
API testing in Playwright is performed using the built-in request fixture, where we send HTTP requests like GET or POST, validate the response status and data, and ensure backend functionality works correctly.

Playwright provides a built-in fixture:

```ts 
test('User API Test', async ({ request }) => {
  const response = await request.get('https://api.example.com/users');

  expect(response.status()).toBe(200);

  const data = await response.json();
  expect(data.length).toBeGreaterThan(0);
});
```

This allows you to send API calls directly


### 38.3 GET Request
A GET request in Playwright is used to retrieve data from an API using request.get(). The response is validated using status codes and response body to ensure correct data is returned.

```ts id="api_get"
import { test, expect } from '@playwright/test';

test('GET API test', async ({ request }) => {
  const response = await request.get('https://jsonplaceholder.typicode.com/posts/1');

  expect(response.status()).toBe(200);

  const data = await response.json();
  console.log(data);
});
```



### 38.4 POST Request 
A POST request in Playwright is used to send data to a server to create a new resource using request.post(). The request includes a payload, and the response is validated using status codes and response data.

```ts 
test('POST API test', async ({ request }) => {
  const response = await request.post('https://jsonplaceholder.typicode.com/posts', {
    data: {
      title: 'Test',
      body: 'Playwright API',
      userId: 1,
    },
  });

  expect(response.status()).toBe(201);

  const data = await response.json();
  console.log(data);
});
```



### 38.5 PUT Request 
A PUT request in Playwright is used to update an existing resource by sending data using request.put(). It replaces the resource completely and the response is validated using status codes and updated data.

```ts
test('Update User', async ({ request }) => {
  const response = await request.put('https://reqres.in/api/users/2', {
    data: {
      name: 'morpheus',
      job: 'zion resident'
    }
  });

  expect(response.status()).toBe(200);

  const body = await response.json();
  expect(body.name).toBe('morpheus');
});
```

### 38.6 DELETE Request
A DELETE request in Playwright is used to remove a resource from the server using request.delete(). The response is validated using status codes like 200 or 204, and often followed by verification to ensure the resource is deleted.
```ts
import { test, expect } from '@playwright/test';

test('DELETE API Test', async ({ request }) => {
  const response = await request.delete('https://api.example.com/users/1');

  expect(response.status()).toBe(200);
});

```
### 38.9 PATCH Request
A PATCH request in Playwright is used to partially update an existing resource using request.patch(). It updates only specific fields instead of replacing the entire resource, making it more efficient than PUT for partial updates.

```ts
test('Update User Partially', async ({ request }) => {
  const response = await request.patch('https://reqres.in/api/users/2', {
    data: {
      job: 'zion resident'
    }
  });

  expect(response.status()).toBe(200);

  const body = await response.json();
  expect(body.job).toBe('zion resident');
});
```



### 38.10 Setting Base URL (Best Practice)

```ts id="api_config"
export default defineConfig({
  use: {
    baseURL: 'https://jsonplaceholder.typicode.com',
  },
});
```

 Then use:

```ts id="api_short"
await request.get('/posts');
```

### 38.11 Adding Headers / Auth

```ts
await request.get('/secure-api', {
  headers: {
    Authorization: 'Bearer token123',
  },
});
```

### 38.12 Validate Response

```ts id="api_validate"
const response = await request.get('/posts/1');

expect(response.ok()).toBeTruthy();
expect(response.status()).toBe(200);

const body = await response.json();
expect(body.id).toBe(1);
```

### 38.13 API + UI Combined Testing

```ts 
test('API + UI test', async ({ request, page }) => {
  const response = await request.post('/login', {
    data: { username: 'admin', password: '1234' },
  });

  const data = await response.json();

  await page.goto('/dashboard');
});
```

 Use API for setup → UI for validation


### 38.14 Creating API Context (Advanced)

```ts 
import { request } from '@playwright/test';

const apiContext = await request.newContext({
  baseURL: 'https://api.example.com',
});
```

---

### 38.15 Advantages of API Testing in Playwright

✔ No need for external tools (like Postman)
✔ Fast execution
✔ Can combine API + UI testing
✔ Built-in assertions

---
---
## 39. What is Visual Testing? Why do we need it?
Visual testing is the process of validating the UI appearance of an application by comparing screenshots against a baseline. It helps detect layout issues, styling problems, and visual regressions that functional tests cannot catch.

> In simple terms: Visual Testing = Comparing screenshots to detect UI changes or bugs

- **How Visual Testing Works*
Basic flow:
✔ Take a **baseline screenshot** (expected UI)
✔ Run test → capture new screenshot
✔ Compare both images
✔ Highlight differences (if any)

- **Visual Testing in Playwright**
Playwright provides built-in visual testing using:
```ts
await expect(page).toHaveScreenshot();
```
Automatically:
✔ Captures screenshot
✔ Compares with baseline
✔ Fails test if mismatch

- ** Example Test**

```ts
import { test, expect } from '@playwright/test';

test('visual test example', async ({ page }) => {
  await page.goto('https://example.com');

  await expect(page).toHaveScreenshot();
});
```

- **Element-Level Visual Testing**

```ts
await expect(page.locator('#login')).toHaveScreenshot();
```
Tests only specific component

### 39.1 Why Do We Need Visual Testing?
Visual testing is needed to detect UI issues such as layout changes, styling problems, and visual regressions that functional tests cannot identify. It ensures the application looks correct and consistent across different environments.
✔ Detect UI Bugs
✔ Broken layout
✔ Misaligned elements
✔ Missing components

- **Catch CSS Issues**
✔ Wrong colors
✔ Font changes
✔ Spacing problems

- ** Prevent Visual Regression**
Ensures new changes don’t break existing UI

- **Validate Design Consistency**

✔ Matches design (Figma/UI specs)
✔ Ensures consistent look across pages

- ** Real-World Scenarios**
✔ After UI changes → verify nothing broke
✔ Responsive design testing
✔ Cross-browser UI consistency

- **Advantages**
✔ Catches issues functional tests miss
✔ Automates UI validation
✔ Improves user experience quality

---
---

## 40. Write a simple code to Test Visually?
In Playwright, visual testing is performed using toHaveScreenshot(), which captures a screenshot and compares it with a baseline image. If differences are detected, the test fails, helping identify UI changes.

- **Basic Visual Test (Full Page)**

```ts
import { test, expect } from '@playwright/test';

test('visual test - full page', async ({ page }) => {
  await page.goto('https://example.com');

  // Compare with baseline screenshot
  await expect(page).toHaveScreenshot();
});
```
 ✔ First run → creates baseline
✔ Next runs → compares automatically


- **Visual Test for Specific Element**

```ts
import { test, expect } from '@playwright/test';

test('visual test - element', async ({ page }) => {
  await page.goto('https://example.com');

  const loginButton = page.locator('#login');

  await expect(loginButton).toHaveScreenshot();
});
```

✔ Useful for testing UI components

- **Visual Test with Custom Name**

```ts
await expect(page).toHaveScreenshot('homepage.png');
```

✔ Saves baseline with custom file name

 
- **Visual Test with Options**

```ts
await expect(page).toHaveScreenshot({
  maxDiffPixels: 50,
  threshold: 0.3,
});
```
✔ Options:

 `maxDiffPixels` → allowed pixel differences
 `threshold` → sensitivity level


- **Handling Dynamic Content (Masking)**

```ts
await expect(page).toHaveScreenshot({
  mask: [page.locator('.dynamic-content')],
});
```

✔ Ignores changing elements (ads, timestamps)


### 40.1 Full Real Example

```ts
import { test, expect } from '@playwright/test';

test('homepage visual regression', async ({ page }) => {
  await page.goto('https://example.com');

  // Wait for page to stabilize
  await page.waitForLoadState('networkidle');

  // Visual comparison
  await expect(page).toHaveScreenshot('homepage.png', {
    fullPage: true,
    maxDiffPixels: 100,
  });
});
```

---

- **Folder Structure (Auto Generated)**

```
tests/
  example.spec.ts
  example.spec.ts-snapshots/
    homepage.png
```

✔ Baseline screenshots are stored automatically

- ** How It Works**
✔ First run → baseline image saved
✔ Next runs → new screenshot taken
✔ Playwright compares both
✔ If mismatch → test fails

---
---
## 41. How to configure multiple reporters in Playwright?
In Playwright, multiple reporters can be configured using the reporter array in the configuration file. Each reporter is added as an entry in the array, allowing generation of different report formats like HTML, JSON, and JUnit in a single test run.

- **Basic Configuration**

You configure reporters in the `playwright.config.ts` file using an **array**.

```ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  reporter: [
    ['list'],
    ['html'],
  ],
});
```
 This will:

✔ Show results in console (`list`)
✔ Generate HTML report (`html`)

- **Example with Multiple Reporters**

```ts
export default defineConfig({
  reporter: [
    ['list'],                         // Console output
    ['html', { open: 'never' }],      // HTML report
    ['junit', { outputFile: 'results.xml' }], // CI integration
  ],
});
```

### 41.1 Common Reporter Combinations

- ** Local Development**

```ts
reporter: [
  ['list'],
  ['html']
]
```

- **CI/CD Pipelines (e.g., Jenkins)**

```ts
reporter: [
  ['dot'],
  ['junit', { outputFile: 'results.xml' }]
]
```

- **Debugging + Reports**

```ts
reporter: [
  ['list'],
  ['html', { open: 'on-failure' }]
]
```

- **Reporter Options**

Each reporter can have its own configuration:

```ts
['html', { open: 'never' }]
```

✔ Common options:
 `open: 'always' | 'never' | 'on-failure'`
 `outputFile` → for junit/json
 `outputFolder` → for html


- **CLI Alternative**

You can also override reporters via command line:

```bash
npx playwright test --reporter=list,html
```

- **How It Works**

✔ Playwright runs tests
✔ Each reporter processes results independently
✔ Outputs are generated simultaneously

- **Best Practices**

✔ Use **HTML + List** for local development
✔ Use **JUnit + Dot/Line** for CI
✔ Avoid too many reporters (performance impact)
✔ Customize output paths properly

---
---
## 42.What is the serial mode in Playwright?
Serial mode in Playwright ensures that tests are executed sequentially in a specific order using test.describe.serial(). It is used when tests are dependent on each other, and if one test fails, the remaining tests are skipped.
> In simple terms: Serial mode = tests run step-by-step in order

- **Why Serial Mode is Needed**

By default, Playwright runs tests **in parallel** for speed.
But sometimes you need order when:
✔ Tests depend on previous test results
✔ Shared state is required
✔ Sequential workflow (login → action → logout)

- ** How to Enable Serial Mode**

Use `test.describe.configure()`:

```ts id="ser1"
import { test, expect } from '@playwright/test';

test.describe.configure({ mode: 'serial' });

test('test 1', async ({ page }) => {
  console.log('Test 1');
});

test('test 2', async ({ page }) => {
  console.log('Test 2');
});
```
Output:

```
Test 1 → Test 2
```

- ** Using Inside a Test Suite**

```ts 
  test.describe('serial tests', () => {
  test.describe.configure({ mode: 'serial' });

  test('step 1', async ({ page }) => {
    // login
  });

  test('step 2', async ({ page }) => {
    // perform action
  });

  test('step 3', async ({ page }) => {
    // logout
  });
});
```

- ** Important Behavior**
If One Test Fails → Others Skip
In serial mode:
✔ If **test 1 fails**
✔ Then **test 2, test 3 are skipped**

- **Serial vs Parallel**
In serial mode tests run one by one, making execution slower but allowing dependencies and stopping on failure, whereas in parallel mode tests run simultaneously for faster execution, avoid dependencies, and continue even if one fails.

| Feature    | Serial Mode         | Parallel Mode         |
| ---------- | ------------------- | --------------------- |
| Execution  | One by one          | Multiple at same time |
| Speed      | Slower              | Faster                |
| Dependency | Allowed             | Not recommended       |
| Failure    | Stops further tests | Others continue       |


## 42.2 Real-World Example
Scenario: Order Flow

```ts id="ser3"
test.describe('order flow', () => {
  test.describe.configure({ mode: 'serial' });

  test('login', async ({ page }) => {
    // login logic
  });

  test('add to cart', async ({ page }) => {
    // depends on login
  });

  test('checkout', async ({ page }) => {
    // depends on cart
  });
});
```

- ** When to Use Serial Mode**

Use when:
✔ Tests depend on each other
✔ Stateful workflows
✔ Multi-step scenarios

Avoid when:
✔ Tests are independent
✔ You want faster execution

- **Best Practices**
✔ Prefer independent tests (parallel)
✔ Use serial only when necessary
✔ Keep serial blocks small

---
---
## 43. How to perform parallel execution in PLaywright?
Parallel execution in Playwright is achieved using multiple worker processes. It can be configured using the workers setting in the config file or CLI, and tests can be run in parallel within files using test.describe.configure({ mode: 'parallel' }).

> In simple terms: Parallel execution = multiple tests run simultaneously

- **Default Behavior**
✔ Playwright already runs tests in parallel **across test files**
✔ Each file is executed in a separate **worker**

- ** Using CLI (Quick Way)**

```bash
npx playwright test --workers=4
```

Runs tests using **4 parallel workers**

- **Configure in `playwright.config.ts`**

```ts 
import { defineConfig } from '@playwright/test';

export default defineConfig({
  workers: 4,
});
```

 Sets default parallel workers

- **Fully Parallel Mode (Inside Same File)**
✔ By default: Tests inside a file run **sequentially**
To make them parallel:

```ts 
import { test } from '@playwright/test';

test.describe.configure({ mode: 'parallel' });

test('test 1', async ({ page }) => {
  console.log('Test 1');
});

test('test 2', async ({ page }) => {
  console.log('Test 2');
});
```

Both tests run simultaneously

- **Example (Real Test)**

```ts
test.describe('parallel tests', () => {
  test.describe.configure({ mode: 'parallel' });

  test('login test', async ({ page }) => {
    await page.goto('https://example.com');
  });

  test('search test', async ({ page }) => {
    await page.goto('https://example.com/search');
  });
});
```

- **Parallel Across Browsers**

```ts
projects: [
  { name: 'chromium', use: { browserName: 'chromium' } },
  { name: 'firefox', use: { browserName: 'firefox' } },
]
```
Same tests run in parallel across browsers

- **Important Notes**
✔ Tests must be **independent**
✔ Avoid shared data/state
✔ Use fixtures for isolation

- **Common Mistakes**
✔ Using shared variables
✔ Depending on execution order
✔ Not handling test data properly

- **Best Practices**
✔ Keep tests independent
✔ Use unique test data
✔ Avoid global state
✔ Use fixtures properly

---
---
## 44. What is actionability in Playwright? Explain in detail?
Actionability in Playwright refers to the set of checks performed before interacting with an element, such as ensuring it is visible, enabled, stable, and attached to the DOM. This automatic validation makes tests more reliable and reduces the need for manual waits.

> Playwright checks “Can I safely interact with this element?” before clicking or typing

- **Why Actionability is Important**
 Without checks:
✔ Click may happen too early
✔ Element may not be visible
✔ Tests become flaky 
With actionability:
✔ Reliable tests
✔ No manual waits needed

- **Actionability Checks (Core Conditions 🔥)**
Before performing actions like `click()` or `fill()`, Playwright automatically checks:
✔ Element is Attached or Present in DOM
✔ Element is Visible
✔ Element is Stable or Not moving (no animation)
✔ Element is Enabled orNot disabled
✔ Element Receives Events or Not covered by another element
- **Example**

```ts
await page.locator('#login').click();
```
Playwright will:
✔ Wait for element
✔ Check visibility
✔ Ensure it's clickable
✔ Then perform click

- ** How It Works Internally**

```text
Find element → Check conditions → Wait if needed → Perform action
```
- **Actions That Use Actionability**

✔ `click()`
✔ `fill()`
✔ `check()`
✔ `hover()`
✔ `selectOption()`


- **What Happens If Conditions Fail**
 Playwright throws error:

```text 
Element is not visible / not clickable
```

- **Can We Bypass Actionability?**
 Yes (not recommended)

```ts id="act5"
await page.click('#btn', { force: true });
```

✔ Forces action
✔ Skips checks
- **Why It Makes Playwright Powerful**

✔ No need for `sleep()`
✔ Reduces flaky tests
✔ Smart waiting
✔ Better stability

---
---


