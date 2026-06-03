# 1. What are **Test Design Techniques?**

**Test Design Techniques** are **methods used to create effective test cases from requirements** so that testing covers maximum functionality with minimum test cases.

In simple terms:

> **Test Design Techniques help testers decide *how to design test cases* to find defects efficiently.**

They help testers:

* Reduce the **number of test cases**
* Improve **test coverage**
* Identify **edge cases and defects**
* Ensure **systematic testing**

These techniques are used mainly during the **Test Case Design phase of the Software Testing Life Cycle (STLC)** when testers create test cases based on requirements. 

 

## Types of Test Design Techniques

Test design techniques are mainly divided into **three categories**.

| Category                        | Description                                      |
| ------------------------------- | ------------------------------------------------ |
| **Black Box Techniques**        | Test based on functionality without knowing code |
| **White Box Techniques**        | Test based on internal code structure            |
| **Experience-Based Techniques** | Test based on tester experience                  |

 

## 1. Black Box Test Design Techniques

In **Black Box Testing**, testers focus on **input and output without looking at the internal code**.

Common techniques:

### Equivalence Partitioning (EP)

Divide input data into **valid and invalid groups**.

Example:
Age field allowed **18–60**

Partitions:

* 18–60 → Valid
* <18 → Invalid
* > 60 → Invalid

Instead of testing all values, testers test **one value from each partition**.

 

### Boundary Value Analysis (BVA)

Test the **boundary values** of input ranges.

Example:

Age range: **18–60**

Test values:

* 17 (below boundary)
* 18 (minimum)
* 19 (above minimum)
* 59 (below maximum)
* 60 (maximum)
* 61 (above maximum)

Boundary values often contain **more defects**.

 

### Decision Table Testing

Used when **multiple conditions affect the result**.

Example: Login system

| Username | Password | Result        |
| -------- | -------- | ------------- |
| Valid    | Valid    | Login success |
| Valid    | Invalid  | Error         |
| Invalid  | Valid    | Error         |
| Invalid  | Invalid  | Error         |



### State Transition Testing

Used when the system behavior **changes based on state**.

Example: ATM PIN

| State                   | Action       |
| ----------------------- | ------------ |
| Enter wrong PIN 3 times | Card blocked |


## 2  White Box Test Design Techniques

White Box testing focuses on **internal code logic**.

Performed mostly by **developers**.

Examples:

* **Statement Coverage** – execute every statement
* **Branch Coverage** – execute all branches (if/else)
* **Path Coverage** – execute all possible paths

Example:

```java
if (age >= 18) {
   System.out.println("Eligible");
} else {
   System.out.println("Not Eligible");
}
```

White box testing ensures both **if and else conditions** are tested.



## 3 Experience-Based Techniques

These techniques depend on **tester knowledge and experience**.

### Exploratory Testing

Tester explores the application **without predefined test cases**.

### Error Guessing

Tester guesses possible errors based on experience.

Example:

* Empty fields
* Special characters
* Very long input values



## Summary of Test Design Techniques

| Technique Type   | Techniques                                                        |
| ---------------- | ----------------------------------------------------------------- |
| Black Box        | Equivalence Partitioning, Boundary Value Analysis, Decision Table |
| White Box        | Statement Coverage, Branch Coverage                               |
| Experience-Based | Exploratory Testing, Error Guessing                               |


## Short Interview Answer

> **Test Design Techniques are methods used to design effective test cases from requirements. Common techniques include Equivalence Partitioning, Boundary Value Analysis, Decision Table Testing, and State Transition Testing. These techniques help improve test coverage and detect defects efficiently.**

---

# 2. What is **Equivalence Partitioning (EP)?**

**Equivalence Partitioning (EP)** is a **test design technique** used in software testing where **input data is divided into groups (partitions)** that are expected to behave in the same way.

Instead of testing **every possible input value**, the tester selects **one representative value from each group**.

👉 The idea is:

> **If one value in a partition works correctly, all values in that partition are assumed to work correctly.**

This technique helps **reduce the number of test cases while maintaining good test coverage**. 



## Key Idea of Equivalence Partitioning

Input data is divided into:

* **Valid partitions** → acceptable inputs
* **Invalid partitions** → unacceptable inputs

The tester selects **one value from each partition** for testing.



## Example: Age Field Validation

Requirement:

> User age must be between **18 and 60**.

### Step 1: Identify Partitions

| Partition Type    | Input Range |
| ----------------- | ----------- |
| Invalid Partition | Age < 18    |
| Valid Partition   | Age 18 – 60 |
| Invalid Partition | Age > 60    |



### Step 2: Select Test Values

| Test Case | Input Age | Expected Result |
| --------- | --------- | --------------- |
| TC1       | 15        | Rejected        |
| TC2       | 30        | Accepted        |
| TC3       | 65        | Rejected        |

Here:

* **15** represents the partition **<18**
* **30** represents the partition **18–60**
* **65** represents the partition **>60**

Instead of testing **every age value**, we test **one value from each partition**.


## Another Example: Password Length

Requirement:

> Password length must be **6–12 characters**.

### Partitions

| Partition | Input       |
| --------- | ----------- |
| Invalid   | Length < 6  |
| Valid     | Length 6–12 |
| Invalid   | Length > 12 |

### Test Cases

| Test Case | Password Length | Expected Result |
| --------- | --------------- | --------------- |
| TC1       | 4               | Invalid         |
| TC2       | 8               | Valid           |
| TC3       | 15              | Invalid         |


# Advantages of Equivalence Partitioning

* Reduces **number of test cases**
* Saves **testing time**
* Provides **good test coverage**
* Helps identify **invalid input conditions**



## Short Interview Answer

> **Equivalence Partitioning is a test design technique where input data is divided into valid and invalid partitions, and one representative value from each partition is tested instead of testing all possible values.**

---

# 3️. What is **Boundary Value Analysis (BVA)?**

**Boundary Value Analysis (BVA)** is a **test design technique** used to test the **boundary (edge) values of input ranges**.

The idea behind BVA is:

> **Errors are more likely to occur at the boundaries of input values rather than in the middle.**

So testers focus on **minimum, maximum, and values just inside and outside the boundary** to detect defects. 



## Key Idea of BVA

When a range is given:

```
Minimum Value ----- Valid Range ----- Maximum Value
```

Test these values:

1. **Below the minimum**
2. **Minimum value**
3. **Just above minimum**
4. **Just below maximum**
5. **Maximum value**
6. **Above maximum**


## Example: Age Validation

Requirement:

> User age must be between **18 and 60**.

### Boundary Values

| Test Case | Input Age | Expected Result            |
| --------- | --------- | -------------------------- |
| TC1       | 17        | Invalid (below minimum)    |
| TC2       | 18        | Valid (minimum boundary)   |
| TC3       | 19        | Valid (just above minimum) |
| TC4       | 59        | Valid (just below maximum) |
| TC5       | 60        | Valid (maximum boundary)   |
| TC6       | 61        | Invalid (above maximum)    |

These values test the **edges of the range**, where bugs commonly occur.



## Another Example: Password Length

Requirement:

> Password must be **6–12 characters**.

### Boundary Values

| Test Case | Length | Expected Result |
| --------- | ------ | --------------- |
| TC1       | 5      | Invalid         |
| TC2       | 6      | Valid           |
| TC3       | 7      | Valid           |
| TC4       | 11     | Valid           |
| TC5       | 12     | Valid           |
| TC6       | 13     | Invalid         |

Here we test the **boundaries 6 and 12**.



## Advantages of Boundary Value Analysis

* Detects **edge-case defects**
* Improves **test coverage**
* Reduces **number of test cases**
* Very effective for **input validation testing**



## Equivalence Partitioning vs Boundary Value Analysis

| Feature | Equivalence Partitioning      | Boundary Value Analysis            |
| ------- | ----------------------------- | ---------------------------------- |
| Focus   | Test groups of input data     | Test boundary values               |
| Purpose | Reduce test cases             | Detect edge defects                |
| Example | One value from each partition | Test min, max, and near boundaries |



## Short Interview Answer

> **Boundary Value Analysis (BVA) is a test design technique that focuses on testing the boundary values of input ranges, such as minimum, maximum, and values just inside or outside the boundaries, because defects often occur at these points.**

---

# 4️ What is **Decision Table Testing?**

**Decision Table Testing** is a **black-box test design technique** used when the **system behavior depends on multiple input conditions**.

It uses a **table format** to represent different combinations of conditions and their corresponding actions or results.

> **Decision Table Testing helps testers verify all possible combinations of inputs and outputs.** 



## Why Decision Table Testing is Used

It is useful when:

* The system has **multiple conditions**
* Each condition can lead to **different results**
* The logic is **complex**

Instead of writing many test cases randomly, testers create a **decision table to organize them clearly**.



## Structure of a Decision Table

A decision table usually has **four parts**:

| Part             | Description                          |
| ---------------- | ------------------------------------ |
| Conditions       | Input conditions                     |
| Condition Values | True/False or Valid/Invalid          |
| Actions          | Expected system behavior             |
| Rules            | Different combinations of conditions |



## Example: Login System

Requirement:

User can log in only when **username and password are correct**.

| Rule | Username | Password | Result           |
| ---- | -------- | -------- | ---------------- |
| 1    | Valid    | Valid    | Login successful |
| 2    | Valid    | Invalid  | Error message    |
| 3    | Invalid  | Valid    | Error message    |
| 4    | Invalid  | Invalid  | Error message    |



## Derived Test Cases

From the decision table we create test cases:

| Test Case | Username | Password | Expected Result  |
| --------- | -------- | -------- | ---------------- |
| TC1       | Valid    | Valid    | Login successful |
| TC2       | Valid    | Invalid  | Error message    |
| TC3       | Invalid  | Valid    | Error message    |
| TC4       | Invalid  | Invalid  | Error message    |

This ensures **all possible input combinations are tested**.



## Another Example: Online Payment

Conditions:

* Card valid
* Sufficient balance

| Rule | Card Valid | Balance Available | Result             |
| ---- | ---------- | ----------------- | ------------------ |
| 1    | Yes        | Yes               | Payment successful |
| 2    | Yes        | No                | Payment failed     |
| 3    | No         | Yes               | Payment failed     |
| 4    | No         | No                | Payment failed     |



## Advantages of Decision Table Testing

* Handles **complex business rules**
* Ensures **all combinations are tested**
* Improves **test coverage**
* Easy to **understand and maintain**



## Short Interview Answer

> **Decision Table Testing is a test design technique used to test different combinations of input conditions and their corresponding outcomes using a table format. It is useful when system behavior depends on multiple conditions.**

---

# 5️. What is **State Transition Testing?**

**State Transition Testing** is a **test design technique used to verify how a system behaves when it moves from one state to another based on specific events or inputs.**

In simple terms:

> **State Transition Testing checks how the system changes from one condition (state) to another when a user performs an action.**

It is useful when the system behavior depends on **previous actions or states**. 



## Key Idea

A **state** represents the condition of the system at a given time.

When an **event or action occurs**, the system moves to another state.

```
Current State → Event → Next State
```



## Example: ATM PIN Validation

Requirement:

* User can enter **PIN only 3 times**.
* If the PIN is wrong **3 times**, the **card gets blocked**.

### States

| Current State | Event                      | Next State     |
| ------------- | -------------------------- | -------------- |
| Card inserted | Enter correct PIN          | Access granted |
| Card inserted | Enter wrong PIN (1st time) | Try again      |
| Try again     | Enter wrong PIN (2nd time) | Try again      |
| Try again     | Enter wrong PIN (3rd time) | Card blocked   |



## State Transition Diagram (Concept)

```
Start
  ↓
Insert Card
  ↓
Enter PIN
   ├── Correct PIN → Access Account
   └── Wrong PIN
          ↓
       Try Again
          ↓
   3 Wrong Attempts → Card Blocked
```



## Derived Test Cases

| Test Case | Input                            | Expected Result |
| --------- | -------------------------------- | --------------- |
| TC1       | Correct PIN first time           | Access granted  |
| TC2       | Wrong PIN twice then correct PIN | Access granted  |
| TC3       | Wrong PIN three times            | Card blocked    |



## Another Example: Login Account Lock

Requirement:

* After **3 failed login attempts**, account gets **locked**.

| State          | Action                   | Result         |
| -------------- | ------------------------ | -------------- |
| Account active | Correct login            | Login success  |
| Account active | Wrong password 1–2 times | Retry          |
| Account active | Wrong password 3 times   | Account locked |



## Advantages of State Transition Testing

* Useful for **systems with different states**
* Helps detect **state-related defects**
* Ensures **correct behavior after events**
* Ideal for **workflow-based applications**

Examples:

* ATM machines
* Login systems
* Online transactions
* Traffic lights



## Short Interview Answer

> **State Transition Testing is a test design technique used to verify how a system behaves when it moves from one state to another based on specific inputs or events. It is commonly used in systems where the output depends on previous actions.**

---

# 6️. What is **Error Guessing in Testing?**

**Error Guessing** is an **experience-based test design technique** where testers use their **knowledge, intuition, and past experience** to identify areas where defects are likely to occur.

In simple terms:

> **Error Guessing means predicting possible errors in the application based on tester experience.**

Instead of following strict rules or techniques, testers **guess where bugs might exist and design test cases to find them**. This technique depends heavily on the tester’s **domain knowledge and previous testing experience**. 



## Key Idea

Experienced testers often know **common mistakes developers make**, such as:

* Missing validations
* Incorrect input handling
* Boundary issues
* Logical errors

Using this knowledge, testers try **unusual or unexpected inputs** to reveal defects.



## Example: Login Form Testing

A login form requires:

* **Username**
* **Password**

Using **Error Guessing**, a tester may try the following test cases:

| Test Case                   | Input           | Expected Result             |
| --------------------------- | --------------- | --------------------------- |
| Empty username and password | ""              | Validation error            |
| Only spaces in username     | "   "           | Validation error            |
| Very long username          | 100+ characters | Error message               |
| Special characters          | `@#$%^`         | Validation handled properly |
| SQL injection attempt       | `' OR '1'='1`   | System should reject        |

These cases are **not always specified in requirements**, but testers guess them based on experience.



## Another Example: Payment System

Tester may try:

* Payment amount = **0**
* Payment amount = **negative value**
* Very **large transaction amount**
* **Network interruption** during payment

These tests help reveal **hidden defects**.



## Advantages of Error Guessing

* Helps detect **unexpected defects**
* Requires **no formal documentation**
* Useful for **complex systems**
* Works well with **experienced testers**



## Limitation

* Depends heavily on **tester experience**
* No systematic approach like EP or BVA



## Short Interview Answer

> **Error Guessing is a test design technique where testers use their experience and intuition to predict possible defects and design test cases to uncover them.**

---
---



# 7️. What is **Use Case Testing?**

**Use Case Testing** is a **black-box testing technique** where test cases are designed based on **use cases that describe how users interact with the system**.

In simple terms:

> **Use Case Testing verifies whether the application works correctly according to real user actions and workflows.**

A **use case** represents a **step-by-step interaction between a user and the system** to achieve a specific goal (for example: login, purchase product, withdraw money). 



## Key Idea

Use Case Testing focuses on:

* **User actions**
* **System responses**
* **End-to-end functionality**

Instead of testing individual components, it tests the **complete user workflow**.



## Example: Login System

### Use Case

**User logs into the application**

### Steps

| Step | User Action           | System Response             |
| ---- | --------------------- | --------------------------- |
| 1    | User opens login page | Login form displayed        |
| 2    | User enters username  | System accepts input        |
| 3    | User enters password  | System accepts password     |
| 4    | User clicks login     | System verifies credentials |
| 5    | Valid credentials     | User logged in successfully |



## Test Cases Derived from the Use Case

| Test Case | Scenario                    | Expected Result    |
| --------- | --------------------------- | ------------------ |
| TC1       | Valid username and password | Login successful   |
| TC2       | Invalid password            | Error message      |
| TC3       | Empty username              | Validation message |
| TC4       | Empty password              | Validation message |



## Another Example: Online Shopping

### Use Case

**Customer purchases a product**

Steps:

1. User searches product
2. User adds product to cart
3. User proceeds to checkout
4. User enters payment details
5. Order confirmed

Testers verify that **each step works correctly**.



## Advantages of Use Case Testing

* Tests **real user scenarios**
* Ensures **end-to-end functionality**
* Easy to understand for **business stakeholders**
* Improves **requirement coverage**



## Limitation

* May **miss edge cases**
* Depends on **quality of use case documentation**


## Short Interview Answer

> **Use Case Testing is a test design technique where test cases are derived from use cases to verify how users interact with the system and ensure the application works correctly for real-world scenarios.**

---
---

# 8. What is **Exploratory Testing?**

**Exploratory Testing** is a **testing approach where testers explore the application, learn its behavior, and design test cases at the same time without predefined test cases or scripts.**

In simple terms:

> **Exploratory Testing = Testing by exploring the application to find defects.**

The tester interacts with the application like a **real user**, trying different actions and scenarios to discover bugs.



## Key Idea

In Exploratory Testing:

* **Testing and learning happen simultaneously**
* Testers **do not follow predefined test cases**
* Testers use **experience, intuition, and creativity**

This approach is often used when:

* Requirements are **not very clear**
* **New features** are released
* There is **limited time for testing**


## Example: Login Page Testing

A tester opens the login page and explores different scenarios.

Possible actions:

| Action                            | Expected Result                     |
| --------------------------------- | ----------------------------------- |
| Enter valid username and password | Login successful                    |
| Enter wrong password              | Error message                       |
| Leave fields empty                | Validation message                  |
| Enter special characters          | System should handle input properly |

The tester **tries many different combinations while exploring the application**.



## Another Example: E-Commerce Website

A tester explores the **shopping process**:

1. Search for products
2. Add product to cart
3. Remove product from cart
4. Change product quantity
5. Proceed to checkout

While doing this, the tester may discover bugs like:

* Cart not updating correctly
* Payment page crashing
* Incorrect price calculation



## Advantages of Exploratory Testing

* Helps discover **unexpected defects**
* **Quick testing** without writing test cases
* Encourages **creative thinking**
* Useful for **complex applications**



## Limitations

* Difficult to **track test coverage**
* Depends on **tester skill and experience**
* Not suitable for **regression testing**



## Exploratory Testing vs Scripted Testing

| Feature       | Exploratory Testing  | Scripted Testing    |
| ------------- | -------------------- | ------------------- |
| Test cases    | Not predefined       | Predefined          |
| Approach      | Flexible             | Structured          |
| Focus         | Discover new defects | Verify requirements |
| Documentation | Minimal              | Detailed            |



## Short Interview Answer

> **Exploratory Testing is a testing approach where testers explore the application, learn its functionality, and design test cases simultaneously without predefined test scripts to discover defects.**

---
---
# 9. What is **Exploratory Testing?**

**Exploratory Testing** is a **testing approach where testers explore the application, learn its behavior, and design test cases at the same time without predefined test cases or scripts.**

In simple terms:

> **Exploratory Testing = Testing by exploring the application to find defects.**

The tester interacts with the application like a **real user**, trying different actions and scenarios to discover bugs.



## Key Idea

In Exploratory Testing:

* **Testing and learning happen simultaneously**
* Testers **do not follow predefined test cases**
* Testers use **experience, intuition, and creativity**

This approach is often used when:

* Requirements are **not very clear**
* **New features** are released
* There is **limited time for testing**



## Example: Login Page Testing

A tester opens the login page and explores different scenarios.

Possible actions:

| Action                            | Expected Result                     |
| --------------------------------- | ----------------------------------- |
| Enter valid username and password | Login successful                    |
| Enter wrong password              | Error message                       |
| Leave fields empty                | Validation message                  |
| Enter special characters          | System should handle input properly |

The tester **tries many different combinations while exploring the application**.



## Another Example: E-Commerce Website

A tester explores the **shopping process**:

1. Search for products
2. Add product to cart
3. Remove product from cart
4. Change product quantity
5. Proceed to checkout

While doing this, the tester may discover bugs like:

* Cart not updating correctly
* Payment page crashing
* Incorrect price calculation


## Advantages of Exploratory Testing

* Helps discover **unexpected defects**
* **Quick testing** without writing test cases
* Encourages **creative thinking**
* Useful for **complex applications**



## Limitations

* Difficult to **track test coverage**
* Depends on **tester skill and experience**
* Not suitable for **regression testing**



## Exploratory Testing vs Scripted Testing

| Feature       | Exploratory Testing  | Scripted Testing    |
| ------------- | -------------------- | ------------------- |
| Test cases    | Not predefined       | Predefined          |
| Approach      | Flexible             | Structured          |
| Focus         | Discover new defects | Verify requirements |
| Documentation | Minimal              | Detailed            |



# 🎯 Short Interview Answer

> **Exploratory Testing is a testing approach where testers explore the application, learn its functionality, and design test cases simultaneously without predefined test scripts to discover defects.**

---
---

# 10 What is **Pairwise Testing?**

**Pairwise Testing** is a **test design technique** used to test **all possible combinations of pairs of input parameters** instead of testing every possible combination.

In simple terms:

> **Pairwise Testing checks combinations of two input parameters at a time to reduce the number of test cases while maintaining good coverage.**

It is based on the idea that **most defects are caused by interactions between two parameters rather than many parameters together**.



# 🧠 Why Pairwise Testing is Used

When a system has **many input parameters**, testing all combinations becomes very large.

Example:

3 parameters with 3 values each:

```
3 × 3 × 3 = 27 combinations
```

Testing all combinations is **time-consuming**.

Pairwise testing reduces this by **testing only pairs of parameters**.

This technique is part of **test design techniques used to design efficient test cases with good coverage**. 


## Example: Login System

Suppose a login system has three parameters:

| Parameter        | Values            |
| ---------------- | ----------------- |
| Browser          | Chrome, Firefox   |
| Operating System | Windows, Linux    |
| Network          | WiFi, Mobile Data |

### All Combinations (Full Testing)

```
2 × 2 × 2 = 8 test cases
```

### Pairwise Testing

Instead of testing all 8 combinations, we test only combinations where **every pair appears at least once**.

| Test Case | Browser | OS      | Network     |
| --------- | ------- | ------- | ----------- |
| TC1       | Chrome  | Windows | WiFi        |
| TC2       | Chrome  | Linux   | Mobile Data |
| TC3       | Firefox | Windows | Mobile Data |
| TC4       | Firefox | Linux   | WiFi        |

This ensures that **every pair of inputs is tested at least once**.



## Another Example: Mobile App Testing

Parameters:

| Parameter | Values           |
| --------- | ---------------- |
| Device    | Android, iPhone  |
| Network   | WiFi, 4G         |
| Language  | English, Spanish |

Full combinations = **8 tests**

Pairwise testing may reduce to **4 tests** while still covering all pairs.



## Advantages of Pairwise Testing

* Reduces **number of test cases**
* Saves **time and testing effort**
* Maintains **good test coverage**
* Useful for **systems with many input parameters**



## Limitation

* May miss defects caused by **interaction of more than two parameters**



## Short Interview Answer

> **Pairwise Testing is a test design technique where test cases are created to cover all possible combinations of two input parameters. It helps reduce the number of test cases while still providing good test coverage.**

---
---

## What is **White-Box Testing?**

**White-Box Testing** (also called **Structural Testing or Glass Box Testing**) is a testing technique where the **internal code structure, logic, and implementation of the software are tested**.

In simple terms:

> **White-Box Testing tests the internal working of the program, including code, logic, branches, and paths.**

The tester must **have knowledge of the source code** to perform this type of testing.

White-box testing belongs to **test design techniques based on internal code logic**. 



# 🔎 Key Characteristics of White-Box Testing

* Requires **knowledge of programming code**
* Focuses on **internal logic and structure**
* Usually performed by **developers**
* Ensures **code coverage**



## Example

Consider the following code:

```java
if (age >= 18) {
   System.out.println("Eligible to vote");
} else {
   System.out.println("Not eligible");
}
```

White-box testing ensures that:

* The **if condition** is executed
* The **else condition** is also executed

### Test Cases

| Input Age | Expected Output  |
| --------- | ---------------- |
| 20        | Eligible to vote |
| 15        | Not eligible     |

This verifies **both code paths**.



## Types of White-Box Testing

Common techniques include:

| Technique          | Description                          |
| ------------------ | ------------------------------------ |
| Statement Coverage | Execute every line of code           |
| Branch Coverage    | Test every decision branch (if/else) |
| Path Coverage      | Test all possible execution paths    |
| Loop Testing       | Test loops for correct execution     |



## What is **Black-Box Testing?**

**Black-Box Testing** is a testing technique where testers **verify the functionality of the software without knowing the internal code or implementation**.

In simple terms:

> **Black-Box Testing focuses only on inputs and outputs.**

Testers only check whether the **application behaves according to requirements**.



## Example

Testing a **Login Page**

Input:

* Username
* Password

Test cases:

| Username | Password | Expected Result    |
| -------- | -------- | ------------------ |
| Valid    | Valid    | Login success      |
| Valid    | Invalid  | Error message      |
| Empty    | Empty    | Validation message |

The tester **does not check the code**, only the behavior.



## White-Box Testing vs Black-Box Testing

| Feature           | White-Box Testing       | Black-Box Testing           |
| ----------------- | ----------------------- | --------------------------- |
| Focus             | Internal code structure | System functionality        |
| Knowledge of Code | Required                | Not required                |
| Performed By      | Developers              | Testers / QA                |
| Testing Level     | Unit testing            | System / Functional testing |
| Example           | Checking code branches  | Testing login functionality |



## Simple Real-World Example

### Black-Box Testing

Testing a **calculator app**:

* Enter **2 + 3**
* Check result = **5**

Tester doesn't know how the calculation is implemented.



### White-Box Testing

Developer checks:

* Whether the **addition function code executes correctly**
* Whether **all branches and conditions are tested**



## Short Interview Answer

> **White-Box Testing is a testing technique that verifies the internal code structure and logic of a program, while Black-Box Testing verifies the functionality of the application without knowledge of the internal code.**

---
---





