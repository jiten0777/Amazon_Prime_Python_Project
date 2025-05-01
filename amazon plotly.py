import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load data
file_path = r'C:\Users\Jitendra\PycharmProjects\amazon_prime_new\.venv\amazon_prime_titles.csv'
df = pd.read_csv(file_path)

# Clean missing values safely (no FutureWarnings)
df = df.fillna({
    'director': 'Unknown',
    'cast': 'Unknown',
    'country': 'Unknown',
    'rating': 'Not Rated'
})

# Drop unnecessary column
df.drop(columns=['date_added'], inplace=True)

# --- Content Type Distribution ---
content_distribution = df['type'].value_counts().reset_index()
content_distribution.columns = ['Type', 'Count']

fig1 = px.bar(content_distribution, x='Type', y='Count',
              color='Type', title='Content Type Distribution (Movies vs. TV Shows)',
              color_discrete_sequence=px.colors.qualitative.Dark2)
fig1.show()

# --- Top 10 Countries by Content Count ---
country_content_count = df['country'].value_counts().head(10).reset_index()
country_content_count.columns = ['Country', 'Content Count']

fig2 = px.bar(country_content_count, x='Country', y='Content Count',
              color='Country', title='Top 10 Countries by Content Count',
              color_discrete_sequence=px.colors.qualitative.Dark2)
fig2.update_layout(xaxis_tickangle=-45)
fig2.show()

# --- Top 10 Directors by Title Count ---
top_directors = df['director'].value_counts().head(10).reset_index()
top_directors.columns = ['Director', 'Count']

fig3 = px.pie(top_directors, names='Director', values='Count',
              title='Top 10 Directors by Title Count',
              color_discrete_sequence=px.colors.qualitative.Dark2,
              hole=0.3)
fig3.update_traces(textinfo='percent+label+value')
fig3.show()

# --- Content Ratings per Year (Stacked Bar) ---
ratings_per_year = df.groupby(['release_year', 'rating']).size().reset_index(name='count')

fig4 = px.bar(ratings_per_year, x='release_year', y='count', color='rating',
              title='Content Ratings per Year', barmode='stack',
              color_discrete_sequence=px.colors.sequential.Viridis)
fig4.update_layout(xaxis_title='Release Year', yaxis_title='Count')
fig4.show()

# --- Unique Directors per Year ---
unique_directors_per_year = df.groupby('release_year')['director'].nunique().reset_index()
unique_directors_per_year.columns = ['release_year', 'unique_directors']

fig5 = px.bar(unique_directors_per_year, x='release_year', y='unique_directors',
              title='Unique Directors Producing Content Each Year',
              color='unique_directors', color_continuous_scale='Viridis')
fig5.update_layout(xaxis_title='Release Year', yaxis_title='Unique Directors')
fig5.show()

# --- Average Release Year by Rating ---
average_release_year_by_rating = df.groupby('rating')['release_year'].mean().sort_values(ascending=False).reset_index()
average_release_year_by_rating.columns = ['Rating', 'Average Release Year']

fig6 = px.bar(average_release_year_by_rating, x='Rating', y='Average Release Year',
              title='Average Release Year by Rating',
              color='Average Release Year', color_continuous_scale='Blues')
fig6.update_layout(xaxis_tickangle=-45)
fig6.show()

# --- Line Chart: Content Releases per Year ---
# Count of content per year (movies + TV shows)
content_per_year = df.groupby('release_year')['type'].value_counts().unstack(fill_value=0).reset_index()
content_per_year.columns = ['Release Year', 'Movies', 'TV Shows']

fig7 = px.line(content_per_year, x='Release Year', y=['Movies', 'TV Shows'],
               title='Content Releases per Year (Movies vs TV Shows)',
               labels={'value': 'Count', 'Release Year': 'Year'},
               markers=True)
fig7.update_layout(xaxis_title='Release Year', yaxis_title='Content Count')
fig7.show()
