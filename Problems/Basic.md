
# Programming Problem – Hello World

## 1. Problem

Write a program that prints the following two lines to the console:

Hello, World.  
Hello, Java.

The program should display the text exactly as shown above, each sentence on a new line.

---

## 2. Answer

### Java

```java
public class Solution {

    public static void main(String[] args) {
        System.out.println("Hello, World.");
        System.out.println("Hello, Java.");
    }
}
````

---

### Python

```python
print("Hello, World.")
print("Hello, Java.")
```

---

### JavaScript

```javascript
console.log("Hello, World.");
console.log("Hello, Java.");
```

---

## 3. Clear Explanation

This problem is a basic programming exercise designed to help beginners understand how to display output in different programming languages.

### Key Concept

Most programming languages provide built-in functions to print output to the console (standard output).

| Language   | Output Function        |
| ---------- | ---------------------- |
| Java       | `System.out.println()` |
| Python     | `print()`              |
| JavaScript | `console.log()`        |

### Step-by-Step Logic

1. Start the program.
2. Use the language's output function to print the first line: **"Hello, World."**
3. Print the second line: **"Hello, Java."**
4. Each statement automatically moves to a new line.

### Language-Specific Details

#### Java

* Java programs require a **class** and a **main method**.
* `System.out.println()` prints text and moves to the next line.

Example:

```java
System.out.println("Hello, World.");
```

#### Python

* Python is simpler and does not require a class or main method for basic scripts.
* `print()` directly prints text to the console.

Example:

```python
print("Hello, World.")
```

#### JavaScript

* JavaScript prints output to the console using `console.log()`.

Example:

```javascript
console.log("Hello, World.");
```

### Output

```
Hello, World.
Hello, Java.
```

### Summary

This example demonstrates how different programming languages perform the same basic task: printing text to the console. Although syntax varies between languages, the concept of sending output to standard output remains the same.

---
# HackerRank – Java Stdin and Stdout I

## 1. Problem

In this problem, you need to read **three integers** from standard input and print them to standard output.

### Input Format
You are given three integers as input.

### Output Format
Print the three integers on separate lines in the same order as they were entered.

### Sample Input
```

42
100
125

```

### Sample Output
```

42
100
125

````

The program should read input from the user and display the same values exactly as they were entered.

---

# 2. Answer

## Java Solution

```java
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);

        scan.close();
    }
}
````

---

## Python Solution

```python
a = int(input())
b = int(input())
c = int(input())

print(a)
print(b)
print(c)
```

---

## JavaScript Solution

```javascript
const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split("\n");

const a = parseInt(input[0]);
const b = parseInt(input[1]);
const c = parseInt(input[2]);

console.log(a);
console.log(b);
console.log(c);
```

---

# 3. Clear Explanation

This problem demonstrates **reading input from the user and printing output**.

## Java Explanation

### 1. Importing Scanner

```java
import java.util.*;
```

The `Scanner` class is used to read input from the keyboard.

### 2. Creating Scanner Object

```java
Scanner scan = new Scanner(System.in);
```

This object reads input from **standard input (keyboard)**.

### 3. Reading Integers

```java
int a = scan.nextInt();
int b = scan.nextInt();
int c = scan.nextInt();
```

* `nextInt()` reads an integer value from input.
* Each call reads the next number entered by the user.

### Example Input

```
5
10
15
```

Values stored:

```
a = 5
b = 10
c = 15
```

### 4. Printing Values

```java
System.out.println(a);
System.out.println(b);
System.out.println(c);
```

`println()` prints the value and moves to the next line.

Output:

```
5
10
15
```

### 5. Closing Scanner

```java
scan.close();
```

Closing the scanner prevents resource leaks.

---

## Python Explanation

Python uses the `input()` function.

```python
a = int(input())
```

* `input()` reads text
* `int()` converts it into an integer

Printing is done using:

```python
print(a)
```

---

## JavaScript Explanation

In JavaScript (Node.js), input is read using the `fs` module.

```javascript
const input = fs.readFileSync(0, "utf8")
```

This reads the entire input from standard input.

Then values are split:

```javascript
.split("\n")
```

Numbers are converted using:

```javascript
parseInt()
```

Finally printed using:

```javascript
console.log()
```

---

# Key Concepts Learned

* Reading input from **standard input**
* Printing output to **standard output**
* Basic syntax in **Java, Python, and JavaScript**
* Using **Scanner**, **input()**, and **console.log()**

This is one of the **fundamental problems for learning input/output in programming**.

---

# Java If-Else (Conditional Statements)

## 1. Problem

Given an integer **N**, perform the following conditional actions:

- If **N is odd**, print **"Weird"**.
- If **N is even** and in the inclusive range **2 to 5**, print **"Not Weird"**.
- If **N is even** and in the inclusive range **6 to 20**, print **"Weird"**.
- If **N is even** and **greater than 20**, print **"Not Weird"**.

### Input Format

A single integer **N**.

### Constraints

```

1 ≤ N ≤ 100

```

### Output Format

Print **Weird** or **Not Weird** according to the conditions.

### Sample Input

```

3

```

### Sample Output

```

Weird

````

---

# 2. Answer

## Java Solution

```java
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();

        if (N % 2 != 0) {
            System.out.println("Weird");
        } 
        else if (N >= 2 && N <= 5) {
            System.out.println("Not Weird");
        } 
        else if (N >= 6 && N <= 20) {
            System.out.println("Weird");
        } 
        else {
            System.out.println("Not Weird");
        }

        scanner.close();
    }
}
````

---

## Python Solution

```python
N = int(input())

if N % 2 != 0:
    print("Weird")
elif 2 <= N <= 5:
    print("Not Weird")
elif 6 <= N <= 20:
    print("Weird")
else:
    print("Not Weird")
```

---

## JavaScript Solution

```javascript
const fs = require("fs");

const N = parseInt(fs.readFileSync(0, "utf8").trim());

if (N % 2 !== 0) {
    console.log("Weird");
} else if (N >= 2 && N <= 5) {
    console.log("Not Weird");
} else if (N >= 6 && N <= 20) {
    console.log("Weird");
} else {
    console.log("Not Weird");
}
```

---

# 3. Clear Explanation

This problem demonstrates **conditional statements (if-else logic)** used to control program flow.

## Step 1: Determine if the number is odd

A number is **odd** if it is not divisible by 2.

Example condition:

```
N % 2 != 0
```

`%` is the **modulus operator**, which gives the remainder.

Example:

```
7 % 2 = 1
```

Since the remainder is not zero, the number is **odd**, so we print:

```
Weird
```

---

## Step 2: Handle even numbers

If the number is **even**, the program checks ranges.

### Condition 1: 2 ≤ N ≤ 5

Example numbers:

```
2, 4
```

Output:

```
Not Weird
```

---

### Condition 2: 6 ≤ N ≤ 20

Example numbers:

```
6, 8, 10, 12, 20
```

Output:

```
Weird
```

---

### Condition 3: N > 20

Example numbers:

```
22, 24, 30
```

Output:

```
Not Weird
```

---

# Logical Flow

The decision process works like this:

```
          N
          |
   Is N odd?
     /   \
   Yes    No
   |       |
 Weird   Check Range
            |
   2–5 → Not Weird
   6–20 → Weird
   >20 → Not Weird
```

---

# Example Walkthrough

### Input

```
N = 4
```

Evaluation:

```
4 % 2 == 0  → even
4 is between 2 and 5
```

Output:

```
Not Weird
```

---

### Input

```
N = 18
```

Evaluation:

```
18 % 2 == 0
18 is between 6 and 20
```

Output:

```
Weird
```

---

# Key Concepts Learned

* Conditional statements (**if, else if, else**)
* Modulus operator `%`
* Checking number ranges
* Program flow control

This problem is fundamental for learning **decision-making logic in programming**.


# HackerRank – Java Stdin and Stdout II

## 1. Problem

In this problem, you must read **three different types of input** from standard input and print them in a specific format.

The inputs are:

1. An **integer**
2. A **double**
3. A **string**

After reading the inputs, print them in the following order:

1. String  
2. Double  
3. Integer  

### Input Format

- The first line contains an **integer**.
- The second line contains a **double**.
- The third line contains a **string**.

### Output Format

Print the following three lines:

```

String: <string value>
Double: <double value>
Int: <integer value>

```

### Sample Input

```

42
3.1415
Welcome to HackerRank's Java tutorials!

```

### Sample Output

```

String: Welcome to HackerRank's Java tutorials!
Double: 3.1415
Int: 42

````

---

# 2. Answer

## Java Solution

```java
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        int i = scan.nextInt();
        double d = scan.nextDouble();
        scan.nextLine(); 
        String s = scan.nextLine();

        scan.close();

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}
````

---

## Python Solution

```python
i = int(input())
d = float(input())
s = input()

print("String:", s)
print("Double:", d)
print("Int:", i)
```

---

## JavaScript Solution

```javascript
const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split("\n");

const i = parseInt(input[0]);
const d = parseFloat(input[1]);
const s = input[2];

console.log("String: " + s);
console.log("Double: " + d);
console.log("Int: " + i);
```

---

# 3. Clear Explanation

This problem teaches how to **read multiple data types from input** and print them in a specific format.

The three types involved are:

* **Integer**
* **Double (decimal number)**
* **String (text)**

---

## Java Explanation

### 1. Import Scanner

```java
import java.util.Scanner;
```

The `Scanner` class is used to read user input from the keyboard.

---

### 2. Create Scanner Object

```java
Scanner scan = new Scanner(System.in);
```

This allows the program to read data from **standard input**.

---

### 3. Read Integer

```java
int i = scan.nextInt();
```

`nextInt()` reads an **integer value**.

Example:

```
42
```

The variable becomes:

```
i = 42
```

---

### 4. Read Double

```java
double d = scan.nextDouble();
```

`nextDouble()` reads a **floating-point number**.

Example:

```
3.1415
```

The variable becomes:

```
d = 3.1415
```

---

### 5. Clear the Input Buffer

```java
scan.nextLine();
```

This line is very important.

When `nextInt()` and `nextDouble()` are used, they **do not consume the newline character**.
`nextLine()` clears the leftover newline before reading the string.

---

### 6. Read String

```java
String s = scan.nextLine();
```

This reads the **entire line of text**.

Example:

```
Welcome to HackerRank's Java tutorials!
```

---

### 7. Print Output

```java
System.out.println("String: " + s);
System.out.println("Double: " + d);
System.out.println("Int: " + i);
```

Output example:

```
String: Welcome to HackerRank's Java tutorials!
Double: 3.1415
Int: 42
```

---

# Python Explanation

Python uses the `input()` function.

```python
i = int(input())
```

Converts input to **integer**.

```python
d = float(input())
```

Converts input to **decimal number**.

```python
s = input()
```

Reads a **string**.

Printing:

```python
print("String:", s)
```

---

# JavaScript Explanation

In **Node.js**, input is read using the `fs` module.

```javascript
const input = fs.readFileSync(0, "utf8")
```

This reads all input from **standard input**.

Split input lines:

```javascript
.split("\n")
```

Convert values:

```
parseInt()   → integer
parseFloat() → decimal number
```

Print output:

```javascript
console.log()
```

---

# Key Concepts Learned

* Reading multiple **data types**
* Handling **input buffering in Java**
* Using **Scanner, input(), and Node.js fs module**
* Formatting output strings
* Understanding **basic input/output operations**

This is an important foundational problem for learning **console input handling in programming languages**.


# Java Output Formatting

## 1. Problem

In this problem, you must print formatted output using **Java's formatted printing**.

You will be given **3 lines of input**, and each line contains:

- A **String**
- An **Integer**

Your task is to print them using the following formatting rules:

1. The **String** must be **left-justified**.
2. The **String must occupy exactly 15 characters**.
3. The **Integer must be exactly 3 digits**.
4. If the integer has fewer than 3 digits, it must be **padded with leading zeros**.

### Input Format

Three lines of input:

```

java 100
cpp 65
python 50

```

### Output Format

```

================================
java           100
cpp            065
python         050
==================

````

Rules applied:

- `"java"` takes 4 characters, so **11 spaces are added** to make it 15.
- `"65"` becomes `"065"`.
- `"50"` becomes `"050"`.

---

# 2. Answer

## Java Solution

```java
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("================================");

        for (int i = 0; i < 3; i++) {

            String s1 = sc.next();
            int x = sc.nextInt();

            System.out.printf("%-15s%03d%n", s1, x);
        }

        System.out.println("================================");

        sc.close();
    }
}
````

---

## Python Solution

```python
print("================================")

for _ in range(3):
    s, x = input().split()
    x = int(x)
    print(f"{s:<15}{x:03d}")

print("================================")
```

---

## JavaScript Solution

```javascript
const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split("\n");

console.log("================================");

for (let i = 0; i < 3; i++) {

    let [s, x] = input[i].split(" ");
    x = parseInt(x);

    let formattedString = s.padEnd(15, " ");
    let formattedNumber = x.toString().padStart(3, "0");

    console.log(formattedString + formattedNumber);
}

console.log("================================");
```

---

# 3. Clear Explanation

This problem focuses on **output formatting**, which is very important in programming when displaying aligned tables or reports.

---

# Java Explanation

The key line is:

```java
System.out.printf("%-15s%03d%n", s1, x);
```

### `% -15s`

* `%s` → prints a string
* `15` → width of 15 characters
* `-` → left-justified

Example:

```
java
```

becomes:

```
java           (11 spaces added)
```

---

### `%03d`

* `%d` → integer
* `3` → minimum width of 3 digits
* `0` → fill missing digits with zeros

Examples:

```
5   → 005
65  → 065
100 → 100
```

---

### `%n`

`%n` creates a **new line** (similar to `\n` but platform-independent).

---

# Python Explanation

Python uses **f-string formatting**.

```
{s:<15}
```

* `<` → left alignment
* `15` → width

Example:

```
java           (spaces added)
```

For numbers:

```
{x:03d}
```

* `3` → width
* `0` → leading zeros

Example:

```
5 → 005
```

---

# JavaScript Explanation

JavaScript uses string methods.

### `padEnd()`

```
s.padEnd(15, " ")
```

Adds spaces to the **right** until the string length becomes 15.

Example:

```
java           (11 spaces)
```

---

### `padStart()`

```
x.toString().padStart(3, "0")
```

Adds zeros to the **left** until the number becomes 3 digits.

Example:

```
5 → 005
```

---

# Key Concepts Learned

* Output formatting
* String alignment
* Padding numbers with zeros
* Using formatting functions in different languages
* Producing clean table-like output

This problem is commonly used to teach **formatted printing in Java using `printf()`**.

# Java Loops I (Multiplication Table)

## 1. Problem

Given an integer **N**, print its multiplication table from **1 to 10**.

Each line of the output must follow this exact format:

```

N x i = result

```

Where:

- **N** is the input number  
- **i** ranges from **1 to 10**  
- **result = N × i**

### Input Format

A single integer **N**.

### Constraints

```

2 ≤ N ≤ 20

```

### Output Format

Print **10 lines** showing the multiplication table of **N**.

### Sample Input

```

2

```

### Sample Output

```

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20

````

---

# 2. Answer

## Java Solution

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Solution {

    public static void main(String[] args) throws IOException {

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(bufferedReader.readLine().trim());

        for (int i = 1; i <= 10; i++) {
            System.out.println(N + " x " + i + " = " + (N * i));
        }

        bufferedReader.close();
    }
}
````

---

## Python Solution

```python
N = int(input())

for i in range(1, 11):
    print(f"{N} x {i} = {N * i}")
```

---

## JavaScript Solution

```javascript
const fs = require("fs");

const N = parseInt(fs.readFileSync(0, "utf8").trim());

for (let i = 1; i <= 10; i++) {
    console.log(N + " x " + i + " = " + (N * i));
}
```

---

# 3. Clear Explanation

This problem teaches how to use **loops** to repeatedly perform calculations.

The goal is to generate a **multiplication table**.

---

## Step 1: Read the Input Number

The program first reads an integer **N**.

Example:

```
N = 5
```

---

## Step 2: Use a Loop

We must print **10 lines**, so we use a loop that runs from **1 to 10**.

### Java Example

```java
for (int i = 1; i <= 10; i++)
```

Meaning:

* Start at **i = 1**
* Continue while **i ≤ 10**
* Increase **i** by 1 each iteration

---

## Step 3: Calculate the Result

Each iteration calculates:

```
result = N × i
```

Example when **N = 5**:

| i  | Calculation | Result |
| -- | ----------- | ------ |
| 1  | 5 × 1       | 5      |
| 2  | 5 × 2       | 10     |
| 3  | 5 × 3       | 15     |
| 4  | 5 × 4       | 20     |
| 5  | 5 × 5       | 25     |
| 6  | 5 × 6       | 30     |
| 7  | 5 × 7       | 35     |
| 8  | 5 × 8       | 40     |
| 9  | 5 × 9       | 45     |
| 10 | 5 × 10      | 50     |

---

## Step 4: Print the Output

The format must exactly match:

```
N x i = result
```

Example:

```
5 x 3 = 15
```

---

# Language-Specific Concepts

## Java

Uses:

```
BufferedReader
```

to read input efficiently.

Convert string to integer:

```
Integer.parseInt()
```

Loop:

```
for (int i = 1; i <= 10; i++)
```

---

## Python

Uses:

```
range(1, 11)
```

because the ending value is **exclusive**.

Formatted output using **f-strings**:

```
f"{N} x {i} = {N * i}"
```

---

## JavaScript

Input is read using:

```
fs.readFileSync()
```

Loop:

```
for (let i = 1; i <= 10; i++)
```

Print using:

```
console.log()
```

---

# Key Concepts Learned

* Loops (`for` loop)
* Multiplication tables
* Reading input
* String formatting
* Iteration logic

This problem is a fundamental exercise for understanding **loops and repeated calculations in programming**.
---
# Java Loops II

## 1. Problem

You are given **t queries**. Each query consists of three integers:

- **a**
- **b**
- **n**

For each query, print a series of **n values** using the following formula:

```

(a + 2^0 * b)
(a + 2^0 * b + 2^1 * b)
(a + 2^0 * b + 2^1 * b + 2^2 * b)
...

```

In general, the **k-th term** of the series is:

```

S(k) = a + b*(2^0 + 2^1 + 2^2 + ... + 2^k)

```

You must print **n values** for each query on the **same line separated by spaces**.

### Input Format

```

t
a b n
a b n
...

```

- **t** → number of queries  
- Each of the next **t lines** contains three integers **a, b, n**

### Constraints

```

0 ≤ t ≤ 500
0 ≤ a, b ≤ 50
1 ≤ n ≤ 15

```

### Sample Input

```

2
0 2 10
5 3 5

```

### Sample Output

```

2 6 14 30 62 126 254 510 1022 2046
8 14 26 50 98

````

---

# 2. Answer

## Java Solution

```java
import java.util.*;

class Solution {
    public static void main(String[] argh) {

        Scanner in = new Scanner(System.in);
        int t = in.nextInt();

        for (int i = 0; i < t; i++) {

            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();

            int sum = a;

            for (int j = 0; j < n; j++) {

                sum = sum + (int)(Math.pow(2, j) * b);
                System.out.print(sum + " ");
            }

            System.out.println();
        }

        in.close();
    }
}
````

---

## Python Solution

```python
t = int(input())

for _ in range(t):

    a, b, n = map(int, input().split())

    total = a

    for j in range(n):
        total += (2 ** j) * b
        print(total, end=" ")

    print()
```

---

## JavaScript Solution

```javascript
const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

let index = 0;
const t = input[index++];

for (let i = 0; i < t; i++) {

    const a = input[index++];
    const b = input[index++];
    const n = input[index++];

    let sum = a;

    let output = [];

    for (let j = 0; j < n; j++) {
        sum = sum + (Math.pow(2, j) * b);
        output.push(sum);
    }

    console.log(output.join(" "));
}
```

---

# 3. Clear Explanation

This problem teaches how to use **nested loops and mathematical series**.

Each query generates a **sequence of numbers**.

---

# Step 1: Understand the Formula

The sequence builds incrementally using powers of **2**.

For example:

```
a + 2^0*b
a + 2^0*b + 2^1*b
a + 2^0*b + 2^1*b + 2^2*b
```

Instead of recalculating everything each time, we **keep adding the next value**.

---

# Step 2: Example Walkthrough

Input:

```
a = 5
b = 3
n = 5
```

Start with:

```
sum = a = 5
```

Now calculate each step.

### Iteration 1 (j = 0)

```
sum = 5 + (2^0 * 3)
sum = 5 + 3
sum = 8
```

Output:

```
8
```

---

### Iteration 2 (j = 1)

```
sum = 8 + (2^1 * 3)
sum = 8 + 6
sum = 14
```

Output:

```
8 14
```

---

### Iteration 3 (j = 2)

```
sum = 14 + (2^2 * 3)
sum = 14 + 12
sum = 26
```

Output:

```
8 14 26
```

---

### Iteration 4 (j = 3)

```
sum = 26 + (2^3 * 3)
sum = 26 + 24
sum = 50
```

Output:

```
8 14 26 50
```

---

### Iteration 5 (j = 4)

```
sum = 50 + (2^4 * 3)
sum = 50 + 48
sum = 98
```

Final Output:

```
8 14 26 50 98
```

---

# Step 3: Loop Structure

Two loops are used.

### Outer Loop

Handles multiple queries.

Example:

```
for each query
```

---

### Inner Loop

Generates the **series values**.

```
for j from 0 to n-1
```

Each iteration:

```
sum = sum + (2^j * b)
```

---

# Key Concepts Learned

* Nested loops
* Mathematical series
* Powers of numbers
* Efficient accumulation of values
* Input handling for multiple test cases

This problem is important because it strengthens understanding of **loops, exponentiation, and sequence generation**.


#  Java End-of-file

## 1. Problem

In this problem, you must read input **until the end-of-file (EOF)** and print each line of input preceded by its **line number**.

The numbering should start from **1** and increment for each new line.

### Input Format

An unknown number of lines of input.

Each line contains a **string of text**.

### Output Format

For each line of input, print:

```

line_number space input_line

```

### Example Input

```

Hello world
I am learning Java
EOF handling is useful

```

### Example Output

```

1 Hello world
2 I am learning Java
3 EOF handling is useful

````

---

# 2. Answer

## Java Solution

```java
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        int line = 1;

        while (scan.hasNext()) {

            String words = scan.nextLine();

            System.out.println(line + " " + words);

            line++;
        }

        scan.close();
    }
}
````

---

## Python Solution

```python
import sys

line = 1

for text in sys.stdin:
    print(f"{line} {text.strip()}")
    line += 1
```

---

## JavaScript Solution

```javascript
const fs = require("fs");

const input = fs.readFileSync(0, "utf8").split("\n");

for (let i = 0; i < input.length; i++) {

    if (input[i].trim() !== "") {
        console.log((i + 1) + " " + input[i]);
    }
}
```

---

# 3. Clear Explanation

This problem focuses on **reading input until the end of file (EOF)**.

Normally, programs read a **fixed number of inputs**, but here we do not know how many lines exist.

So we keep reading input **until no more data is available**.

---

# Step 1: Understanding End-of-File (EOF)

EOF means:

```
No more input is available.
```

The program stops reading when input ends.

Example input:

```
Java
Python
JavaScript
```

The program processes **each line one by one**.

---

# Step 2: Number the Lines

We maintain a counter.

```
line = 1
```

Each time we read a line:

```
print line_number + text
```

Then increase the counter:

```
line++
```

---

# Example Execution

Input:

```
Apple
Banana
Cherry
```

Processing:

| Line Number | Input  | Output   |
| ----------- | ------ | -------- |
| 1           | Apple  | 1 Apple  |
| 2           | Banana | 2 Banana |
| 3           | Cherry | 3 Cherry |

Output:

```
1 Apple
2 Banana
3 Cherry
```

---

# Java Explanation

### Scanner Loop

```java
while(scan.hasNext())
```

* `hasNext()` checks if more input exists.
* Loop continues **until EOF**.

Read line:

```java
String words = scan.nextLine();
```

Print line number and text:

```java
System.out.println(line + " " + words);
```

---

# Python Explanation

Python uses `sys.stdin` to read input until EOF.

```python
for text in sys.stdin:
```

This automatically loops through every line of input.

Printing:

```python
print(f"{line} {text.strip()}")
```

`strip()` removes newline characters.

---

# JavaScript Explanation

Node.js reads all input using:

```
fs.readFileSync()
```

Then splits lines:

```
split("\n")
```

Loop through each line:

```
console.log((i + 1) + " " + input[i])
```

---

# Key Concepts Learned

* Handling **unknown input size**
* Reading input **until EOF**
* Using loops to process multiple lines
* Maintaining a **line counter**
* Working with standard input streams

This problem is important for learning **file-style input processing in programming**.
---

# HackerRank – Java Static Initializer Block

## 1. Problem

You are given two integers:

- **B** (Breadth)
- **H** (Height)

Your task is to compute the **area of a parallelogram** using the formula:

```

Area = B × H

```

However, before calculating the area, you must verify the following condition:

- **B > 0**
- **H > 0**

If **both values are positive**, print the area.

If **either B or H is less than or equal to 0**, print the following exception message:

```

java.lang.Exception: Breadth and height must be positive

```

### Input Format

Two integers:

```

B
H

```

### Output Format

- If **B > 0 and H > 0**, print the **area**
- Otherwise print the **exception message**

### Sample Input

```

1
3

```

### Sample Output

```

3

```

### Sample Input

```

-1
2

```

### Sample Output

```

java.lang.Exception: Breadth and height must be positive

````

---

# 2. Answer

## Java Solution

```java
import java.util.*;

public class Solution {

    static int B;
    static int H;
    static boolean flag = true;

    static {

        Scanner scan = new Scanner(System.in);

        B = scan.nextInt();
        H = scan.nextInt();

        if (B <= 0 || H <= 0) {

            flag = false;

            System.out.println("java.lang.Exception: Breadth and height must be positive");
        }
    }

    public static void main(String[] args) {

        if (flag) {

            int area = B * H;

            System.out.println(area);
        }
    }
}
````

---

## Python Solution

```python
try:
    B = int(input())
    H = int(input())

    if B <= 0 or H <= 0:
        raise Exception("Breadth and height must be positive")

    area = B * H
    print(area)

except Exception as e:
    print("java.lang.Exception:", e)
```

---

## JavaScript Solution

```javascript
const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const B = input[0];
const H = input[1];

if (B <= 0 || H <= 0) {
    console.log("java.lang.Exception: Breadth and height must be positive");
} else {
    console.log(B * H);
}
```

---

# 3. Clear Explanation

This problem teaches two important concepts:

1. **Static initializer blocks (Java)**
2. **Input validation**

---

# Step 1: Understanding the Area Formula

The area of a parallelogram is:

```
Area = Breadth × Height
```

Example:

```
B = 5
H = 4
```

Calculation:

```
Area = 5 × 4 = 20
```

---

# Step 2: Validation Condition

Before calculating the area, we must ensure:

```
B > 0
H > 0
```

If this condition fails, the program must print:

```
java.lang.Exception: Breadth and height must be positive
```

Example invalid input:

```
B = -2
H = 5
```

Output:

```
java.lang.Exception: Breadth and height must be positive
```

---

# Step 3: Static Block in Java

A **static block** runs **before the main method**.

Example:

```java
static {
   // code executes before main()
}
```

In this problem, the static block:

1. Reads input
2. Validates values
3. Sets a flag if input is invalid

---

# Step 4: Using a Flag

We use a boolean variable:

```
flag = true
```

If invalid values occur:

```
flag = false
```

Then in `main()` we check:

```
if(flag)
```

Only then do we calculate the area.

---

# Execution Flow

```
Program Start
     |
Static Block Executes
     |
Read B and H
     |
Check if B <= 0 or H <= 0
     |
     ├── Yes → Print Exception
     |
     └── No → Continue
              |
             main()
              |
           Calculate Area
              |
           Print Area
```

---

# Example Walkthrough

### Input

```
B = 4
H = 7
```

Static block validation:

```
4 > 0 and 7 > 0 ✔
```

Area:

```
4 × 7 = 28
```

Output:

```
28
```

---

# Key Concepts Learned

* Static initializer blocks
* Input validation
* Exception-like error handling
* Boolean flags
* Program execution order in Java

This problem is important because it demonstrates **how static blocks execute before the main method**, which is a key concept in Java program initialization.
---


# HackerRank – Java Int to String

## 1. Problem

You are given an integer **n**.  
Your task is to convert this integer into a **string**.

After converting the integer to a string, check if converting the string back to an integer produces the **same value** as the original integer.

If the values match, print:

```

Good job

```

Otherwise, print:

```

Wrong answer

```

### Input Format

A single integer **n**.

### Constraints

```

-100 ≤ n ≤ 100

```

### Output Format

Print **"Good job"** if the conversion from integer to string works correctly; otherwise print **"Wrong answer"**.

### Sample Input

```

100

```

### Sample Output

```

Good job

````

---

# 2. Answer

## Java Solution

```java
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        int number = scan.nextInt();

        String s = String.valueOf(number);

        if (Integer.parseInt(s) == number) {
            System.out.println("Good job");
        } else {
            System.out.println("Wrong answer");
        }

        scan.close();
    }
}
````

---

## Python Solution

```python
n = int(input())

s = str(n)

if int(s) == n:
    print("Good job")
else:
    print("Wrong answer")
```

---

## JavaScript Solution

```javascript
const fs = require("fs");

const n = parseInt(fs.readFileSync(0, "utf8").trim());

const s = String(n);

if (parseInt(s) === n) {
    console.log("Good job");
} else {
    console.log("Wrong answer");
}
```

---

# 3. Clear Explanation

This problem demonstrates **type conversion** between integers and strings.

Programming languages allow converting values between different data types.

In this problem:

1. Convert an **integer → string**
2. Convert the **string → integer**
3. Check if the values remain the same.

---

# Step 1: Convert Integer to String

Example:

```
number = 123
```

Convert to string:

```
"123"
```

### Java

```java
String s = String.valueOf(number);
```

### Python

```python
s = str(number)
```

### JavaScript

```javascript
let s = String(number);
```

---

# Step 2: Convert String Back to Integer

Now convert the string back into a number.

Example:

```
"123" → 123
```

### Java

```java
Integer.parseInt(s)
```

### Python

```python
int(s)
```

### JavaScript

```javascript
parseInt(s)
```

---

# Step 3: Compare Values

We check whether:

```
converted_integer == original_integer
```

Example:

```
123 == 123 → true
```

So the program prints:

```
Good job
```

---

# Example Walkthrough

### Input

```
42
```

Step 1: Convert to string

```
"42"
```

Step 2: Convert back to integer

```
42
```

Step 3: Compare

```
42 == 42 ✔
```

Output:

```
Good job
```

---

# Alternative Ways to Convert Integer to String (Java)

Java provides several methods to convert integers to strings.

### Method 1

```java
String s = String.valueOf(number);
```

### Method 2

```java
String s = Integer.toString(number);
```

### Method 3

```java
String s = "" + number;
```

### Method 4

```java
String s = String.format("%d", number);
```

All of these produce the same result.

---

# Key Concepts Learned

* Data type conversion
* Integer to string conversion
* String to integer conversion
* Input and output handling
* Validation using conditional statements

This problem is important because **type conversion is frequently used in real-world programming and data processing tasks**.


# Java Date and Time

## 1. Problem

You are given a **date** consisting of three integers:

- **month**
- **day**
- **year**

Your task is to determine the **day of the week** for that date.

The result must be printed in **uppercase letters**.

### Input Format

A single line containing three space-separated integers:

```

month day year

```

### Constraints

```

1 ≤ month ≤ 12
1 ≤ day ≤ 31
2000 ≤ year ≤ 3000

```

### Output Format

Print the **day of the week** in uppercase.

### Sample Input

```

08 05 2015

```

### Sample Output

```

WEDNESDAY

````

---

# 2. Answer

## Java Solution

```java
import java.time.LocalDate;

class Result {

    public static String findDay(int month, int day, int year) {

        LocalDate date = LocalDate.of(year, month, day);

        return date.getDayOfWeek().toString();
    }
}

public class Solution {

    public static void main(String[] args) throws Exception {

        java.util.Scanner sc = new java.util.Scanner(System.in);

        int month = sc.nextInt();
        int day = sc.nextInt();
        int year = sc.nextInt();

        System.out.println(Result.findDay(month, day, year));

        sc.close();
    }
}
````

---

## Python Solution

```python
import datetime

month, day, year = map(int, input().split())

date = datetime.date(year, month, day)

print(date.strftime("%A").upper())
```

---

## JavaScript Solution

```javascript
const fs = require("fs");

const [month, day, year] = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const date = new Date(year, month - 1, day);

const days = [
    "SUNDAY",
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY"
];

console.log(days[date.getDay()]);
```

---

# 3. Clear Explanation

This problem requires determining the **day of the week** for a given date.

Most programming languages provide **built-in date libraries**, which make this task easier.

---

# Step 1: Understand the Input

Input example:

```
8 5 2015
```

Meaning:

```
Month = 8 (August)
Day = 5
Year = 2015
```

We need to determine which weekday corresponds to **August 5, 2015**.

Result:

```
WEDNESDAY
```

---

# Step 2: Use Date Libraries

Instead of manually calculating the weekday, programming languages provide **date/time APIs**.

These libraries handle:

* leap years
* calendar calculations
* weekday determination

---

# Java Explanation

Java uses the **java.time** package.

Create a date object:

```java
LocalDate date = LocalDate.of(year, month, day);
```

Example:

```
LocalDate.of(2015, 8, 5)
```

Get the weekday:

```java
date.getDayOfWeek()
```

This returns:

```
WEDNESDAY
```

Convert to string:

```java
.toString()
```

Which already returns uppercase.

---

# Python Explanation

Python uses the **datetime module**.

Create the date:

```python
datetime.date(year, month, day)
```

Get weekday name:

```python
strftime("%A")
```

Example result:

```
Wednesday
```

Convert to uppercase:

```python
.upper()
```

Final output:

```
WEDNESDAY
```

---

# JavaScript Explanation

JavaScript uses the **Date object**.

Create date:

```javascript
new Date(year, month - 1, day)
```

Important detail:

JavaScript months are **0-based**.

```
0 = January
1 = February
...
7 = August
```

Get weekday index:

```javascript
date.getDay()
```

Return values:

```
0 = Sunday
1 = Monday
2 = Tuesday
3 = Wednesday
4 = Thursday
5 = Friday
6 = Saturday
```

Use an array to map values to weekday names.

---

# Example Walkthrough

Input:

```
08 05 2015
```

Processing:

```
Date → August 5, 2015
```

Calendar lookup:

```
Wednesday
```

Output:

```
WEDNESDAY
```

---

# Key Concepts Learned

* Working with **dates**
* Using **date/time libraries**
* Formatting date outputs
* Handling different date implementations across languages

This problem helps developers understand how to use **built-in date APIs instead of manually calculating calendar values**.





















