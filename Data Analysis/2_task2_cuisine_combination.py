import pandas as pd
from collections import Counter

# Load the dataset (update the file path if needed)
file_path = "Copy of Dataset .csv"  # Ensure the file is in the same directory or provide a full path
df = pd.read_csv(file_path)

# Drop rows with missing cuisines and ratings
df = df.dropna(subset=['Cuisines', 'Aggregate rating'])

# Standardize cuisine combinations (remove spaces and sort to treat "Indian, Chinese" the same as "Chinese, Indian")
df['Cuisines'] = df['Cuisines'].apply(lambda x: ', '.join(sorted([c.strip() for c in x.split(',')])))

# Count occurrences of each cuisine combination
cuisine_combinations_counts = Counter(df['Cuisines'])

# Get the top 5 most common cuisine combinations
top_5_cuisine_combinations = cuisine_combinations_counts.most_common(5)

# Calculate the average rating for each cuisine combination
average_ratings = df.groupby('Cuisines')['Aggregate rating'].mean()

# Determine if certain cuisine combinations tend to have higher ratings
top_combinations_ratings = {cuisine: average_ratings[cuisine] for cuisine, _ in top_5_cuisine_combinations}

# Print results
print("Top 5 Most Common Cuisine Combinations:")
for cuisine, count in top_5_cuisine_combinations:
    print(f"{cuisine}: {count} restaurants")

print("\nAverage Ratings for Top Cuisine Combinations:")
for cuisine, rating in top_combinations_ratings.items():
    print(f"{cuisine}: {rating:.2f} average rating")
