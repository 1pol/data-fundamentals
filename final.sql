-- DISPLAY ALL SALES RECORDS
SELECT * FROM sales_data;

--DISPLAY TOTAL SALES REVENUE
SELECT SUM(quantity * price) AS total_revenue
FROM sales_data;

--TOP SELLING PRODUCT BY QUANTITY
SELECT product, SUM(quantity) AS total_quantity
FROM sales_data
GROUP BY product
ORDER BY total_quantity DESC
LIMIT 1;

--REVENUE BY CITY 
SELECT city, SUM(quantity * price) AS revenue
FROM sales_data
GROUP BY city;

--CATEGOR WISE REVENUE
SELECT category, SUM(quantity * price) AS revenue
FROM sales_data
GROUP BY category;

--HIGHEST ORDER VALUE
SELECT order_id, (quantity * price) AS order_value
FROM sales_data
ORDER BY order_value DESC
LIMIT 1;

--AVERAGE PRODUCT PRICE
SELECT AVG(price) AS avg_price
FROM sales_data;