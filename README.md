Sales Data Analysis Project
Overview

This project performs basic data analysis and visualization on a sales dataset using Python. It processes raw transactional data, extracts insights, and generates visual representations to understand sales performance across products, categories, cities, and time.

The goal is simple: turn raw CSV data into meaningful business insights.

Files in the Project
analysis.py
Main script that performs data cleaning, analysis, and visualization.
data.csv
Dataset containing sales records (products, price, quantity, city, category, order date, etc.).
final excel analysis.xlsx
Processed or summarized data (likely used for reporting or manual inspection).
final.sql
SQL queries for analyzing or extracting insights from the dataset.
What the Script Actually Does
1. Loads Data
Reads the dataset using pandas
Displays:
First 5 rows
Dataset structure (info())
Statistical summary (describe())
2. Data Processing

Creates a new column:

total_sales = price * quantity
Converts order_date into proper datetime format
3. Key Insights Generated
Total revenue
Category-wise frequency
Average sales per category
Most sold products
City-wise total sales
4. Business Observation (from code logic)
Accessories contribute less revenue compared to electronics
(based on lower average sales and quantity)
Visualizations

The script generates 3 main plots:

1. Product vs Total Sales (Bar Chart)
Shows which products generate the most revenue
2. Category Distribution (Pie Chart)
Displays contribution of each category to total sales
3. Sales Over Time (Line Chart)
Tracks how sales change over time
How to Run
Step 1: Install Dependencies
pip install pandas matplotlib
Step 2: Run the Script
python analysis.py
Requirements
Python 3.x
pandas
matplotlib
