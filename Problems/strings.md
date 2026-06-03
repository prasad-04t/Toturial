# Python String Manipulation Code Snippets and Their Outputs

Below is a collection of Python code snippets, each followed by a description of what it does and the expected output when executed.


### 1. Reverse a Name Using Loop (prepending)
```python
def reverse_name(name):
    rev = ""
    for ch in name:
        rev = ch + rev
    return rev

print(reverse_name("prasad"))
```
**Output:**
```
dasarp
```
**Explanation:** The loop builds the reversed string by prepending each character, so `"prasad"` becomes `"dasarp"`.

### 2. Reverse a String Using Slicing
```python
def reverse_string(name):
    return name[::-1]

print(reverse_string("Prasad"))
```
**Output:**
```
dasarP
```
**Explanation:** `[::-1]` slices the string in reverse order. Note that case is preserved.


### 3. Reverse Using `reversed()` and `join`
```python
def reverse_string(name):
    rev = reversed(name)
    return ''.join(rev)

print(reverse_string("prasad"))
```
**Output:**
```
dasarp
```
**Explanation:** `reversed(name)` returns an iterator of characters in reverse order, which `join` combines into a string.



### 4. Split a Sentence and Return the List of Words
```python
def reverse_string(sentence):
    word = sentence.split()
    return word

print(reverse_string("I am prasad"))
```
**Output:**
```
['I', 'am', 'prasad']
```
**Explanation:** `split()` without arguments splits on whitespace and returns a list of words.



### 5. Reverse the Order of Words (List)
```python
def reverse_string(sentence):
    word = sentence.split()
    rev_word = word[::-1]
    return rev_word

print(reverse_string("I am prasad"))
```
**Output:**
```
['prasad', 'am', 'I']
```
**Explanation:** The list of words is reversed, so the words appear in reverse order.



### 6. Reverse Word Order and Join Into a String
```python
def reverse_string(sentence):
    word = sentence.split()
    rev_word = word[::-1]
    return " ".join(rev_word)

print(reverse_string("I am prasad"))
```
**Output:**
```
prasad am I
```
**Explanation:** The reversed list of words is joined with spaces, resulting in a sentence with reversed word order.



### 7. Reverse Each Word Individually
```python
def reverse_string(sentence):
    word = sentence.split()
    return ' '.join(w[::-1] for w in word)

print(reverse_string("I am prasad"))
```
**Output:**
```
I ma dasarp
```
**Explanation:** Every word is reversed (characters inside each word flipped), but word order stays the same.



### 8. Reverse Each Word Using `reversed()` Inside `join`
```python
def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(''.join(reversed(word)) for word in words)

print(reverse_words("I am Prasad"))
```
**Output:**
```
I ma dasarP
```
**Explanation:** Same as previous, using `reversed()` per word. Case is preserved.



### 9. Reverse Each Word With Manual Loop
```python
def reverse_words(sentence):
    result = ""
    word = ""
    for ch in sentence:
        if ch != " ":
            word = ch + word   # build reversed word
        else:
            result += word + " "
            word = ""          # reset for next word
    result += word   # add last word
    return result

print(reverse_words("I am Prasad"))
```
**Output:**
```
I ma dasarP
```
**Explanation:** Manually builds reversed words character by character.



### 10. Palindrome Check Using Slicing
```python
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("Prasad"))
```
**Output:**
```
False
```
**Explanation:** `"Prasad"` reversed is `"dasarP"`, so they are not equal.



### 11. Palindrome Check Using `reversed()`
```python
def is_palindrome(s):
    rev_string = "".join(reversed(s))
    return s == rev_string

print(is_palindrome("madam"))
```
**Output:**
```
True
```
**Explanation:** `"madam"` reads the same forward and backward.



### 12. Palindrome Check With Manual Loop
```python
def is_palindrome(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev == s

print(is_palindrome("madam"))
```
**Output:**
```
True
```
**Explanation:** Same logic as the slice version but built manually.



### 13. Progressively Printing Reversed Name (prepending)
```python
def reverse_name(name):
    rev = ""
    for ch in name:
        rev = ch + rev
        print(rev)

reverse_name("prasad")
```
**Output:**
```
p
rp
arp
sarp
asarp
dasarp
```
**Explanation:** Each line shows the reversed string after adding one character from the original input (left to right). The final reversed string is `dasarp`.



### 14. Progressively Printing Name (appending)
```python
def reverse_name(name):
    rev = ""
    for ch in name:
        rev = rev + ch
        print(rev)

reverse_name("prasad")
```
**Output:**
```
p
pr
pra
pras
prasa
prasad
```
**Explanation:** Characters are appended, so the output shows the original string built step by step.


### 15. Building Reversed Name From Pre-reversed String
```python
def reverse_name(name):
    rev_name = name[::-1]
    rev = ""
    for ch in rev_name:
        rev = rev + ch
        print(rev)

reverse_name("prasad")
```
**Output:**
```
d
da
das
dasa
dasar
dasarp
```
**Explanation:** The name is first reversed, then the loop builds it back character by character, printing each intermediate step.


### 16. Character Frequency Using Dictionary
```python
def char_count(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    return count

print(char_count("prasad"))
```
**Output:**
```
{'p': 1, 'r': 1, 'a': 2, 's': 1, 'd': 1}
```
**Explanation:** A dictionary of character frequencies is returned and printed.


### 17. Character Frequency Using `Counter`
```python
from collections import Counter

def count_character_frequency(string):
    dict = Counter(string)
    for key, value in dict.items():
         print(f"{key} : {value}")

count_character_frequency("prasad")
```
**Output:**
```
p : 1
r : 1
a : 2
s : 1
d : 1
```
**Explanation:** `Counter` creates a frequency map; then each character and its count are printed line by line.


### 18. Remove Duplicates (Preserving Order, String Concatenation)
```python
def remove_duplicates(s):
    result = ""
    for ch in s:
        if ch not in result:
            result += ch
    return result

print(remove_duplicates("prasad"))
```
**Output:**
```
prasd
```
**Explanation:** Only the first occurrence of each character is kept, preserving original order.


### 19. Remove Duplicates Using a Set and String Building
```python
def remove_duplicates(s):
    seen = set()
    result = ""
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result += ch
    return result

print(remove_duplicates("prasad"))
```
**Output:**
```
prasd
```
**Explanation:** Same as above, using a set to track seen characters.


### 20. Remove Duplicates Using List and Join
```python
def remove_duplicates(s):
    seen = set()
    result = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return "".join(result)

print(remove_duplicates("prasad"))
```
**Output:**
```
prasd
```
**Explanation:** Characters are collected in a list and then joined; order is preserved.



### 21. Remove Duplicates by Joining Set Directly (Order May Vary)
```python
def remove_duplicates(s):
    seen = set()
    for ch in s:
        if ch not in seen:
            seen.add(ch)
    return "".join(seen)

print(remove_duplicates("prasad"))
```
**Output:**  
An arbitrary permutation of `'p','r','a','s','d'`, for example:
```
prasd
```
or
```
raspd
```
**Explanation:** Sets do not guarantee insertion order (before Python 3.7) or may vary across implementations; thus the output may reorder characters. The exact output depends on the Python version and runtime.


### 22. Anagram Check Using Sorted
```python
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("prasad", "sadpra"))
```
**Output:**
```
True
```
**Explanation:** Both strings contain the same characters (`a,a,d,p,r,s`), so they are anagrams.


### 23. Finding Duplicate Characters
```python
def duplicates(s):
    seen = set()
    dup = set()
    for ch in s:
        if ch in seen:
            dup.add(ch)
        else:
            seen.add(ch)
    return "".join(dup)

print(duplicates("prasadrs"))
```
**Output:**  
A string of duplicate characters, likely (but order not guaranteed from set):
```
ars
```
or a different order like `"sra"`.  
**Explanation:** Characters that appear more than once are collected. In `"prasadrs"`, `a`, `r`, and `s` appear at least twice. The output is a string formed from a set, so the order may vary.

### 24. First Non-repeating Character (Manual Frequency)
```python
def first_non_repeating(s):
    count = {}
    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    for ch in s:
        if count[ch] == 1:
            return ch
    return None

print(first_non_repeating("aabbcde"))
```
**Output:**
```
c
```
**Explanation:** The first character with frequency 1 is `c`.


### 25. First Non-repeating Character Using `Counter`
```python
from collections import Counter

def first_non_repeating(s):
    freq = Counter(s)
    for ch in s:
        if freq[ch] == 1:
            return ch

print(first_non_repeating("prasad"))
```
**Output:**
```
p
```
**Explanation:** `p` has a count of 1 and appears first.


### 26. Custom Reverse – Reverse Middle Words Only
```python
def custom_reverse(sentence):
    words = sentence.split()
    result = []

    for i in range(len(words)):
        if i == 0 or i == len(words) - 1:
            result.append(words[i])
        elif len(words[i]) > 3:
            word = words[i]
            rev_word = word[::-1]
            result.append(rev_word)
        else:
            result.append(words[i])

    return ' '.join(result)

print(custom_reverse("I am quality engineer in accenture"))
```
**Output:**
```
I am ytilauq reenigne in accenture
```
**Explanation:** First and last words are kept unchanged. Middle words longer than 3 characters are reversed (`quality` -> `ytilauq`, `engineer` -> `reenigne`). Words with length 3 or less remain as is.


### 27. Same Custom Reverse Without Extra Variable
```python
def custom_reverse(sentence):
    words = sentence.split()
    result = []

    for i in range(len(words)):
        if i == 0 or i == len(words) - 1:
            result.append(words[i])
        elif len(words[i]) > 3:
            result.append(words[i][::-1])
        else:
            result.append(words[i])

    return ' '.join(result)

print(custom_reverse("I am quality engineer in accenture"))
```
**Output:**
```
I am ytilauq reenigne in accenture
```
**Explanation:** Functionally identical to the previous snippet.

### 28. Most Common Character Using `Counter`
```python
from collections import Counter

def most_common_char(s):
    c = Counter(s)
    return c.most_common(1)[0]

print(most_common_char("aabbccaa"))
```
**Output:**
```
('a', 4)
```
**Explanation:** `most_common(1)` returns a list with one tuple: `('a', 4)`, which is the most frequent character and its count.


### 29. Reverse Words at Odd Indices Only
```python
def reverse_by_position(sentence):
    words = sentence.split()
    result = []

    for i in range(len(words)):
        if i % 2 == 1:   # odd index
            result.append(words[i][::-1])
        else:
            result.append(words[i])

    return ' '.join(result)

print(reverse_by_position("I am learning python"))
```
**Output:**
```
I ma learning nohtyp
```
**Explanation:** Words at index 1 (`am` -> `ma`) and index 3 (`python` -> `nohtyp`) are reversed; others remain unchanged.


### 30. Mask Words (Hide Middle Characters)
```python
def mask_words(sentence):
    words = sentence.split()
    result = []

    for word in words:
        if len(word) <= 2:
            result.append(word)
        else:
            masked = word[0] + '*' * (len(word) - 2) + word[-1]
            result.append(masked)

    return " ".join(result)

print(mask_words("T Sam Prasad"))
```
**Output:**
```
T S*m P****d
```
**Explanation:** Words with more than two characters get their middle characters replaced by asterisks, keeping the first and last character: `Sam` -> `S*m`, `Prasad` -> `P****d`. `T` stays unchanged.


### 31. Reverse Odd-Indexed Words and Mask All Words
```python
def reverse_and_mask(sentence):
    words = sentence.split()
    result = []

    for i in range(len(words)):
        word = words[i]

        if i % 2 == 1:
            word = word[::-1]

        if len(word) > 2:
            word = word[0] + '*' * (len(word) - 2) + word[-1]

        result.append(word)

    return ' '.join(result)

print(reverse_and_mask("T Sam Prasad"))
```
**Output:**
```
T m*S P****d
```
**Explanation:**  
- Index 0 `"T"` unchanged -> `"T"`.  
- Index 1 `"Sam"` reversed to `"maS"`, then masked to `"m*S"`.  
- Index 2 `"Prasad"` unchanged (even index), then masked to `"P****d"`.  

### 32. Anagram Check Using `sorted()` – Revisited
```python
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))  # True
print(is_anagram("prasad", "sad"))     # False
```
**Output:**
```
True
False
```
**Explanation:** `"listen"` and `"silent"` have identical sorted character lists. `"prasad"` and `"sad"` do not.


### 33. Anagram Check Using `Counter`
```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

print(is_anagram("listen", "silent"))  # True
print(is_anagram("prasad", "sardar"))  # False
```
**Output:**
```
True
False
```
**Explanation:** The comment in the original code suggested `True` for `("prasad", "sardar")`, but the correct result is `False` because the character counts differ (`"prasad"` has one `r`, `"sardar"` has two `r`s). The output reflects this.


### 34. Group Anagrams Together
```python
from collections import defaultdict

def group_anagrams(words):
    d = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        d[key].append(word)
    return list(d.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
```
**Output:**
```
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```
**Explanation:** Words that are anagrams share the same sorted character key and are grouped into lists. The order of groups may vary, but the content is as shown.


### 35. Word Count and Print Frequency (Function Returns None)
```python
from collections import Counter

def word_count(sentence):
    words = sentence.split()
    words_with_frequency = Counter(words)
    for word, freq in words_with_frequency.items():
        print(f"{word}:{freq}")

print(word_count("I am sam prasad"))
```
**Output:**
```
I:1
am:1
sam:1
prasad:1
None
```
**Explanation:** The function prints each word and its count, but does not return a value (returns `None`). The outer `print(word_count(...))` prints `None` after all the word counts are displayed.


















































# Java Strings Introduction

## 1. Problem

You are given two strings **A** and **B**.  
Your task is to perform the following operations:

1. Print the **sum of the lengths** of both strings.
2. Determine if **A is lexicographically greater than B**.  
   - If **A > B**, print `Yes`
   - Otherwise, print `No`
3. Print both strings with their **first letter capitalized** and separated by a space.

### Input Format

Two lines of input:

```

A
B

```

Where:

- **A** is the first string
- **B** is the second string

### Constraints

```

1 ≤ length of A, B ≤ 1000
A and B consist only of lowercase English letters.

```

### Sample Input

```

hello
java

```

### Sample Output

```

9
No
Hello Java

````

---

# 2. Answer

## Java Solution

```java
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);

        String word1 = s.nextLine();
        String word2 = s.nextLine();

        int sum = word1.length() + word2.length();
        System.out.println(sum);

        if (word1.compareTo(word2) > 0) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

        String cap1 = word1.substring(0,1).toUpperCase() + word1.substring(1);
        String cap2 = word2.substring(0,1).toUpperCase() + word2.substring(1);

        System.out.println(cap1 + " " + cap2);

        s.close();
    }
}
````

---

## Python Solution

```python
A = input().strip()
B = input().strip()

# Sum of lengths
print(len(A) + len(B))

# Lexicographical comparison
if A > B:
    print("Yes")
else:
    print("No")

# Capitalize first letter
A_cap = A[0].upper() + A[1:]
B_cap = B[0].upper() + B[1:]

print(A_cap + " " + B_cap)
```

---

## JavaScript Solution

```javascript
const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split("\n");

const A = input[0];
const B = input[1];

// Sum of lengths
console.log(A.length + B.length);

// Lexicographical comparison
if (A > B) {
    console.log("Yes");
} else {
    console.log("No");
}

// Capitalize first letters
const capA = A.charAt(0).toUpperCase() + A.slice(1);
const capB = B.charAt(0).toUpperCase() + B.slice(1);

console.log(capA + " " + capB);
```

---

# 3. Clear Explanation

This problem focuses on **basic string operations**, including:

* Finding string length
* Comparing strings lexicographically
* Manipulating characters in strings

---

# Step 1: Calculate the Sum of String Lengths

We compute:

```
length(A) + length(B)
```

Example:

```
A = "hello" → length = 5
B = "java" → length = 4
```

Result:

```
5 + 4 = 9
```

Output:

```
9
```

---

# Step 2: Lexicographical Comparison

Lexicographical order is **dictionary order**.

Example:

```
apple < banana
cat > ball
```

Comparison is done character by character using **ASCII values**.

Example:

```
"hello" vs "java"
```

Compare first characters:

```
h (ASCII 104)
j (ASCII 106)
```

Since:

```
104 < 106
```

Therefore:

```
hello < java
```

Output:

```
No
```

---

# Step 3: Capitalize the First Letter

We convert the first character to **uppercase** and keep the remaining characters unchanged.

Example:

```
hello → Hello
java → Java
```

### Java

```
word.substring(0,1).toUpperCase() + word.substring(1)
```

### Python

```
word[0].upper() + word[1:]
```

### JavaScript

```
word.charAt(0).toUpperCase() + word.slice(1)
```

---

# Example Walkthrough

Input:

```
hello
java
```

Step 1: Length sum

```
5 + 4 = 9
```

Step 2: Lexicographic comparison

```
hello < java → No
```

Step 3: Capitalization

```
Hello Java
```

Final Output:

```
9
No
Hello Java
```

---

# Key Concepts Learned

* String length calculation
* Lexicographical comparison
* String manipulation
* Character case conversion
* Basic input/output handling

This problem helps beginners understand **fundamental string operations used frequently in programming and interview questions**.
---

# Java Strings Introduction (Without Using Substring)

## 1. Problem

You are given two strings **A** and **B**. Perform the following operations:

1. Print the **sum of the lengths** of both strings.
2. Determine whether **A is lexicographically greater than B**.
   - If **A > B**, print **Yes**
   - Otherwise print **No**
3. Print both strings with their **first letter capitalized**, separated by a space.

In this variation, the capitalization in Java should be done **without using the `substring()` method**.

### Input Format

Two lines of input:

```

A
B

```

Where:

- **A** is the first string
- **B** is the second string

### Constraints

```

1 ≤ length(A), length(B) ≤ 1000
A and B consist only of lowercase English letters.

```

### Sample Input

```

hello
java

```

### Sample Output

```

9
No
Hello Java

````

---

# 2. Answer

## Java Solution

```java
import java.util.*;

public class Solution {
    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);

        String word1 = s.nextLine();
        String word2 = s.nextLine();

        // 1. Sum of lengths
        int sum = word1.length() + word2.length();
        System.out.println(sum);

        // 2. Lexicographic comparison
        if (word1.compareTo(word2) > 0) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

        // 3. Capitalize first letter without substring
        char[] arr1 = word1.toCharArray();
        arr1[0] = Character.toUpperCase(arr1[0]);
        String cap1 = new String(arr1);

        char[] arr2 = word2.toCharArray();
        arr2[0] = Character.toUpperCase(arr2[0]);
        String cap2 = new String(arr2);

        System.out.println(cap1 + " " + cap2);

        s.close();
    }
}
````

---

## Python Solution

```python
A = input().strip()
B = input().strip()

# 1. Sum of lengths
print(len(A) + len(B))

# 2. Lexicographic comparison
if A > B:
    print("Yes")
else:
    print("No")

# 3. Capitalize first letter
A_list = list(A)
A_list[0] = A_list[0].upper()
A_cap = "".join(A_list)

B_list = list(B)
B_list[0] = B_list[0].upper()
B_cap = "".join(B_list)

print(A_cap + " " + B_cap)
```

---

## JavaScript Solution

```javascript
const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split("\n");

let A = input[0];
let B = input[1];

// 1. Sum of lengths
console.log(A.length + B.length);

// 2. Lexicographic comparison
if (A > B) {
    console.log("Yes");
} else {
    console.log("No");
}

// 3. Capitalize first letter
let arrA = A.split("");
arrA[0] = arrA[0].toUpperCase();
let capA = arrA.join("");

let arrB = B.split("");
arrB[0] = arrB[0].toUpperCase();
let capB = arrB.join("");

console.log(capA + " " + capB);
```

---

# 3. Clear Explanation

This problem focuses on **string manipulation and comparison**.

You must perform three main tasks:

1. Calculate string lengths
2. Compare strings lexicographically
3. Modify the first character of a string

---

## Step 1: Calculate the Sum of String Lengths

Every string has a **length**, which represents the number of characters.

Example:

```
A = "hello"
B = "java"
```

Lengths:

```
length(A) = 5
length(B) = 4
```

Sum:

```
5 + 4 = 9
```

Output:

```
9
```

---

## Step 2: Lexicographic Comparison

Lexicographic order is **dictionary order**.

Example dictionary order:

```
apple
banana
cat
dog
```

Strings are compared **character by character** using ASCII/Unicode values.

Example:

```
hello vs java
```

First characters:

```
h → ASCII 104
j → ASCII 106
```

Since:

```
104 < 106
```

We conclude:

```
hello < java
```

Therefore the output is:

```
No
```

---

## Step 3: Capitalize the First Letter

We convert the **first character** of each string to uppercase.

Example:

```
hello → Hello
java → Java
```

Instead of using `substring()`, we convert the string into a **character array**.

### Java Example

```
char[] arr = word.toCharArray();
arr[0] = Character.toUpperCase(arr[0]);
String result = new String(arr);
```

Steps:

1. Convert string → char array
2. Modify first character
3. Convert array → string

---

## Example Walkthrough

Input:

```
hello
java
```

Step 1: Length sum

```
5 + 4 = 9
```

Step 2: Lexicographic comparison

```
hello < java → No
```

Step 3: Capitalization

```
Hello Java
```

Final Output:

```
9
No
Hello Java
```

---

# Key Concepts Learned

* String length calculation
* Lexicographical string comparison
* Character array manipulation
* Converting between strings and arrays
* Basic input/output operations

This problem is commonly used to strengthen understanding of **string handling and character manipulation**, which are essential skills in programming and technical interviews.


# Java Substring

## 1. Problem

You are given a **string `S`** and two integers:

- **start**
- **end**

Your task is to print the **substring of `S`** starting from index **start** and ending at index **end - 1**.

The substring operation follows this rule:

```

substring(start, end)

```

- **start** → inclusive index  
- **end** → exclusive index  

This means the character at position **start** is included, but the character at position **end** is **not included**.

### Input Format

```

S
start
end

```

Where:

- `S` → a string
- `start` → starting index
- `end` → ending index (exclusive)

### Constraints

```

0 ≤ start < end ≤ length(S)
S consists of lowercase English letters.

```

### Sample Input

```

Helloworld
3
7

```

### Sample Output

```

lowo

````

---

# 2. Answer

## Java Solution

```java
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        String S = in.next();
        int start = in.nextInt();
        int end = in.nextInt();

        System.out.println(S.substring(start, end));

        in.close();
    }
}
````

---

## Python Solution

```python
S = input().strip()
start = int(input())
end = int(input())

print(S[start:end])
```

---

## JavaScript Solution

```javascript
const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/);

const S = input[0];
const start = parseInt(input[1]);
const end = parseInt(input[2]);

console.log(S.substring(start, end));
```

---

# 3. Clear Explanation

This problem teaches how to **extract a part of a string** using **substring operations**.

---

## Step 1: Understand String Indexing

Strings use **zero-based indexing**.

Example:

```
Helloworld
```

Index positions:

| Index | Character |
| ----- | --------- |
| 0     | H         |
| 1     | e         |
| 2     | l         |
| 3     | l         |
| 4     | o         |
| 5     | w         |
| 6     | o         |
| 7     | r         |
| 8     | l         |
| 9     | d         |

---

## Step 2: Understand `start` and `end`

The substring rule:

```
substring(start, end)
```

Meaning:

```
start → included
end → excluded
```

Example input:

```
S = "Helloworld"
start = 3
end = 7
```

Characters included:

```
index 3 → l
index 4 → o
index 5 → w
index 6 → o
```

Character at index **7** is excluded.

Result:

```
lowo
```

---

## Step 3: Language Implementations

### Java

Java provides the method:

```
String.substring(start, end)
```

Example:

```java
S.substring(3,7)
```

Output:

```
lowo
```

---

### Python

Python uses **slice notation**:

```
string[start:end]
```

Example:

```
S[3:7]
```

Output:

```
lowo
```

---

### JavaScript

JavaScript provides the method:

```
substring(start, end)
```

Example:

```
S.substring(3,7)
```

Output:

```
lowo
```

---

## Example Walkthrough

Input:

```
Helloworld
3
7
```

Step 1: Identify substring range

```
start = 3
end = 7
```

Step 2: Extract characters

```
index 3 → l
index 4 → o
index 5 → w
index 6 → o
```

Result:

```
lowo
```

Output:

```
lowo
```

---

# Key Concepts Learned

* String indexing
* Substring extraction
* Zero-based indexing
* Inclusive vs exclusive indices
* String slicing across different programming languages

This problem strengthens understanding of **string manipulation**, which is essential for tasks like parsing text, processing data, and solving algorithm problems.


# Java Substring Comparisons

## 1. Problem

Given a string **S** and an integer **k**, you must find:

1. The **lexicographically smallest substring** of length **k**
2. The **lexicographically largest substring** of length **k**

A substring is a **continuous sequence of characters** taken from the string.

Lexicographical order means **dictionary order**.

### Input Format

```

S
k

```

Where:

- **S** → a string consisting of lowercase letters
- **k** → the length of the substrings to consider

### Constraints

```

1 ≤ length(S) ≤ 1000
1 ≤ k ≤ length(S)

```

### Output Format

Print two lines:

```

smallest_substring
largest_substring

```

### Sample Input

```

welcometojava
3

```

### Sample Output

```

ava
wel

````

---

# 2. Answer

## Java Solution

```java
import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {

        String smallest = s.substring(0, k);
        String largest = s.substring(0, k);

        for (int i = 1; i <= s.length() - k; i++) {

            String sub = s.substring(i, i + k);

            if (sub.compareTo(smallest) < 0) {
                smallest = sub;
            }

            if (sub.compareTo(largest) > 0) {
                largest = sub;
            }
        }

        return smallest + "\n" + largest;
    }

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        String s = scan.next();
        int k = scan.nextInt();

        scan.close();

        System.out.println(getSmallestAndLargest(s, k));
    }
}
````

---

## Python Solution

```python
def getSmallestAndLargest(s, k):

    smallest = s[0:k]
    largest = s[0:k]

    for i in range(1, len(s) - k + 1):

        sub = s[i:i+k]

        if sub < smallest:
            smallest = sub

        if sub > largest:
            largest = sub

    return smallest + "\n" + largest


s = input().strip()
k = int(input())

print(getSmallestAndLargest(s, k))
```

---

## JavaScript Solution

```javascript
const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split("\n");

const s = input[0];
const k = parseInt(input[1]);

function getSmallestAndLargest(s, k) {

    let smallest = s.substring(0, k);
    let largest = s.substring(0, k);

    for (let i = 1; i <= s.length - k; i++) {

        let sub = s.substring(i, i + k);

        if (sub < smallest) {
            smallest = sub;
        }

        if (sub > largest) {
            largest = sub;
        }
    }

    return smallest + "\n" + largest;
}

console.log(getSmallestAndLargest(s, k));
```

---

# 3. Clear Explanation

This problem focuses on **substring generation** and **lexicographical comparison**.

You must:

1. Generate all substrings of length **k**
2. Compare them
3. Find the **smallest and largest** in dictionary order

---

## Step 1: Generate Substrings of Length k

If:

```
S = welcometojava
k = 3
```

All substrings of length **3**:

| Index | Substring |
| ----- | --------- |
| 0     | wel       |
| 1     | elc       |
| 2     | lco       |
| 3     | com       |
| 4     | ome       |
| 5     | met       |
| 6     | eto       |
| 7     | toj       |
| 8     | oja       |
| 9     | jav       |
| 10    | ava       |

Total substrings:

```
length(S) - k + 1
```

```
13 - 3 + 1 = 11 substrings
```

---

## Step 2: Lexicographical Comparison

Lexicographical order means **dictionary order**.

Example:

```
apple < banana
cat > ball
```

Comparison happens **character by character**.

Example:

```
ava < wel
```

Because:

```
a < w
```

---

## Step 3: Track Smallest and Largest

Initialize both values with the **first substring**.

```
smallest = first substring
largest = first substring
```

Then compare each substring.

Example:

```
current substring = "elc"
```

Check:

```
elc < wel → smallest = elc
```

Continue until all substrings are processed.

---

## Step 4: Final Result

From the example:

```
welcometojava
k = 3
```

Smallest substring:

```
ava
```

Largest substring:

```
wel
```

Output:

```
ava
wel
```

---

# Algorithm Complexity

Let:

```
n = length of string
```

Substrings generated:

```
n - k + 1
```

Each comparison costs:

```
O(k)
```

Total complexity:

```
O(n * k)
```

Which is efficient for the constraint **n ≤ 1000**.

---

# Key Concepts Learned

* Substring generation
* Sliding window technique
* Lexicographical comparison
* String manipulation
* Iterative scanning

This problem is a classic example of **string window scanning**, a technique used in many algorithms involving substrings and pattern matching.

---


```md
# Java String Reverse (Palindrome Check)

## 1. Problem

You are given a **string `S`**.  
Your task is to determine whether the string is a **palindrome**.

A **palindrome** is a string that reads the same **forward and backward**.

If the string is a palindrome, print:

```

Yes

```

Otherwise print:

```

No

```

### Input Format

A single string:

```

S

```

### Constraints

```

1 ≤ length(S) ≤ 50
S consists of lowercase letters.

```

### Sample Input

```

madam

```

### Sample Output

```

Yes

````

### Explanation

The reverse of `"madam"` is also `"madam"`, so it is a palindrome.

---

# 2. Answer

## Java Solution

```java
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String s = sc.next();
        String reverse = "";

        for (int i = s.length() - 1; i >= 0; i--) {
            reverse += s.charAt(i);
        }

        if (s.equalsIgnoreCase(reverse)) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

        sc.close();
    }
}
````

---

## Python Solution

```python
s = input().strip()

reverse = ""

for i in range(len(s) - 1, -1, -1):
    reverse += s[i]

if s.lower() == reverse.lower():
    print("Yes")
else:
    print("No")
```

---

## JavaScript Solution

```javascript
const fs = require("fs");

const s = fs.readFileSync(0, "utf8").trim();

let reverse = "";

for (let i = s.length - 1; i >= 0; i--) {
    reverse += s[i];
}

if (s.toLowerCase() === reverse.toLowerCase()) {
    console.log("Yes");
} else {
    console.log("No");
}
```

---

# 3. Clear Explanation

This problem checks whether a string is a **palindrome**.

A palindrome reads the **same forward and backward**.

Examples of palindromes:

```
madam
racecar
level
noon
```

Examples that are **not palindromes**:

```
hello
java
world
```

---

## Step 1: Reverse the String

To check if a string is a palindrome, we first **reverse the string**.

Example:

```
original = "madam"
reverse  = "madam"
```

If both strings are equal → it is a palindrome.

---

## Step 2: Reversing Using a Loop

We iterate from the **last character to the first**.

Example:

```
s = "hello"
```

Indexes:

| Index | Character |
| ----- | --------- |
| 0     | h         |
| 1     | e         |
| 2     | l         |
| 3     | l         |
| 4     | o         |

Loop from index **4 → 0**.

Reverse construction:

```
o
ol
oll
olle
olleh
```

Final reversed string:

```
olleh
```

---

## Step 3: Compare Original and Reversed Strings

We compare the strings:

```
original == reversed
```

Example:

```
madam == madam → true
```

Output:

```
Yes
```

Example:

```
hello == olleh → false
```

Output:

```
No
```

---

## Case-Insensitive Comparison

The Java code uses:

```
equalsIgnoreCase()
```

Meaning:

```
Madam == madam
```

This ensures that uppercase/lowercase differences do not affect the result.

Python and JavaScript achieve the same using:

```
lower()
toLowerCase()
```

---

## Example Walkthrough

Input:

```
racecar
```

Reverse:

```
racecar
```

Comparison:

```
racecar == racecar → true
```

Output:

```
Yes
```

---

# Key Concepts Learned

* String traversal
* Reversing a string
* Palindrome detection
* Case-insensitive comparison
* Looping through characters

This problem is a **classic interview question** used to test understanding of **strings and loops** in programming.

---


#  Java Anagrams

## 1. Problem

Two strings are called **anagrams** if they contain the **same characters in the same frequency**, but possibly in a **different order**.

Given two strings **A** and **B**, determine whether they are **anagrams of each other**.

- The comparison should be **case-insensitive**.
- Only **English alphabet characters (a–z)** are considered.

### Input Format

Two lines of input:

```

A
B

```

Where:

- **A** → first string  
- **B** → second string  

### Constraints

```

1 ≤ length(A), length(B) ≤ 50
Strings consist only of alphabetic characters.

```

### Output Format

Print:

```

Anagrams

```

if the strings are anagrams, otherwise print:

```

Not Anagrams

```

### Sample Input

```

anagram
margana

```

### Sample Output

```

Anagrams

```

### Explanation

Both words contain the same letters with the same frequency:

```

a n a g r a m
m a r g a n a

````

Therefore they are **anagrams**.

---

# 2. Answer

## Java Solution

```java
import java.util.*;

public class Solution {

    static boolean isAnagram(String a, String b) {

        if (a.length() != b.length()) {
            return false;
        }

        a = a.toLowerCase();
        b = b.toLowerCase();

        int[] freq = new int[26];

        for (int i = 0; i < a.length(); i++) {
            freq[a.charAt(i) - 'a']++;
            freq[b.charAt(i) - 'a']--;
        }

        for (int count : freq) {
            if (count != 0) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String s1 = sc.next();
        String s2 = sc.next();

        sc.close();

        if (isAnagram(s1, s2)) {
            System.out.println("Anagrams");
        } else {
            System.out.println("Not Anagrams");
        }
    }
}
````

---

## Python Solution

```python
def is_anagram(a, b):

    if len(a) != len(b):
        return False

    a = a.lower()
    b = b.lower()

    freq = [0] * 26

    for i in range(len(a)):
        freq[ord(a[i]) - ord('a')] += 1
        freq[ord(b[i]) - ord('a')] -= 1

    for count in freq:
        if count != 0:
            return False

    return True


a = input().strip()
b = input().strip()

if is_anagram(a, b):
    print("Anagrams")
else:
    print("Not Anagrams")
```

---

## JavaScript Solution

```javascript
const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split("\n");

let a = input[0].toLowerCase();
let b = input[1].toLowerCase();

function isAnagram(a, b) {

    if (a.length !== b.length) {
        return false;
    }

    let freq = new Array(26).fill(0);

    for (let i = 0; i < a.length; i++) {
        freq[a.charCodeAt(i) - 97]++;
        freq[b.charCodeAt(i) - 97]--;
    }

    for (let count of freq) {
        if (count !== 0) {
            return false;
        }
    }

    return true;
}

if (isAnagram(a, b)) {
    console.log("Anagrams");
} else {
    console.log("Not Anagrams");
}
```

---

# 3. Clear Explanation

This problem checks whether two strings contain **exactly the same characters with the same frequency**.

---

# Step 1: Understand Anagrams

Examples of **anagrams**:

```
listen → silent
triangle → integral
anagram → margana
```

Examples that are **not anagrams**:

```
hello → world
test → best
java → python
```

---

# Step 2: Check Length First

If two strings have **different lengths**, they cannot be anagrams.

Example:

```
hello → length = 5
helloo → length = 6
```

Since the lengths differ:

```
Not Anagrams
```

---

# Step 3: Convert to Same Case

Anagram comparison should ignore **uppercase/lowercase differences**.

Example:

```
Listen
Silent
```

Convert both to lowercase:

```
listen
silent
```

---

# Step 4: Count Character Frequencies

We create an array of size **26** because there are **26 lowercase letters**.

```
freq[26]
```

Each index represents a letter:

| Index | Letter |
| ----- | ------ |
| 0     | a      |
| 1     | b      |
| 2     | c      |
| ...   | ...    |
| 25    | z      |

---

# Step 5: Update Counts

For each character:

1. **Increase count** for string A
2. **Decrease count** for string B

Example:

```
a = "ab"
b = "ba"
```

Process:

```
freq[a] +1
freq[b] +1
freq[b] -1
freq[a] -1
```

Final array:

```
all values = 0
```

Therefore:

```
Anagrams
```

---

# Step 6: Verify All Counts Are Zero

If any value in the frequency array is **not zero**, the strings are **not anagrams**.

Example:

```
a = hello
b = world
```

Character counts differ, so:

```
Not Anagrams
```

---

# Example Walkthrough

Input:

```
anagram
margana
```

Character counts:

```
a → 3
n → 1
g → 1
r → 1
m → 1
```

Both strings match exactly.

Output:

```
Anagrams
```

---

# Time and Space Complexity

### Time Complexity

```
O(n)
```

Where **n = length of the string**.

We iterate through the string once.

### Space Complexity

```
O(1)
```

The frequency array always has **26 elements**, regardless of input size.

---

# Key Concepts Learned

* Character frequency counting
* Array indexing using characters
* Case-insensitive string comparison
* Efficient string comparison algorithms
* Time-efficient anagram detection

This problem is a common **interview question** because it tests **string processing, arrays, and algorithm efficiency**.


---

# String Tokens

## 1. Problem

You are given a string **S** containing words separated by spaces and possibly other non-letter characters such as punctuation marks.

Your task is to:

1. Split the string into **tokens** (words).
2. A token is defined as a **sequence of English alphabetic characters (A–Z or a–z)**.
3. Any **non-alphabetic character** acts as a separator.
4. Print:
   - The **number of tokens**
   - Each token on a **new line**

### Input Format

A single line containing a string:

```

S

```

### Constraints

```

0 < length(S) ≤ 4 * 10^5
S consists of alphabetic characters, spaces, and punctuation marks.

```

### Sample Input

```

He is a very very good boy, isn't he?

```

### Sample Output

```

10
He
is
a
very
very
good
boy
isn
t
he

````

### Explanation

The punctuation characters such as commas and apostrophes are treated as **separators**, so the string is split wherever a non-letter character appears.

---

# 2. Answer

## Java Solution

```java
import java.util.*;

public class Solution {

    static String[] token(String s) {
        return s.split("[^A-Za-z]+");
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        sc.close();

        String[] tokens = token(s);

        System.out.println(tokens.length);

        for (String t : tokens) {
            if (!t.isEmpty()) {
                System.out.println(t);
            }
        }
    }
}
````

---

## Python Solution

```python
import re

s = input().strip()

tokens = re.split("[^A-Za-z]+", s)

tokens = [t for t in tokens if t]

print(len(tokens))

for t in tokens:
    print(t)
```

---

## JavaScript Solution

```javascript
const fs = require("fs");

let s = fs.readFileSync(0, "utf8").trim();

let tokens = s.split(/[^A-Za-z]+/).filter(t => t.length > 0);

console.log(tokens.length);

for (let t of tokens) {
    console.log(t);
}
```

---

# 3. Clear Explanation

This problem focuses on **string splitting and tokenization**.

The main idea is to extract **only alphabetic words** from a sentence.

---

## Step 1: Understand Tokens

A **token** is a sequence of letters:

Examples:

```
Hello
world
Java
Python
```

Characters that are **not letters** act as separators.

Examples of separators:

```
space
comma ,
apostrophe '
question mark ?
period .
```

---

## Step 2: Example Input Breakdown

Input:

```
He is a very very good boy, isn't he?
```

Remove separators:

```
He
is
a
very
very
good
boy
isn
t
he
```

Number of tokens:

```
10
```

---

## Step 3: Regular Expression Used

The key regex pattern is:

```
[^A-Za-z]+
```

Explanation:

| Symbol | Meaning                 |
| ------ | ----------------------- |
| `A-Z`  | uppercase letters       |
| `a-z`  | lowercase letters       |
| `[^ ]` | NOT inside the bracket  |
| `+`    | one or more occurrences |

So the pattern means:

```
split wherever one or more non-letter characters appear
```

---

## Step 4: Example of Splitting

String:

```
boy,isn't
```

Separators:

```
,
'
```

Result tokens:

```
boy
isn
t
```

---

## Step 5: Removing Empty Tokens

Sometimes splitting creates empty strings.

Example:

```
",hello,,world"
```

Split result:

```
["", "hello", "", "world"]
```

We remove empty strings to ensure correct token counting.

---

## Step 6: Printing Results

The output must contain:

1. Total number of tokens
2. Each token on its own line

Example output:

```
10
He
is
a
very
very
good
boy
isn
t
he
```

---

# Time Complexity

Let:

```
n = length of string
```

Splitting the string:

```
O(n)
```

Filtering tokens:

```
O(n)
```

Total complexity:

```
O(n)
```

---

# Key Concepts Learned

* String tokenization
* Regular expressions
* String splitting
* Filtering empty values
* Input handling

This problem is important because **tokenization is widely used in text processing, compilers, natural language processing (NLP), and data parsing**.

---









