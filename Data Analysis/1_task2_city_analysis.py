import pandas as pd

file_path = "Copy of Dataset .csv"
df = pd.read_csv(file_path)

city_counts = df['City'].value_counts()
top_city = city_counts.idxmax()
top_city_count = city_counts.max()

average_ratings = df.groupby('City')['Aggregate rating'].mean()

highest_avg_rating_city = average_ratings.idxmax()
highest_avg_rating = average_ratings.max()

print(f"City with the highest number of restaurants: {top_city} ({top_city_count} restaurants)")
print("\nAverage rating per city:")
print(average_ratings.sort_values(ascending=False))

print(f"\nCity with the highest average rating: {highest_avg_rating_city} ({highest_avg_rating:.2f} rating)")
