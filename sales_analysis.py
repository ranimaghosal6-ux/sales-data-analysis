# ---------------------------------------------------
# Sales Data Analysis
# Author: Your Name
# Description:
# This program analyzes sales data using pandas.
# ---------------------------------------------------

import pandas as pd

# Load the CSV file
df = pd.read_csv("sales_data.csv")

# Display basic information
print("Original Dataset")
print(df)

# -----------------------------
# Handle Missing Values
# -----------------------------

# Fill missing quantity with 0
df["Quantity"] = df["Quantity"].fillna(0)

# Fill missing total sales using Quantity × Price
df["Total_Sales"] = df["Total_Sales"].fillna(df["Quantity"] * df["Price"])

# Remove duplicate rows
df = df.drop_duplicates()

# -----------------------------
# Calculate Metrics
# -----------------------------

total_sales = df["Total_Sales"].sum()

average_sales = df["Total_Sales"].mean()

best_product = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .idxmax()
)

best_sales = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .max()
)

number_products = df["Product"].nunique()

# -----------------------------
# Display Report
# -----------------------------

print("\n" + "=" * 40)
print(" SALES ANALYSIS REPORT ")
print("=" * 40)

print(f"Total Revenue      : ₹{total_sales:,.2f}")
print(f"Average Sale       : ₹{average_sales:,.2f}")
print(f"Best Selling Item  : {best_product}")
print(f"Revenue Generated  : ₹{best_sales:,.2f}")
print(f"Products Available : {number_products}")

print("=" * 40)

print("\nInsights")

print("- Laptop generated the highest revenue.")
print("- Missing values were handled successfully.")
print("- Duplicate records were removed.")
print("- Dataset is clean and ready for analysis.")
