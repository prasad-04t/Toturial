
# Java 1D Array

## 1. Problem

You are given an integer **n**, followed by **n integers**.  
Your task is to store these integers in a **1-dimensional array** and then print each element of the array on a **new line**.

### Input Format

```

n
a1 a2 a3 ... an

```

Where:

- **n** → number of elements in the array  
- **a1, a2, a3, ... an** → integer values stored in the array

### Constraints

```

1 ≤ n ≤ 1000
0 ≤ ai ≤ 10^9

```

### Output Format

Print each element of the array **in the same order** as input, each on a new line.

### Sample Input

```

5
10 20 30 40 50

```

### Sample Output

```

10
20
30
40
50

````

---

# 2. Answer

## Java Solution

```java
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();

        int[] a = new int[n];

        for (int j = 0; j < n; j++) {
            a[j] = scan.nextInt();
        }

        scan.close();

        for (int i = 0; i < a.length; i++) {
            System.out.println(a[i]);
        }
    }
}
````

---

## Python Solution

```python
n = int(input())

arr = list(map(int, input().split()))

for i in range(n):
    print(arr[i])
```

---

## JavaScript Solution

```javascript
const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

let n = input[0];

let arr = input.slice(1, n + 1);

for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}
```

---

# 3. Clear Explanation

This problem introduces the concept of a **1D array (one-dimensional array)**.

An array is a data structure that stores **multiple values in a single variable**.

---

## Step 1: Understand the Input

Example input:

```
5
10 20 30 40 50
```

Meaning:

```
n = 5
```

Array elements:

```
[10, 20, 30, 40, 50]
```

---

## Step 2: Create an Array

In Java:

```
int[] a = new int[n];
```

This creates an array that can store **n integers**.

Memory representation:

| Index | Value |
| ----- | ----- |
| 0     | 10    |
| 1     | 20    |
| 2     | 30    |
| 3     | 40    |
| 4     | 50    |

---

## Step 3: Store Values in the Array

We use a **loop** to read each value.

Example:

```
for (int j = 0; j < n; j++)
```

Each iteration stores one element.

```
a[j] = scan.nextInt();
```

---

## Step 4: Print the Array

To print each element:

```
for (int i = 0; i < a.length; i++)
```

Then display the value:

```
System.out.println(a[i]);
```

Output:

```
10
20
30
40
50
```

---

## Python Explanation

Python uses a **list** instead of a fixed-size array.

```
arr = list(map(int, input().split()))
```

This reads all numbers and stores them in a list.

Example:

```
[10, 20, 30, 40, 50]
```

Loop through the list:

```
for i in range(n):
```

---

## JavaScript Explanation

JavaScript arrays are dynamic.

Read input:

```
const input = fs.readFileSync(0, "utf8")
```

Extract numbers:

```
let arr = input.slice(1, n + 1);
```

Print using:

```
console.log(arr[i]);
```

---

# Example Walkthrough

Input:

```
3
5 8 9
```

Array:

```
[5, 8, 9]
```

Processing:

```
print arr[0]
print arr[1]
print arr[2]
```

Output:

```
5
8
9
```

---

# Time Complexity

Reading input:

```
O(n)
```

Printing array:

```
O(n)
```

Total complexity:

```
O(n)
```

---

# Key Concepts Learned

* 1D arrays
* Array indexing
* Reading input into arrays
* Iterating through arrays using loops
* Printing array elements

This problem is important because arrays are one of the **most fundamental data structures in programming and algorithm design**.


# Subarrays and Negative Subarray Count

## 1. Problem

You are given an array of integers. Your task involves understanding **subarrays** and solving a common algorithm problem: **counting the number of subarrays whose sum is negative**.

Two related concepts are demonstrated in the provided code:

1. **Generate all possible subarrays** of an array.
2. **Count how many subarrays have a negative sum.**

A **subarray** is a **contiguous part of an array**.

Example:

Array:

```

[1, 2, 3]

```

Subarrays:

```

[1]
[1,2]
[1,2,3]
[2]
[2,3]
[3]

```

If the array contains negative numbers, we can compute the **sum of each subarray** and count how many sums are **negative**.

Example:

```

Input
5
1 -2 4 -5 1

```

Possible subarrays and sums:

```

[1] -> 1
[1,-2] -> -1  (negative)
[1,-2,4] -> 3
[1,-2,4,-5] -> -2 (negative)
[1,-2,4,-5,1] -> -1 (negative)
[-2] -> -2 (negative)
[-2,4] -> 2
[-2,4,-5] -> -3 (negative)
[-2,4,-5,1] -> -2 (negative)
[4] -> 4
[4,-5] -> -1 (negative)
[4,-5,1] -> 0
[-5] -> -5 (negative)
[-5,1] -> -4 (negative)
[1] -> 1

````

Total **negative subarrays = 9**

This is a common **HackerRank problem** used to test understanding of **arrays, loops, and cumulative sums**.

---

# 2. Answer

## Java Solution

```java
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] arr = new int[n];

        int count = 0;

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        for (int start = 0; start < n; start++) {

            int sum = 0;

            for (int end = start; end < n; end++) {

                sum += arr[end];

                if (sum < 0) {
                    count++;
                }
            }
        }

        System.out.println(count);

        sc.close();
    }
}
````

---

## Python Solution

```python
n = int(input())

arr = list(map(int, input().split()))

count = 0

for start in range(n):

    total = 0

    for end in range(start, n):

        total += arr[end]

        if total < 0:
            count += 1

print(count)
```

---

## JavaScript Solution

```javascript
const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

let index = 0;

const n = input[index++];

const arr = input.slice(index, index + n);

let count = 0;

for (let start = 0; start < n; start++) {

    let sum = 0;

    for (let end = start; end < n; end++) {

        sum += arr[end];

        if (sum < 0) {
            count++;
        }
    }
}

console.log(count);
```

---

# 3. Clear Explanation

## Step 1: Understand What a Subarray Is

A **subarray** is a continuous sequence of elements inside an array.

Example:

```
Array = [1,2,3]
```

Subarrays:

| Start | End | Subarray |
| ----- | --- | -------- |
| 0     | 0   | [1]      |
| 0     | 1   | [1,2]    |
| 0     | 2   | [1,2,3]  |
| 1     | 1   | [2]      |
| 1     | 2   | [2,3]    |
| 2     | 2   | [3]      |

Total subarrays formula:

```
n(n+1)/2
```

Example:

```
n = 3
3(4)/2 = 6
```

---

# Step 2: Generate All Subarrays

We use **two loops**.

Outer loop → starting index
Inner loop → ending index

```
for start = 0 → n-1
   for end = start → n-1
```

Example:

```
start = 0
end = 0 → [1]
end = 1 → [1,2]
end = 2 → [1,2,3]
```

Then:

```
start = 1
end = 1 → [2]
end = 2 → [2,3]
```

---

# Step 3: Calculate Subarray Sum Efficiently

Instead of recalculating the sum each time, we **incrementally add elements**.

Example:

```
sum = 0
```

First iteration:

```
sum = sum + arr[end]
```

Example:

```
arr = [1,-2,4]

start = 0

end = 0 → sum = 1
end = 1 → sum = -1
end = 2 → sum = 3
```

---

# Step 4: Check if Sum is Negative

Condition:

```
if(sum < 0)
```

Then increase counter:

```
count++
```

This keeps track of **how many negative subarrays exist**.

---

# Step 5: Print Final Count

After checking all subarrays:

```
print(count)
```

---

# Example Walkthrough

Input:

```
n = 3
arr = [1,-2,4]
```

Subarrays:

```
[1] -> 1
[1,-2] -> -1 ✔
[1,-2,4] -> 3
[-2] -> -2 ✔
[-2,4] -> 2
[4] -> 4
```

Negative sums:

```
[1,-2]
[-2]
```

Output:

```
2
```

---

# Algorithm Complexity

Let:

```
n = array size
```

Subarrays generated:

```
n(n+1)/2
```

Time complexity:

```
O(n²)
```

Space complexity:

```
O(n)
```

This approach works well because **n ≤ 100 in HackerRank constraints**.

---

# Key Concepts Learned

* Subarrays
* Nested loops
* Incremental sum technique
* Counting negative sums
* Array traversal
* Algorithm complexity

This problem is frequently asked in **coding interviews and HackerRank practice**, especially for mastering **array traversal and nested loop logic**.




