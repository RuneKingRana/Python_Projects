import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (update the file path if needed)
file_path = "Copy of Dataset .csv"  # Ensure the file is in the same directory or provide a full path
df = pd.read_csv(file_path)

# Drop missing values in 'Votes' and 'Aggregate rating' columns
df = df.dropna(subset=['Votes', 'Aggregate rating'])

# Convert 'Votes' and 'Aggregate rating' to numeric
df['Votes'] = pd.to_numeric(df['Votes'], errors='coerce')
df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')

# Identify the restaurants with the highest and lowest number of votes
highest_votes_restaurant = df.loc[df['Votes'].idxmax(), ['Restaurant Name', 'Votes', 'Aggregate rating']]
lowest_votes_restaurant = df.loc[df['Votes'].idxmin(), ['Restaurant Name', 'Votes', 'Aggregate rating']]

# Calculate correlation between number of votes and aggregate rating
correlation = df[['Votes', 'Aggregate rating']].corr().iloc[0, 1]

# Print results
print(f"Restaurant with highest votes: {highest_votes_restaurant['Restaurant Name']} ({highest_votes_restaurant['Votes']} votes, Rating: {highest_votes_restaurant['Aggregate rating']})")
print(f"Restaurant with lowest votes: {lowest_votes_restaurant['Restaurant Name']} ({lowest_votes_restaurant['Votes']} votes, Rating: {lowest_votes_restaurant['Aggregate rating']})")
print(f"\nCorrelation between number of votes and rating: {correlation:.2f}")

# Plot a scatter plot to visualize correlation
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Votes', y='Aggregate rating', alpha=0.5)
plt.xlabel("Number of Votes")
plt.ylabel("Aggregate Rating")
plt.title("Correlation Between Number of Votes and Rating")
plt.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
