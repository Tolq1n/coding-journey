#2356. Number of Unique Subjects Taught by Each Teacher

# SELECT DISTINCT teacher_id ,COUNT(DISTINCT subject_id) as CNT
# FROM Teacher
# GROUP BY teacher_id;


#183. Customers Who Never Order

# SELECT name AS customers FROM customers
# WHERE id NOT IN (SELECT customerId FROM orders);