import pandas as pd
import os

from feature_engineering.feature_extractor import extract_features


# Load Dataset

df = pd.read_csv(
    "data/raw/python_codes.csv"
)

print("Dataset Loaded!")
print(df.shape)


# Extract Code List

codes = df["code"].tolist()

feature_rows = []


# Feature Extraction

for idx, code in enumerate(codes):

    features = extract_features(code)

    if features is not None:
        feature_rows.append(features)

    if idx % 500 == 0:
        print(f"Processed {idx} samples")


# Convert to DataFrame

features_df = pd.DataFrame(feature_rows)


# Create Folder

os.makedirs(
    "data/processed",
    exist_ok=True
)


# Save Dataset

features_df.to_csv(
    "data/processed/features_dataset.csv",
    index=False
)

print("Features saved successfully!")
print(features_df.shape)