import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# Load data
file_path =r'C:\Users\Jitendra\PycharmProjects\amazon_prime_new\.venv\amazon_prime_titles.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the data
print(df.head())
print(df.columns)
#
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['rating'].fillna('Not Rated', inplace=True)
print(df)

df.drop(columns=['date_added'], inplace=True)

# print(df.isnull().sum())

duplicate_rows = df[df.duplicated()]
print(duplicate_rows)

# .Content Type Distribution (Movies vs. TV Shows)
content_distribution = df['type'].value_counts()
print(content_distribution)

# Plotting the distribution of content types
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='type',palette='dark')
plt.title('Content Type Distribution (Movies vs. TV Shows)')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()


# Plot the top 10 countries by content count
country_content_count = df['country'].value_counts().head(10)
print(country_content_count)

plt.figure(figsize=(10, 6))
sns.barplot( x=country_content_count.index, y=country_content_count.values, palette='dark')
plt.title('Top 10 Countries by Content Count')
plt.xlabel('Country')
plt.ylabel('Content Count')
plt.xticks(rotation=45)
plt.show()


# Top 10 directors with most titles
top_directors = df['director'].value_counts().head(10)

# Create the pie chart
plt.figure(figsize=(8, 8))

# Using a lambda function in autopct to show both count and percentage
plt.pie(top_directors.values, labels=top_directors.index,
        autopct=lambda pct: f"{int(pct / 100 * np.sum(top_directors.values))} ({pct:.1f}%)",
        startangle=140, colors=sns.color_palette('dark', n_colors=10))

plt.title('Top 10 Directors by Title Count')
plt.show()


# # Group by 'release_year' and 'rating' to get counts
ratings_per_year = df.groupby(['release_year', 'rating']).size().unstack(fill_value=0)
print(ratings_per_year)

# Plotting
ratings_per_year.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='viridis')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.xticks(ha= "right")
plt.title('Content Ratings per Year')

plt.show()



# # Group by 'release_year' and count unique directors per year
unique_directors_per_year = df.groupby('release_year')['director'].nunique()
print(unique_directors_per_year)

# Plotting
unique_directors_per_year.plot(kind='bar', figsize=(12, 6), color='darkcyan')
plt.xlabel('Release Year')
plt.ylabel('Unique Directors')
plt.title('Unique Directors Producing Content Each Year')
plt.show()



# # Group by 'rating' and calculate the average release year
average_release_year_by_rating = df.groupby('rating')['release_year'].mean().sort_values(ascending=False)
print(average_release_year_by_rating)

# Plotting
average_release_year_by_rating.plot(kind='bar', figsize=(10, 6), color='indigo')
plt.xlabel('Rating')
plt.ylabel('Average Release Year')
plt.title('Average Release Year by Rating')
plt.show()