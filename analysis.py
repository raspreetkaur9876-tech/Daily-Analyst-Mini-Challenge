import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset/SampleSuperstore.csv")

# Display basic information
print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())

# Total Sales and Profit
print("\nTotal Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Category:")
print(category_sales)

# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Region:")
print(region_sales)

# Sales by Sub-Category
subcategory_sales = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False)
print("\nTop 5 Sub-Categories:")
print(subcategory_sales.head())

# Category Sales Chart
category_sales.plot(kind="bar", title="Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# Region Sales Chart
region_sales.plot(kind="bar", title="Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()