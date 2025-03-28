import pandas as pd
import matplotlib.pyplot as plt

file_path = "Copy of Dataset .csv"
df = pd.read_csv(file_path)

price_range_counts = df['Price range'].value_counts().sort_index()

total_restaurants = len(df)
price_range_percentages = (price_range_counts / total_restaurants) * 100

print("Percentage of Restaurants in Each Price Range:")
for price, percentage in price_range_percentages.items():
    print(f"Price Range {price}: {percentage:.2f}%")

plt.figure(figsize=(8, 5))
plt.bar(price_range_counts.index.astype(str), price_range_counts.values, color='skyblue')
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.title("Distribution of Price Ranges Among Restaurants")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
