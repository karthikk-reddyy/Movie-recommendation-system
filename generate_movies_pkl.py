import pandas as pd
import pickle

# Load the MovieLens dataset (you should have downloaded and extracted it)
df = pd.read_csv("ml-latest-small/movies.csv")  # adjust path if needed

# Rename movieId to match expected schema
df.rename(columns={'movieId': 'movie_id'}, inplace=True)

# Save the DataFrame as a pickle file
with open("movies.pkl", "wb") as f:
    pickle.dump(df, f)

print("✅ movies.pkl created successfully with", len(df), "movies!")
