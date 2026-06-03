# 1. Purpose of Test Documentation

**Test Documentation** refers to all the documents created during the **software testing process** to plan, execute, track, and report testing activities. These documents help ensure that testing is organized, repeatable, and aligned with project requirements. 

---

## Main Purposes of Test Documentation

### 1️. Provides Clear Testing Guidelines

Test documentation defines **how testing should be performed**, including the scope, strategy, and approach.

Example:
A **Test Plan** explains what modules will be tested and which tools will be used.

---

### 2️. Ensures Complete Test Coverage

Documentation helps ensure **all requirements are tested**.

Example:
Using **test cases and RTM (Requirement Traceability Matrix)** ensures every requirement has a corresponding test.

---

### 3️. Helps Track Testing Progress

Test documentation allows teams to monitor **testing status and results**.

Example:

* Number of test cases executed
* Passed / Failed test cases
* Open defects

---

### 4️. Improves Communication

Documentation acts as a **communication bridge between team members** such as:

* Testers
* Developers
* Project managers
* Clients

---

### 5️. Helps in Future Maintenance

Documentation can be reused for:

* Regression testing
* Future releases
* Knowledge transfer to new team members

---

### 6️. Provides Evidence of Testing

Test documentation serves as **proof that testing was performed properly** before releasing the software.

Example documents:

* Test Plan
* Test Cases
* Test Summary Report
* Bug Reports

---

## Common Test Documents

| Document                | Purpose                            |
| ----------------------- | ---------------------------------- |
| **Test Plan**           | Defines testing strategy and scope |
| **Test Case**           | Steps to test a feature            |
| **Test Scenario**       | High-level testing idea            |
| **Test Data**           | Input values for testing           |
| **Bug Report**          | Records defects                    |
| **Test Summary Report** | Final testing results              |

---

✅ **Short Interview Answer**

> **The purpose of test documentation is to plan, organize, and record testing activities so that testing is systematic, traceable, and ensures complete verification of software requirements.**

---

# 2. What is a Test Scenario?

A **Test Scenario** is a **high-level description of a functionality that needs to be tested** in a software application.

In simple terms:

> **A Test Scenario describes *what to test* in the application.**

It identifies possible ways a user might interact with the system to verify that the application works correctly. Software testing ensures that the system behaves as expected and meets user requirements. 

---

## Key Characteristics of a Test Scenario

* High-level testing concept
* Focuses on **functionality to be tested**
* Usually derived from **requirements or user stories**
* One test scenario can have **multiple test cases**

---

## Example: Login Page

### Test Scenario

**Verify login functionality**

### Possible Test Cases under this Scenario

| Test Case | Description                            |
| --------- | -------------------------------------- |
| TC_01     | Login with valid username and password |
| TC_02     | Login with invalid password            |
| TC_03     | Login with empty username              |
| TC_04     | Login with empty password              |

Here:

* **Test Scenario** → Login functionality
* **Test Cases** → Different ways to test login

---

## Example: E-Commerce Website

### Test Scenario

**Verify Add to Cart functionality**

Possible test cases:

* Add single product to cart
* Add multiple products to cart
* Remove product from cart
* Update product quantity

---

## Why Test Scenarios are Important

Test scenarios help to:

* Identify **important functionalities to test**
* Ensure **complete test coverage**
* Simplify **test planning**
* Provide a **high-level view of testing**

---

## Test Scenario vs Test Case

| Test Scenario             | Test Case                   |
| ------------------------- | --------------------------- |
| High-level testing idea   | Detailed testing steps      |
| Defines **what to test**  | Defines **how to test**     |
| Derived from requirements | Derived from test scenarios |

---

✅ **Short Interview Answer**

> **A Test Scenario is a high-level description of a functionality that needs to be tested in a software application. It defines what needs to be tested without detailing the specific test steps.**

---

# 3 What is a Test Case?

A **Test Case** is a **set of conditions, inputs, steps, and expected results** used to verify whether a particular functionality of a software application works correctly.

In simple terms:

> **A Test Case describes *how to test* a specific feature of the application.**

It provides detailed instructions that testers follow to validate software functionality and ensure it behaves as expected. 

---

## Components of a Test Case

A typical test case contains the following elements:

| Field               | Description                         |
| ------------------- | ----------------------------------- |
| **Test Case ID**    | Unique identifier for the test case |
| **Test Scenario**   | Feature being tested                |
| **Preconditions**   | Conditions before execution         |
| **Test Steps**      | Step-by-step actions                |
| **Test Data**       | Input values                        |
| **Expected Result** | Expected output                     |
| **Actual Result**   | Actual outcome after execution      |
| **Status**          | Pass / Fail                         |

---

## Example: Login Test Case

**Test Scenario:** Verify Login Functionality

| Step | Action               | Expected Result             |
| ---- | -------------------- | --------------------------- |
| 1    | Open login page      | Login page displayed        |
| 2    | Enter valid username | Username accepted           |
| 3    | Enter valid password | Password accepted           |
| 4    | Click Login          | User logged in successfully |

---

## Difference Between Test Case and Test Scenario

| Feature      | Test Scenario                    | Test Case              |
| ------------ | -------------------------------- | ---------------------- |
| Definition   | High-level functionality to test | Detailed steps to test |
| Focus        | **What to test**                 | **How to test**        |
| Detail Level | High-level                       | Detailed               |
| Created From | Requirements                     | Test scenarios         |
| Count        | Few scenarios                    | Many test cases        |

---

## Example

### Test Scenario

Verify **Login Functionality**

### Test Cases

1. Login with valid username and password
2. Login with invalid password
3. Login with empty username
4. Login with empty password

Here:

* **Test Scenario → Login functionality**
* **Test Cases → Different ways to test login**

---

✅ **Short Interview Answer**

> **A Test Case is a detailed set of steps, inputs, and expected results used to verify a specific functionality of a software application, while a Test Scenario is a high-level description of what needs to be tested.**

---


# 4. What is a Traceability Matrix (RTM)?

A **Traceability Matrix**, commonly called a **Requirement Traceability Matrix (RTM)**, is a document used in software testing to **map and track requirements with corresponding test cases**.

In simple terms:

> **RTM ensures that every requirement has at least one test case and that all requirements are properly tested.**

It helps maintain traceability between **requirements, test cases, and defects** throughout the testing process. RTM is often prepared during the **requirement analysis phase of STLC** to ensure complete test coverage. 

---

## Purpose of RTM

The main purpose of RTM is to ensure that:

* All **requirements are covered by test cases**
* No **requirement is missed during testing**
* Testing progress can be **tracked easily**
* Changes in requirements can be **managed effectively**

---

## Types of Traceability

There are mainly **three types of traceability**.

| Type                           | Description                        |
| ------------------------------ | ---------------------------------- |
| **Forward Traceability**       | Maps requirements → test cases     |
| **Backward Traceability**      | Maps test cases → requirements     |
| **Bidirectional Traceability** | Combines both forward and backward |

---

## Example of RTM

| Requirement ID | Requirement Description  | Test Case ID | Status |
| -------------- | ------------------------ | ------------ | ------ |
| REQ_01         | User login functionality | TC_01, TC_02 | Pass   |
| REQ_02         | Password validation      | TC_03        | Pass   |
| REQ_03         | Forgot password feature  | TC_04        | Fail   |

This table shows which **test cases validate which requirements**.

---

## Why RTM is Important

RTM is important because it:

1. Ensures **complete requirement coverage**
2. Helps **track testing progress**
3. Prevents **missing test cases**
4. Helps analyze **impact of requirement changes**
5. Improves **quality assurance and documentation**

Documentation like RTM helps organize and track testing activities to ensure systematic verification of software requirements. 

---

## Simple Example

Requirement:

> User should be able to **login using username and password**

RTM mapping:

| Requirement         | Test Case              |
| ------------------- | ---------------------- |
| Login functionality | TC_01 Valid login      |
| Login functionality | TC_02 Invalid password |
| Login functionality | TC_03 Empty fields     |

This confirms that **all login requirements are tested**.

---

✅ **Short Interview Answer**

> **A Requirement Traceability Matrix (RTM) is a document that maps requirements with test cases to ensure that all requirements are covered during testing and nothing is missed.**

---

# 5. What is a Bug / Defect in Software Testing?

A **Bug** or **Defect** is an **error, flaw, or unexpected behavior in a software application that causes it to produce incorrect or unexpected results**.

In simple terms:

> **A Bug/Defect is a problem in the software that makes it behave differently from the expected result.**

Software testing is mainly performed to **identify and report these defects so they can be fixed before the product is released.** 

---

## Example

### Expected Behavior

User enters **valid username and password** → Login should be successful.

### Actual Behavior

User enters **valid credentials** → Application shows **error message**.

This difference between **expected result and actual result** is called a **Bug/Defect**.

---

## Real-World Example

Testing a **Login Page**:

| Test Input                | Expected Result  | Actual Result           | Bug? |
| ------------------------- | ---------------- | ----------------------- | ---- |
| Valid username & password | Login successful | Error message displayed | Yes  |
| Wrong password            | Error message    | Error message           | No   |

If the **actual result ≠ expected result**, it is considered a **defect**.

---

## Common Causes of Bugs

Bugs can occur due to:

* Incorrect **coding**
* Misunderstood **requirements**
* Design errors
* Integration issues
* Environment problems

---

## Example Bug Report Fields

When testers find a bug, they usually report it with details such as:

| Field              | Description                  |
| ------------------ | ---------------------------- |
| Bug ID             | Unique identifier            |
| Summary            | Short description of the bug |
| Steps to Reproduce | Steps to recreate the issue  |
| Expected Result    | Correct behavior             |
| Actual Result      | What actually happened       |
| Severity           | Impact of the bug            |
| Priority           | Urgency to fix               |

---

## Example Bug

**Bug Title:** Login button not working

**Steps:**

1. Open login page
2. Enter username and password
3. Click login button

**Expected Result:** User should login successfully

**Actual Result:** Nothing happens after clicking login.

---

✅ **Short Interview Answer**

> **A Bug or Defect is an error or flaw in a software application where the actual result differs from the expected result.**

---

# 6. Explain the Defect Life Cycle (Bug Life Cycle)

The **Defect Life Cycle**, also called the **Bug Life Cycle**, is the **process through which a defect goes from the moment it is discovered until it is fixed and closed**.

In simple terms:

> **The Defect Life Cycle describes the different stages a bug goes through during the testing process.**

During software testing, testers identify defects and report them so that developers can fix them before the software is released. 

---

## Stages of the Defect Life Cycle

```text
New
↓
Assigned
↓
Open
↓
Fixed
↓
Retest
↓
Closed
```

Sometimes additional states are used such as **Rejected, Deferred, Duplicate, or Reopened**.

---

## 1️⃣ New

* When the tester **identifies a defect**, it is logged in the bug tracking tool.
* Status of the bug is **New**.

Example:
Tester finds that **login button is not working**.

---

## 2️⃣ Assigned

* The defect is **assigned to a developer** by the test lead or manager.

Example:
Bug assigned to **Developer A**.

---

## 3️⃣ Open

* The developer **starts analyzing and fixing the defect**.

---

## 4️⃣ Fixed

* The developer **fixes the defect** and updates the status to **Fixed**.
* The bug is sent back to the **testing team for verification**.

---

## 5️⃣ Retest

* The tester **retests the application** to verify whether the defect is fixed.

If the issue is resolved → move to **Closed**.

If the issue still exists → **Reopened**.

---

## 6️⃣ Closed

* If the defect is fixed successfully, the tester marks the defect as **Closed**.

---

## Additional Defect Status

Sometimes defects may have other statuses.

| Status    | Meaning                               |
| --------- | ------------------------------------- |
| Rejected  | Developer says it is not a bug        |
| Deferred  | Bug will be fixed in a future release |
| Duplicate | Bug already reported earlier          |
| Reopened  | Bug still exists after fixing         |

---

## Example

Bug found: **Login button not working**

| Stage    | Action                       |
| -------- | ---------------------------- |
| New      | Tester logs the bug          |
| Assigned | Manager assigns to developer |
| Open     | Developer analyzes bug       |
| Fixed    | Developer fixes the issue    |
| Retest   | Tester verifies the fix      |
| Closed   | Bug resolved                 |

---

✅ **Short Interview Answer**

> **The Defect Life Cycle is the process through which a bug goes from identification to closure, including stages like New, Assigned, Open, Fixed, Retest, and Closed.**

---




# 7. What is Defect Severity vs Priority?

When a defect (bug) is found in software testing, it is categorized using **Severity** and **Priority** to determine **how serious the defect is and how urgently it should be fixed**. 

---

## 1 Defect Severity

**Severity** refers to **the impact of the defect on the system functionality**.

👉 It shows **how serious the bug is technically**.

### Determined By

👩‍💻 **Tester / QA team**

### Severity Levels

| Level    | Description                                 |
| -------- | ------------------------------------------- |
| Critical | System crash or major functionality failure |
| High     | Important feature not working               |
| Medium   | Function works but with issues              |
| Low      | Minor UI or cosmetic issue                  |

### Example

**Bug:** Application crashes when clicking the **Pay Now** button.

* Severity → **Critical**
  (Because the main functionality is broken)

---

## 2 Defect Priority

**Priority** refers to **how quickly the defect should be fixed**.

👉 It indicates the **urgency of fixing the defect**.

### Determined By

👨‍💼 **Project Manager / Product Owner**

### Priority Levels

| Level  | Description               |
| ------ | ------------------------- |
| High   | Must be fixed immediately |
| Medium | Fix in next release       |
| Low    | Can be fixed later        |

### Example

**Bug:** Logo alignment issue on homepage.

* Severity → **Low**
* Priority → **High** (client wants it fixed quickly)

---

## Severity vs Priority

| Feature    | Severity                                     | Priority                     |
| ---------- | -------------------------------------------- | ---------------------------- |
| Definition | Impact of the defect on system functionality | Urgency of fixing the defect |
| Focus      | Technical impact                             | Business importance          |
| Decided By | Tester                                       | Manager/Product Owner        |
| Concern    | System functionality                         | Release schedule             |

---

## Example Scenarios

| Bug                | Severity | Priority |
| ------------------ | -------- | -------- |
| Application crash  | Critical | High     |
| Login not working  | High     | High     |
| Spelling mistake   | Low      | Low      |
| UI alignment issue | Low      | High     |

---

⭐ Short Interview Answer

> **Severity indicates how serious a defect is in terms of system impact, while Priority indicates how urgently the defect should be fixed. Severity is decided by testers, and Priority is decided by project managers or product owners.**

---

# 8 How do you write a good Bug Report?

A **Bug Report** is a document used by testers to **report defects found in a software application** so that developers can reproduce and fix them. A clear bug report helps developers understand the issue quickly and resolve it efficiently. 

---

## Characteristics of a Good Bug Report

A good bug report should be:

* **Clear** – Easy to understand
* **Accurate** – Correct information about the issue
* **Detailed** – Includes steps and environment details
* **Reproducible** – Developers should be able to reproduce the issue

---

## Important Fields in a Bug Report

| Field                  | Description                                       |
| ---------------------- | ------------------------------------------------- |
| **Bug ID**             | Unique identifier of the bug                      |
| **Title / Summary**    | Short description of the issue                    |
| **Environment**        | OS, browser, application version                  |
| **Steps to Reproduce** | Step-by-step actions to reproduce the bug         |
| **Expected Result**    | What should happen                                |
| **Actual Result**      | What actually happened                            |
| **Severity**           | Impact of the bug                                 |
| **Priority**           | Urgency of fixing the bug                         |
| **Status**             | Current state of the bug (New, Open, Fixed, etc.) |
| **Attachments**        | Screenshots or logs                               |

---

## Example Bug Report

**Bug ID:** BUG_101

**Title:** Login button not working

**Environment:**

* OS: Windows 11
* Browser: Chrome 120
* Application Version: v2.1

**Steps to Reproduce:**

1. Open the login page
2. Enter valid username and password
3. Click the **Login** button

**Expected Result:**
User should successfully log in to the application.

**Actual Result:**
Nothing happens after clicking the login button.

**Severity:** High
**Priority:** High

---

## Best Practices for Writing a Bug Report

✔ Use a **clear and descriptive title**
✔ Provide **exact steps to reproduce**
✔ Include **screenshots or logs**
✔ Mention **environment details**
✔ Avoid **ambiguous or vague descriptions**

Example of a **bad title**:
❌ *Login issue*

Example of a **good title**:
✅ *Login button does not respond when valid credentials are entered*

---

 ⭐ Short Interview Answer

> **A good bug report should clearly describe the defect, include steps to reproduce, expected and actual results, environment details, severity, and priority so that developers can easily reproduce and fix the issue.**

---

## 9 What are Entry and Exit Criteria in Testing?

**Entry Criteria** and **Exit Criteria** are the **conditions that must be satisfied before starting and after completing a testing phase**. They help ensure testing activities are performed in a controlled and structured way within the testing process. 

---

## 1️ Entry Criteria

**Entry Criteria** are the **conditions that must be met before the testing process begins**.

They ensure that the **test team is ready to start testing**.

### Examples of Entry Criteria

* Requirements are **clearly defined and approved**
* **Test plan and test cases** are prepared
* **Test environment** is ready
* Application build is **stable**
* Test data is available

### Example

Before testing a **login module**, ensure:

* Login functionality is developed
* Test cases for login are written
* QA environment is ready

Only after these conditions are met → **testing can start**.

---

## 2 Exit Criteria

**Exit Criteria** are the **conditions that must be satisfied before testing is considered complete**.

They ensure the **software meets the required quality standards before release**.

### Examples of Exit Criteria

* All **test cases are executed**
* **Critical and high severity defects are fixed**
* **Test coverage is achieved**
* No **open critical defects**
* Test summary report is prepared

### Example

Testing can be completed when:

* 95% test cases passed
* All critical bugs fixed
* Client approval obtained

---

## Entry Criteria vs Exit Criteria

| Feature    | Entry Criteria              | Exit Criteria                            |
| ---------- | --------------------------- | ---------------------------------------- |
| Definition | Conditions to start testing | Conditions to stop testing               |
| Purpose    | Ensure testing can begin    | Ensure testing is completed successfully |
| Timing     | Before testing              | After testing                            |
| Example    | Test environment ready      | All test cases executed                  |

---

## Simple Example

Testing a **bank login system**.

**Entry Criteria**

* Login module developed
* Test cases prepared
* QA environment ready

**Exit Criteria**

* All login test cases executed
* No critical defects remaining
* Testing report prepared

---

## Short Interview Answer

> **Entry Criteria are the conditions that must be met before testing begins, while Exit Criteria are the conditions that must be satisfied before testing can be completed or stopped.**

---

# 10 What is a Test Summary Report?

A **Test Summary Report (TSR)** is a **document prepared at the end of the testing phase** that summarizes the **overall testing activities, results, and quality status of the application**.

It provides a **high-level overview of testing outcomes**, including the number of test cases executed, defects found, and the readiness of the product for release. 

---

## Purpose of a Test Summary Report

The main purpose of a Test Summary Report is to:

* Provide a **summary of testing activities**
* Show **test execution results**
* Report **defects identified during testing**
* Evaluate whether the **software is ready for release**
* Communicate **testing results to stakeholders**

---

## Contents of a Test Summary Report

A typical Test Summary Report contains the following sections:

| Section                    | Description                                 |
| -------------------------- | ------------------------------------------- |
| **Project Information**    | Project name, build version, testing period |
| **Testing Scope**          | Modules or features tested                  |
| **Test Execution Summary** | Total test cases executed, passed, failed   |
| **Defect Summary**         | Number of defects found and their severity  |
| **Test Environment**       | Hardware and software used for testing      |
| **Risks / Issues**         | Known limitations or unresolved issues      |
| **Test Conclusion**        | Final decision about product readiness      |

---

## Example Test Summary

| Metric           | Result |
| ---------------- | ------ |
| Total Test Cases | 120    |
| Executed         | 118    |
| Passed           | 110    |
| Failed           | 8      |
| Blocked          | 2      |
| Critical Defects | 0      |
| High Defects     | 2      |
| Medium Defects   | 5      |
| Low Defects      | 3      |

---

## Simple Example

Testing an **E-commerce application**.

The Test Summary Report might include:

* Login module tested
* Payment module tested
* 95% test cases passed
* All critical defects fixed

Conclusion → **Application ready for release.**

---

## Short Interview Answer

> **A Test Summary Report is a document prepared after testing that summarizes the testing activities, test results, defects found, and the overall quality status of the software.**

---

# 11. Types of Test Documentation

**Test Documentation** includes all the documents created during the **software testing process** to plan, execute, track, and report testing activities. These documents help ensure testing is organized, traceable, and aligned with requirements. 

---

### Common Types of Test Documentation

## 1️⃣ Test Plan

A **Test Plan** describes the **overall strategy, scope, objectives, schedule, and resources required for testing**.

**Key contents**

* Testing scope
* Testing strategy
* Test environment
* Roles and responsibilities
* Entry and exit criteria

---

## 2️⃣ Test Strategy

A **Test Strategy** is a **high-level document that defines the overall testing approach** for the organization or project.

**Includes**

* Testing types to be performed
* Testing tools used
* Test environment strategy
* Risk management

---

## 3️⃣ Test Scenario

A **Test Scenario** is a **high-level description of what functionality needs to be tested**.

Example:

* Verify login functionality
* Verify payment process

A single scenario can contain multiple test cases. 

---

## 4️⃣ Test Case

A **Test Case** is a **detailed set of steps, inputs, and expected results used to verify a specific functionality**.

**Typical fields**

* Test Case ID
* Test steps
* Test data
* Expected result
* Actual result
* Status

Test cases explain **how to test a feature**. 

---

## 5️⃣ Test Data

**Test Data** is the **input data used during testing**.

Examples:

* Username and password
* Payment details
* Product IDs

---

## 6️⃣ Requirement Traceability Matrix (RTM)

An **RTM** maps **requirements to corresponding test cases** to ensure every requirement is tested.

Purpose:

* Ensure complete requirement coverage
* Track testing progress
* Identify missing test cases 

---

## 7️⃣ Bug Report (Defect Report)

A **Bug Report** documents **defects found during testing** so developers can reproduce and fix them.

Typical fields:

* Bug ID
* Steps to reproduce
* Expected result
* Actual result
* Severity and priority 

---

## 8️⃣ Test Summary Report

A **Test Summary Report** is prepared **after testing is completed** and summarizes testing activities, results, and defects found. 

---

# 📊 Summary Table

| Document            | Purpose                            |
| ------------------- | ---------------------------------- |
| Test Plan           | Defines testing scope and strategy |
| Test Strategy       | High-level testing approach        |
| Test Scenario       | High-level functionality to test   |
| Test Case           | Detailed testing steps             |
| Test Data           | Input data used for testing        |
| RTM                 | Maps requirements to test cases    |
| Bug Report          | Records defects                    |
| Test Summary Report | Final testing report               |

---

✅ **Short Interview Answer**

> **The main types of test documentation include Test Plan, Test Strategy, Test Scenario, Test Case, Test Data, Requirement Traceability Matrix (RTM), Bug Report, and Test Summary Report. These documents help plan, execute, track, and report testing activities.**

---

# 12. Difference Between **Test Plan** and **Test Strategy**

Both **Test Plan** and **Test Strategy** are important documents in software testing, but they serve different purposes in the testing process. 

---

## Test Plan vs Test Strategy

| Feature     | **Test Plan**                                                                     | **Test Strategy**                                                                        |
| ----------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Definition  | A document that describes **how testing will be executed for a specific project** | A document that defines the **overall testing approach for the organization or project** |
| Level       | **Project-level document**                                                        | **High-level organizational document**                                                   |
| Prepared By | Test Lead / QA Lead                                                               | Test Manager / Senior Management                                                         |
| Focus       | Details of testing activities                                                     | Overall testing methodology                                                              |
| Contents    | Scope, schedule, resources, environment                                           | Testing types, tools, standards                                                          |
| Changes     | Can change during the project                                                     | Usually stable and rarely changed                                                        |

---

## Simple Explanation

### Test Strategy

* Defines the **overall testing approach**
* Explains **which testing types and tools will be used**

Example:

* Functional testing
* Automation testing
* Performance testing

---

### Test Plan

* Explains **how the strategy will be implemented for a specific project**

Example contents:

* What modules to test
* Who will test
* Test schedule
* Test environment

---

## Example

### Test Strategy (Organization Level)

Testing approach for all projects:

* Use **Selenium for automation**
* Follow **Agile testing**
* Perform **functional + regression testing**

---

### Test Plan (Project Level)

Project: **Online Banking System**

* Module tested → Login, Payment, Account
* Test environment → Chrome, Windows
* Team → 3 QA Engineers
* Timeline → 2 weeks testing

---

## Short Interview Answer

> **Test Strategy defines the overall testing approach and standards for testing, while a Test Plan describes how testing will be executed for a specific project, including scope, resources, and schedule.**

---

# 13. Difference Between **Test Scenario** and **Test Case**

In software testing, **Test Scenario** and **Test Case** are both used to verify application functionality, but they differ in **level of detail and purpose**. 

---

## Test Scenario vs Test Case

| Feature      | **Test Scenario**                      | **Test Case**                    |
| ------------ | -------------------------------------- | -------------------------------- |
| Definition   | High-level description of what to test | Detailed steps to test a feature |
| Focus        | **What to test**                       | **How to test**                  |
| Detail Level | General idea                           | Step-by-step instructions        |
| Source       | Derived from requirements/user stories | Derived from test scenarios      |
| Number       | Few scenarios                          | Multiple test cases per scenario |

---

## Simple Explanation

### Test Scenario

A **Test Scenario** describes the **functionality to be tested** at a high level.

Example:

* Verify login functionality
* Verify payment process
* Verify search feature

One scenario can contain **multiple test cases**. 

---

### Test Case

A **Test Case** provides **detailed steps, inputs, and expected results** to validate the scenario.

Example fields:

* Test Case ID
* Test Steps
* Test Data
* Expected Result
* Actual Result
* Status (Pass/Fail)

It explains **how to test the functionality**. 

---

## Example (Login Module)

### Test Scenario

**Verify Login Functionality**

### Test Cases under this Scenario

| Test Case | Description                            |
| --------- | -------------------------------------- |
| TC_01     | Login with valid username and password |
| TC_02     | Login with invalid password            |
| TC_03     | Login with empty username              |
| TC_04     | Login with empty password              |

Here:

* **Scenario → Login functionality**
* **Test Cases → Different ways to test login**

---

## Short Interview Answer

> **A Test Scenario is a high-level description of what functionality needs to be tested, while a Test Case is a detailed set of steps, inputs, and expected results that describe how to test that functionality.**

---

# 14. Components of a Good Test Case

A **Test Case** is a detailed document that defines the **conditions, steps, and expected results** used to verify whether a specific feature of a software application works correctly. 

A well-written test case ensures **clarity, repeatability, and complete test coverage**.

---

## Main Components of a Good Test Case

| Component            | Description                                        |
| -------------------- | -------------------------------------------------- |
| **Test Case ID**     | Unique identifier for the test case                |
| **Test Scenario**    | High-level functionality being tested              |
| **Preconditions**    | Conditions that must be satisfied before execution |
| **Test Steps**       | Step-by-step instructions to perform the test      |
| **Test Data**        | Input values used for testing                      |
| **Expected Result**  | Expected outcome of the test                       |
| **Actual Result**    | Actual outcome after executing the test            |
| **Status**           | Pass / Fail result                                 |
| **Postconditions**   | System state after test execution                  |
| **Comments / Notes** | Additional observations or details                 |

These components help testers **execute tests consistently and track results effectively**. 

---

## Example Test Case (Login Functionality)

| Field           | Example                                                                        |
| --------------- | ------------------------------------------------------------------------------ |
| Test Case ID    | TC_LOGIN_01                                                                    |
| Test Scenario   | Verify login functionality                                                     |
| Preconditions   | User account must exist                                                        |
| Test Steps      | 1. Open login page<br>2. Enter username<br>3. Enter password<br>4. Click Login |
| Test Data       | Username: user123<br>Password: pass123                                         |
| Expected Result | User should successfully login                                                 |
| Actual Result   | User logged in successfully                                                    |
| Status          | Pass                                                                           |

---

## Characteristics of a Good Test Case

A good test case should be:

* **Clear and easy to understand**
* **Reusable**
* **Independent of other test cases**
* **Accurate and detailed**
* **Traceable to requirements**

---

## Short Interview Answer

> **The main components of a good test case include Test Case ID, Test Scenario, Preconditions, Test Steps, Test Data, Expected Result, Actual Result, and Status. These elements help testers clearly define and execute tests to verify software functionality.**

---








