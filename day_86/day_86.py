#181. Employees Earning More Than Their Managers

# SELECT E.name AS Employee FROM Employee E,Employee M
# WHERE E.managerId=M.id AND E.salary>M.salary

#595. Big Countries

#SELECT name, population, area FROM World WHERE (area >= 3000000 OR population >= 25000000)