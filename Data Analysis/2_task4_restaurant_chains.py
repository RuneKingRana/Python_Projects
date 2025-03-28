import pandas as pd

# Load the dataset (update the file path if needed)
file_path = "Copy of Dataset .csv"  # Ensure the file is in the same directory or provide a full path
df = pd.read_csv(file_path)

# Identify restaurant chains by counting occurrences of restaurant names
restaurant_counts = df['Restaurant Name'].value_counts()

# Filter to get only restaurant chains (restaurants with more than one occurrence)
restaurant_chains = restaurant_counts[restaurant_counts > 1]

# Analyze ratings and popularity of restaurant chains
chain_data = df[df['Restaurant Name'].isin(restaurant_chains.index)]

# Calculate the average rating for each restaurant chain
chain_avg_ratings = chain_data.groupby('Restaurant Name')['Aggregate rating'].mean()

# Calculate the total number of votes for each restaurant chain (popularity measure)
chain_total_votes = chain_data.groupby('Restaurant Name')['Votes'].sum()

# Combine rating and popularity data
chain_analysis = pd.DataFrame({'Average Rating': chain_avg_ratings, 'Total Votes': chain_total_votes})

# Sort by popularity (total votes) to see the most popular chains
chain_analysis = chain_analysis.sort_values(by='Total Votes', ascending=False)

# Print results
print("Identified Restaurant Chains:")
print(restaurant_chains)

print("\nAnalysis of Ratings and Popularity of Restaurant Chains:")
print(chain_analysis)
