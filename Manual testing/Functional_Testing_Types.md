# 1. What is **Functional Testing?**

**Functional Testing** is a type of software testing that verifies whether the **software application functions according to the specified requirements**.

In simple terms:

> **Functional Testing checks whether each feature of the application works as expected.**

It focuses on **what the system does**, not how the internal code works. Testers validate the **inputs, outputs, and behavior of the system** based on the functional requirements. 

## Key Points of Functional Testing

* Based on **business requirements and specifications**
* Tests **application functionality**
* Does **not require knowledge of source code**
* Usually performed using **Black-Box Testing techniques**
* Ensures the system works **correctly from the user's perspective**



## Example: Login Functionality

Requirement:
User should be able to **log in using a valid username and password**.

Test cases:

| Test Case | Input                             | Expected Result    |
| --------- | --------------------------------- | ------------------ |
| TC1       | Valid username + valid password   | Login successful   |
| TC2       | Valid username + invalid password | Error message      |
| TC3       | Empty username/password           | Validation message |

Testing these behaviors is **Functional Testing**.


## Common Types of Functional Testing

Some common types include:

* **Unit Testing**
* **Integration Testing**
* **System Testing**
* **User Acceptance Testing (UAT)**
* **Smoke Testing**
* **Sanity Testing**
* **Regression Testing**
* **Retesting** 


## Real-World Example

For an **E-commerce website**, functional testing verifies:

* User registration
* Login functionality
* Product search
* Add to cart
* Payment processing
* Order confirmation

If all these features work correctly, the system passes **functional testing**.


✅ **Short Interview Answer**

> **Functional Testing is a type of software testing that verifies whether the application functions according to the specified requirements by validating inputs, outputs, and system behavior.**

---
---

# 2️. What is **Smoke Testing? Why is it called so?**

**Smoke Testing** is a **type of software testing performed to verify that the basic and critical functionalities of an application are working properly after a new build is received**.

In simple terms:

> **Smoke Testing checks whether the major features of the application work before detailed testing begins.**

If the smoke test fails, the build is **rejected and returned to the development team** for fixing. 

---

## 🎯 Purpose of Smoke Testing

Smoke testing is performed to ensure that:

* The **application build is stable**
* **Critical functionalities are working**
* The build is **ready for further testing**
* Testers do not waste time testing an unstable build


## 🧩 Example

Suppose a **Login Application** has the following features:

* Open application
* Login with username and password
* Logout functionality

### Smoke Test Cases

| Test Case                    | Expected Result                |
| ---------------------------- | ------------------------------ |
| Application launches         | Application opens successfully |
| Login with valid credentials | Login successful               |
| Logout functionality         | User logs out successfully     |

If these **basic features work**, the build **passes smoke testing**.



## 🧠 Why is it Called **Smoke Testing?**

The term comes from **hardware testing**.

When engineers build hardware devices, they first **turn on the device to check whether smoke comes out**.

* If **smoke appears**, the device is faulty.
* If **no smoke appears**, the device is considered stable enough for further testing.

Similarly in software:

* If the **basic functionality fails**, the build is rejected.
* If **basic functionality works**, detailed testing continues.


## ⭐ Characteristics of Smoke Testing

* Performed **after receiving a new build**
* Tests **basic and critical features**
* Usually **quick and shallow testing**
* Can be done **manually or using automation**
* Also called **Build Verification Testing (BVT)**


## 🎯 Short Interview Answer

> **Smoke Testing is a type of testing performed to verify that the basic functionalities of an application work correctly after a new build is received. It is called Smoke Testing because it originates from hardware testing, where a device is powered on to check if smoke appears, indicating a major failure.**

---
---

# 3️. What is **Sanity Testing? How is it different from Smoke Testing?**

## What is **Sanity Testing?**

**Sanity Testing** is a type of **software testing performed after bug fixes or minor changes** to verify that the **specific functionality works correctly**.

In simple terms:

> **Sanity Testing checks whether the particular module or functionality works properly after changes or bug fixes.**

Instead of testing the entire application, testers **focus only on the affected functionality** to confirm that the issue is fixed and no new problems are introduced. 



### 🧩 Example

Suppose there is a **bug in the login feature**.

Bug:
User cannot log in even with **valid credentials**.

Developer fixes the bug and provides a new build.

### Sanity Testing

Tester checks only the **login functionality**:

| Test Case                    | Expected Result         |
| ---------------------------- | ----------------------- |
| Login with valid credentials | Login successful        |
| Login with invalid password  | Error message displayed |
| Login with empty fields      | Validation message      |

If these tests pass, the tester confirms the **fix is working**.

# 📊 Sanity Testing vs Smoke Testing

| Feature        | **Smoke Testing**                             | **Sanity Testing**                            |
| -------------- | --------------------------------------------- | --------------------------------------------- |
| Purpose        | Verify basic functionality of the application | Verify specific functionality after bug fixes |
| When performed | After receiving a new build                   | After bug fixes or minor changes              |
| Scope          | Broad and shallow                             | Narrow and deep                               |
| Focus          | Entire application’s basic features           | Only affected modules                         |
| Goal           | Check if build is stable for testing          | Check if bug fix works correctly              |


## Simple Example

### Smoke Testing

Testing basic features of an **E-commerce website**:

* Application launches
* Login works
* Add to cart works
* Checkout page opens

Purpose → Check whether the **build is stable**.

### Sanity Testing

If a bug is fixed in **Add to Cart**, tester checks:

* Add product to cart
* Remove product from cart
* Update product quantity

Purpose → Verify **that specific functionality works correctly**.


## Short Interview Answer

> **Sanity Testing is performed after bug fixes or minor changes to verify that the specific functionality works correctly, while Smoke Testing is performed after receiving a new build to check whether the basic functionalities of the application are working.**

---
---

# 4. What is **Regression Testing? Why is it Important?**

## What is **Regression Testing?**

**Regression Testing** is a type of **software testing performed to ensure that new code changes, bug fixes, or enhancements do not negatively affect the existing functionality of the application.**

In simple terms:

> **Regression Testing checks whether previously working features still work correctly after changes are made to the software.**

Whenever developers modify the code (fix bugs, add features, or optimize code), testers perform regression testing to confirm that the **existing system behavior remains unchanged**. 

## Example

Suppose an **E-commerce application** has these features:

* Login
* Search product
* Add to cart
* Payment

A developer fixes a bug in the **payment module**.

During **Regression Testing**, the tester checks:

| Feature        | Expected Result                   |
| -------------- | --------------------------------- |
| Login          | User should login successfully    |
| Search product | Products should display correctly |
| Add to cart    | Items added successfully          |
| Payment        | Payment processed correctly       |

This ensures that **the payment fix did not break other functionalities**.


## Why is Regression Testing Important?

Regression testing is important because it:

### 1️. Ensures Existing Features Still Work

Changes in one part of the system may unintentionally affect other parts.

Example:
Fixing login functionality may accidentally affect **session handling**.


### 2️. Prevents New Bugs

Regression testing helps detect **new defects introduced by code changes**.


### 3️. Maintains Software Stability

It ensures that the application remains **stable and reliable after updates**.



### 4️. Supports Continuous Development

In **Agile and CI/CD environments**, frequent updates require continuous regression testing.


### 5️. Protects Business-Critical Features

Critical features like **login, payments, and transactions** must always work correctly.

## Types of Regression Testing

| Type                | Description              |
| ------------------- | ------------------------ |
| Unit Regression     | Tests individual modules |
| Partial Regression  | Tests affected modules   |
| Complete Regression | Tests entire application |


## Example Scenario

Bug fixed: **User cannot login with valid credentials**

After fixing the bug, testers check:

* Login functionality
* Password reset
* User profile access

This confirms that **the fix did not break other related features**.


## Short Interview Answer

> **Regression Testing is performed to verify that recent code changes, bug fixes, or enhancements have not affected the existing functionality of the application. It ensures that previously working features continue to work correctly.**

---
---

# Difference Between **Regression Testing** and **Retesting**

Both **Regression Testing** and **Retesting** are important activities in software testing, but they serve **different purposes**.



## 1️. Retesting

**Retesting** means **testing a specific defect again after it has been fixed by the developer** to verify that the issue is resolved.

### Key Points

* Focuses on **one specific defect**
* Performed **after the developer fixes a bug**
* Uses the **same test case that previously failed**
* Ensures the **bug is actually fixed**

### Example

Bug reported:
User cannot login with **valid credentials**.

Steps:

1. Tester reports the bug.
2. Developer fixes the issue.
3. Tester runs the **same login test case again**.

If login works → **Bug is fixed**.


## 2. Regression Testing

**Regression Testing** means **testing the existing functionality of the application after code changes to ensure that new changes did not break existing features**. 

### Key Points

* Focuses on **existing functionality**
* Ensures **new changes did not affect old features**
* Tests **multiple modules or the entire application**
* Often **automated using tools like Selenium**

### Example

Developer fixes bug in **payment module**.

During regression testing, tester checks:

* Login
* Search product
* Add to cart
* Payment

This ensures the **payment fix did not break other features**.


## Regression Testing vs Retesting

| Feature         | **Retesting**             | **Regression Testing**                    |
| --------------- | ------------------------- | ----------------------------------------- |
| Purpose         | Verify a specific bug fix | Ensure existing functionality still works |
| Scope           | Specific defect           | Entire application or related modules     |
| Test Cases      | Same test case used again | Multiple existing test cases              |
| Performed After | Bug fix                   | Code change / new feature                 |
| Automation      | Usually manual            | Often automated                           |



## Simple Example

Bug: **Add to Cart button not working**

### Retesting

Tester checks only:

* Add to Cart functionality

### Regression Testing

Tester checks:

* Login
* Search product
* Add to Cart
* Checkout
* Payment


✅ **Short Interview Answer**

> **Retesting verifies that a specific defect has been fixed, while Regression Testing ensures that recent code changes have not affected existing functionalities of the application.**

---
---

# Why is **Regression Testing usually automated?**

**Regression Testing** checks whether existing features still work correctly after code changes, bug fixes, or new features are added. 

Because regression testing is performed **frequently and involves many test cases**, it is usually **automated using tools like Selenium, Cypress, or Playwright**.


## 1️. Large Number of Test Cases

Regression testing often includes **hundreds or thousands of existing test cases**.

Running them manually would take **a lot of time and effort**.

✅ Automation can execute all these tests **quickly and repeatedly**.

**Example**

An e-commerce application may require regression testing for:

* Login
* Search product
* Add to cart
* Payment
* Order history

Automation scripts can run all these tests **in minutes**.



## 2️. Frequent Code Changes

In modern development (especially **Agile and CI/CD**), developers update the application **frequently**.

Every update requires regression testing.

Automation helps run regression tests **after every build automatically**.

Example workflow:

```
Code change → Build → Automated Regression Tests → Report
```


## 3️. Saves Time and Effort

Manual regression testing:

* Slow
* Repetitive
* Prone to human errors

Automation testing:

* Fast
* Consistent
* Less human effort

This is why automation is **ideal for repetitive regression tests**.

---

## 4️. Improves Test Coverage

Automation allows testers to run **more test cases across different environments**.

Example:

* Chrome
* Firefox
* Edge
* Mobile browsers

Automation frameworks can execute tests on **multiple browsers simultaneously**.


## 5️. Supports Continuous Integration (CI/CD)

Automation enables regression tests to run automatically in **CI/CD pipelines**.

Example tools:

* Jenkins
* GitHub Actions
* GitLab CI

Whenever new code is pushed, regression tests run automatically.



## Example (Selenium Automation)

Instead of manually testing login every time, a Selenium script can run automatically.

Example:

```java
WebDriver driver = new ChromeDriver();
driver.get("https://example.com/login");
driver.findElement(By.id("username")).sendKeys("user");
driver.findElement(By.id("password")).sendKeys("pass");
driver.findElement(By.id("loginBtn")).click();
```

This script can run **every time a new build is deployed**.



## Short Interview Answer

> **Regression Testing is usually automated because it involves running a large number of repetitive test cases after every code change. Automation helps execute these tests quickly, improves accuracy, and supports continuous integration and frequent releases.**

---
---

# Which Test Cases Should Be Automated in Regression Testing?
In **Regression Testing**, we usually have **many existing test cases**. However, **not all test cases should be automated**. Testers select specific types of test cases that provide the most value when automated.


## 1️. Frequently Executed Test Cases

Test cases that are executed **again and again** in every build should be automated.

**Example**

* Login functionality
* User registration
* Search functionality

Automation saves time because these tests run repeatedly in regression cycles.



## 2️. Business-Critical Test Cases

Important features that affect **core business operations** should always be automated.

**Example**

* Payment processing in an e-commerce system
* Money transfer in a banking application
* Booking confirmation in a travel app

If these fail, it can cause **major business loss**, so automation ensures they are always tested.



## 3️. High-Risk or Complex Areas

Modules that are **complex or prone to defects** should be automated.

**Example**

* Pricing calculations
* Tax calculations
* Discount logic

Automation helps ensure these areas remain stable after code changes.



## 4️. Test Cases with Large Data Sets

Some tests require **multiple data combinations**.

Automation can run them quickly.

**Example**

* Testing login with multiple usernames/passwords
* Product search with many filters



## 5️. Cross-Browser / Cross-Platform Tests

If the application must work on **multiple browsers or devices**, automation is very useful.

**Example**
Test the same functionality on:

* Chrome
* Firefox
* Edge
* Safari

Automation frameworks can run tests across browsers automatically.



## 6️. Stable Features

Features that **do not change frequently** are good candidates for automation.

**Example**

* Login page
* User profile page
* Search functionality

If a feature changes often, automation scripts may break frequently.



## 7️. Repetitive Test Cases

Test cases that are **boring and repetitive for manual testers** should be automated.

Automation tools execute them **quickly and consistently** without human errors.



## Test Cases That Should NOT Be Automated

Usually these are **not automated**:

* Exploratory testing
* UI tests that change frequently
* One-time test cases
* Usability testing

These are better done manually.


## Example (Regression Suite)

For an **E-commerce Application**, automation might include:

| Automated Test Case | Reason                  |
| ------------------- | ----------------------- |
| Login functionality | Frequently used         |
| Search product      | Core feature            |
| Add to cart         | Business critical       |
| Checkout / Payment  | High-risk module        |
| Order history       | Important functionality |

Automation ensures these **key features always work after code changes**.


✅ **Short Interview Answer**

> **Test cases that are frequently executed, business-critical, stable, repetitive, involve large datasets, or require cross-browser testing should be automated in regression testing.**

---
---

# Test Cases That Should NOT Be Automated
In **automation testing**, not all test cases are good candidates for automation. Some tests are better executed **manually** because automation may be inefficient, unstable, or too expensive to maintain.

Here are the **test cases that should NOT be automated**

## 1️. Test Cases That Change Frequently

If the functionality or UI changes very often, the automation scripts will **break frequently**.

Example:

* UI layout changes
* Rapidly evolving features

Reason:

* High **maintenance cost** for automation scripts.

## 2️. One-Time Test Cases

Tests that will be executed **only once** are not suitable for automation.

Example:

* Testing a feature that will be removed later
* One-time migration testing

Reason:

* Writing automation scripts takes time, so it is **not worth automating** one-time tests.



## 3️. Exploratory Testing

Exploratory testing requires **human thinking, creativity, and observation** while interacting with the system.

Example:

* Exploring a new feature to find unexpected bugs.

Reason:

* Automation cannot replicate **human intuition and exploration**. 



## 4️. Usability Testing

Usability testing evaluates **user experience, design, and ease of use**.

Example:

* Is the UI easy to understand?
* Is the navigation intuitive?

Reason:

* Automation cannot judge **user satisfaction or visual comfort**.



## 5️. Test Cases with Unstable Requirements

If requirements are **not finalized or frequently changing**, automation scripts will need constant updates.

Example:

* Features under active development.

Reason:

* Automation becomes **inefficient and costly to maintain**.



## 6️. Complex Test Cases with Visual Validation

Tests requiring **visual verification** are difficult to automate.

Example:

* UI color alignment
* Font styles
* Layout design

Reason:

* Human testers are better at **visual inspection**.



## 7️. Small or Low-Priority Features

If a feature has **low risk or low business impact**, automation may not be necessary.

Example:

* Minor UI text validation.

Reason:

* Automation effort may **not justify the benefit**.



## 8️. Test Cases with Random or Dynamic Results

Some scenarios involve **unpredictable outputs or external systems**.

Example:

* CAPTCHA validation
* Random content generation

Reason:

* These tests are **hard to automate reliably**.



## Summary Table

| Test Case Type         | Why Not Automate              |
| ---------------------- | ----------------------------- |
| Frequently changing UI | Scripts break often           |
| One-time tests         | Not worth automation effort   |
| Exploratory testing    | Needs human creativity        |
| Usability testing      | Requires human judgment       |
| Unstable requirements  | Scripts need constant updates |
| Visual validation      | Hard for automation tools     |
| Low-priority features  | Low ROI                       |
| Random/dynamic results | Hard to automate reliably     |


✅ **Short Interview Answer**

> **Test cases that change frequently, one-time tests, exploratory testing, usability testing, unstable requirements, visual validation tests, low-priority features, and scenarios with dynamic results should not be automated because automation would be inefficient or difficult to maintain.**

---
---

## What is **User Acceptance Testing (UAT)?**

**User Acceptance Testing (UAT)** is the **final phase of testing** where the **end users, clients, or business stakeholders test the software to ensure it meets their business requirements before it is released to production.**

In simple terms:

> **UAT verifies that the software works correctly for real users and satisfies business needs.**

It confirms that the system is **ready for deployment and real-world use**. 



## Key Points of UAT

* Performed **after system testing**
* Conducted by **clients, end users, or business analysts**
* Focuses on **business requirements and real-world scenarios**
* Determines whether the system is **acceptable for release**



## Example

Suppose a company develops an **E-commerce website**.

Before launching the system, the **client or business team performs UAT** to check:

| Scenario            | Expected Result              |
| ------------------- | ---------------------------- |
| User registration   | Account created successfully |
| Login functionality | User can log in              |
| Add product to cart | Product added successfully   |
| Payment processing  | Payment completed            |
| Order confirmation  | Order placed successfully    |

If all these **business workflows work correctly**, the client approves the system for **production release**.



## Who Performs UAT?

| Role                | Responsibility                 |
| ------------------- | ------------------------------ |
| Clients / Customers | Validate business requirements |
| Business Analysts   | Verify workflows               |
| End Users           | Test real user scenarios       |



## Types of UAT

Common types include:

1. **Alpha Testing** – Testing done internally by the organization.
2. **Beta Testing** – Testing done by a limited group of external users.
3. **Contract Acceptance Testing** – Ensures software meets contract requirements.
4. **Operational Acceptance Testing (OAT)** – Verifies system readiness for production.



# Example Workflow

```
Development
      ↓
System Testing
      ↓
User Acceptance Testing (UAT)
      ↓
Production Release
```

UAT ensures the system is **ready for real users**.


## Short Interview Answer

> **User Acceptance Testing (UAT) is the final phase of testing where end users or clients verify that the software meets business requirements and is ready for production release.**

---
---

# What is **System Testing?**

**System Testing** is a level of software testing where the **entire integrated application is tested as a complete system** to verify that it meets the **specified functional and non-functional requirements**. 

In simple terms:

> **System Testing checks whether the whole application works correctly as a complete system.**

It is performed **after Integration Testing** and **before User Acceptance Testing (UAT)**.



## Key Characteristics of System Testing

* Tests the **complete application**
* Performed by the **QA / testing team**
* Based on **system requirements**
* Usually done using **Black-Box testing**
* Validates both **functional and non-functional requirements**



## Example

Consider an **Online Banking Application**.

System testing verifies the complete workflow:

| Functionality         | Expected Result                  |
| --------------------- | -------------------------------- |
| User login            | User should log in successfully  |
| Check account balance | Correct balance displayed        |
| Transfer money        | Transfer completed successfully  |
| Transaction history   | Transactions displayed correctly |

Here, the **entire system is tested together**, not individual modules.



## What is Tested in System Testing?

System testing verifies:

* Functional requirements
* Performance
* Security
* Usability
* Compatibility

Examples of tests performed during system testing:

* Functional testing
* Performance testing
* Security testing
* Load testing
* Usability testing



## Example Scenario

For an **E-commerce website**, system testing may include:

1. User registration
2. Login functionality
3. Search product
4. Add product to cart
5. Payment processing
6. Order confirmation

The tester ensures the **entire end-to-end flow works correctly**.



## System Testing in the Testing Levels

```
Unit Testing
     ↓
Integration Testing
     ↓
System Testing
     ↓
User Acceptance Testing (UAT)
```

System testing ensures the **whole system works correctly before it is delivered to the client**.



## Short Interview Answer

> **System Testing is the testing of the complete integrated application to verify that the system works according to the specified requirements. It is performed after integration testing and before user acceptance testing.**

---
---
# Difference Between **System Testing** and **User Acceptance Testing (UAT)**

Both **System Testing** and **User Acceptance Testing (UAT)** are testing levels performed after development, but they have different purposes and are performed by different people.


## 1️. System Testing

**System Testing** is testing the **entire integrated system** to verify that the application meets the **functional and non-functional requirements**. 

**Key Points**

* Tests the **complete system**
* Performed by the **QA / testing team**
* Focuses on **technical and functional requirements**
* Done **before UAT**
* Uses **test cases and test scenarios**

**Example**

Testing an **E-commerce application**:

* User registration
* Login
* Product search
* Add to cart
* Payment processing
* Order confirmation

QA testers verify that the **entire system works correctly**.

## 2️. User Acceptance Testing (UAT)

**User Acceptance Testing (UAT)** is the **final phase of testing** where **end users or clients validate the software** to ensure it meets **business requirements before release**. 

**Key Points**

* Performed by **clients, end users, or business analysts**
* Focuses on **business workflows**
* Ensures the system is **ready for production**
* Conducted **after system testing**
* Validates **real-world scenarios**

**Example**

For an **E-commerce website**, the client checks:

* Can users register successfully?
* Can users log in?
* Can users purchase products?
* Is payment working correctly?

If everything meets business needs → **system is approved for release**.

## 📊 System Testing vs UAT

| Feature       | System Testing                             | User Acceptance Testing (UAT)          |
| ------------- | ------------------------------------------ | -------------------------------------- |
| Purpose       | Verify the complete system works correctly | Verify the system meets business needs |
| Performed By  | QA / Testers                               | Clients / End users                    |
| Focus         | Functional & technical requirements        | Business requirements                  |
| Testing Level | Before UAT                                 | Final testing phase                    |
| Goal          | Find defects in the system                 | Approve the system for release         |


✅ **Short Interview Answer**

> **System Testing verifies that the entire application works according to the system requirements and is performed by the QA team, whereas User Acceptance Testing (UAT) is performed by end users or clients to ensure the software meets business requirements before release.**

---
---

# What is **Integration Testing?**

**Integration Testing** is a level of software testing where **multiple modules or components of an application are combined and tested together to verify that they interact correctly.** 

In simple terms:

> **Integration Testing checks whether different modules of a system work properly when integrated together.**

It is performed **after Unit Testing** and **before System Testing**.

### Example

Consider a **Login System** with two modules:

* **Login Module**
* **Database Module**

During **Integration Testing**, testers verify:

| Interaction                        | Expected Result                |
| ---------------------------------- | ------------------------------ |
| Login page sends username/password | Data sent to database          |
| Database verifies credentials      | Correct response returned      |
| System displays result             | Login success or error message |

This ensures **modules communicate correctly**.

## Types of Integration Testing

Integration testing is mainly performed using **four approaches**.


## 1️. Big Bang Integration Testing

All modules are **combined at once and tested together**.

### Characteristics

* All components integrated simultaneously
* Testing done after all modules are developed
* Difficult to find the exact cause of defects

### Example

Modules integrated at once:

```
Login + Payment + Search + Cart → Test together
```

### Advantages

* Simple approach
* Suitable for small systems

### Disadvantages

* Hard to identify bugs
* Testing starts late


## 2️. Top-Down Integration Testing

Testing starts from the **top-level modules** and gradually integrates **lower-level modules**.

### Approach

```
Main Module
     ↓
Sub Module 1
     ↓
Sub Module 2
```

### Key Point

Uses **Stubs** (temporary programs simulating lower modules).

### Example

Testing:

* Main application menu
* Then integrate login module
* Then integrate database module


## 3️. Bottom-Up Integration Testing

Testing starts from **lower-level modules** and moves upward.

### Approach

```
Database Module
     ↑
Login Module
     ↑
Main Application
```

### Key Point

Uses **Drivers** (temporary programs simulating higher modules).

### Advantages

* Easy to detect defects early
* Lower modules tested thoroughly


## 4️. Sandwich (Hybrid) Integration Testing

Combination of **Top-Down** and **Bottom-Up** testing.

### Approach

```
Top Modules ↓
            Middle Layer
Bottom Modules ↑
```

### Advantages

* Faster testing
* Combines benefits of both approaches

---

## Example: Online Shopping Application

Modules:

* User login
* Product search
* Add to cart
* Payment gateway

Integration testing verifies:

| Module Interaction        | Expected Result       |
| ------------------------- | --------------------- |
| Login → Database          | Credentials validated |
| Search → Product database | Products displayed    |
| Cart → Payment gateway    | Payment processed     |


## Integration Testing in Testing Levels

```
Unit Testing
     ↓
Integration Testing
     ↓
System Testing
     ↓
User Acceptance Testing
```



## Short Interview Answer

> **Integration Testing is a level of testing where individual modules are combined and tested together to verify that they interact correctly. The main types of integration testing are Big Bang, Top-Down, Bottom-Up, and Sandwich (Hybrid) integration testing.**

---
---

# Difference Between **Unit Testing** and **Integration Testing**

**Unit Testing** and **Integration Testing** are two different **levels of software testing** used to verify software quality during development. 

---

## 1️. Unit Testing

**Unit Testing** is the process of testing **individual components or functions of the software independently**.

👉 It focuses on **testing a single unit of code** such as a method, class, or function.

### Key Points

* Tests **smallest parts of code**
* Usually performed by **developers**
* Done **before integration testing**
* Helps detect **bugs early in development**

### Example (Java)

```java
public int add(int a, int b) {
    return a + b;
}
```

Unit test cases:

| Input    | Expected Output |
| -------- | --------------- |
| add(2,3) | 5               |
| add(5,7) | 12              |

Tools used:

* **JUnit**
* **TestNG**
* **NUnit**

---

## 2️. Integration Testing

**Integration Testing** verifies whether **multiple modules work correctly when combined together**. 

👉 It focuses on **interaction between different modules**.

### Key Points

* Tests **communication between components**
* Performed after **unit testing**
* Detects **interface or data flow issues**

### Example

Modules in a login system:

* Login module
* Database module

Integration testing checks:

| Module Interaction      | Expected Result             |
| ----------------------- | --------------------------- |
| Login sends credentials | Data reaches database       |
| Database verifies user  | Correct response returned   |
| System displays result  | Login success/error message |

---

## Unit Testing vs Integration Testing

| Feature       | Unit Testing                               | Integration Testing                 |
| ------------- | ------------------------------------------ | ----------------------------------- |
| Definition    | Testing individual components              | Testing interaction between modules |
| Focus         | Single unit of code                        | Multiple modules working together   |
| Performed By  | Developers                                 | Developers / Testers                |
| Testing Stage | First level of testing                     | After unit testing                  |
| Purpose       | Verify correctness of individual functions | Verify module communication         |
| Example       | Test `add()` function                      | Test login module + database        |



## Simple Real-World Example

### Unit Testing

Testing **engine separately** in a car.

### Integration Testing

Testing **engine + transmission + wheels working together**.



## Short Interview Answer

> **Unit Testing verifies individual components or functions of a program, while Integration Testing verifies that multiple modules work together correctly after they are integrated.**

---
---

# Levels of Testing Flow

```
Unit Testing → Integration Testing → System Testing → UAT
```

These are the **four main levels of software testing**, and each level checks the software from a different perspective to ensure quality. 


## 1️. Unit Testing

**Unit Testing** tests the **smallest part of the code (individual functions or methods)**.

**Performed by:** Developers

**Purpose:**
Verify that each unit of code works correctly.

**Example**

Testing a Java method:

```java
public int add(int a, int b){
    return a + b;
}
```

Test cases:

| Input    | Output |
| -------- | ------ |
| add(2,3) | 5      |
| add(5,7) | 12     |

**Tools**

* JUnit
* TestNG

---

## 2️. Integration Testing

**Integration Testing** checks whether **multiple modules work correctly when combined together**. 

**Performed by:** Developers / Testers

**Purpose:**
Verify **communication between modules**.

**Example**

Login system modules:

* Login module
* Database module

Integration testing verifies:

| Interaction             | Expected Result        |
| ----------------------- | ---------------------- |
| Login sends credentials | Database receives data |
| Database verifies user  | Response returned      |
| System shows result     | Login success/error    |

---

## 3️. System Testing

**System Testing** tests the **entire application as a complete system**. 

**Performed by:** QA / Testing Team

**Purpose:**
Ensure the **complete system works according to requirements**.

**Example (E-commerce system)**

Test end-to-end workflow:

* User registration
* Login
* Search product
* Add to cart
* Payment
* Order confirmation

---

## 4️. User Acceptance Testing (UAT)

**UAT** is the **final testing phase**, where **clients or end users validate the software** before release. 

**Performed by:** Client / End users / Business team

**Purpose:**
Ensure the system meets **business requirements**.

**Example**

Client verifies:

* User can register
* User can log in
* User can purchase product
* Payment works correctly

If everything works → **Product is approved for production**.



## 📊 Summary

| Level               | Tested By       | Focus                 |
| ------------------- | --------------- | --------------------- |
| Unit Testing        | Developers      | Individual functions  |
| Integration Testing | Dev/Testers     | Module interaction    |
| System Testing      | QA Team         | Complete system       |
| UAT                 | Clients / Users | Business requirements |



✅ **Interview One-Line Answer**

> **Software testing levels follow the order: Unit Testing → Integration Testing → System Testing → User Acceptance Testing (UAT), where testing progresses from individual components to the complete system and finally validation by end users.**

---
---

# What is **End-to-End (E2E) Testing?**

**End-to-End (E2E) Testing** is a testing approach where the **entire application workflow is tested from start to finish to ensure that all integrated components work together correctly in a real-world scenario**.

In simple terms:

> **End-to-End Testing verifies the complete user journey through the system from beginning to end.**

It checks whether the **system, databases, external services, and interfaces work together properly** as a full workflow.

## Example: E-Commerce Application

A typical **E2E test scenario** for an online shopping website may include:

| Step | Action                       | Expected Result              |
| ---- | ---------------------------- | ---------------------------- |
| 1    | User registers               | Account created successfully |
| 2    | User logs in                 | Login successful             |
| 3    | User searches product        | Product list displayed       |
| 4    | User adds product to cart    | Product added to cart        |
| 5    | User proceeds to checkout    | Checkout page loads          |
| 6    | User makes payment           | Payment processed            |
| 7    | Order confirmation displayed | Order placed successfully    |

This tests the **entire business flow**, not just individual modules.

## Why End-to-End Testing is Important

E2E testing helps ensure that:

1. **Complete system workflow works correctly**
2. **Integration between different modules is correct**
3. **External systems (APIs, databases, payment gateways) work properly**
4. The system behaves correctly **from the user’s perspective**



## Example: Banking Application

End-to-End test scenario:

1. User logs into banking app
2. User checks account balance
3. User transfers money
4. Transaction recorded in database
5. Confirmation message displayed

This verifies the **full business transaction flow**.



## Difference Between E2E Testing and Other Testing Types

| Testing Type        | Focus                         | Example                         |
| ------------------- | ----------------------------- | ------------------------------- |
| Unit Testing        | Individual component          | Test `add()` function           |
| Integration Testing | Interaction between modules   | Login module + database         |
| System Testing      | Entire system functionality   | Complete application testing    |
| End-to-End Testing  | Full user workflow            | Login → Search → Cart → Payment |
| UAT                 | Business validation by client | Client verifies real scenarios  |



## Simple Understanding

Imagine testing an **ATM machine**:

| Testing Type        | Example                                                |
| ------------------- | ------------------------------------------------------ |
| Unit Testing        | Test PIN validation function                           |
| Integration Testing | ATM machine + bank server communication                |
| System Testing      | Entire ATM system working                              |
| End-to-End Testing  | Insert card → Enter PIN → Withdraw money → Get receipt |


## Short Interview Answer

> **End-to-End (E2E) Testing is a testing approach that verifies the complete application workflow from start to finish to ensure that all integrated components, systems, and external services work together correctly.**

---
---

# Difference Between **System Testing** and **End-to-End (E2E) Testing**

Both **System Testing** and **End-to-End (E2E) Testing** verify the behavior of a complete application, but they differ in **scope, focus, and purpose**.

## 1. System Testing

**System Testing** is testing the **entire integrated application as a whole** to ensure it meets **functional and non-functional requirements**. 

### Key Points

* Tests the **complete system**
* Performed by **QA/Testers**
* Focuses on **requirements validation**
* Includes functional and non-functional tests

### Example (E-commerce system)

Testers verify:

* User registration
* Login functionality
* Product search
* Add to cart
* Payment module

The goal is to confirm that the **system works correctly according to requirements**.



## 2. End-to-End (E2E) Testing

**End-to-End Testing** verifies the **complete user workflow from start to finish**, including interactions with **external systems, databases, APIs, and services**. 

### Key Points

* Tests **real user journeys**
* Validates **full business workflows**
* Checks **integration with external systems**
* Simulates **real-world usage**

### Example (E-commerce workflow)

A complete E2E scenario:

1. User registers
2. User logs in
3. User searches product
4. User adds product to cart
5. User makes payment
6. Order confirmation displayed

This verifies the **complete customer journey**.


# 📊 System Testing vs End-to-End Testing

| Feature          | System Testing               | End-to-End (E2E) Testing           |
| ---------------- | ---------------------------- | ---------------------------------- |
| Purpose          | Validate the complete system | Validate full user workflow        |
| Focus            | System functionality         | Business process flow              |
| Scope            | Inside the application       | Across multiple systems            |
| External systems | Usually not included         | Included (APIs, DB, payment, etc.) |
| Example          | Test login module works      | Login → Search → Cart → Payment    |


## Simple Real-World Example

### System Testing (ATM system)

Tester checks:

* Card insertion
* PIN validation
* Balance check
* Cash withdrawal

### End-to-End Testing (ATM transaction)

Full user journey:

```
Insert Card → Enter PIN → Select Withdraw → Cash Dispensed → Receipt Printed
```

This tests the **entire transaction flow**.


## Interview-Ready Answer

> **System Testing verifies the complete application against system requirements, while End-to-End (E2E) Testing verifies the complete user workflow across the entire system, including external integrations, to ensure the business process works correctly.**

---
---

# What is **Exploratory Testing?**

**Exploratory Testing** is a testing approach where the **tester explores the application, learns its behavior, and designs test cases at the same time without predefined test cases or scripts**.

In simple terms:

> **Exploratory Testing = Testing the application by exploring it to discover defects.**

Instead of following written test cases, the tester **interacts with the system like a real user and investigates different scenarios**.

According to your notes, exploratory testing allows testers to **learn, design, and execute tests simultaneously**. 


## Key Characteristics

* No predefined test cases
* Testing and learning happen simultaneously
* Depends on **tester experience and creativity**
* Focuses on **discovering unexpected defects**



## Example: Login Page

A tester explores different scenarios on the login page.

| Action                            | Expected Result         |
| --------------------------------- | ----------------------- |
| Enter valid username and password | Login successful        |
| Enter wrong password              | Error message           |
| Leave fields empty                | Validation message      |
| Enter special characters          | Input handled correctly |

The tester keeps trying **different combinations while exploring the application**.



## Another Example: E-commerce Website

A tester explores the shopping flow:

1. Search for products
2. Add product to cart
3. Remove product from cart
4. Change product quantity
5. Proceed to checkout

While exploring, the tester may find issues like:

* Cart not updating correctly
* Payment page crashing
* Incorrect price calculation



## Advantages of Exploratory Testing

* Helps find **unexpected bugs**
* **Fast testing** without writing test cases
* Encourages **creative testing**
* Useful for **new or complex features**


## Limitations

* Difficult to **track test coverage**
* Depends heavily on **tester skill**
* Not suitable for **regression testing**



## Exploratory Testing vs Scripted Testing

| Feature       | Exploratory Testing  | Scripted Testing    |
| ------------- | -------------------- | ------------------- |
| Test cases    | Not predefined       | Predefined          |
| Approach      | Flexible             | Structured          |
| Focus         | Discover new defects | Verify requirements |
| Documentation | Minimal              | Detailed            |



## **Interview-Ready Answer**

> **Exploratory Testing is a testing approach where testers explore the application, learn its behavior, and design and execute test cases simultaneously without predefined scripts to discover defects.**

---
---
## What is **Ad-hoc Testing?**

**Ad-hoc Testing** is an **informal and unstructured testing technique** where testers test the application **randomly without any test cases, documentation, or planning**.

In simple terms:

> **Ad-hoc Testing = Random testing done without any predefined test cases.**

The main goal is to **find defects quickly by trying unusual or unexpected inputs**.


## Key Characteristics

* No test cases
* No documentation
* No planning
* Performed **randomly**
* Depends on **tester intuition and experience**



## Example: Login Page

A tester randomly tests the login page.

| Action                   | Expected Result                |
| ------------------------ | ------------------------------ |
| Enter username only      | Error message                  |
| Enter password only      | Validation message             |
| Enter special characters | System handles input correctly |
| Enter very long text     | Application should not crash   |

The tester **tries unusual combinations randomly** to find bugs.



## Example: E-commerce Website

Tester randomly performs actions:

1. Add 10 items to cart
2. Remove items quickly
3. Refresh page during checkout
4. Enter invalid coupon codes
5. Change quantity multiple times

This may reveal bugs like:

* Cart calculation errors
* Checkout page crashes
* Incorrect discount applied



## Advantages of Ad-hoc Testing

* Quickly finds **unexpected defects**
* No time needed to write test cases
* Good for **quick bug discovery**
* Useful when **time is limited**



## Limitations

* No documentation
* Difficult to **reproduce defects**
* No **test coverage tracking**
* Not suitable for **large projects**



## Ad-hoc Testing vs Exploratory Testing

| Feature       | Ad-hoc Testing    | Exploratory Testing   |
| ------------- | ----------------- | --------------------- |
| Structure     | Completely random | Semi-structured       |
| Planning      | No planning       | Some planning         |
| Documentation | None              | Minimal               |
| Approach      | Random testing    | Learn + design + test |



⭐ **Interview-Ready Answer**

> **Ad-hoc Testing is an informal testing technique where testers test the application randomly without predefined test cases or documentation in order to quickly find defects.**

---
---

# Difference Between **Exploratory Testing** and **Ad-hoc Testing**

Both **Exploratory Testing** and **Ad-hoc Testing** are **informal testing techniques**, but they differ in **structure, planning, and approach**.



## 1️. Exploratory Testing

**Exploratory Testing** is a **structured testing approach** where the tester **learns the application, designs test cases, and executes tests at the same time**.

👉 It is **planned but not scripted**.

### Key Points

* Some **planning exists**
* Tester **explores the application systematically**
* Learning, test design, and execution happen together
* Usually **documented**

### Example

Tester explores an **online shopping site**:

1. Search product
2. Filter products
3. Add to cart
4. Apply coupon
5. Checkout

Tester **carefully observes the system behavior** and records defects.


## 2️. Ad-hoc Testing

**Ad-hoc Testing** is **completely random testing** performed **without any planning, documentation, or test cases**.

👉 It is done **to quickly find defects**.

### Key Points

* **No planning**
* **No documentation**
* Completely **random testing**
* Done to **break the system quickly**

### Example

Tester randomly tries:

* Enter very long username
* Use special characters
* Refresh page during payment
* Click buttons rapidly

Goal: **Find bugs quickly**.


## 📊 Exploratory Testing vs Ad-hoc Testing

| Feature       | Exploratory Testing             | Ad-hoc Testing          |
| ------------- | ------------------------------- | ----------------------- |
| Structure     | Semi-structured                 | Completely unstructured |
| Planning      | Some planning exists            | No planning             |
| Documentation | Minimal documentation           | No documentation        |
| Approach      | Learn + Design + Test           | Random testing          |
| Purpose       | Understand system and find bugs | Quickly find defects    |



## 🧠 Simple Example

### Exploratory Testing

Tester **systematically explores features** of a banking app.

Example flow:

```
Login → Check Balance → Transfer Money → View Transaction
```

### Ad-hoc Testing

Tester randomly tries:

```
Wrong inputs → Refresh page → Multiple clicks → Invalid data
```



⭐ **Interview-Ready Answer**

> **Exploratory Testing is a structured approach where testers explore the application while learning and designing tests simultaneously, whereas Ad-hoc Testing is random testing performed without planning or documentation to quickly find defects.**

---
---

# What is **Usability Testing?**

**Usability Testing** is a type of testing that evaluates **how easy, user-friendly, and efficient a software application is for real users**.

In simple terms:

> **Usability Testing checks whether users can easily understand and use the application without confusion.**

It focuses on **user experience (UX)** and ensures the system is **simple, intuitive, and comfortable to use**.

## Example

Consider an **online shopping website**.

A usability test checks whether users can easily:

1. Register an account
2. Search for products
3. Add products to cart
4. Complete checkout

If users struggle to find buttons or navigation, the **design needs improvement**.

## Key Areas Tested in Usability Testing

1️⃣ **Ease of use**
Is the system easy for users to understand?

2️⃣ **Navigation**
Can users move between pages easily?

3️⃣ **Design clarity**
Are buttons, icons, and labels clear?

4️⃣ **User satisfaction**
Are users comfortable using the application?


## Example Issues Found in Usability Testing

| Problem              | Example                               |
| -------------------- | ------------------------------------- |
| Confusing navigation | Users cannot find the checkout button |
| Poor design          | Important buttons are hidden          |
| Complex workflow     | Too many steps to complete payment    |
| Slow interface       | Pages take too long to load           |


## Why Usability Testing is Important

### 1️⃣ Improves User Experience

Ensures users can **easily interact with the application**.

### 2️⃣ Increases Customer Satisfaction

A user-friendly application makes users **happy and comfortable**.

### 3️⃣ Reduces Training Time

If the system is easy to use, **users don't need training**.

### 4️⃣ Identifies Design Issues Early

Helps detect **UI/UX problems before release**.

### 5️⃣ Improves Product Success

Better usability leads to **more users and better business outcomes**.


## Real Example

### Bad Usability

A banking app requires **10 steps to transfer money**.

### Good Usability

Money transfer completed in **3 simple steps**.


⭐ **Interview-Ready Answer**

> **Usability Testing is a type of testing that evaluates how easy and user-friendly a software application is for end users. It ensures the system is simple to use, intuitive, and provides a good user experience.**

---
---












