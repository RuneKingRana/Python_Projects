import pandas as pd
import re
import nltk
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords

# Download stopwords if not already present
nltk.download('stopwords')

# Load the dataset (update the file path if needed)
file_path = "Copy of Dataset .csv"  # Ensure the file is in the same directory or provide a full path
df = pd.read_csv(file_path)

# Drop missing values in 'Reviews' and 'Aggregate rating' columns
df = df.dropna(subset=['Rating text', 'Aggregate rating'])

# Function to clean text
def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]  # Remove stopwords
    return words

# Process reviews
df['Cleaned Rating text'] = df['Rating text'].astype(str).apply(clean_text)

# Flatten the list of words for positive and negative keyword analysis
all_words = [word for review in df['Cleaned Rating text'] for word in review]
word_counts = Counter(all_words)

# Define some common positive and negative words (for simplicity)
positive_words = {'good', 'great', 'amazing', 'excellent', 'best', 'tasty', 'delicious'}
negative_words = {'bad', 'worst', 'poor', 'terrible', 'awful', 'horrible', 'disappointing'}

# Count positive and negative words
positive_keywords = {word: count for word, count in word_counts.items() if word in positive_words}
negative_keywords = {word: count for word, count in word_counts.items() if word in negative_words}

# Identify most common positive and negative keywords
most_common_positive = max(positive_keywords, key=positive_keywords.get, default="None")
most_common_negative = max(negative_keywords, key=negative_keywords.get, default="None")

# Calculate the average length of reviews
df['Rating text Length'] = df['Rating text'].astype(str).apply(lambda x: len(x.split()))
average_review_length = df['Rating text Length'].mean()

# Scatter plot: Relationship between review length and rating
plt.figure(figsize=(8, 5))
plt.scatter(df['Rating text Length'], df['Aggregate rating'], alpha=0.5, color='blue')
plt.xlabel("Rating text Length (Number of Words)")
plt.ylabel("Aggregate Rating")
plt.title("Relationship Between Rating text Length and Rating")
plt.grid(True)

# Show the plot
plt.show()

# Print results
print(f"Most common positive keyword: {most_common_positive}")
print(f"Most common negative keyword: {most_common_negative}")
print(f"Average review length: {average_review_length:.2f} words")
