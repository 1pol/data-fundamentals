import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv")
print("the first 5 rows of data :")
df.head()
print("dataset structure: ")
print(df.info())
print(df.describe())
print(df.dtypes)
print("creating total sales")
df["total_sales"] = df["price"]*df["quantity"]
print("Total Revenue:", df["total_sales"].sum())
df["order_date"] = pd.to_datetime(df["order_date"])
print(df["category"].value_counts())
print(df.groupby("category")["total_sales"].mean())
'''
SINCE HERE THE AVERAGE REVENUE IS LESSER AND QUANTITY SOLD IS LESS,
WE CAN CONCLUDE THAT THE CONTRIBUTION OF ACCESSORIES TOWARDS TOTAL
REVENUE IS LESSER COMPARED TO ELECTRONICS.
'''
print("the most sold product is : ",df.groupby("product")["quantity"].sum().sort_values(ascending=False))

print("sales in order of cities are : ",df.groupby("city")["total_sales"].sum())
print("final summarised stats :")
print(df.describe())

print("the relation between product and sales :")
df.groupby("product")["total_sales"].sum().plot(kind="bar")
plt.title("Product vs Total Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

print("category sales distribution :")
df.groupby("category")["total_sales"].sum().plot(kind="pie", autopct='%1.1f%%')
plt.title("Category Sales Distribution")
plt.ylabel("")
plt.show()

print("sales trend over time :")
df["order_date"] = pd.to_datetime(df["order_date"])
df.groupby("order_date")["total_sales"].sum().plot(kind="line", marker='o')
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()

