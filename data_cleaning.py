import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

print("All libraries imported successfully!")
# Load the Excel dataset
file_path = Path("data") / "Online Retail.xlsx"

df = pd.read_excel(file_path)

# Display the first 5 rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Display dataset information
print("\nDataset shape (rows, columns):")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())
# Check missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Check duplicate rows
print("\n--- Duplicate Rows ---")
print("Number of duplicate rows:", df.duplicated().sum())

# Check dataset information
print("\n--- Dataset Information ---")
df.info()
# Create a copy of the original dataset
cleaned_df = df.copy()

# Remove duplicate rows
cleaned_df = cleaned_df.drop_duplicates()

# Fill missing product descriptions with "Unknown"
cleaned_df["Description"] = cleaned_df["Description"].fillna("Unknown")

# Check missing values after cleaning
print("\n--- Missing Values After Cleaning ---")
print(cleaned_df.isnull().sum())

# Compare row counts
print("\n--- Cleaning Summary ---")
print("Original rows:", len(df))
print("Rows after removing duplicates:", len(cleaned_df))
print("Duplicate rows removed:", len(df) - len(cleaned_df))
cleaned_df.to_csv("data/Online_Retail_Cleaned.csv", index=False)
cleaned_df.to_csv("data/Online_Retail_Cleaned.csv", index=False)
# Validate the cleaned dataset
print("\n--- Data Validation ---")

print("Duplicate rows remaining:", cleaned_df.duplicated().sum())

print("Missing Description values:", cleaned_df["Description"].isnull().sum())

print("Total rows in cleaned dataset:", len(cleaned_df))

print("Total columns:", len(cleaned_df.columns))
# Check invalid or unusual values
print("\n--- Quantity and Price Checks ---")

print("Quantity zero or below:",
      (cleaned_df["Quantity"] <= 0).sum())

print("UnitPrice zero or below:",
      (cleaned_df["UnitPrice"] <= 0).sum())

print("Missing CustomerID:",
      cleaned_df["CustomerID"].isnull().sum())
# Inspect unusual values before deciding what to do
print("\n--- Sample Rows with Non-positive Quantity ---")
print(cleaned_df[cleaned_df["Quantity"] <= 0].head())

print("\n--- Sample Rows with Non-positive UnitPrice ---")
print(cleaned_df[cleaned_df["UnitPrice"] <= 0].head())
# Check data types after cleaning
print("\n--- Data Types Check ---")
print(cleaned_df.dtypes)
# Count transactions by country
country_counts = cleaned_df["Country"].value_counts().head(10)

print("\n--- Top 10 Countries by Number of Records ---")
print(country_counts)
# Create a bar chart
plt.figure(figsize=(10, 6))

country_counts.plot(kind="bar")

plt.title("Top 10 Countries by Number of Records")
plt.xlabel("Country")
plt.ylabel("Number of Records")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("data/top_10_countries.png")
plt.show()

print("\nChart saved successfully!")
# Calculate sales revenue
cleaned_df["Revenue"] = cleaned_df["Quantity"] * cleaned_df["UnitPrice"]

# Group revenue by month
cleaned_df["Month"] = cleaned_df["InvoiceDate"].dt.to_period("M")

monthly_sales = cleaned_df.groupby("Month")["Revenue"].sum()

print("\n--- Monthly Sales Revenue ---")
print(monthly_sales)
# Create monthly sales line chart
plt.figure(figsize=(12, 6))

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.savefig("data/monthly_sales_trend.png")
plt.show()

print("\nMonthly sales chart saved successfully!")
# Final testing of the cleaned CSV file
print("\n--- Final Project Testing ---")

saved_df = pd.read_csv("data/Online_Retail_Cleaned.csv")

print("CSV file loaded successfully:", not saved_df.empty)
print("Total rows:", len(saved_df))
print("Total columns:", len(saved_df.columns))
print("Duplicate rows:", saved_df.duplicated().sum())
print("Missing Description values:",
      saved_df["Description"].isnull().sum())

print("\nFinal testing completed!")