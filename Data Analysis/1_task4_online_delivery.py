import pandas as pd

file_path = "Copy of Dataset .csv"
df = pd.read_csv(file_path)

df['Has Online delivery'] = df['Has Online delivery'].str.strip().str.lower()

delivery_counts = df['Has Online delivery'].value_counts()
total_restaurants = len(df)

delivery_percentages = (delivery_counts / total_restaurants) * 100
average_rating_with_delivery = df[df['Has Online delivery'] == 'yes']['Aggregate rating'].mean()
average_rating_without_delivery = df[df['Has Online delivery'] == 'no']['Aggregate rating'].mean()

print(f"Percentage of restaurants offering online delivery: {delivery_percentages.get('yes', 0):.2f}%")
print(f"Percentage of restaurants without online delivery: {delivery_percentages.get('no', 0):.2f}%")
print(f"\nAverage rating of restaurants with online delivery: {average_rating_with_delivery:.2f}")
print(f"Average rating of restaurants without online delivery: {average_rating_without_delivery:.2f}")

