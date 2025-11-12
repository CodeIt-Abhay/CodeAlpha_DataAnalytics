import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv("amazon_products.csv")

# Convert Price safely
data["Price"] = pd.to_numeric(data["Price"], errors="coerce")

# Extract numeric ratings (e.g., '4.3 out of 5 stars' → 4.3)
data["Rating"] = data["Rating"].astype(str).str.extract(r"(\d+\.\d+)").astype(float)

# Drop rows with missing values
data.dropna(subset=["Price", "Rating"], inplace=True)

# Sort and take top 10
top_rated = data.sort_values(by="Rating", ascending=False).head(10)

# Bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x="Rating", y="Product Name", data=top_rated, palette="mako", edgecolor="black")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.title("Top 10 Highest Rated Laptops on Amazon", fontsize=14, weight="bold")
plt.xlabel("Rating (out of 5)", fontsize=12)
plt.ylabel("Product Name", fontsize=12)
plt.tight_layout(pad=3)
plt.subplots_adjust(left=0.35, right=0.95, top=0.9, bottom=0.1)  # add space for long names
plt.show()

# Histogram of prices
plt.figure(figsize=(8, 5))
sns.histplot(data["Price"], bins=20, kde=True)
plt.title("Distribution of Laptop Prices")
plt.xlabel("Price (INR)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Scatter plot
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Price", y="Rating", data=data)
plt.title("Price vs Rating of Laptops")
plt.xlabel("Price (INR)")
plt.ylabel("Rating")
plt.tight_layout()
plt.show()

print("✅ Visualization completed successfully!")
