import pandas as pd
import numpy as np

df = pd.read_csv("sales.csv")
print(df)

df["Total"] = df["Quantity"] * df["Price"]

print("\nWith Total column:")
print(df)



# total sales
total_sales = np.sum(df["Total"])

# daily sales
daily_sales = df.groupby("Date")["Total"].sum()

avg_daily_sales = np.mean(daily_sales)
std_daily_sales = np.std(daily_sales)

print("\nTotal Sales:", total_sales)
print("Average Daily Sales:", avg_daily_sales)
print("Standard Deviation of Daily Sales:", std_daily_sales)

product_qty = df.groupby("Product")["Quantity"].sum()
best_product = product_qty.idxmax()

print("\nBest Selling Product:", best_product)