import pandas as pd
import matplotlib.pyplot as plt
import joblib


# Load Dataset
df = pd.read_csv(
    "data/processed/labeled_dataset.csv"
)


# Features
X = df.drop(
    columns=["quality_score", "label"]
)


# Load Model
model = joblib.load(
    "models/random_forest.pkl"
)

# Feature Importance
importance = model.feature_importances_

feature_names = X.columns

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print(importance_df)

# Plot
plt.figure(figsize=(10, 6))

plt.bar(
    importance_df["Feature"],
    importance_df["Importance"]
)

plt.xticks(rotation=45)

plt.title("Feature Importance")

plt.tight_layout()

plt.show()