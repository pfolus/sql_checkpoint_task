1. SELECT name FROM customers
	WHERE gender = "Female";

2. SELECT SUM(net_value) FROM sales;

3. SELECT * FROM customers
	WHERE birthyear <= 1999
		ORDER BY birthyear;

4. SELECT * FROM customers
	ORDER BY surname;

5. SELECT * FROM sales
	WHERE product_name LIKE "%a%";

6. SELECT * FROM sales
	WHERE net_value > 500;

7. SELECT max(id) FROM customers;

8. SELECT max(id) FROM sales;

9. SELECT SUM(net_value) FROM sales
	WHERE customer_id = 7;

10.