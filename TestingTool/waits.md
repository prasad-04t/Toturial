
# 1️⃣ WAITS


## 1️⃣ Problem

Modern web applications are highly dynamic. Elements on a web page often take time to load due to:

- AJAX requests
- API responses
- JavaScript rendering
- Page transitions
- Dynamic UI updates

Automation scripts may attempt to interact with elements **before they are available in the DOM**, which causes test failures.

Common errors in automation testing:

- NoSuchElementException
- ElementNotInteractableException
- TimeoutException
- StaleElementReferenceException

This leads to common automation interview questions:

• What are waits in Selenium?  
• Why are waits required in automation testing?  
• What is the difference between implicit wait and explicit wait?  
• What is Fluent Wait?  
• When should each wait type be used?

### Why this concept is important in automation testing

Waits ensure automation scripts **synchronize with application behavior**.

Without waits:

- Tests become flaky
- Scripts fail intermittently
- Automation frameworks become unstable

### Problems solved by waits

Waits solve problems such as:

• Synchronizing test scripts with application load time  
• Handling dynamic elements  
• Preventing test failures caused by timing issues  
• Improving reliability of automation frameworks


---

## 2️⃣ Answer

### Definition

**Waits** are mechanisms used in automation testing to pause the execution of a script until a specific condition is met.

### Purpose

The purpose of waits is to:

- Synchronize automation scripts with the application
- Ensure elements are available before interaction
- Improve test stability

### Where waits are used in automation frameworks

Waits are used in:

- Page Object Model methods
- Test scripts
- Framework utility classes
- Synchronization helpers

### Tools where waits are used

| Tool | Wait Implementation |
|-----|-----|
| Selenium | Implicit Wait, Explicit Wait, Fluent Wait |
| Cypress | Built-in automatic waits |
| Playwright | Auto-waiting with locator actions |

Example Selenium:

```java
WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("username")));
````

Example Cypress:

```javascript
cy.get('#username').should('be.visible')
```

Example Playwright:

```javascript
await page.locator('#username').waitFor()
```

---

## 3️⃣ Clear Explanation

### Definition

Waits allow automation scripts to **pause execution until a condition becomes true**.

Example scenario:

A login button appears **after an API call completes**.

Without waits:

Automation script fails.

With waits:

Automation script waits until the button becomes visible.

---

### Why waits are used

Web applications load elements asynchronously.

Automation must wait for:

* Elements to appear
* Elements to become clickable
* Pages to finish loading
* AJAX requests to complete

---

### Key Features

• Synchronization between test scripts and application
• Reduced test flakiness
• Supports conditional waiting
• Improves automation reliability

---

### Advantages

| Advantage              | Explanation                                |
| ---------------------- | ------------------------------------------ |
| Reliable automation    | Tests wait for elements before interacting |
| Handles dynamic pages  | Works with AJAX and JavaScript             |
| Prevents test failures | Avoids timing issues                       |

---

### Limitations

| Limitation                      | Explanation                               |
| ------------------------------- | ----------------------------------------- |
| Poor implementation slows tests | Overuse of waits increases execution time |
| Hardcoded waits are inefficient | Static waits waste time                   |

---

### Real-world usage in automation testing

Example login automation:

```
Open login page
Wait for username field
Enter username
Wait for password field
Enter password
Wait for login button
Click login
```

---

# TYPES / COMPONENTS

## 1️⃣ Implicit Wait

### Explanation

Implicit wait tells Selenium to **wait for a specified time when searching for elements**.

### Syntax

```java
driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
```

### Example

```java
driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
driver.findElement(By.id("username")).sendKeys("admin");
```

### When to use

* Global wait across the entire test
* Basic synchronization

---

## 2️⃣ Explicit Wait

### Explanation

Explicit wait waits for **a specific condition** before proceeding.

### Syntax

```java
WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("username")));
```

### Example

```java
WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

WebElement element =
wait.until(ExpectedConditions.elementToBeClickable(By.id("loginBtn")));

element.click();
```

### When to use

* Waiting for specific elements
* Dynamic web pages
* AJAX content

---

## 3️⃣ Fluent Wait

### Explanation

Fluent wait allows:

* Custom polling interval
* Ignoring exceptions
* Flexible wait configuration

### Syntax

```java
Wait<WebDriver> wait = new FluentWait<>(driver)
.withTimeout(Duration.ofSeconds(10))
.pollingEvery(Duration.ofSeconds(2))
.ignoring(NoSuchElementException.class);
```

### Example

```java
Wait<WebDriver> wait = new FluentWait<>(driver)
.withTimeout(Duration.ofSeconds(10))
.pollingEvery(Duration.ofSeconds(2));

WebElement element =
wait.until(driver -> driver.findElement(By.id("username")));
```

### When to use

* Highly dynamic elements
* Custom wait strategies

---

## 4️⃣ Hard Wait (Thread.sleep)

### Explanation

Hard wait pauses execution for a fixed time.

### Syntax

```java
Thread.sleep(5000);
```

### Example

```java
Thread.sleep(3000);
driver.findElement(By.id("loginBtn")).click();
```

### When to use

Rarely recommended.

Problems:

* Slows tests
* Not dynamic

---

# ADVANCED CONCEPTS

## Expected Conditions

Common conditions used with explicit waits.

| Condition                  | Example           |
| -------------------------- | ----------------- |
| visibilityOfElementLocated | Element visible   |
| elementToBeClickable       | Element clickable |
| presenceOfElementLocated   | Element exists    |
| textToBePresentInElement   | Text appears      |

Example:

```java
wait.until(ExpectedConditions.elementToBeClickable(By.id("loginBtn")));
```

---

## Wait for AJAX Calls

Example approach:

Wait until element appears after API response.

---

## Handling Stale Elements

Example:

```java
wait.until(ExpectedConditions.refreshed(
ExpectedConditions.visibilityOfElementLocated(By.id("username"))
));
```

---

## Smart Wait Strategy

Professional frameworks use:

* Explicit waits
* Retry mechanisms
* Utility wait classes

---

# IMPLEMENTATION USING PAGE OBJECT MODEL (POM)

Example project structure

```
pages/
   LoginPage.java

tests/
   LoginTest.java
```

Wait logic can be placed in:

* BasePage class
* Utility classes

---

# JAVA IMPLEMENTATION with Selenium WebDriver

## Page Class

```java
public class LoginPage {

    WebDriver driver;
    WebDriverWait wait;

    By username = By.id("username");
    By password = By.id("password");
    By loginBtn = By.id("loginBtn");

    public LoginPage(WebDriver driver){

        this.driver = driver;
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));

    }

    public void login(String user,String pass){

        wait.until(ExpectedConditions.visibilityOfElementLocated(username)).sendKeys(user);

        driver.findElement(password).sendKeys(pass);

        wait.until(ExpectedConditions.elementToBeClickable(loginBtn)).click();

    }

}
```

---

## Test Class

```java
public class LoginTest {

    WebDriver driver;

    @Test
    public void loginTest(){

        driver = new ChromeDriver();

        driver.get("https://example.com/login");

        LoginPage login = new LoginPage(driver);

        login.login("admin","password");

    }

}
```

---

# PYTHON IMPLEMENTATION with Selenium WebDriver

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, user, pwd):

        self.wait.until(EC.visibility_of_element_located((By.ID,"username"))).send_keys(user)

        self.driver.find_element(By.ID,"password").send_keys(pwd)

        self.wait.until(EC.element_to_be_clickable((By.ID,"loginBtn"))).click()
```

---

# JAVASCRIPT IMPLEMENTATION with CYPRESS

Cypress automatically waits for elements.

```javascript
class LoginPage {

    username(){
        return cy.get('#username')
    }

    password(){
        return cy.get('#password')
    }

    loginBtn(){
        return cy.get('#loginBtn')
    }

    login(user,pass){
        this.username().should('be.visible').type(user)
        this.password().type(pass)
        this.loginBtn().should('be.enabled').click()
    }

}

export default new LoginPage()
```

---

# JAVA IMPLEMENTATION with Playwright

Playwright has **auto-waiting built in**.

```java
public class LoginPage {

    private Page page;

    public LoginPage(Page page){
        this.page = page;
    }

    public void login(String user,String pass){

        page.locator("#username").fill(user);
        page.locator("#password").fill(pass);
        page.locator("#loginBtn").click();

    }

}
```

---

# PYTHON IMPLEMENTATION with Playwright

```python
class LoginPage:

    def __init__(self, page):
        self.page = page

    def login(self, user, pwd):

        self.page.locator("#username").fill(user)
        self.page.locator("#password").fill(pwd)
        self.page.locator("#loginBtn").click()
```

---

# JAVASCRIPT IMPLEMENTATION with Playwright

```javascript
import { test } from '@playwright/test';

test('login test', async ({ page }) => {

    await page.goto('https://example.com');

    await page.locator('#username').fill('admin');
    await page.locator('#password').fill('password');
    await page.locator('#loginBtn').click();

});
```

---

# BEST PRACTICES

Professional automation engineers follow these practices.

### Prefer Explicit Waits

Explicit waits provide better control.

---

### Avoid Thread.sleep()

Hard waits slow down test execution.

---

### Centralize Wait Logic

Create a **WaitUtility class** in frameworks.

---

### Use Smart Wait Conditions

Examples:

* visibilityOfElement
* elementToBeClickable

---

### Combine Waits with POM

Waits should be inside page methods.

---

# COMMON INTERVIEW QUESTIONS

### What are waits in Selenium?

Waits pause execution until conditions are satisfied.

---

### Difference between implicit and explicit wait?

| Feature     | Implicit Wait  | Explicit Wait    |
| ----------- | -------------- | ---------------- |
| Scope       | Global         | Specific element |
| Flexibility | Low            | High             |
| Performance | Less efficient | More efficient   |

---

### What is Fluent Wait?

Fluent wait allows custom polling intervals and exception handling.

---

### Why avoid Thread.sleep()?

Because it causes unnecessary delays and slows automation.

---

# SUMMARY

Waits are essential synchronization mechanisms in automation testing.

Key ideas:

• Waits synchronize automation scripts with application behavior
• Selenium supports implicit, explicit, and fluent waits
• Cypress and Playwright provide automatic waits
• Explicit waits are preferred for dynamic elements
• Proper wait strategies reduce flaky tests

Mastering waits is critical for building **stable, reliable, and scalable automation frameworks.**

```
```
