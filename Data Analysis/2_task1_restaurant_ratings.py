import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (update the file path if needed)
file_path = "Copy of Dataset .csv"  # Ensure the file is in the same directory or provide a full path
df = pd.read_csv(file_path)

# Drop missing values in 'Aggregate rating' and 'Votes' columns
df = df.dropna(subset=['Aggregate rating', 'Votes'])

# Convert 'Aggregate rating' to numeric in case of inconsistencies
df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')

# Analyze the distribution of aggregate ratings
rating_counts = df['Aggregate rating'].value_counts().sort_index()

# Determine the most common rating range
most_common_rating = rating_counts.idxmax()
most_common_count = rating_counts.max()

# Calculate the average number of votes received by restaurants
average_votes = df['Votes'].mean()

# Print results
print(f"Most common rating: {most_common_rating} (appears {most_common_count} times)")
print(f"Average number of votes received by restaurants: {average_votes:.2f}")

# Plot a histogram to visualize rating distribution
plt.figure(figsize=(8, 5))
plt.hist(df['Aggregate rating'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")
plt.title("Distribution of Aggregate Ratings")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()
