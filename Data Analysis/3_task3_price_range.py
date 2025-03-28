import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "Copy of Dataset .csv"  # Ensure the file is in the same directory or provide a full path
df = pd.read_csv(file_path)

# Clean and standardize columns
df['Has Online delivery'] = df['Has Online delivery'].astype(str).str.strip().str.lower()
df['Has Table booking'] = df['Has Table booking'].astype(str).str.strip().str.lower()

# Group by price range and calculate percentages of restaurants offering online delivery & table booking
price_delivery = df.groupby('Price range')['Has Online delivery'].value_counts(normalize=True).unstack() * 100
price_table_booking = df.groupby('Price range')['Has Table booking'].value_counts(normalize=True).unstack() * 100

# Fill NaN values with 0 in case some categories are missing
price_delivery = price_delivery.fillna(0)
price_table_booking = price_table_booking.fillna(0)

# Print results
print("Online Delivery Availability by Price Range:\n", price_delivery)
print("\nTable Booking Availability by Price Range:\n", price_table_booking)

# Determine if higher-priced restaurants are more likely to offer these services
higher_price_delivery = price_delivery.loc[price_delivery.index.max(), 'yes']
higher_price_table_booking = price_table_booking.loc[price_table_booking.index.max(), 'yes']

lower_price_delivery = price_delivery.loc[price_delivery.index.min(), 'yes']
lower_price_table_booking = price_table_booking.loc[price_table_booking.index.min(), 'yes']

print("\nConclusion:")
if higher_price_delivery > lower_price_delivery:
    print(f"Higher-priced restaurants ({higher_price_delivery:.2f}%) are more likely to offer online delivery than lower-priced restaurants ({lower_price_delivery:.2f}%).")
else:
    print(f"Lower-priced restaurants ({lower_price_delivery:.2f}%) are more likely to offer online delivery than higher-priced restaurants ({higher_price_delivery:.2f}%).")

if higher_price_table_booking > lower_price_table_booking:
    print(f"Higher-priced restaurants ({higher_price_table_booking:.2f}%) are more likely to offer table booking than lower-priced restaurants ({lower_price_table_booking:.2f}%).")
else:
    print(f"Lower-priced restaurants ({lower_price_table_booking:.2f}%) are more likely to offer table booking than higher-priced restaurants ({higher_price_table_booking:.2f}%).")

# Plot Online Delivery vs Price Range
plt.figure(figsize=(8, 5))
price_delivery.plot(kind='bar', stacked=True, color=['lightcoral', 'lightgreen'])
plt.xlabel("Price Range")
plt.ylabel("Percentage of Restaurants")
plt.title("Online Delivery Availability by Price Range")
plt.xticks(rotation=0)
plt.legend(title="Online Delivery")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Plot Table Booking vs Price Range
plt.figure(figsize=(8, 5))
price_table_booking.plot(kind='bar', stacked=True, color=['lightcoral', 'lightblue'])
plt.xlabel("Price Range")
plt.ylabel("Percentage of Restaurants")
plt.title("Table Booking Availability by Price Range")
plt.xticks(rotation=0)
plt.legend(title="Table Booking")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
