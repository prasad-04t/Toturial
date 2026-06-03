# SQL PRACTICE — CUSTOMERS, ORDERS, AND SHIPPINGS TABLES

This document provides SQL practice examples using three related tables:

- Customers
- Orders
- Shippings

Each section contains:

1. Table  
2. Problem  
3. Answer (SQL Query)  
4. Clear Explanation  

All queries follow **standard SQL syntax** and work in:

- MySQL  
- PostgreSQL  
- SQLite  
- Oracle  
- SQL Server  

------------------------------------------
------------------------------------------

# 1. TABLE

## Customers

| Column       | Type |
|---------------|------|
| customer_id   | INT |
| first_name    | VARCHAR(100) |
| last_name     | VARCHAR(100) |
| age           | INT |
| country       | VARCHAR(100) |

Description:

The **Customers** table stores customer information.

- **customer_id** → Unique customer identifier
- **first_name** → Customer's first name
- **last_name** → Customer's last name
- **age** → Customer age
- **country** → Country of residence

------------------------------------------

## Orders

| Column      | Type |
|--------------|------|
| order_id     | INT |
| item         | VARCHAR(100) |
| amount       | INT |
| customer_id  | INT |

Description:

The **Orders** table stores purchase information.

- **order_id** → Unique order identifier
- **item** → Purchased product
- **amount** → Price or quantity of order
- **customer_id** → Foreign key referencing **Customers.customer_id**

------------------------------------------

## Shippings

| Column        | Type |
|---------------|------|
| shipping_id   | INT |
| status        | INT |
| customer      | INT |

Description:

The **Shippings** table tracks shipment status.

- **shipping_id** → Unique shipping identifier
- **status** → Shipping status code
- **customer** → Customer associated with the shipment

------------------------------------------
------------------------------------------

# 2. PROBLEM

Write SQL queries to retrieve useful business insights from the tables.

Problems include:

1. Retrieve all customers.
2. Retrieve all orders placed by customers.
3. Retrieve customers along with their orders.
4. Retrieve customers and shipping status.
5. Retrieve customers who have placed orders greater than a specific amount.

------------------------------------------
------------------------------------------

# 3. ANSWER

## Query 1 — Retrieve All Customers

```sql
SELECT *
FROM Customers;
```

------------------------------------------

## Query 2 — Retrieve All Orders

```sql
SELECT *
FROM Orders;
```

------------------------------------------

## Query 3 — Retrieve Customers with Their Orders

```sql
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    o.order_id,
    o.item,
    o.amount
FROM Customers c
JOIN Orders o
ON c.customer_id = o.customer_id;
```

------------------------------------------

## Query 4 — Retrieve Customers and Their Shipping Status

```sql
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    s.shipping_id,
    s.status
FROM Customers c
JOIN Shippings s
ON c.customer_id = s.customer;
```

------------------------------------------

## Query 5 — Retrieve Customers with Orders Greater Than 100

```sql
SELECT
    c.first_name,
    c.last_name,
    o.amount
FROM Customers c
JOIN Orders o
ON c.customer_id = o.customer_id
WHERE o.amount > 100;
```

------------------------------------------
------------------------------------------

# 4. CLEAR EXPLANATION

## Query 1 Explanation

```
SELECT *
FROM Customers
```

- `SELECT *` retrieves all columns.
- `FROM Customers` specifies the table.

Result:

All customers stored in the database are displayed.

------------------------------------------

## Query 2 Explanation

```
SELECT *
FROM Orders
```

This retrieves all order information.

Useful for:

- Viewing transaction history
- Auditing order records

------------------------------------------

## Query 3 Explanation

```
JOIN Orders o
ON c.customer_id = o.customer_id
```

This query joins two tables:

Customers → contains customer details  
Orders → contains order details  

The join condition ensures that each order is matched with the correct customer.

Result example:

| customer_id | first_name | order_id | item | amount |
|--------------|-------------|----------|------|--------|

------------------------------------------

## Query 4 Explanation

```
JOIN Shippings s
ON c.customer_id = s.customer
```

This join links:

Customers → personal information  
Shippings → shipping information

Result:

Displays the shipping status associated with each customer.

------------------------------------------

## Query 5 Explanation

```
WHERE o.amount > 100
```

Filters results to show only high-value orders.

Use cases:

- Identifying high-value customers
- Analyzing revenue-generating purchases

------------------------------------------
------------------------------------------

# 5. SQL CONCEPTS USED

| Concept | Purpose |
|------|------|
SELECT | Retrieve data |
JOIN | Combine data from tables |
WHERE | Filter rows |
Aliases | Shorten table names |
Comparison operators | Filter conditions |

------------------------------------------
------------------------------------------

# INTERVIEW TIP

These tables demonstrate a **typical relational database design**:

```
Customers
   │
   ├── Orders
   │
   └── Shippings
```

Key SQL concept tested here:

**Foreign Key Relationships**

Example:

```
Orders.customer_id → Customers.customer_id
```

This allows queries to combine data across tables using **JOIN operations**.

------------------------------------------
------------------------------------------