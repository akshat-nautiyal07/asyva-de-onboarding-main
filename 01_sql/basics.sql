-- basics.sql
-- Add your queries here

## Online SQL Compiler
  SELECT * FROM Customers;
  SELECT first_name, last_name, age FROM Customers;
  
  INSERT INTO Orders VALUES (6, "Headphones", 500,5)
  
  select order_id,item, customer_id
  from Orders
  where amount = 250;
  
  UPDATE Shippings SET status = "Failed" where shipping_id=4;
  
  DELETE FROM Customers WHERE first_name="John" AND last_name="Doe";
  
  SELECT * FROM Shippings WHERE status <> "Failed";
  
  
  SELECT min(amount) as Minimum, max(amount) as Maximum FROM Orders;

  -- handle the null value
  SELECT employee_id, COALESCE(employee_name, "Unknown") AS Cleaned_name, COALESCE(employee_salary, 0) AS Adjusted_salary
  FROM Employees;

  SELECT Customers.first_name, Customers.country, Orders.item, Orders.amount
  FROM Customers
  INNER JOIN Orders ON Customers.customer_id = Orders.customer_id
  GROUP BY Customers.first_name;

  SELECT Customers.first_name, Customers.country, Employees.employee_salary
  FROM Customers
  LEFT JOIN Employees ON Customers.first_name = Employees.employee_name;

  SELECT Customers.first_name, Customers.last_name, Orders.item
  FROM Customers
  CROSS JOIN Orders;

  -- Left Anti Join
  SELECT e.employee_id,e.employee_name,e.employee_salary
  FROM Employees AS e
  LEFT JOIN Customers as c ON c.customer_id = e.employee_id
  WHERE c.customer_id IS NULL;

  -- Union remove the duplicate data
  SELECT first_name FROM Customers
  UNION
  SELECT employee_name FROM Employees;
  
  SELECT first_name FROM Customers
  UNION ALL
  SELECT employee_name FROM Employees;

## W3 Schools

  SELECT DISTINCT Unit FROM Products;

  SELECT SUM(Price) FROM Products;

  SELECT MIN(Price) FROM Products;
  
  SELECT MAX(Price) FROM Products;
  
  SELECT AVG(Price) FROM Products;

  SELECT Unit, COUNT(Unit) 
  FROM Products
  GROUP BY Unit;

  SELECT City, COUNT(CustomerID) as [Number of customers]
  FROM Customers
  GROUP BY City;
  
  SELECT * FROM Products
  ORDER BY ProductName ASC;


## CTE 

  WITH completeRecord AS (
  SELECT e.employee_id,e.employee_name,e.employee_salary
  FROM Employees AS e
  LEFT JOIN Customers as c ON c.customer_id = e.employee_id
  )
  
  SELECT * FROM completeRecord;


  WITH customerTable AS (
    SELECT * FROM Customers
  ),
  
  EmployeeTable AS (
  SELECT * FROM Employees
  )
  
  SELECT * 
  FROM customerTable as c
  INNER JOIN EmployeeTable as e ON c.first_name = e.employee_name;

  -- give second highest salary if there are no duplicate records
  SELECT *
  FROM Employees
  ORDER BY employee_salary DESC
  LIMIT 1 OFFSET 1;
  -- we can also use sub quries in this case

## Window Functions

  # Ranking window functions
  
    SELECT name, salary,
    RANK() OVER (ORDER BY salary DESC) as rank,
    ROW_NUMBER() OVER (ORDER BY salary DESC) as row_number,
    DENSE_RANK() OVER (ORDER BY salary DESC) as dense
    FROM Employees;
