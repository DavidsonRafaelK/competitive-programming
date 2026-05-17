# Write your MySQL query statement below
SELECT e.name AS Employee
FROM employee AS e
INNER JOIN
employee AS m ON e.managerId = m.id AND e.salary > m.salary;