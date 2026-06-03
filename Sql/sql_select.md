# SQL CITY TABLE QUERIES — PRACTICE PROBLEMS

This document contains SQL practice problems based on the **CITY** table schema.  
Each section includes:

1. Table Structure  
2. Problem  
3. SQL Answer  
4. Explanation  

All queries follow **standard SQL syntax** and work in:

- MySQL
- PostgreSQL
- SQLite
- Oracle
- SQL Server

------------------------------------------
------------------------------------------

## 1. TABLE STRUCTURE

### CITY Table

| Field        | Type            |
|---------------|----------------|
| ID            | NUMBER          |
| NAME          | VARCHAR2(17)    |
| COUNTRYCODE   | VARCHAR2(3)     |
| DISTRICT      | VARCHAR2(20)    |
| POPULATION    | NUMBER          |

Explanation:

The **CITY** table stores information about cities including:

- unique identifier (ID)
- city name (NAME)
- country code (COUNTRYCODE)
- administrative district (DISTRICT)
- population size (POPULATION)

Example record:

| ID | NAME      | COUNTRYCODE | DISTRICT | POPULATION |
|----|-----------|-------------|----------|-----------|
| 1  | New York  | USA         | New York | 8000000   |

------------------------------------------
------------------------------------------

# PROBLEM 1

## Problem

Query **all columns** for all **American cities** in the CITY table with **populations larger than 100000**.

CountryCode for America = **USA**

------------------------------------------

## Answer

```sql
SELECT *
FROM CITY
WHERE COUNTRYCODE = 'USA'
AND POPULATION > 100000;
```

------------------------------------------

## Explanation

Step 1  
`SELECT *` retrieves all columns.

Step 2  
`FROM CITY` specifies the table.

Step 3  
`COUNTRYCODE = 'USA'` filters cities located in the United States.

Step 4  
`POPULATION > 100000` restricts results to cities with population greater than 100000.

Result:

Only American cities with population above **100,000** are returned.

------------------------------------------
------------------------------------------

# PROBLEM 2

## Problem

Query the **NAME field** for all **American cities** in the CITY table with **populations larger than 120000**.

CountryCode for America = **USA**

------------------------------------------

## Answer

```sql
SELECT NAME
FROM CITY
WHERE COUNTRYCODE = 'USA'
AND POPULATION > 120000;
```

------------------------------------------

## Explanation

Step 1  
`SELECT NAME` retrieves only the city name column.

Step 2  
`COUNTRYCODE = 'USA'` ensures only American cities are included.

Step 3  
`POPULATION > 120000` filters cities with population above 120000.

Result:

The output will contain **only the names** of cities meeting these conditions.

------------------------------------------
------------------------------------------

# PROBLEM 3

## Problem

Query the **NAME field** for all **American cities** in the CITY table with **populations larger than 120000**.

CountryCode for America = **USA**

------------------------------------------

## Answer

```sql
SELECT NAME
FROM CITY
WHERE COUNTRYCODE = 'USA'
AND POPULATION > 120000;
```

------------------------------------------

## Explanation

This query is identical to Problem 2.

Execution logic:

1. Filter rows where COUNTRYCODE = 'USA'
2. Filter rows where POPULATION > 120000
3. Return only the NAME column

------------------------------------------
------------------------------------------

# PROBLEM 4

## Problem

Query **all columns** for the city in CITY where **ID = 1661**.

------------------------------------------

## Answer

```sql
SELECT *
FROM CITY
WHERE ID = 1661;
```

------------------------------------------

## Explanation

Step 1  
`SELECT *` retrieves every column in the table.

Step 2  
`WHERE ID = 1661` filters for the specific city with ID value 1661.

Since **ID is usually a primary key**, this query normally returns **one row**.

------------------------------------------
------------------------------------------

# PROBLEM 5

## Problem

Query the **names of all Japanese cities** in the CITY table.

CountryCode for Japan = **JPN**

------------------------------------------

## Answer

```sql
SELECT NAME
FROM CITY
WHERE COUNTRYCODE = 'JPN';
```

------------------------------------------

## Explanation

Step 1  
`SELECT NAME` returns only the city name.

Step 2  
`COUNTRYCODE = 'JPN'` filters cities located in Japan.

Result:

All Japanese city names will be returned.

Example Output

| NAME |
|------|
Tokyo  
Osaka  
Kyoto  
Nagoya  

------------------------------------------
------------------------------------------

# SUMMARY

| Query | Purpose |
|------|--------|
Query 1 | American cities population > 100000 |
Query 2 | American city names population > 120000 |
Query 3 | Same as Query 2 |
Query 4 | Retrieve city by ID |
Query 5 | Japanese city names |

------------------------------------------
------------------------------------------

# Key SQL Concepts Used

- SELECT
- WHERE
- Logical filtering
- Comparison operators
- String comparison

------------------------------------------
------------------------------------------

# Interview Tip

A very common SQL interview pattern is:

```
SELECT column
FROM table
WHERE condition
```

Always remember:

1. SELECT → columns  
2. FROM → table  
3. WHERE → filtering  

------------------------------------------
------------------------------------------



------------------------------------------
------------------------------------------

# 1. TABLE STRUCTURE

## STATION

| Field  | Type          |
|-------|---------------|
| ID     | NUMBER        |
| CITY   | VARCHAR2(21)  |
| STATE  | VARCHAR2(2)   |
| LAT_N  | NUMBER        |
| LONG_W | NUMBER        |

Explanation:

The **STATION** table contains geographic information about weather stations.

Column descriptions:

- **ID** → Unique station identifier  
- **CITY** → Name of the city where the station is located  
- **STATE** → State code  
- **LAT_N** → Latitude coordinate  
- **LONG_W** → Longitude coordinate  

------------------------------------------
------------------------------------------

# PROBLEM 1

## Problem

Query a list of **CITY and STATE** from the STATION table.

------------------------------------------

## Answer

```sql
SELECT CITY, STATE
FROM STATION;
```

------------------------------------------

## Explanation

- `SELECT CITY, STATE` retrieves two columns.
- `FROM STATION` specifies the table.

Result:  
All city and state combinations in the table.

------------------------------------------
------------------------------------------

# PROBLEM 2

## Problem

Query a list of **CITY names** from STATION for cities that have an **even ID number**.

Print results in any order but **exclude duplicates**.

------------------------------------------

## Answer

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE MOD(ID, 2) = 0;
```

------------------------------------------

## Explanation

- `MOD(ID,2) = 0` filters even ID numbers.
- `DISTINCT` removes duplicate city names.

------------------------------------------
------------------------------------------

# PROBLEM 3

## Problem

Find the difference between:

- Total number of CITY entries
- Number of distinct CITY entries

------------------------------------------

## Answer

```sql
SELECT COUNT(CITY) - COUNT(DISTINCT CITY)
FROM STATION;
```

------------------------------------------

## Explanation

- `COUNT(CITY)` counts all rows.
- `COUNT(DISTINCT CITY)` counts unique cities.
- The difference gives number of duplicate entries.

------------------------------------------
------------------------------------------

# PROBLEM 4

## Problem

Query the **two cities with the shortest and longest CITY names**, along with their **lengths**.

If there are ties, choose the city that comes **first alphabetically**.

------------------------------------------

## Answer

```sql
(
SELECT CITY, LENGTH(CITY) AS CITY_LENGTH
FROM STATION
ORDER BY LENGTH(CITY), CITY
FETCH FIRST 1 ROW ONLY
)

UNION ALL

(
SELECT CITY, LENGTH(CITY) AS CITY_LENGTH
FROM STATION
ORDER BY LENGTH(CITY) DESC, CITY
FETCH FIRST 1 ROW ONLY
);
```

------------------------------------------

## Explanation

First Query  
Finds the city with the **shortest name**.

Second Query  
Finds the city with the **longest name**.

Ordering rules:

- `ORDER BY LENGTH(CITY)` ensures shortest first.
- `ORDER BY LENGTH(CITY) DESC` ensures longest first.
- `CITY` ensures alphabetical tie-breaking.

------------------------------------------
------------------------------------------

# PROBLEM 5

## Problem

Query CITY names **starting with vowels** (a, e, i, o, u).

Exclude duplicates.

------------------------------------------

## Answer

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(SUBSTRING(CITY,1,1)) IN ('a','e','i','o','u');
```

------------------------------------------

## Explanation

- `SUBSTRING(CITY,1,1)` extracts first character.
- `LOWER()` ensures case-insensitive comparison.
- `DISTINCT` removes duplicates.

------------------------------------------
------------------------------------------

# PROBLEM 6

## Problem

Query CITY names **ending with vowels**.

Exclude duplicates.

------------------------------------------

## Answer

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(SUBSTRING(CITY, LENGTH(CITY), 1)) IN ('a','e','i','o','u');
```

------------------------------------------

## Explanation

- `LENGTH(CITY)` finds string length.
- `SUBSTRING(... LENGTH(CITY),1)` extracts last character.

------------------------------------------
------------------------------------------

# PROBLEM 7

## Problem

Query CITY names with **vowels as both first and last characters**.

Exclude duplicates.

------------------------------------------

## Answer

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(SUBSTRING(CITY,1,1)) IN ('a','e','i','o','u')
AND LOWER(SUBSTRING(CITY, LENGTH(CITY),1)) IN ('a','e','i','o','u');
```

------------------------------------------

## Explanation

Two conditions:

1. First character is vowel.
2. Last character is vowel.

Both must be true.

------------------------------------------
------------------------------------------

# PROBLEM 8

## Problem

Query CITY names **that do not start with vowels**.

Exclude duplicates.

------------------------------------------

## Answer

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(SUBSTRING(CITY,1,1)) NOT IN ('a','e','i','o','u');
```

------------------------------------------

## Explanation

`NOT IN` ensures the first character is not a vowel.

------------------------------------------
------------------------------------------

# PROBLEM 9

## Problem

Query CITY names **that do not end with vowels**.

Exclude duplicates.

------------------------------------------

## Answer

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(SUBSTRING(CITY, LENGTH(CITY),1)) NOT IN ('a','e','i','o','u');
```

------------------------------------------

## Explanation

The last character is checked and filtered using `NOT IN`.

------------------------------------------
------------------------------------------

# PROBLEM 10

## Problem

Query CITY names that **either do not start with vowels OR do not end with vowels**.

Exclude duplicates.

------------------------------------------

## Answer

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(SUBSTRING(CITY,1,1)) NOT IN ('a','e','i','o','u')
OR LOWER(SUBSTRING(CITY, LENGTH(CITY),1)) NOT IN ('a','e','i','o','u');
```

------------------------------------------

## Explanation

The `OR` operator means:

At least one condition must be true.

------------------------------------------
------------------------------------------

# PROBLEM 11

## Problem

Query CITY names that **do not start with vowels AND do not end with vowels**.

Exclude duplicates.

------------------------------------------

## Answer

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(SUBSTRING(CITY,1,1)) NOT IN ('a','e','i','o','u')
AND LOWER(SUBSTRING(CITY, LENGTH(CITY),1)) NOT IN ('a','e','i','o','u');
```

------------------------------------------

## Explanation

The `AND` operator ensures both conditions are satisfied.

- First letter is not a vowel
- Last letter is not a vowel

------------------------------------------
------------------------------------------

# SUMMARY OF SQL CONCEPTS USED

| Concept | Purpose |
|------|------|
SELECT | Retrieve data |
WHERE | Filter rows |
DISTINCT | Remove duplicates |
COUNT | Count rows |
LENGTH | Find string length |
SUBSTRING | Extract characters |
MOD | Find even numbers |
ORDER BY | Sort results |

------------------------------------------
------------------------------------------

# INTERVIEW TIP

Common SQL interview topics covered here:

- String filtering
- DISTINCT vs COUNT
- Pattern matching
- Conditional filtering
- Aggregation
- Sorting logic

Practice writing these queries **without looking at solutions** to master SQL.

------------------------------------------
------------------------------------------

------------------------------------------
------------------------------------------

# 1. TABLE

## STUDENTS

| Column | Type    |
|------|---------|
| ID   | Integer |
| Name | String  |
| Marks| Integer |

Additional information:

- The **Name** column contains only alphabetic characters.
- Names may include both **uppercase (A–Z)** and **lowercase (a–z)** letters.

### Example Data

| ID | Name      | Marks |
|----|-----------|------|
| 1  | Ashley    | 81   |
| 2  | Samantha  | 75   |
| 4  | Julia     | 76   |
| 3  | Belvet    | 84   |

------------------------------------------
------------------------------------------

# 2. PROBLEM

Query the **Name** of any student in **STUDENTS** who scored **higher than 75 marks**.

Sort the result:

1. First by the **last three characters of each name**
2. If two names have the same last three characters, then sort by **ascending ID**

------------------------------------------
------------------------------------------

# 3. ANSWER

```sql
SELECT Name
FROM STUDENTS
WHERE Marks > 75
ORDER BY SUBSTRING(Name, LENGTH(Name) - 2, 3), ID;
```

------------------------------------------
------------------------------------------

# 4. EXPLANATION

Step 1 — Filtering Students

```
WHERE Marks > 75
```

This condition ensures only students with **marks greater than 75** are included.

------------------------------------------

Step 2 — Extracting Last Three Characters

```
SUBSTRING(Name, LENGTH(Name) - 2, 3)
```

Explanation:

- `LENGTH(Name)` finds the total length of the name.
- `LENGTH(Name) - 2` identifies the starting position of the **last three characters**.
- `SUBSTRING(..., 3)` extracts exactly three characters.

Example:

| Name    | Length | Last 3 Characters |
|--------|-------|------------------|
Ashley  | 6     | ley |
Julia   | 5     | lia |
Belvet  | 6     | vet |

------------------------------------------

Step 3 — Ordering Results

```
ORDER BY
SUBSTRING(Name, LENGTH(Name) - 2, 3),
ID
```

Sorting rules:

Primary sorting → Last three characters of name  
Secondary sorting → ID (ascending)

This ensures consistent ordering when names end with the same characters.

------------------------------------------

Step 4 — Output

Based on the sample data:

Students with marks greater than 75:

| Name   | Marks |
|-------|------|
Ashley | 81 |
Julia  | 76 |
Belvet | 84 |

Sorted by last three characters:

| Name |
|------|
Julia |
Ashley |
Belvet |

------------------------------------------
------------------------------------------

# 5. SQL CONCEPTS USED

| Concept | Purpose |
|------|------|
SELECT | Retrieve column data |
WHERE | Filter rows |
ORDER BY | Sort results |
SUBSTRING | Extract part of string |
LENGTH | Determine string length |

------------------------------------------
------------------------------------------

# INTERVIEW TIP

A common SQL interview trick is **sorting by a substring** of a column.

Example pattern:

```
ORDER BY SUBSTRING(column, start_position, length)
```

This is frequently used for:

- Sorting by suffix
- Sorting by prefixes
- Extracting domain names from emails
- Parsing identifiers

------------------------------------------
------------------------------------------

------------------------------------------
------------------------------------------

# 1. TABLE

## Employee

| Column       | Type    |
|--------------|---------|
| employee_id  | Integer |
| name         | String  |
| months       | Integer |
| salary       | Integer |

Column descriptions:

- **employee_id** → Unique employee identifier
- **name** → Employee name
- **months** → Total number of months worked in the company
- **salary** → Monthly salary

### Example Data

| employee_id | name      | months | salary |
|-------------|-----------|--------|--------|
| 12228 | Rose      | 15 | 1968 |
| 33645 | Angela    | 1  | 3443 |
| 45692 | Frank     | 17 | 1608 |
| 56118 | Patrick   | 7  | 1345 |
| 59725 | Lisa      | 11 | 2330 |
| 74197 | Kimberly  | 16 | 4372 |
| 78454 | Bonnie    | 8  | 1771 |
| 83565 | Michael   | 6  | 2017 |
| 98607 | Todd      | 5  | 3396 |
| 99989 | Joe       | 9  | 3573 |

------------------------------------------
------------------------------------------

# PROBLEM 1

## Problem

Write a query that prints a list of **employee names** from the **Employee** table in **alphabetical order**.

------------------------------------------

## Answer

```sql
SELECT name
FROM Employee
ORDER BY name ASC;
```

------------------------------------------

## Explanation

Step 1 — Select the Name Column

```
SELECT name
```

This retrieves only the employee names.

------------------------------------------

Step 2 — Specify the Table

```
FROM Employee
```

The query pulls data from the **Employee** table.

------------------------------------------

Step 3 — Sort Alphabetically

```
ORDER BY name ASC
```

- `ORDER BY` sorts the output.
- `ASC` means **ascending order** (A → Z).

Example Output

| name |
|------|
Angela  
Bonnie  
Frank  
Joe  
Kimberly  
Lisa  
Michael  
Patrick  
Rose  
Todd  

------------------------------------------
------------------------------------------

# PROBLEM 2

## Problem

Write a query that prints a list of **employee names** for employees who:

- have a **salary greater than $2000**
- have worked **less than 10 months**

Sort the results by **ascending employee_id**.

------------------------------------------

## Answer

```sql
SELECT name
FROM Employee
WHERE salary > 2000
AND months < 10
ORDER BY employee_id ASC;
```

------------------------------------------

## Explanation

Step 1 — Select Name Column

```
SELECT name
```

Returns only employee names.

------------------------------------------

Step 2 — Apply Salary Condition

```
salary > 2000
```

Select employees earning more than **$2000 per month**.

------------------------------------------

Step 3 — Apply Months Condition

```
months < 10
```

Select employees with **less than 10 months of work experience**.

------------------------------------------

Step 4 — Combine Conditions

```
WHERE salary > 2000
AND months < 10
```

Both conditions must be satisfied.

------------------------------------------

Step 5 — Sort by Employee ID

```
ORDER BY employee_id ASC
```

Sort results in increasing order of employee ID.

------------------------------------------

Example Evaluation

Employees satisfying conditions:

| employee_id | name   | months | salary |
|--------------|--------|--------|--------|
| 33645 | Angela | 1 | 3443 |
| 83565 | Michael | 6 | 2017 |
| 98607 | Todd | 5 | 3396 |
| 99989 | Joe | 9 | 3573 |

Sorted by employee_id:

| name |
|------|
Angela  
Michael  
Todd  
Joe  

------------------------------------------
------------------------------------------

# SQL CONCEPTS USED

| Concept | Purpose |
|--------|--------|
SELECT | Retrieve column data |
FROM | Specify table |
WHERE | Filter rows |
AND | Combine conditions |
ORDER BY | Sort results |
ASC | Ascending order |

------------------------------------------
------------------------------------------

# INTERVIEW TIP

This question tests **three core SQL concepts**:

Filtering

```
WHERE salary > 2000
```

Multiple Conditions

```
AND months < 10
```

Sorting

```
ORDER BY employee_id
```

These patterns are extremely common in **SQL interviews and production queries**.

------------------------------------------
------------------------------------------ 

------------------------------------------
------------------------------------------

# 1. TABLE

## TRIANGLES

| Column | Type    |
|-------|---------|
| A     | Integer |
| B     | Integer |
| C     | Integer |

Description:

Each row represents the **lengths of the three sides of a triangle**.

### Example Data

| A  | B  | C  |
|----|----|----|
| 20 | 20 | 20 |
| 13 | 20 | 20 |
| 21 | 14 | 23 |
| 20 | 22 | 30 |

Meaning of columns:

- **A** → Side length 1  
- **B** → Side length 2  
- **C** → Side length 3  

------------------------------------------
------------------------------------------

# 2. PROBLEM

Write a SQL query that identifies the **type of triangle** represented by each row.

The output must return one of the following classifications:

| Type | Description |
|-----|-------------|
| Equilateral | All three sides are equal |
| Isosceles | Exactly two sides are equal |
| Scalene | All three sides are different |
| Not A Triangle | The given sides cannot form a triangle |

Triangle validity rule:

A triangle is valid only if:

```
A + B > C
A + C > B
B + C > A
```

If any of these conditions fail, the sides **cannot form a triangle**.

------------------------------------------
------------------------------------------

# 3. ANSWER

```sql
SELECT
CASE
    WHEN A + B <= C OR A + C <= B OR B + C <= A
        THEN 'Not A Triangle'
    WHEN A = B AND B = C
        THEN 'Equilateral'
    WHEN A = B OR B = C OR A = C
        THEN 'Isosceles'
    ELSE 'Scalene'
END AS triangle_type
FROM TRIANGLES;
```

------------------------------------------
------------------------------------------

# 4. EXPLANATION

The query uses a **CASE expression** to classify each triangle.

------------------------------------------

### Step 1 — Check for Invalid Triangle

```
WHEN A + B <= C
OR A + C <= B
OR B + C <= A
```

If any of these conditions are true, the triangle **cannot exist**.

Example:

| A | B | C |
|---|---|---|
2 | 3 | 6

Since:

```
2 + 3 <= 6
```

This is **Not A Triangle**.

------------------------------------------

### Step 2 — Check for Equilateral Triangle

```
A = B AND B = C
```

All three sides are equal.

Example:

| A | B | C |
|---|---|---|
20 | 20 | 20 |

Result:

```
Equilateral
```

------------------------------------------

### Step 3 — Check for Isosceles Triangle

```
A = B OR B = C OR A = C
```

Exactly **two sides are equal**.

Example:

| A | B | C |
|---|---|---|
13 | 20 | 20 |

Result:

```
Isosceles
```

------------------------------------------

### Step 4 — Scalene Triangle

If none of the previous conditions are satisfied:

```
ELSE 'Scalene'
```

All three sides are different.

Example:

| A | B | C |
|---|---|---|
21 | 14 | 23 |

Result:

```
Scalene
```

------------------------------------------
------------------------------------------

# 5. EXAMPLE OUTPUT

Based on the sample dataset:

| A  | B  | C  | Result |
|----|----|----|--------|
| 20 | 20 | 20 | Equilateral |
| 13 | 20 | 20 | Isosceles |
| 21 | 14 | 23 | Scalene |
| 20 | 22 | 30 | Scalene |

------------------------------------------
------------------------------------------

# SQL CONCEPTS USED

| Concept | Purpose |
|------|------|
SELECT | Retrieve data |
CASE | Conditional logic |
WHEN | Evaluate conditions |
OR | Combine conditions |
ELSE | Default case |

------------------------------------------
------------------------------------------

# INTERVIEW TIP

This problem tests **three important SQL concepts**:

### 1. Conditional Logic

```
CASE WHEN ... THEN ...
```

### 2. Mathematical Constraints

Triangle inequality rule.

### 3. Logical Order

Conditions must be evaluated in the correct sequence:

1. Invalid triangle  
2. Equilateral  
3. Isosceles  
4. Scalene  

------------------------------------------
------------------------------------------

# BONUS — COMMON INTERVIEW FOLLOW-UP

A common follow-up question is:

**Return the side lengths along with the triangle type**

Example:

```sql
SELECT
A,
B,
C,
CASE
    WHEN A + B <= C OR A + C <= B OR B + C <= A
        THEN 'Not A Triangle'
    WHEN A = B AND B = C
        THEN 'Equilateral'
    WHEN A = B OR B = C OR A = C
        THEN 'Isosceles'
    ELSE 'Scalene'
END AS triangle_type
FROM TRIANGLES;
```

------------------------------------------
------------------------------------------

------------------------------------------
------------------------------------------

# 1. TABLE

## OCCUPATIONS

| Column | Type   |
|-------|--------|
| Name  | String |
| Occupation | String |

Constraint:

The **Occupation** column contains only the following values:

- Doctor
- Professor
- Singer
- Actor

### Example Data

| Name      | Occupation |
|-----------|-----------|
| Samantha  | Doctor |
| Julia     | Actor |
| Maria     | Actor |
| Meera     | Singer |
| Ashely    | Professor |
| Ketty     | Professor |
| Christeen | Professor |
| Jane      | Actor |
| Jenny     | Doctor |
| Priya     | Singer |

------------------------------------------
------------------------------------------

# 2. PROBLEM

Pivot the **Occupation** column so that:

- Each occupation becomes its own column.
- Names appear **alphabetically** under their corresponding occupation column.
- The final output must contain **four columns in this order**:

```
Doctor | Professor | Singer | Actor
```

Additional rules:

- Each column must contain names **sorted alphabetically**.
- If an occupation has fewer names than others, the remaining cells should display **NULL**.

------------------------------------------
------------------------------------------

# 3. ANSWER

```sql
SELECT
MAX(CASE WHEN Occupation = 'Doctor' THEN Name END) AS Doctor,
MAX(CASE WHEN Occupation = 'Professor' THEN Name END) AS Professor,
MAX(CASE WHEN Occupation = 'Singer' THEN Name END) AS Singer,
MAX(CASE WHEN Occupation = 'Actor' THEN Name END) AS Actor
FROM
(
    SELECT
        Name,
        Occupation,
        ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS rn
    FROM OCCUPATIONS
) t
GROUP BY rn
ORDER BY rn;
```

------------------------------------------
------------------------------------------

# 4. EXPLANATION

The query performs a **manual pivot operation** using window functions and conditional aggregation.

------------------------------------------

## Step 1 — Assign Row Numbers

```
ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name)
```

This creates a ranking of names within each occupation.

Example intermediate result:

| Name      | Occupation | rn |
|-----------|-----------|----|
| Jenny     | Doctor    | 1 |
| Samantha  | Doctor    | 2 |
| Ashely    | Professor | 1 |
| Christeen | Professor | 2 |
| Ketty     | Professor | 3 |
| Meera     | Singer    | 1 |
| Priya     | Singer    | 2 |
| Jane      | Actor     | 1 |
| Julia     | Actor     | 2 |
| Maria     | Actor     | 3 |

------------------------------------------

## Step 2 — Convert Rows to Columns

The following pattern pivots rows into columns:

```
MAX(CASE WHEN Occupation='Doctor' THEN Name END)
```

Explanation:

- `CASE` selects names belonging to a specific occupation.
- `MAX()` ensures only one value appears per grouped row.

------------------------------------------

## Step 3 — Group by Row Number

```
GROUP BY rn
```

This aligns names across different occupations by their alphabetical ranking.

------------------------------------------

## Step 4 — Sort Output

```
ORDER BY rn
```

Ensures rows appear in correct order.

------------------------------------------

# 5. RESULT EXAMPLE

Final output:

| Doctor   | Professor | Singer | Actor |
|---------|-----------|--------|-------|
| Jenny   | Ashely    | Meera  | Jane |
| Samantha| Christeen | Priya  | Julia |
| NULL    | Ketty     | NULL   | Maria |

Explanation:

- Each column contains names alphabetically.
- Empty positions are filled with **NULL**.

------------------------------------------
------------------------------------------

# SQL CONCEPTS USED

| Concept | Purpose |
|------|------|
ROW_NUMBER | Rank rows within groups |
PARTITION BY | Divide rows into groups |
CASE | Conditional selection |
MAX | Aggregate function for pivot |
GROUP BY | Align rows by index |
ORDER BY | Sort results |

------------------------------------------
------------------------------------------

# INTERVIEW TIP

This problem tests **advanced SQL concepts**, especially:

1. **Window Functions**

```
ROW_NUMBER() OVER (PARTITION BY ...)
```

2. **Conditional Aggregation**

```
MAX(CASE WHEN ... THEN ... END)
```

3. **Manual Pivoting**

Many databases do not support pivot syntax uniformly, so this pattern works **across all major SQL systems**.

------------------------------------------
------------------------------------------

------------------------------------------
------------------------------------------

# 1. TABLE

## BST

| Column | Type    |
|-------|---------|
| N     | Integer |
| P     | Integer |

Description:

The **BST** table represents a Binary Tree structure.

- **N** → Node value  
- **P** → Parent node value  

If **P is NULL**, then the node is the **root node**.

### Sample Input

| N | P    |
|---|------|
| 1 | 2    |
| 3 | 2    |
| 6 | 8    |
| 9 | 8    |
| 2 | 5    |
| 8 | 5    |
| 5 | NULL |

------------------------------------------
------------------------------------------

# 2. PROBLEM

Write a SQL query to determine the **type of each node** in the Binary Tree.

Each node must be classified as one of the following:

| Node Type | Description |
|----------|-------------|
| Root | Node with no parent (P is NULL) |
| Leaf | Node with no children |
| Inner | Node with both parent and child |

Output requirements:

- Display the **node value (N)** followed by its **node type**
- Sort the result by **N (ascending)**

### Expected Output

| N | Type |
|---|------|
| 1 | Leaf |
| 2 | Inner |
| 3 | Leaf |
| 5 | Root |
| 6 | Leaf |
| 8 | Inner |
| 9 | Leaf |

------------------------------------------
------------------------------------------

# 3. ANSWER

```sql
SELECT 
    N,
    CASE
        WHEN P IS NULL THEN 'Root'
        WHEN N NOT IN (SELECT P FROM BST WHERE P IS NOT NULL) THEN 'Leaf'
        ELSE 'Inner'
    END AS Node_Type
FROM BST
ORDER BY N;
```

------------------------------------------
------------------------------------------

# 4. EXPLANATION

The query classifies nodes based on **parent-child relationships**.

------------------------------------------

## Step 1 — Identify Root Node

```
WHEN P IS NULL THEN 'Root'
```

If the parent column is **NULL**, the node has no parent.

Example:

| N | P |
|---|---|
| 5 | NULL |

This node is the **Root**.

------------------------------------------

## Step 2 — Identify Leaf Nodes

Leaf nodes **never appear as a parent** in the table.

Condition used:

```
N NOT IN (SELECT P FROM BST WHERE P IS NOT NULL)
```

Explanation:

- The subquery collects all parent node values.
- If a node does **not appear as a parent**, it has no children.
- Therefore it is a **Leaf node**.

Example:

| N | P |
|---|---|
| 1 | 2 |
| 3 | 2 |

Nodes **1 and 3** never appear in column **P**, so they are leaves.

------------------------------------------

## Step 3 — Identify Inner Nodes

If the node:

- has a parent
- and also appears as a parent of other nodes

Then it is an **Inner node**.

Example:

| N | P |
|---|---|
| 2 | 5 |

Node **2** is parent of nodes **1 and 3**, therefore:

```
Inner
```

------------------------------------------

## Step 4 — Sorting Output

```
ORDER BY N
```

Ensures nodes appear in **ascending order**.

------------------------------------------

# 5. SQL CONCEPTS USED

| Concept | Purpose |
|------|------|
SELECT | Retrieve data |
CASE | Conditional logic |
WHEN | Evaluate conditions |
IS NULL | Detect root node |
Subquery | Identify parent nodes |
NOT IN | Find nodes without children |
ORDER BY | Sort results |

------------------------------------------
------------------------------------------

# INTERVIEW TIP

This problem tests **tree structure logic using SQL**.

Key idea:

```
Root  → P IS NULL
Leaf  → N never appears in P column
Inner → Appears as parent and has parent
```

Many SQL interviews include **hierarchical data problems**, especially for:

- Tree structures
- Organizational hierarchies
- Graph relationships

------------------------------------------
------------------------------------------

# BONUS — ALTERNATIVE QUERY USING JOIN

```sql
SELECT
    b.N,
    CASE
        WHEN b.P IS NULL THEN 'Root'
        WHEN c.P IS NULL THEN 'Leaf'
        ELSE 'Inner'
    END
FROM BST b
LEFT JOIN BST c
ON b.N = c.P
ORDER BY b.N;
```

Explanation:

- The **LEFT JOIN** checks if a node has children.
- If no matching child exists → Leaf node.

------------------------------------------
------------------------------------------
# SQL PRACTICE — OCCUPATIONS TABLE (STRING FORMATTING & AGGREGATION)

This document demonstrates SQL problems involving **string formatting, ordering, and aggregation** using the **OCCUPATIONS** table.

Each section includes:

1. Table  
2. Problem  
3. Answer (SQL Query)  
4. Explanation  

All queries follow **standard SQL syntax** and work in:

- MySQL  
- PostgreSQL  
- SQLite  
- Oracle  
- SQL Server  

------------------------------------------
------------------------------------------

# 1. TABLE

## OCCUPATIONS

| Column | Type   |
|------|--------|
| Name | String |
| Occupation | String |

Constraint:

The **Occupation** column contains only the following values:

- Doctor
- Professor
- Singer
- Actor

### Example Data

| Name      | Occupation |
|-----------|------------|
| Samantha  | Doctor     |
| Julia     | Actor      |
| Maria     | Actor      |
| Meera     | Singer     |
| Ashely    | Professor  |
| Ketty     | Professor  |
| Christeen | Professor  |
| Jane      | Actor      |
| Jenny     | Doctor     |
| Priya     | Singer     |

------------------------------------------
------------------------------------------

# 2. PROBLEM

Generate **two result sets** from the OCCUPATIONS table.

### Result Set 1

Query an **alphabetically ordered list of all names**, immediately followed by the **first letter of their occupation enclosed in parentheses**.

Example format:

```
Name(FirstLetterOfOccupation)
```

Examples:

```
Ashley(P)
Julia(A)
Maria(A)
Meera(S)
Samantha(D)
```

------------------------------------------

### Result Set 2

Query the **number of occurrences of each occupation**.

Output format:

```
There are a total of [occupation_count] [occupation]s.
```

Rules:

- Sort by **ascending occupation_count**
- If counts are equal → **sort alphabetically by occupation**
- Occupation names must appear **in lowercase**

Example format:

```
There are a total of 2 doctors.
There are a total of 2 singers.
There are a total of 3 actors.
There are a total of 3 professors.
```

------------------------------------------
------------------------------------------

# 3. ANSWER

## Query 1 — Names with Occupation Initial

```sql
SELECT 
    CONCAT(Name, '(', SUBSTRING(Occupation,1,1), ')') AS formatted_name
FROM OCCUPATIONS
ORDER BY Name;
```

------------------------------------------

## Query 2 — Count of Each Occupation

```sql
SELECT 
    CONCAT('There are a total of ', COUNT(*), ' ', LOWER(Occupation), 's.') AS occupation_summary
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(*), Occupation;
```

------------------------------------------
------------------------------------------

# 4. EXPLANATION

## Query 1 Explanation

Step 1 — Extract First Letter of Occupation

```
SUBSTRING(Occupation,1,1)
```

This retrieves the **first character** of the occupation.

Example:

| Occupation | Result |
|-----------|--------|
Doctor | D |
Actor | A |
Professor | P |
Singer | S |

------------------------------------------

Step 2 — Combine Name and Occupation Initial

```
CONCAT(Name, '(', SUBSTRING(Occupation,1,1), ')')
```

Creates formatted output like:

```
Samantha(D)
Julia(A)
Maria(A)
```

------------------------------------------

Step 3 — Sort Alphabetically

```
ORDER BY Name
```

Ensures names appear in **alphabetical order**.

------------------------------------------

## Query 2 Explanation

Step 1 — Count Occupations

```
COUNT(*)
```

Counts the number of rows for each occupation.

------------------------------------------

Step 2 — Convert Occupation to Lowercase

```
LOWER(Occupation)
```

Ensures the output matches required formatting.

Example:

| Occupation | Output |
|-----------|--------|
Doctor | doctor |
Professor | professor |

------------------------------------------

Step 3 — Create Output Sentence

```
CONCAT('There are a total of ', COUNT(*), ' ', LOWER(Occupation), 's.')
```

Example output:

```
There are a total of 3 actors.
```

------------------------------------------

Step 4 — Group by Occupation

```
GROUP BY Occupation
```

This groups rows by occupation so counts can be calculated.

------------------------------------------

Step 5 — Sorting Results

```
ORDER BY COUNT(*), Occupation
```

Sorting rules:

1. By **number of occurrences (ascending)**
2. If counts match → sort by **occupation alphabetically**

------------------------------------------
------------------------------------------

# 5. SQL CONCEPTS USED

| Concept | Purpose |
|------|------|
SELECT | Retrieve data |
CONCAT | Combine strings |
SUBSTRING | Extract first character |
LOWER | Convert text to lowercase |
COUNT | Aggregate row counts |
GROUP BY | Group rows |
ORDER BY | Sort results |

------------------------------------------
------------------------------------------

# INTERVIEW TIP

This problem tests **three important SQL skills**:

### 1. String Formatting

```
CONCAT(Name,'(',initial,')')
```

### 2. Aggregation

```
COUNT(*) + GROUP BY
```

### 3. Custom Output Formatting

Transforming query results into **human-readable sentences**.

These patterns appear frequently in:

- Reporting queries
- Dashboard outputs
- Log summarization systems

------------------------------------------
------------------------------------------