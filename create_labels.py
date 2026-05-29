import pandas as pd
import os


# Load Feature Dataset

df = pd.read_csv(
    "data/processed/features_dataset.csv"
)

print("Dataset Loaded!")
print(df.shape)


# Calculate Quality Score

def calculate_quality_score(row):

    score = 50

   
    # Maintainability
   
    score += row["maintainability"] * 0.25

   
    # Penalize Complexity
 
    score -= row["avg_complexity"] * 8

  
    # Penalize Large LOC

    score -= row["loc"] * 0.15

    # Reward Comments
   
    score += row["comments"] * 1.5

   
    # Penalize Too Many Functions
   
    score -= row["function_count"] * 2

    # Clamp Score
   
    score = max(0, min(score, 100))

    return score



# Generate Scores

df["quality_score"] = df.apply(
    calculate_quality_score,
    axis=1
)


# Create Labels

def assign_label(score):

    if score >= 65:
        return "Good"

    elif score >= 45:
        return "Average"

    else:
        return "Poor"


df["label"] = df["quality_score"].apply(
    assign_label
)


# Save Dataset

os.makedirs(
    "data/processed",
    exist_ok=True
)

df.to_csv(
    "data/processed/labeled_dataset.csv",
    index=False
)


# Display Results

print(df.head())

print("\nLabel Distribution:")
print(df["label"].value_counts())

print("\nDataset Saved!")