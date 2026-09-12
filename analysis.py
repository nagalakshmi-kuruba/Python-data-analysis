import pandas as pd

data = pd.read_csv("sales_data.csv")

data["Sales"] = data["Quantity"] * data["Price"]

total_sales = data["Sales"].sum()

print("Total Sales:", total_sales)
product_sales = data.groupby("Product")["Sales"].sum()

print("\nSales by Product:")
print(product_sales)
import matplotlib.pyplot as plt

product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("sales_by_product.png")
plt.show()