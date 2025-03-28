import pandas as pd
from collections import Counter

file_path = "Copy of Dataset .csv"
df = pd.read_csv(file_path)

df = df.dropna(subset=['Cuisines'])

cuisine_list = [cuisine.strip() for cuisines in df['Cuisines'] for cuisine in cuisines.split(",")]
cuisine_counts = Counter(cuisine_list)

top_3_cuisines = cuisine_counts.most_common(3)

total_restaurants = len(df)
top_cuisine_percentages = {cuisine: (count / total_restaurants) * 100 for cuisine, count in top_3_cuisines}

print("Top 3 Most Common Cuisines:")
for cuisine, count in top_3_cuisines:
    percentage = top_cuisine_percentages[cuisine]
    print(f"{cuisine}: {count} restaurants ({percentage:.2f}%)")
